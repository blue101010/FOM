# CTFTCTE-REV-009 — Disassemble and annotate asm snippets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-009`](../techniques/CTFTTE-REV-009.md) — Assembly-level code-golf / shellcode RE

---

## Offensive Recovery (CTF practitioner / solver)

Disassemble (nasm/objdump/radare2), annotate registers and stack, and trace the check.

## Forensic / Blue-Team Perspective (DFIR analyst)

Raw instruction sequences are analyzed the same way as extracted shellcode evidence.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Code-golf obfuscation. |

## Tools

- nasm
- objdump
- radare2
- ghidra

## References

- <https://www.nasm.us/>

