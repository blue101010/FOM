# CTFTCTE-FPN-007 — Reconcile dual-stack management exposure

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-007`](../techniques/CTFTTE-FPN-007.md) — Uninventoried dual-stack management path

---

## Offensive Recovery (CTF practitioner / solver)

Compare the supplied interface inventory, service binds and policy declarations.
Create a candidate route only when all three name the same authorized challenge
asset and access boundary.

## Forensic / Blue-Team Perspective (DFIR analyst)

Maintain one inventory across address families and verify that management
services have consistent access controls, logging and ownership.

## Preconditions

- A dual-stack interface and service inventory is supplied by the challenge.
- The management path is inside the declared laboratory scope.

## Indicators

- A service bind exists on an address family omitted by the primary inventory.
- The policy treatment differs across address families.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | Dual-stack management exposure. |

## References

- <https://www.rfc-editor.org/rfc/rfc8200>
