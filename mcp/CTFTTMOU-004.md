# CTFTTMOU-004 — volatility-mcp

> **MCP ID:** `CTFTTMOU-004`  
> **Related tool:** [`CTFTTOU-134`](../tools/CTFTTOU-134.md) — volatility3  
> **Related techniques/counters:** CTFTTE-FOR-005, CTFTCTE-FOR-005, CTFTTE-FOR-026, CTFTCTE-FOR-026, CTFTTE-REV-002, CTFTCTE-REV-002

## Description

MCP server (stdio, Python) exposing Volatility 3 memory analysis to AI agents. Two
processes: a FastAPI backend that runs `vol -f <image> <plugin>` (no shell) and the MCP
server that calls it over HTTP. Three MCP tools, all **Windows** plugins, on the image
fixed at server start (`-i`):

- `get_processes` — `windows.pslist.PsList`
- `get_connections` — `windows.netscan.NetScan`
- `get_cmdline` — `windows.cmdline.CmdLine`

Narrow by design: first-pass triage of a Windows image (which processes, which
connections, which command lines). Everything else (Linux/macOS images, `pstree`,
`malfind`, `filescan`, `dumpfiles`, `hashdump`, memory dumps of a process) is plain
`vol` on the command line. Installed in Kali WSL from a reviewed clone (`8c9aafc`) with
volatility3 2.27.0 in `~/.venvs/volmcp`; `~/TOOLS/volatility-mcp-launch.sh` starts the
backend on `127.0.0.1:8000` when needed and serves MCP. Registered as `volatility` in
`.mcp.json`, `.vscode/mcp.json`, `.codex/config.toml`.

## Start / Stop / Check

```sh
# Point the server at the challenge image (a symlink, re-read on every call)
mkdir -p ~/memdumps && ln -sfn /path/to/memory.raw ~/memdumps/current

# Start the backend alone and check it (the MCP launcher also does this itself)
~/TOOLS/volatility-mcp-launch.sh --backend
curl -s http://127.0.0.1:8000/plugins          # -> process, connections, cmdline
curl -s "http://127.0.0.1:8000/analyze/process?image_path=$HOME/memdumps/current" | head -c 400

# Start the MCP server: the client runs, from Windows
#   wsl.exe -d kali-linux -e /home/fhp/TOOLS/volatility-mcp-launch.sh
claude mcp add volatility -- wsl.exe -d kali-linux -e /home/fhp/TOOLS/volatility-mcp-launch.sh
# Check: tools/list exposes get_processes, get_connections, get_cmdline

# Stop the backend (the MCP server exits with the client)
~/TOOLS/volatility-mcp-launch.sh --stop          # backend log: /tmp/volatility-mcp-backend.log
```

## Notes

- Errors come back as normal text (`Error 500: {"detail": "Plugin process failed: ..."}`),
  not as MCP errors: read the first line of every reply.
- The MCP→backend HTTP timeout is 30 s (upstream `http_client.py`). A first run on a
  Windows image downloads PDB symbols and builds the cache; if a call times out, warm the
  cache with `~/.venvs/volmcp/bin/vol -f ~/memdumps/current windows.info` and retry.
- `VOL_IMAGE`, `VOL_PORT`, `VOLATILITY_BIN` override the launcher defaults.

## URL

<https://github.com/Gaffx/volatility-mcp>

## Related Techniques

CTFTTE-FOR-005, CTFTCTE-FOR-005, CTFTTE-FOR-026, CTFTCTE-FOR-026, CTFTTE-REV-002, CTFTCTE-REV-002
