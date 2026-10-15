# CTFTTE-AIM-004 — Malicious / opaque serialized model

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-004`](../countertechniques/CTFTCTE-AIM-004.md) — Safely inspect serialized model files

---

## How the challenge author hides

A pickle/serialized model hides logic or data that executes/loads on deserialization.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Malicious serialized models echo public-app exploitation on ML serving endpoints. |

## Tools

- [fickling](../tools/CTFTTOU-045.md)
- [python](../tools/CTFTTOU-050.md) [pickletools](../tools/CTFTTOU-046.md)

## References

- <https://github.com/trailofbits/fickling>
- Add challenge write-up link