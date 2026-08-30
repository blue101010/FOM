# CTFTTE-FPN-006 — Chained database trust-context escalation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-006`](../countertechniques/CTFTCTE-FPN-006.md) — Map database trust contexts and privilege boundaries

---

## How the challenge author hides

Several declared database services trust one another with different execution
contexts. A low-privilege entry can traverse a chain whose effective identity
has more privileges than the initial identity. The challenge models the trust
relation and privilege boundary; it does not embed a query or credential.

## Evidence expected

- Each trust edge names source service, target service and effective identity.
- A change in privilege is confirmed by a supplied, redacted role observation.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Database trust-context escalation. |

## References

- <https://learn.microsoft.com/sql/relational-databases/linked-servers/linked-servers-database-engine>
