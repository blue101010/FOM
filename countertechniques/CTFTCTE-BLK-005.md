# CTFTCTE-BLK-005 — Craft a transaction abusing missing checks

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Counters technique:** [`CTFTTE-BLK-005`](../techniques/CTFTTE-BLK-005.md) — Access-control flaw to set flag

---

## Offensive Recovery (CTF practitioner / solver)

Call the unprotected function directly with a crafted transaction.

## Forensic / Blue-Team Perspective (DFIR analyst)

The call trace evidences the unauthorized privileged invocation.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1548 | Abuse Elevation Control Mechanism | Missing access checks echo elevation-control abuse. |

## Tools

- foundry cast
- web3.py

## References

- Add challenge write-up link