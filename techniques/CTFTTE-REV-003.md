# CTFTTE-REV-003 — Control-flow obfuscation / opaque predicates

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-003`](../countertechniques/CTFTCTE-REV-003.md) — Deobfuscate flattened control flow

---

## How the challenge author hides

Flattening, junk branches and opaque predicates make the real path hard to follow.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- angr
- miasm
- Ghidra
- Triton

## References

- https://angr.io/
- Add challenge write-up link