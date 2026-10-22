# CTFTCTE-PWN-003 — Groom the heap to corrupt allocator metadata

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-003`](../techniques/CTFTTE-PWN-003.md) — Heap-grooming puzzle

---

## Offensive Recovery (CTF practitioner / solver)

Shape allocations to trigger overlapping chunks or arbitrary write, then hijack a pointer.

## Forensic / Blue-Team Perspective (DFIR analyst)

Documenting the allocation sequence explains the metadata corruption primitive.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Heap-grooming mechanics are omitted by ATT&CK. |

## Tools

- pwntools
- [gdb](../tools/CTFTTOU-163.md)
- [pwndbg](../tools/CTFTTOU-292.md)
- glibc heap viewers

## MCP

- [MDB-MCP (GDB/LLDB)](../mcp/CTFTTMOU-003.md) — dynamic debugging session (gdb or lldb)

## References

- Add challenge write-up link