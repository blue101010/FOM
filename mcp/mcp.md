# CTFT MCP Servers

MCP servers that expose CTFT tools and techniques to AI agents. Each fiche is the MCP
counterpart of a tool fiche in [`../tools/tools.md`](../tools/tools.md) and links back to
it, plus the technique/counter-technique pairs it serves.

| MCP ID | Name | URL | Related tool | Used in |
| --- | --- | --- | --- | --- |
| [CTFTTMOU-001](CTFTTMOU-001.md) | mcp-maigret | <https://github.com/w0h1v/mcp-maigret> | [CTFTTOU-098](../tools/CTFTTOU-098.md) — maigret | CTFTTE-OSI-002, CTFTCTE-OSI-002 |
| [CTFTTMOU-002](CTFTTMOU-002.md) | GhidraMCP (bethington/ghidra-mcp) | <https://github.com/bethington/ghidra-mcp> | [CTFTTOU-073](../tools/CTFTTOU-073.md) — ghidra | CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-008, CTFTTE-REV-009, CTFTTE-REV-010 |

Every MCP fiche carries a `## Start / Stop / Check` section with the exact commands to
start the server, verify it answers, and stop it.
