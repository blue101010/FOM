# OSI — OSINT

> **Domain ID:** `CTFT-TA-OSI`  
> **HTB mapping:** HTB: OSINT  
> **Techniques:** 8

## Description

Information dispersed across public sources and correlated back together.

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
| [CTFTTE-OSI-001](../techniques/CTFTTE-OSI-001.md) | Metadata-dispersed identity/location | [CTFTCTE-OSI-001](../countertechniques/CTFTCTE-OSI-001.md) | Correlate leaked metadata | T1589 |
| [CTFTTE-OSI-002](../techniques/CTFTTE-OSI-002.md) | Cross-platform username pivot | [CTFTCTE-OSI-002](../countertechniques/CTFTCTE-OSI-002.md) | Enumerate accounts across platforms | T1593 |
| [CTFTTE-OSI-003](../techniques/CTFTTE-OSI-003.md) | Historical / cached content concealment | [CTFTCTE-OSI-003](../countertechniques/CTFTCTE-OSI-003.md) | Recover deleted or changed content | T1593.002 |
| [CTFTTE-OSI-004](../techniques/CTFTTE-OSI-004.md) | Geolocation from imagery | [CTFTCTE-OSI-004](../countertechniques/CTFTCTE-OSI-004.md) | Geolocate using visual cues | T1589 |
| [CTFTTE-OSI-005](../techniques/CTFTTE-OSI-005.md) | Public-record / repo leak pivot | [CTFTCTE-OSI-005](../countertechniques/CTFTCTE-OSI-005.md) | Mine public repositories and records | T1596 |
| [CTFTTE-OSI-006](../techniques/CTFTTE-OSI-006.md) | Git-repository archaeology | [CTFTCTE-OSI-006](../countertechniques/CTFTCTE-OSI-006.md) | Mine git history, objects and reflog | T1596 |
| [CTFTTE-OSI-007](../techniques/CTFTTE-OSI-007.md) | Search-engine mining (dorking) | [CTFTCTE-OSI-007](../countertechniques/CTFTCTE-OSI-007.md) | Run advanced dorks and search operators | T1593.002 |
| [CTFTTE-OSI-008](../techniques/CTFTTE-OSI-008.md) | ASN / IP-range / subdomain recon | [CTFTCTE-OSI-008](../countertechniques/CTFTCTE-OSI-008.md) | Map ASN, ranges, subdomains (bbot, assetfinder) | T1596.001 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
