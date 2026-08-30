# CTFTTE-GAM-001 — Networked game / protocol automation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-001`](../countertechniques/CTFTCTE-GAM-001.md) — Script a client to beat the protocol

---

## How the challenge author hides

The flag requires playing or solving many rounds of a networked game or custom protocol faster than is humanly feasible without automation.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Game-protocol automation. |

## Tools

- pwntools
- python sockets

## References

- <https://github.com/Gallopsled/pwntools>
- Add challenge write-up link
