# CTFTTE-BLK-002 — Reentrancy-gated flag

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-BLK`](../tactics/CTFT-TA-BLK.md) — Blockchain  
> **Paired counter-technique:** [`CTFTCTE-BLK-002`](../countertechniques/CTFTCTE-BLK-002.md) — Exploit reentrancy to set the flag

---

## How the challenge author hides

The flag only flips after a withdraw/transfer flow vulnerable to reentrancy.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- foundry
- hardhat
- solidity

## References

- Add challenge write-up link