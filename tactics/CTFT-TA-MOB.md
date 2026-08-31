# MOB — Mobile

> **Domain ID:** `CTFT-TA-MOB`  
> **HTB mapping:** HTB: Mobile  
> **Techniques:** 5

## Description

Secrets concealed in mobile apps and runtime, recovered statically/dynamically.

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
| [CTFTTE-MOB-001](../techniques/CTFTTE-MOB-001.md) | Hardcoded secrets in app resources | [CTFTCTE-MOB-001](../countertechniques/CTFTCTE-MOB-001.md) | Decompile the APK and extract secrets | T1552.001 |
| [CTFTTE-MOB-002](../techniques/CTFTTE-MOB-002.md) | Native-library logic hiding | [CTFTCTE-MOB-002](../countertechniques/CTFTCTE-MOB-002.md) | Reverse the native .so | T1406 |
| [CTFTTE-MOB-003](../techniques/CTFTTE-MOB-003.md) | Certificate pinning as capture barrier | [CTFTCTE-MOB-003](../countertechniques/CTFTCTE-MOB-003.md) | Bypass pinning to observe traffic | T1557 |
| [CTFTTE-MOB-004](../techniques/CTFTTE-MOB-004.md) | DEX obfuscation | [CTFTCTE-MOB-004](../countertechniques/CTFTCTE-MOB-004.md) | Deobfuscate renamed/obfuscated bytecode | T1406 |
| [CTFTTE-MOB-005](../techniques/CTFTTE-MOB-005.md) | Runtime/device-conditioned flag | [CTFTCTE-MOB-005](../countertechniques/CTFTCTE-MOB-005.md) | Hook the app to satisfy runtime checks | T1497 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
