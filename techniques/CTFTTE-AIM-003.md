# CTFTTE-AIM-003 — Adversarial-input requirement

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-003`](../countertechniques/CTFTCTE-AIM-003.md) — Generate an adversarial example

---

## How the challenge author hides

The flag unlocks only when a classifier is driven to a specific (incorrect) prediction.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; adversarial-example craft. |

## Tools

- foolbox
- ART (adversarial-robustness-toolbox)
- torch

## References

- Add challenge write-up link