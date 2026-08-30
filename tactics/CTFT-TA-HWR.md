# HWR — Hardware

> **Tactic ID:** `CTFT-TA-HWR`  
> **HTB mapping:** HTB: Hardware  
> **Techniques:** 2

## Description

Hiding data in embedded interfaces/signals and physically extracting it.

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
| [CTFTTE-HWR-001](../techniques/CTFTTE-HWR-001.md) | USB HID keystroke concealment | [CTFTCTE-HWR-001](../countertechniques/CTFTCTE-HWR-001.md) | Reconstruct keystrokes from captured USB HID traffic | T1056.001 |
| [CTFTTE-HWR-002](../techniques/CTFTTE-HWR-002.md) | Badge / embedded-device firmware concealment | [CTFTCTE-HWR-002](../countertechniques/CTFTCTE-HWR-002.md) | Dump and reverse badge firmware | T1027 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
