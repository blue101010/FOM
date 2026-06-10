# CTFTCTE-MOB-002 — Reverse the native .so

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-002`](../techniques/CTFTTE-MOB-002.md) — Native-library logic hiding

---

## Offensive Recovery (CTF practitioner / solver)

Disassemble the ARM/AArch64 library and reverse the routine that produces the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Native reversing recovers logic invisible to bytecode-only analysis.

## Tools

- Ghidra
- IDA
- jadx

## References

- Add challenge write-up link