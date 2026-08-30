# REV — Reverse Engineering

> **Tactic ID:** `CTFT-TA-REV`  
> **HTB mapping:** HTB: Reversing  
> **Techniques:** 9

## Description

Concealing logic in binaries/bytecode and reconstructing it.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

> Per-entry related ATT&CK IDs are rendered on every technique and
> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).


## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-REV-001](../techniques/CTFTTE-REV-001.md) | Anti-debugging / anti-analysis guards | [CTFTCTE-REV-001](../countertechniques/CTFTCTE-REV-001.md) | Bypass anti-analysis to reach the check | Complements T1622/T1497 (debugger/sandbox evasion) |
| [CTFTTE-REV-002](../techniques/CTFTTE-REV-002.md) | Packing / runtime self-modification | [CTFTCTE-REV-002](../countertechniques/CTFTCTE-REV-002.md) | Unpack and dump the real code | Complements T1027.002 (Software Packing) with CTF unpack-and |
| [CTFTTE-REV-003](../techniques/CTFTTE-REV-003.md) | Control-flow obfuscation / opaque predicates | [CTFTCTE-REV-003](../countertechniques/CTFTCTE-REV-003.md) | Deobfuscate flattened control flow | No ATT&CK equivalent. |
| [CTFTTE-REV-004](../techniques/CTFTTE-REV-004.md) | Custom VM / bytecode interpreter | [CTFTCTE-REV-004](../countertechniques/CTFTCTE-REV-004.md) | Reconstruct the VM and lift its bytecode | No ATT&CK equivalent. |
| [CTFTTE-REV-005](../techniques/CTFTTE-REV-005.md) | Constraint-gated flag check | [CTFTCTE-REV-005](../countertechniques/CTFTCTE-REV-005.md) | Solve the check with an SMT/symbolic engine | No ATT&CK equivalent. |
| [CTFTTE-REV-006](../techniques/CTFTTE-REV-006.md) | Java bytecode / JAR obfuscation | [CTFTCTE-REV-006](../countertechniques/CTFTCTE-REV-006.md) | Decompile and deobfuscate JVM bytecode | T1027 |
| [CTFTTE-REV-007](../techniques/CTFTTE-REV-007.md) | Python bytecode (.pyc/.pyo) concealment | [CTFTCTE-REV-007](../countertechniques/CTFTCTE-REV-007.md) | Decompile Python bytecode | T1027 |
| [CTFTTE-REV-008](../techniques/CTFTTE-REV-008.md) | Functional-language binary concealment | [CTFTCTE-REV-008](../countertechniques/CTFTCTE-REV-008.md) | Reverse Haskell/functional compiled artifacts | T1027 |
| [CTFTTE-REV-009](../techniques/CTFTTE-REV-009.md) | Assembly-level code-golf / shellcode RE | [CTFTCTE-REV-009](../countertechniques/CTFTCTE-REV-009.md) | Disassemble and annotate asm snippets | T1027 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
