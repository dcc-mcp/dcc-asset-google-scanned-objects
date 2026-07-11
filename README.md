# DCC-MCP Google Scanned Objects

![Workflow showcase](docs/workflow-showcase.png)

Google Scanned Objects search and download tools for DCC-MCP.

This skill uses Gazebo Fuel's public model API for the GoogleResearch owner.
It downloads the original SDF/OBJ/texture model files and does not import them
into a DCC scene.

## Install

```bash
dcc-mcp-cli marketplace add dcc-mcp/dcc-asset-google-scanned-objects
dcc-mcp-cli marketplace install dcc-asset-google-scanned-objects
```

## Tools

- `search_google_scanned_objects`
- `list_google_scanned_object_files`
- `download_google_scanned_object`

## License Notes

This wrapper is MIT licensed. Google Scanned Objects are distributed through
Gazebo Fuel under Creative Commons Attribution 4.0 International. Keep
attribution and source metadata with downloaded assets.
