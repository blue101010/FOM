# CTFTTE-AIM-009 — Player-reachable MCP server with an injectable tool surface

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-009`](../countertechniques/CTFTCTE-AIM-009.md) — Enumerate and abuse the MCP surface (tools, resources, prompts, template placeholders)

---

## How the challenge author hides

The challenge exposes a Model Context Protocol server (usually one `/mcp/` endpoint,
JSON-RPC 2.0 over SSE) fronting an "AI agent". The flag is reachable through the tool
surface rather than through persuasion: tool descriptions name admin keys or example
IDs; resources (`resources/read`) hold internal state and double as indirect prompt
injection into the agent's context; tools that render templates with placeholders
(`{ticket[field]}`, `{message}`, …) evaluate those placeholders server-side, so an
attribute walk (`__class__` → `__init__.__globals__` → `__subclasses__()`) turns a
"formatted response" into file read or RCE; prompts can embed the system prompt or
example flags. Distinct from CTFTTE-AIM-007, where the target is the agent's tool-use
policy; here the transport and the server-side evaluation are the attack surface.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Exposed agent-tool endpoints are public-facing application surface. |

## Tools

- [curl](../tools/CTFTTOU-038.md) / [requests](../tools/CTFTTOU-067.md)
- [Playwright](../tools/CTFTTOU-008.md)
- [mcp_probe.py](../../ctf-skills-main/ctf-ai-ml/scripts/mcp_probe.py) ([CTFTTOU-448](../tools/CTFTTOU-448.md))

## Indicators

- an HTTP endpoint answering MCP `initialize` with `serverInfo` and SSE `data:` frames
- `Mcp-Session-Id` response header required for follow-up calls
- `tools/list` descriptions mentioning API keys, admin roles, or example resource IDs
- tools accepting template content with `{...}` placeholders that get rendered
- `resources/list` URIs pointing at internal state (status, tickets, knowledge base)

## References

- <https://modelcontextprotocol.io/specification>
- <https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/>
- <https://github.com/modelcontextprotocol/servers>
