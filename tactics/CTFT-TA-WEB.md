# WEB — Web Exploitation

> **Domain ID:** `CTFT-TA-WEB`  
> **HTB mapping:** HTB: Web  
> **Techniques:** 17

## Description

Hiding/recovering flags inside web applications, APIs and client-side code.

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
| [CTFTTE-WEB-001](../techniques/CTFTTE-WEB-001.md) | Obscured endpoint / source-comment hiding | [CTFTCTE-WEB-001](../countertechniques/CTFTCTE-WEB-001.md) | Content discovery and source review | T1552.001 |
| [CTFTTE-WEB-002](../techniques/CTFTTE-WEB-002.md) | IDOR / predictable object obscurity | [CTFTCTE-WEB-002](../countertechniques/CTFTCTE-WEB-002.md) | Enumerate insecure direct object references | T1213 |
| [CTFTTE-WEB-003](../techniques/CTFTTE-WEB-003.md) | JWT misconfiguration | [CTFTCTE-WEB-003](../countertechniques/CTFTCTE-WEB-003.md) | Forge or downgrade a JSON Web Token | T1606 |
| [CTFTTE-WEB-004](../techniques/CTFTTE-WEB-004.md) | Blind / WAF-evaded SQL injection | [CTFTCTE-WEB-004](../countertechniques/CTFTCTE-WEB-004.md) | Extract data via blind injection | T1190 |
| [CTFTTE-WEB-005](../techniques/CTFTTE-WEB-005.md) | Server-side template injection | [CTFTCTE-WEB-005](../countertechniques/CTFTCTE-WEB-005.md) | Exploit template evaluation | T1190 |
| [CTFTTE-WEB-006](../techniques/CTFTTE-WEB-006.md) | Client-side obfuscated logic | [CTFTCTE-WEB-006](../countertechniques/CTFTCTE-WEB-006.md) | Deobfuscate and dynamically analyze JS | T1027 |
| [CTFTTE-WEB-007](../techniques/CTFTTE-WEB-007.md) | Deployment metadata index disclosure | [CTFTCTE-WEB-007](../countertechniques/CTFTCTE-WEB-007.md) | Analyze a disclosed deployment metadata index | T1083 |
| [CTFTTE-WEB-008](../techniques/CTFTTE-WEB-008.md) | Legacy short-name namespace disclosure | [CTFTCTE-WEB-008](../countertechniques/CTFTCTE-WEB-008.md) | Reconcile a disclosed short-name namespace | T1083 |
| [CTFTTE-WEB-009](../techniques/CTFTTE-WEB-009.md) | Web configuration secret exposure | [CTFTCTE-WEB-009](../countertechniques/CTFTCTE-WEB-009.md) | Classify a configuration secret exposure | T1552 |
| [CTFTTE-WEB-010](../techniques/CTFTTE-WEB-010.md) | LFI / log poisoning / php-filter chains | [CTFTCTE-WEB-010](../countertechniques/CTFTCTE-WEB-010.md) | Exploit LFI to RCE or flag read | T1190 |
| [CTFTTE-WEB-011](../techniques/CTFTTE-WEB-011.md) | Directory-traversal maze | [CTFTCTE-WEB-011](../countertechniques/CTFTCTE-WEB-011.md) | Traverse filtered paths (PHP labyrinth) | T1190 |
| [CTFTTE-WEB-012](../techniques/CTFTTE-WEB-012.md) | XSS-driven flag exfiltration | [CTFTCTE-WEB-012](../countertechniques/CTFTCTE-WEB-012.md) | Craft XSS payloads (stored/reflected/DOM) | T1059.007 |
| [CTFTTE-WEB-013](../techniques/CTFTTE-WEB-013.md) | CSRF-gated state change | [CTFTCTE-WEB-013](../countertechniques/CTFTCTE-WEB-013.md) | Forge cross-site requests | T1606 |
| [CTFTTE-WEB-014](../techniques/CTFTTE-WEB-014.md) | WebSocket message hiding | [CTFTCTE-WEB-014](../countertechniques/CTFTCTE-WEB-014.md) | Intercept and decode WebSocket traffic | T1071.001 |
| [CTFTTE-WEB-015](../techniques/CTFTTE-WEB-015.md) | CMS / WordPress plugin flaw | [CTFTCTE-WEB-015](../countertechniques/CTFTCTE-WEB-015.md) | Enumerate and exploit WordPress (wpscan) | T1190 |
| [CTFTTE-WEB-016](../techniques/CTFTTE-WEB-016.md) | NoSQL injection | [CTFTCTE-WEB-016](../countertechniques/CTFTCTE-WEB-016.md) | Inject Mongo/NoSQL queries | T1190 |
| [CTFTTE-WEB-017](../techniques/CTFTTE-WEB-017.md) | Host-header / vhost fuzzing | [CTFTCTE-WEB-017](../countertechniques/CTFTCTE-WEB-017.md) | Fuzz vhosts and host headers | T1083 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
