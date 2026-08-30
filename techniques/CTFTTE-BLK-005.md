# CTFTTE-BLK-005 — Access-control flaw to set flag

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-005`](../countertechniques/CTFTCTE-BLK-005.md) — Craft a transaction abusing missing checks

---

## How the challenge author hides

A privileged setter lacks proper access control, gating the flag behind a check that is missing.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1548 | Abuse Elevation Control Mechanism | Missing access checks echo elevation-control abuse. |

## Tools

- foundry cast
- web3.py

## References

- Add challenge write-up link