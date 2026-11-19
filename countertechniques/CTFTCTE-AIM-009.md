# CTFTCTE-AIM-009 — Enumerate and abuse the MCP surface (tools, resources, prompts, template placeholders)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-009`](../techniques/CTFTTE-AIM-009.md) — Player-reachable MCP server with an injectable tool surface

---

## Offensive Recovery (CTF practitioner / solver)

Speak JSON-RPC 2.0 to the endpoint directly: `initialize` (keep the `Mcp-Session-Id`
header), `notifications/initialized`, then `tools/list`, `resources/list` +
`resources/read` every URI, `prompts/list` + `prompts/get` each. Read tool
descriptions fully — required keys and example IDs hide there. Then call tools with
probe arguments: template placeholders (`{ticket.__class__}`, `__init__.__globals__`,
`__subclasses__()` chains, `{{ ... }}` SSTI variants — start with a harmless type-name
leak, then escalate to file read / RCE), argument injection into every string field,
and admin-gated tools with keys found in descriptions. Scan every response for
flag-format strings. Automate with
[mcp_probe.py](../../ctf-skills-main/ctf-ai-ml/scripts/mcp_probe.py) (`--selftest`).

## Forensic / Blue-Team Perspective (DFIR analyst)

MCP access logs record the enumeration sequence (initialize → lists → reads → calls)
and the injected placeholder strings that triggered server-side evaluation.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Exposed agent-tool endpoints are public-facing application surface. |

## Tools

- [curl](../tools/CTFTTOU-038.md) / [requests](../tools/CTFTTOU-067.md)
- [Playwright](../tools/CTFTTOU-008.md)
- [mcp_probe.py](../../ctf-skills-main/ctf-ai-ml/scripts/mcp_probe.py) ([CTFTTOU-448](../tools/CTFTTOU-448.md))

## References

- <https://modelcontextprotocol.io/specification>
- <https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/>
- <https://github.com/modelcontextprotocol/servers>
