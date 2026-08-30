# WEB — Web Exploitation

> **Tactic ID:** `CTFT-TA-WEB`  
> **HTB mapping:** HTB: Web  
> **Techniques:** 17

## Description

Hiding/recovering flags inside web applications, APIs and client-side code.

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
| [CTFTTE-WEB-001](../techniques/CTFTTE-WEB-001.md) | Obscured endpoint / source-comment hiding | [CTFTCTE-WEB-001](../countertechniques/CTFTCTE-WEB-001.md) | Content discovery and source review | Complements T1083/T1595 (discovery/recon) but is CTF content |
| [CTFTTE-WEB-002](../techniques/CTFTTE-WEB-002.md) | IDOR / predictable object obscurity | [CTFTCTE-WEB-002](../countertechniques/CTFTCTE-WEB-002.md) | Enumerate insecure direct object references | No direct ATT&CK technique |
| [CTFTTE-WEB-003](../techniques/CTFTTE-WEB-003.md) | JWT misconfiguration | [CTFTCTE-WEB-003](../countertechniques/CTFTCTE-WEB-003.md) | Forge or downgrade a JSON Web Token | No direct ATT&CK technique. |
| [CTFTTE-WEB-004](../techniques/CTFTTE-WEB-004.md) | Blind / WAF-evaded SQL injection | [CTFTCTE-WEB-004](../countertechniques/CTFTCTE-WEB-004.md) | Extract data via blind injection | No direct ATT&CK technique |
| [CTFTTE-WEB-005](../techniques/CTFTTE-WEB-005.md) | Server-side template injection | [CTFTCTE-WEB-005](../countertechniques/CTFTCTE-WEB-005.md) | Exploit template evaluation | No direct ATT&CK technique. |
| [CTFTTE-WEB-006](../techniques/CTFTTE-WEB-006.md) | Client-side obfuscated logic | [CTFTCTE-WEB-006](../countertechniques/CTFTCTE-WEB-006.md) | Deobfuscate and dynamically analyze JS | No direct ATT&CK technique. |
| [CTFTTE-WEB-007](../techniques/CTFTTE-WEB-007.md) | Deployment metadata index disclosure | [CTFTCTE-WEB-007](../countertechniques/CTFTCTE-WEB-007.md) | Analyze a disclosed deployment metadata index | CTF deployment-artifact exposure. |
| [CTFTTE-WEB-008](../techniques/CTFTTE-WEB-008.md) | Legacy short-name namespace disclosure | [CTFTCTE-WEB-008](../countertechniques/CTFTCTE-WEB-008.md) | Reconcile a disclosed short-name namespace | CTF compatibility-layer disclosure. |
| [CTFTTE-WEB-009](../techniques/CTFTTE-WEB-009.md) | Web configuration secret exposure | [CTFTCTE-WEB-009](../countertechniques/CTFTCTE-WEB-009.md) | Classify a configuration secret exposure | CTF configuration-hygiene exposure. |
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
