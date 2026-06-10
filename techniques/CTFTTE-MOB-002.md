# CTFTTE-MOB-002 — Native-library logic hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-002`](../countertechniques/CTFTCTE-MOB-002.md) — Reverse the native .so

---

## How the challenge author hides

Sensitive logic is pushed into a compiled native library to evade Java-level inspection.

## ATT\&CK Complementarity

No direct ATT&CK technique.

## Tools

- Ghidra
- IDA
- jadx

## References

- Add challenge write-up link