# CTFTCTE-BLK-002 — Exploit reentrancy to set the flag

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Counters technique:** [`CTFTTE-BLK-002`](../techniques/CTFTTE-BLK-002.md) — Reentrancy-gated flag

---

## Offensive Recovery (CTF practitioner / solver)

Deploy an attacker contract that re-enters during the external call to drive the state change.

## Forensic / Blue-Team Perspective (DFIR analyst)

Trace analysis shows the nested calls that produced the unintended state.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Reentrancy exploitation of a public contract. |

## Tools

- foundry
- hardhat
- solidity

## References

- Add challenge write-up link