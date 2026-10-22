# CTFT MCP Servers

MCP servers that expose CTFT tools and techniques to AI agents. Each fiche is the MCP
counterpart of a tool fiche in [`../tools/tools.md`](../tools/tools.md) and links back to
it, plus the technique/counter-technique pairs it serves.

| MCP ID | Name | URL | Related tool | Used in |
| --- | --- | --- | --- | --- |
| [CTFTTMOU-001](CTFTTMOU-001.md) | mcp-maigret | <https://github.com/w0h1v/mcp-maigret> | [CTFTTOU-098](../tools/CTFTTOU-098.md) — maigret | CTFTTE-OSI-002, CTFTCTE-OSI-002 |
| [CTFTTMOU-002](CTFTTMOU-002.md) | GhidraMCP (bethington/ghidra-mcp) | <https://github.com/bethington/ghidra-mcp> | [CTFTTOU-073](../tools/CTFTTOU-073.md) — ghidra | CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-008, CTFTTE-REV-009, CTFTTE-REV-010 |
| [CTFTTMOU-003](CTFTTMOU-003.md) | MDB-MCP (GDB/LLDB) | <https://github.com/smadi0x86/MDB-MCP> | [CTFTTOU-163](../tools/CTFTTOU-163.md) — gdb | CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-PWN-002, CTFTCTE-PWN-002, CTFTTE-PWN-003, CTFTCTE-PWN-003, CTFTTE-PWN-006, CTFTCTE-PWN-006, CTFTTE-PWN-007, CTFTCTE-PWN-007, CTFTTE-PWN-011, CTFTCTE-PWN-011, CTFTTE-PWN-012, CTFTCTE-PWN-012, CTFTTE-REV-001, CTFTCTE-REV-001 |
| [CTFTTMOU-004](CTFTTMOU-004.md) | volatility-mcp | <https://github.com/Gaffx/volatility-mcp> | [CTFTTOU-134](../tools/CTFTTOU-134.md) — volatility3 | CTFTTE-FOR-005, CTFTCTE-FOR-005, CTFTTE-FOR-026, CTFTCTE-FOR-026, CTFTTE-REV-002, CTFTCTE-REV-002 |

Every MCP fiche carries a `## Start / Stop / Check` section with the exact commands to
start the server, verify it answers, and stop it.
