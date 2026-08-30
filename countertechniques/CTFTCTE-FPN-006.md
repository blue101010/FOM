# CTFTCTE-FPN-006 — Map database trust contexts and privilege boundaries

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-006`](../techniques/CTFTTE-FPN-006.md) — Chained database trust-context escalation

---

## Offensive Recovery (CTF practitioner / solver)

Build a graph from the challenge's declared service links and redacted identity
observations. Rank only paths whose trust edge, effective context and target
privilege boundary are all evidenced.

## Forensic / Blue-Team Perspective (DFIR analyst)

Audit linked-service identities, delegation settings and effective permissions.
Remove unintended identity translation and apply least-privilege service
contexts.

## Preconditions

- The challenge supplies a service-link inventory and identity observations.
- Every edge is scoped to the authorized lab design.

## Indicators

- A linked service executes under a different declared identity.
- A trust path crosses into a more privileged role boundary.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Database trust-context escalation. |

## References

- <https://learn.microsoft.com/sql/relational-databases/linked-servers/linked-servers-database-engine>
