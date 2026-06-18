from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "google-scanned-objects"
SCRIPTS = SKILL / "scripts"


def load(name: str):
    sys.path.insert(0, str(SCRIPTS))
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def validate_skill() -> None:
    from dcc_mcp_core import validate_skill

    report = validate_skill(str(SKILL))
    assert not report.has_errors, report


def live_google_scanned_smoke() -> None:
    if os.environ.get("RUN_LIVE_API_SMOKE") != "true":
        print("skip live Google Scanned Objects smoke")
        return
    search = load("search_google_scanned_objects").main(query="Billfish", limit=5)
    assert search["success"], search
    assets = search["context"]["assets"]
    assert assets, search
    files = load("list_google_scanned_object_files").main(model_name=assets[0]["name"])
    assert files["success"], files
    assert files["context"]["files"], files


def main() -> None:
    validate_skill()
    live_google_scanned_smoke()


if __name__ == "__main__":
    main()
