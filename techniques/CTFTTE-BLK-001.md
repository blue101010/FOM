# CTFTTE-BLK-001 — Private storage-variable concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-001`](../countertechniques/CTFTCTE-BLK-001.md) — Read contract storage slots directly

---

## How the challenge author hides

The flag is a private variable; the author assumes private means unreadable.

## ATT\&CK Complementarity

No ATT&CK equivalent; smart-contract analysis.

## Tools

- web3.py
- cast (foundry)
- eth_getStorageAt

## References

- <https://book.getfoundry.sh/>
- Add challenge write-up link