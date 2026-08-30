# CTFTTE-REV-006 — Java bytecode / JAR obfuscation

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-006`](../countertechniques/CTFTCTE-REV-006.md) — Decompile and deobfuscate JVM bytecode

---

## How the challenge author hides

The flag check lives in obfuscated or compiled Java (JAR/class); strings and control flow are mangled.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Bytecode obfuscation. |

## Tools

- CFR
- jd-gui
- javap
- procyon

## References

- <https://github.com/leibnitz27/cfr>
- Add challenge write-up link
