# CTFTCTE-REV-004 — Reconstruct the VM and lift its bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-004`](../techniques/CTFTTE-REV-004.md) — Custom VM / bytecode interpreter

---

## Offensive Recovery (CTF practitioner / solver)

Reverse the dispatch loop to recover opcode semantics, then disassemble/lift the bytecode.

## Forensic / Blue-Team Perspective (DFIR analyst)

A documented opcode table turns an opaque interpreter into reviewable logic.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Custom VM bytecode interpretation. |

## Tools

- Ghidra
- IDA
- python
- angr

## References

- Add challenge write-up link