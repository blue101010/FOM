# CTFTTOU-448 — mcp_probe.py

> **Tool ID:** `CTFTTOU-448`  
> **Related techniques/counters:** CTFTTE-AIM-009, CTFTCTE-AIM-009

## Description

Workspace-authored enumerator for player-reachable MCP (Model Context Protocol)
servers (Python, stdlib only). It performs the `initialize` handshake, keeps the
`Mcp-Session-Id` header, sends `notifications/initialized`, then `tools/list`,
`resources/list` (+ `resources/read` each URI, capped), `prompts/list` (+
`prompts/get`), and an optional `tools/call`. Responses are parsed from SSE `data:`
frames (plain JSON also accepted) and every blob is scanned for flag-format strings.
The summary (tool names + descriptions, resource URIs + texts, prompt names, call
results, flags) is printed and optionally appended to a JSONL transcript.

Pairs with the manual curl recipe and the placeholder-injection workflow in
[ctf-skills-main/ctf-ai-ml/mcp-probe.md](../../ctf-skills-main/ctf-ai-ml/mcp-probe.md).

`--selftest` runs against a mock SSE MCP server with one tool, one resource holding
a planted flag, and asserts the handshake, enumeration, resource read, and
`tools/call` all work.

## URL

Local (workspace): [ctf-skills-main/ctf-ai-ml/scripts/mcp_probe.py](../../ctf-skills-main/ctf-ai-ml/scripts/mcp_probe.py)

## Usage

```bash
python3 mcp_probe.py --url http://target:30733/mcp/ --out probe.jsonl
python3 mcp_probe.py --url URL --call respond_to_ticket \
    --args '{"ticket_id":"TKT-1","template_name":"default","message":"x"}'
python3 mcp_probe.py --selftest
```

## Skills

- [ctf-ai-ml](../skills/CTFTSKL-017.md) — domain skill (AIM-009 workflow lives in mcp-probe.md)

## Related Techniques

CTFTTE-AIM-009, CTFTCTE-AIM-009
