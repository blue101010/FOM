# CTFTTE-BLK-002 — Reentrancy-gated flag

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-002`](../countertechniques/CTFTCTE-BLK-002.md) — Exploit reentrancy to set the flag

---

## How the challenge author hides

The flag only flips after a withdraw/transfer flow vulnerable to reentrancy.

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