# CTFTTE-BLK-004 — Hidden event-log / calldata concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-004`](../countertechniques/CTFTCTE-BLK-004.md) — Parse transaction logs and calldata

---

## How the challenge author hides

The flag is emitted in an event or passed in calldata rather than stored visibly.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Transaction-log / calldata mining. |

## Tools

- [web3.py](../tools/CTFTTOU-248.md)
- [cast](../tools/CTFTTOU-250.md)
- [block explorers (Etherscan-style)](../tools/CTFTTOU-284.md)

## References

- Add challenge write-up link