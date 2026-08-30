# CTFTTE-CLD-002 — Over-permissive IAM role

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-002`](../countertechniques/CTFTCTE-CLD-002.md) — Enumerate and assume reachable roles

---

## How the challenge author hides

A role/policy grants more than intended, letting solvers pivot to the flag resource.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.004 | Cloud Accounts | Over-permissive IAM roles. |

## Tools

- enumerate-iam
- awscli
- pacu

## References

- Add challenge write-up link