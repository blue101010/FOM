# CTFTTE-REV-004 — Custom VM / bytecode interpreter

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-004`](../countertechniques/CTFTCTE-REV-004.md) — Reconstruct the VM and lift its bytecode

---

## How the challenge author hides

The flag check runs on a bespoke virtual machine whose opcodes must be understood first.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- Ghidra
- IDA
- python
- angr

## References

- Add challenge write-up link