# CTFTTE-MOB-004 — DEX obfuscation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-004`](../countertechniques/CTFTCTE-MOB-004.md) — Deobfuscate renamed/obfuscated bytecode

---

## How the challenge author hides

ProGuard/R8 renaming and string encryption hide the flag-producing method.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1406 | Obfuscated Files or Information (Mobile) | DEX obfuscation. |

## Tools

- jadx
- apktool
- python

## References

- Add challenge write-up link