# CTFTCTE-MOB-004 — Deobfuscate renamed/obfuscated bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-004`](../techniques/CTFTTE-MOB-004.md) — DEX obfuscation

---

## Offensive Recovery (CTF practitioner / solver)

Decompile and rename systematically, decrypting strings to locate the logic.

## Forensic / Blue-Team Perspective (DFIR analyst)

A reconstructed call graph documents the obfuscation and the recovered routine.

## Tools

- jadx
- apktool
- python

## References

- Add challenge write-up link