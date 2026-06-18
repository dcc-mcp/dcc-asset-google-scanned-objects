from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _google_scanned_objects import LICENSE_NOTICE, search


@skill_entry
def main(query: str | None = None, limit: int = 20, **_: Any) -> dict[str, Any]:
    try:
        assets = search(query, limit)
        return skill_success("Google Scanned Objects found", assets=assets, count=len(assets), license=LICENSE_NOTICE)
    except Exception as exc:
        return skill_exception(exc, message="Failed to search Google Scanned Objects")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
