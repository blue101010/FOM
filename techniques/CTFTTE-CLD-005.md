# CTFTTE-CLD-005 — Container image / registry leak

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-005`](../countertechniques/CTFTCTE-CLD-005.md) — Pull and inspect image layers

---

## How the challenge author hides

The flag is baked into a container layer or left in a pushed image's history.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1613 | Container and Resource Discovery | Container image / registry inspection. |

## Tools

- docker
- dive
- skopeo

## References

- https://github.com/wagoodman/dive
- Add challenge write-up link