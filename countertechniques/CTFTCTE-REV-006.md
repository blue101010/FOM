# CTFTCTE-REV-006 — Decompile and deobfuscate JVM bytecode

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-006`](../techniques/CTFTTE-REV-006.md) — Java bytecode / JAR obfuscation

---

## Offensive Recovery (CTF practitioner / solver)

Decompile with CFR/JD-GUI, recover strings, trace the flag check, and reimplement the logic.

## Forensic / Blue-Team Perspective (DFIR analyst)

Java artifacts preserve bytecode-level evidence; decompilers reconstruct behavior without the source.

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

