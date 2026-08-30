# CTFTCTE-CLD-007 — Enumerate and query exposed cloud databases

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-007`](../techniques/CTFTTE-CLD-007.md) — Cloud NoSQL-store misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate the table/index, query it with the available permissions, and read the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Cloud database exposure is logged via CloudTrail; scan results document the misconfiguration.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Cloud data-store enumeration. |

## Tools

- awscli dynamodb
- NoSQLMap
- boto3

## References

- <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>
