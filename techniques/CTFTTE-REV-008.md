# CTFTTE-REV-008 — Functional-language binary concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-008`](../countertechniques/CTFTCTE-REV-008.md) — Reverse Haskell/functional compiled artifacts

---

## How the challenge author hides

The binary is compiled Haskell (GHC runtime); closures and lazy evaluation obscure the flag logic.

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
- Add challenge write-up link
