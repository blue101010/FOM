# CTFTTE-GAM-002 — Game save-state / memory manipulation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-002`](../countertechniques/CTFTCTE-GAM-002.md) — Hex-edit the save file or patch in-memory values

---

## How the challenge author hides

The flag is gated behind an in-game condition (score, item count, level unlock) stored in a save file or process memory that cannot be legitimately reached through normal gameplay.

## ATT\&CK Complementarity

No ATT&CK equivalent. ATT&CK does not model game-state tamper puzzle craft.

## Tools

- Cheat Engine
- python struct
- hex editors (HxD / 010 Editor)

## References

- Add challenge write-up link
