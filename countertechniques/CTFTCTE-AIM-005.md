# CTFTCTE-AIM-005 — Recover secrets through model inversion

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-005`](../techniques/CTFTTE-AIM-005.md) — Training-data leakage via queries

---

## Offensive Recovery (CTF practitioner / solver)

Query systematically (membership/inversion) to reconstruct the memorized value.

## Forensic / Blue-Team Perspective (DFIR analyst)

The query-response trail evidences memorization-based leakage.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Model inversion echoes data extraction from repositories. |

## Tools

- python
- model query harness

## References

- Add challenge write-up link