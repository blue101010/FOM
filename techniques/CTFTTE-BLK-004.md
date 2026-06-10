# CTFTTE-BLK-004 — Hidden event-log / calldata concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-004`](../countertechniques/CTFTCTE-BLK-004.md) — Parse transaction logs and calldata

---

## How the challenge author hides

The flag is emitted in an event or passed in calldata rather than stored visibly.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- web3.py
- cast
- etherscan-style explorers

## References

- Add challenge write-up link