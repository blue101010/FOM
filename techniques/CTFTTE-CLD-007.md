# CTFTTE-CLD-007 — Cloud NoSQL-store misconfiguration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-007`](../countertechniques/CTFTCTE-CLD-007.md) — Enumerate and query exposed cloud databases

---

## How the challenge author hides

A cloud NoSQL store (DynamoDB or similar) is exposed or over-permissioned and holds the flag.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Cloud data-store enumeration. |

## Tools

- awscli dynamodb
- NoSQLMap
- boto3

## References

- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- Add challenge write-up link
