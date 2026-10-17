# CTFTCTE-BLK-004 — Parse transaction logs and calldata

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Counters technique:** [`CTFTTE-BLK-004`](../techniques/CTFTTE-BLK-004.md) — Hidden event-log / calldata concealment

---

## Offensive Recovery (CTF practitioner / solver)

Decode historical logs and transaction input data to recover the value.

## Forensic / Blue-Team Perspective (DFIR analyst)

Decoded logs/calldata reconstruct the off-state data flow of the contract.

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