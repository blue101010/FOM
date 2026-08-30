# CTFTCTE-AIM-003 — Generate an adversarial example

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-003`](../techniques/CTFTTE-AIM-003.md) — Adversarial-input requirement

---

## Offensive Recovery (CTF practitioner / solver)

Use gradient/black-box methods to craft an input that forces the target class.

## Forensic / Blue-Team Perspective (DFIR analyst)

The crafted input documents the model's decision-boundary fragility.

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