# MOB — Mobile

> **Tactic ID:** `CTFT-TA-MOB`  
> **HTB mapping:** HTB: Mobile  
> **Techniques:** 5

## Description

Secrets concealed in mobile apps and runtime, recovered statically/dynamically.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-MOB-001](../techniques/CTFTTE-MOB-001.md) | Hardcoded secrets in app resources | [CTFTCTE-MOB-001](../countertechniques/CTFTCTE-MOB-001.md) | Decompile the APK and extract secrets | No direct ATT&CK technique |
| [CTFTTE-MOB-002](../techniques/CTFTTE-MOB-002.md) | Native-library logic hiding | [CTFTCTE-MOB-002](../countertechniques/CTFTCTE-MOB-002.md) | Reverse the native .so | No direct ATT&CK technique. |
| [CTFTTE-MOB-003](../techniques/CTFTTE-MOB-003.md) | Certificate pinning as capture barrier | [CTFTCTE-MOB-003](../countertechniques/CTFTCTE-MOB-003.md) | Bypass pinning to observe traffic | No direct ATT&CK technique. |
| [CTFTTE-MOB-004](../techniques/CTFTTE-MOB-004.md) | DEX obfuscation | [CTFTCTE-MOB-004](../countertechniques/CTFTCTE-MOB-004.md) | Deobfuscate renamed/obfuscated bytecode | No direct ATT&CK technique. |
| [CTFTTE-MOB-005](../techniques/CTFTTE-MOB-005.md) | Runtime/device-conditioned flag | [CTFTCTE-MOB-005](../countertechniques/CTFTCTE-MOB-005.md) | Hook the app to satisfy runtime checks | No direct ATT&CK technique. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
