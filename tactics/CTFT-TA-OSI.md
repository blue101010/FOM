# OSI — OSINT

> **Tactic ID:** `CTFT-TA-OSI`  
> **HTB mapping:** HTB: OSINT  
> **Techniques:** 5

## Description

Information dispersed across public sources and correlated back together.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-OSI-001](../techniques/CTFTTE-OSI-001.md) | Metadata-dispersed identity/location | [CTFTCTE-OSI-001](../countertechniques/CTFTCTE-OSI-001.md) | Correlate leaked metadata | Complements the Reconnaissance tactic conceptually |
| [CTFTTE-OSI-002](../techniques/CTFTTE-OSI-002.md) | Cross-platform username pivot | [CTFTCTE-OSI-002](../countertechniques/CTFTCTE-OSI-002.md) | Enumerate accounts across platforms | No direct ATT&CK technique. |
| [CTFTTE-OSI-003](../techniques/CTFTTE-OSI-003.md) | Historical / cached content concealment | [CTFTCTE-OSI-003](../countertechniques/CTFTCTE-OSI-003.md) | Recover deleted or changed content | No direct ATT&CK technique. |
| [CTFTTE-OSI-004](../techniques/CTFTTE-OSI-004.md) | Geolocation from imagery | [CTFTCTE-OSI-004](../countertechniques/CTFTCTE-OSI-004.md) | Geolocate using visual cues | No direct ATT&CK technique. |
| [CTFTTE-OSI-005](../techniques/CTFTTE-OSI-005.md) | Public-record / repo leak pivot | [CTFTCTE-OSI-005](../countertechniques/CTFTCTE-OSI-005.md) | Mine public repositories and records | Complements T1213/T1593 (info from repositories) with CTF ar |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
