from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _google_scanned_objects import LICENSE_NOTICE, files


@skill_entry
def main(model_name: str, **_: Any) -> dict[str, Any]:
    try:
        listed = files(model_name)
        return skill_success("Google Scanned Object files listed", files=listed, count=len(listed), license=LICENSE_NOTICE)
    except Exception as exc:
        return skill_exception(exc, message="Failed to list Google Scanned Object files")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main

    run_main(main)
