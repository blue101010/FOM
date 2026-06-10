# CTFTCTE-REV-003 — Deobfuscate flattened control flow

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-003`](../techniques/CTFTTE-REV-003.md) — Control-flow obfuscation / opaque predicates

---

## Offensive Recovery (CTF practitioner / solver)

Use symbolic/concolic execution to find the path that satisfies the flag check.

## Forensic / Blue-Team Perspective (DFIR analyst)

Recovering the real CFG documents the obfuscation scheme and the intended logic.

## Tools

- angr
- miasm
- Ghidra
- Triton

## References

- https://angr.io/
- Add challenge write-up link