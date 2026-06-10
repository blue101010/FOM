# CTFTTE-MOB-004 — DEX obfuscation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-004`](../countertechniques/CTFTCTE-MOB-004.md) — Deobfuscate renamed/obfuscated bytecode

---

## How the challenge author hides

ProGuard/R8 renaming and string encryption hide the flag-producing method.

## ATT\&CK Complementarity

No direct ATT&CK technique.

## Tools

- jadx
- apktool
- python

## References

- Add challenge write-up link