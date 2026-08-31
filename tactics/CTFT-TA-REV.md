# REV — Reverse Engineering

> **Domain ID:** `CTFT-TA-REV`  
> **HTB mapping:** HTB: Reversing  
> **Techniques:** 9

## Description

Concealing logic in binaries/bytecode and reconstructing it.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-REV-001](../techniques/CTFTTE-REV-001.md) | Anti-debugging / anti-analysis guards | [CTFTCTE-REV-001](../countertechniques/CTFTCTE-REV-001.md) | Bypass anti-analysis to reach the check | T1622 |
| [CTFTTE-REV-002](../techniques/CTFTTE-REV-002.md) | Packing / runtime self-modification | [CTFTCTE-REV-002](../countertechniques/CTFTCTE-REV-002.md) | Unpack and dump the real code | T1027.002 |
| [CTFTTE-REV-003](../techniques/CTFTTE-REV-003.md) | Control-flow obfuscation / opaque predicates | [CTFTCTE-REV-003](../countertechniques/CTFTCTE-REV-003.md) | Deobfuscate flattened control flow | T1027 |
| [CTFTTE-REV-004](../techniques/CTFTTE-REV-004.md) | Custom VM / bytecode interpreter | [CTFTCTE-REV-004](../countertechniques/CTFTCTE-REV-004.md) | Reconstruct the VM and lift its bytecode | T1027 |
| [CTFTTE-REV-005](../techniques/CTFTTE-REV-005.md) | Constraint-gated flag check | [CTFTCTE-REV-005](../countertechniques/CTFTCTE-REV-005.md) | Solve the check with an SMT/symbolic engine | T1480 |
| [CTFTTE-REV-006](../techniques/CTFTTE-REV-006.md) | Java bytecode / JAR obfuscation | [CTFTCTE-REV-006](../countertechniques/CTFTCTE-REV-006.md) | Decompile and deobfuscate JVM bytecode | T1027 |
| [CTFTTE-REV-007](../techniques/CTFTTE-REV-007.md) | Python bytecode (.pyc/.pyo) concealment | [CTFTCTE-REV-007](../countertechniques/CTFTCTE-REV-007.md) | Decompile Python bytecode | T1027 |
| [CTFTTE-REV-008](../techniques/CTFTTE-REV-008.md) | Functional-language binary concealment | [CTFTCTE-REV-008](../countertechniques/CTFTCTE-REV-008.md) | Reverse Haskell/functional compiled artifacts | T1027 |
| [CTFTTE-REV-009](../techniques/CTFTTE-REV-009.md) | Assembly-level code-golf / shellcode RE | [CTFTCTE-REV-009](../countertechniques/CTFTCTE-REV-009.md) | Disassemble and annotate asm snippets | T1027 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
