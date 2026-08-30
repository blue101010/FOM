# CTFTCTE-REV-008 — Reverse Haskell/functional compiled artifacts

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-008`](../techniques/CTFTTE-REV-008.md) — Functional-language binary concealment

---

## Offensive Recovery (CTF practitioner / solver)

Locate GHC runtime entry points, identify CAFs and string literals, and reconstruct the evaluation.

## Forensic / Blue-Team Perspective (DFIR analyst)

Functional binaries differ from C: symbol-heavy GHC RTS artifacts still expose strings and structure.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Unusual-runtime binaries resist analysis. |

## Tools

- ghidra
- radare2
- strings

## References

- <https://github.com/radareorg/radare2>

