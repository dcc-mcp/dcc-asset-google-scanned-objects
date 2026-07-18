# DCC-MCP Google Scanned Objects

<p align="center">
  <img src="docs/assets/dcc-asset-google-scanned-objects.svg" alt="DCC-MCP · GOOGLE-SCANNED-OBJECTS" width="600">
</p>

## Agent workflow

AI agents should use installed package skills through the shared gateway. IDE
users may continue to use the MCP endpoint.

```bash
dcc-mcp-cli dcc-types
dcc-mcp-cli list
dcc-mcp-cli search --query "<task>" --dcc-type <host>
dcc-mcp-cli describe <tool-slug>
dcc-mcp-cli call <tool-slug> --json '{"key":"value"}'
```

If the package skill is not active, call
`dcc-mcp-cli load-skill <skill-name> --dcc-type <host>`. After the task,
query `dcc-mcp-cli stats --range 24h --session-id <task-id>` and pass only
bounded evidence to the `review_skill_improvement` prompt from
`dcc-mcp-skills-creator`.


![Workflow showcase](docs/images/dcc-asset-google-scanned-objects-showcase.webp)

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
