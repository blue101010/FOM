# CTFTCTE-PWN-012 — Compute the target address from the leaked pointer

> **Type:** Counter-technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-012`](../techniques/CTFTTE-PWN-012.md) — Author-gifted pointer leak

---

## Offensive Recovery (CTF practitioner / solver)

Parse the printed pointer, identify what it points at (stack slot or named global via
the decompiler), then compute: PIE target = leaked address + (symbol − leaked
symbol) from the static image; stack target = leaked stack address + fixed delta
observed in GDB. Chain the computed address into the overflow payload.

## Forensic / Blue-Team Perspective (DFIR analyst)

The exploit path documents the arithmetic from a single disclosed pointer to a full
ASLR-defeating payload — evidence of an intended information-disclosure primitive.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Leak arithmetic echoes disclosed-memory exploitation. |

## Tools

- [pwntools](../tools/CTFTTOU-053.md)
- [checksec](../tools/CTFTTOU-289.md)
- [GDB (pwndbg/GEF)](../tools/CTFTTOU-290.md)

## MCP

- [GhidraMCP](../mcp/CTFTTMOU-002.md) — read the leaked global's address and the win offset from the static image

## References

- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-3>
- <https://wintertia.gitbook.io/ctf/writeups-2024/tcp1p-playground-365/ret2win-4>
