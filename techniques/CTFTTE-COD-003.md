# CTFTTE-COD-003 — Scripted protocol / automation marathon

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Paired counter-technique:** [`CTFTCTE-COD-003`](../countertechniques/CTFTCTE-COD-003.md) — Write a pwntools script to complete all rounds

---

## How the challenge author hides

The flag is awarded only after completing a very large number of stateful rounds of a binary or network protocol interaction — far beyond what manual solving allows within the server's timeout.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Protocol-automation marathon. |

## Tools

- pwntools
- python sockets
- telnetlib

## References

- <https://github.com/Gallopsled/pwntools>
- Add challenge write-up link
