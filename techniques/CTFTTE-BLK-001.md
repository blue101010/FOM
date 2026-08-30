# CTFTTE-BLK-001 — Private storage-variable concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-001`](../countertechniques/CTFTCTE-BLK-001.md) — Read contract storage slots directly

---

## How the challenge author hides

The flag is a private variable; the author assumes private means unreadable.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Storage-slot reading echoes data-from-repositories. |

## Tools

- web3.py
- cast (foundry)
- eth_getStorageAt

## References

- <https://book.getfoundry.sh/>
- Add challenge write-up link