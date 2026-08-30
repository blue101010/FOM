# CTFTTE-PWN-003 — Heap-grooming puzzle

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-003`](../countertechniques/CTFTCTE-PWN-003.md) — Groom the heap to corrupt allocator metadata

---

## How the challenge author hides

The flag/control is reachable only by manipulating allocator metadata (use-after-free, tcache).

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1068 | Exploitation for Privilege Escalation | Heap-grooming mechanics are omitted by ATT&CK. |

## Tools

- pwntools
- GDB+pwndbg
- glibc heap viewers

## References

- Add challenge write-up link