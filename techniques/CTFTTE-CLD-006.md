# CTFTTE-CLD-006 — Cross-account role chaining / trust abuse

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-006`](../countertechniques/CTFTCTE-CLD-006.md) — Chain sts:AssumeRole across accounts

---

## How the challenge author hides

The flag is in a second AWS account reachable only by chaining role assumptions through trust relationships.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.004 | Cloud Accounts | Role-based cloud account access. |

## Tools

- awscli
- enumerate-iam
- pacu

## References

- <https://github.com/RhinoSecurityLabs/pacu>
- Add challenge write-up link
