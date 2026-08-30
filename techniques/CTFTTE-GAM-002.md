# CTFTTE-GAM-002 — Game save-state / memory manipulation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-002`](../countertechniques/CTFTCTE-GAM-002.md) — Hex-edit the save file or patch in-memory values

---

## How the challenge author hides

The flag is gated behind an in-game condition (score, item count, level unlock) stored in a save file or process memory that cannot be legitimately reached through normal gameplay.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Save-state manipulation. |

## Tools

- Cheat Engine
- python struct
- hex editors (HxD / 010 Editor)

## References

- Add challenge write-up link
