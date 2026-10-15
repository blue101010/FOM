# CTFTTE-AIM-005 — Training-data leakage via queries

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-005`](../countertechniques/CTFTCTE-AIM-005.md) — Recover secrets through model inversion

---

## How the challenge author hides

A secret memorized in training is reachable only by probing the model's outputs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Model inversion echoes data extraction from repositories. |

## Tools

- [python](../tools/CTFTTOU-050.md)
- [Adversarial Robustness Toolbox](../tools/CTFTTOU-044.md)
- [ML Privacy Meter](../tools/CTFTTOU-268.md)
- [TensorFlow Privacy](../tools/CTFTTOU-269.md)
- [PrivacyRaven](../tools/CTFTTOU-270.md)

## References

- Add challenge write-up link