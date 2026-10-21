# CTFTTMOU-002 — GhidraMCP (bethington/ghidra-mcp)

> **MCP ID:** `CTFTTMOU-002`  
> **Related tool:** [`CTFTTOU-073`](../tools/CTFTTOU-073.md) — ghidra  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-008, CTFTTE-REV-009, CTFTTE-REV-010

## Description

MCP server exposing the Ghidra workbench to AI agents: ~190 REST endpoints over HTTP
(headless server, no GUI required) plus a Python MCP bridge (`bridge-mcp-ghidra`, stdio).
Function decompilation, disassembly, cross-references, call graphs, string and raw-memory
reads, P-code emulation — the RE/pwn triage path for any binary, including stripped Go
ELFs via pclntab symbol recovery. Installed in Kali WSL: plugin v7.0.0 built against the
apt Ghidra 12.1.2, bridge venv `~/.venvs/ghidramcp`, launcher
`~/TOOLS/ghidra-mcp-headless.sh`.

## Start / Stop / Check

```sh
# Start (Kali WSL): headless server + import a binary (~20 s for small ELFs)
nohup ~/TOOLS/ghidra-mcp-headless.sh /path/to/binary 8089 > /tmp/ghidra-mcp-headless.log 2>&1 &

# Check
curl -s http://127.0.0.1:8089/check_connection   # -> {"status":"ok",...,"program":"<name>"}
curl -s http://127.0.0.1:8089/mcp/health
curl -s http://127.0.0.1:8089/analysis_status    # "analyzed": true required; if false:
#   POST http://127.0.0.1:8089/reanalyze         # large binaries import WITHOUT analysis

# Stop
pkill -f GhidraMCPHeadlessServer

# MCP clients: stdio bridge (requires the headless server running first)
~/.venvs/ghidramcp/bin/bridge-mcp-ghidra
```

Notes:

- The launcher passes `-Djava.net.preferIPv4Stack=true` — required under WSL2 NAT
  networking: without it Java binds an IPv6-mapped socket and the localhost relay
  ignores the listener (`localhost:8089` fails from Windows while working inside WSL).
- With `networkingMode=mirrored` in `.wslconfig` (recommended on this host: the NAT
  relay is flaky and dies on rebind), localhost works natively in both directions
  and the relay/IPv4 concern disappears.
- Default tool groups on connect: `listing,function,program`; pull more with the
  `search_tools` / `load_tool_group` MCP tools.

## URL

<https://github.com/bethington/ghidra-mcp>

## Related Techniques

CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-008, CTFTTE-REV-009, CTFTTE-REV-010
