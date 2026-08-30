# CTFTCTE-CLD-006 — Chain sts:AssumeRole across accounts

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-006`](../techniques/CTFTTE-CLD-006.md) — Cross-account role chaining / trust abuse

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate roles, chain sts:AssumeRole across accounts, and reach the target resources.

## Forensic / Blue-Team Perspective (DFIR analyst)

CloudTrail records every AssumeRole hop; the chain is reconstructible from role ARNs.

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
