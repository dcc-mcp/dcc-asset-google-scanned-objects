from __future__ import annotations

import json
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


BASE = "https://fuel.gazebosim.org/1.0/GoogleResearch/models"
HEADERS = {"User-Agent": "dcc-mcp-google-scanned-objects/0.1"}
LICENSE_NOTICE = {
    "provider": "Google Scanned Objects via Gazebo Fuel",
    "license_name": "Creative Commons Attribution 4.0 International",
    "license_url": "https://creativecommons.org/licenses/by/4.0/",
    "usage_notice": "Keep attribution and source metadata with downloaded assets.",
}


def api(url: str) -> Any:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def search(query: str | None = None, limit: int = 20) -> list[dict[str, Any]]:
    params = {"per_page": max(1, min(int(limit), 100))}
    if query:
        params["q"] = query
    data = api(BASE + "?" + urllib.parse.urlencode(params))
    return [
        {
            "name": item.get("name"),
            "description": item.get("description"),
            "categories": item.get("categories", []),
            "filesize": item.get("filesize"),
            "downloads": item.get("downloads"),
            "license_name": item.get("license_name"),
            "license_url": item.get("license_url"),
            "thumbnail_url": item.get("thumbnail_url"),
        }
        for item in data[:limit]
    ]


def file_tree(model_name: str) -> dict[str, Any]:
    name = urllib.parse.quote(model_name.strip("/"), safe="")
    return api(f"{BASE}/{name}/tip/files")


def _flatten(nodes: list[dict[str, Any]]) -> list[str]:
    out = []
    for node in nodes:
        children = node.get("children")
        if isinstance(children, list):
            out.extend(_flatten(children))
        elif node.get("path"):
            out.append(node["path"].lstrip("/"))
    return out


def files(model_name: str) -> list[str]:
    return _flatten(file_tree(model_name).get("file_tree", []))


def download_file(model_name: str, file_path: str, output_dir: str) -> str:
    name = urllib.parse.quote(model_name.strip("/"), safe="")
    path = file_path.strip("/")
    url = f"{BASE}/{name}/tip/files/{urllib.parse.quote(path, safe='/')}"
    target = Path(output_dir) / model_name / path
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=180) as resp:
        target.write_bytes(resp.read())
    return str(target)


def download_model(model_name: str, output_dir: str) -> dict[str, Any]:
    downloaded = [download_file(model_name, path, output_dir) for path in files(model_name)]
    return {"model_name": model_name, "files": downloaded, "count": len(downloaded), **LICENSE_NOTICE}
