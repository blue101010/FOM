# CTFTCTE-COD-003 — Write a pwntools script to complete all rounds

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Counters technique:** [`CTFTTE-COD-003`](../techniques/CTFTTE-COD-003.md) — Scripted protocol / automation marathon

---

## Offensive Recovery (CTF practitioner / solver)

Write a pwntools `remote` or `process` script that parses each server prompt, computes the answer (arithmetic, parsing, encoding), and responds within the timeout for every round until the flag is released.

## Forensic / Blue-Team Perspective (DFIR analyst)

The automation pattern documents server interaction that is indistinguishable from a legitimate compliant client; in production, server-side rate limiting and per-round session tokens limit scripted mass interaction.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Protocol-automation marathon. |

## Tools

- pwntools
- python sockets
- telnetlib

## References

- https://github.com/Gallopsled/pwntools
- Add challenge write-up link
