# CTFTTMOU-001 — mcp-maigret

> **MCP ID:** `CTFTTMOU-001`  
> **Related tool:** [`CTFTTOU-098`](../tools/CTFTTOU-098.md) — maigret  
> **Related techniques/counters:** CTFTTE-OSI-002, CTFTCTE-OSI-002

## Description

MCP server (stdio) that lets AI agents run maigret — the OSINT username search across
thousands of sites — from any MCP client (Claude Code/Desktop, VS Code Copilot, any MCP
client). Exposes two MCP tools:

- `search_username` — check a username across maigret's site database; filter by tags
  (`photo`, `dating`, `us`, ...) or `use_all_sites` mode; six report formats
  (`txt`, `html`, `csv`, `json`, `xmind`, `pdf`) saved to `MAIGRET_REPORTS_DIR`.
- `parse_url` — analyze a profile URL: extract what it can and hunt for linked usernames.

Maigret runs in Docker (`soxoj/maigret` image, pulled on first use), inputs are strictly
validated with no shell involved. Requires Node.js 18+ and Docker.

Docs: <https://w0h1v.github.io/mcp-maigret/>

## Start / Stop / Check

mcp-maigret is a stdio MCP server: the MCP client launches it on demand, it does not
run as a daemon.

```sh
# Check prerequisites (Node.js 18+, Docker running)
node --version
docker version
# Check the npm package resolves
npm view mcp-maigret version

# Start: register once with the client — it then launches the server per session
claude mcp add maigret -e MAIGRET_REPORTS_DIR="$HOME/maigret-reports" -- npx -y mcp-maigret
# (other clients: equivalent mcpServers entry with command "npx" args ["-y","mcp-maigret"])

# Check it answers: from the MCP client, tools/list must expose
#   search_username and parse_url
# Manual smoke test from a terminal (stdio server; MAIGRET_REPORTS_DIR is REQUIRED,
# without it the server exits immediately with
#   "Error: MAIGRET_REPORTS_DIR environment variable must be set"):
MAIGRET_REPORTS_DIR="$HOME/maigret-reports" npx -y mcp-maigret
# (then pipe an MCP initialize + tools/list handshake, or leave Ctrl+C to quit)

# Stop: nothing runs between client sessions; unregister to disconnect
claude mcp remove maigret
```

Agents without MCP-client support drive the stdio protocol directly, no registration
needed: spawn the server, send `initialize` → `notifications/initialized` →
`tools/call` `{"name":"search_username","arguments":{"username":"<target>"}}` over
newline-delimited JSON on stdin, read the dossier (report path + per-site hits) from
stdout. First run downloads the site DB (~8000 sites) inside the container — expect
several minutes.

## URL

<https://github.com/w0h1v/mcp-maigret>

## Related Techniques

CTFTTE-OSI-002, CTFTCTE-OSI-002
