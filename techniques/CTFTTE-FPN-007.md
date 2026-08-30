# CTFTTE-FPN-007 — Uninventoried dual-stack management path

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-007`](../countertechniques/CTFTCTE-FPN-007.md) — Reconcile dual-stack management exposure

---

## How the challenge author hides

A management service is declared on an address family absent from the primary
inventory. The challenge requires reconciling interface records, service binds
and access policy before treating the alternate route as a possible path.

## Evidence expected

- An interface record and a service bind identify the alternate address family.
- The management route is corroborated by the challenge's access policy.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | Dual-stack management exposure. |

## References

- <https://www.rfc-editor.org/rfc/rfc8200>
