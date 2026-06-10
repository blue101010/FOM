# CTFTTE-REV-001 — Anti-debugging / anti-analysis guards

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-001`](../countertechniques/CTFTCTE-REV-001.md) — Bypass anti-analysis to reach the check

---

## How the challenge author hides

The binary detects debuggers/VMs/timing and alters behaviour or refuses to reveal the flag logic.

## ATT\&CK Complementarity

Complements T1622/T1497 (debugger/sandbox evasion); CTFT adds the reach-the-check workflow.

## Tools

- GDB+GEF
- x64dbg
- Frida
- Ghidra

## References

- https://ghidra-sre.org/
- Add challenge write-up link