# CTFTTE-REV-009 — Assembly-level code-golf / shellcode RE

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-009`](../countertechniques/CTFTCTE-REV-009.md) — Disassemble and annotate asm snippets

---

## How the challenge author hides

The flag check is a raw asm snippet or mini shellcode; brevity and tricks obscure intent.

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
- Add challenge write-up link
