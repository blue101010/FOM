# HWR — Hardware

> **Domain ID:** `CTFT-TA-HWR`  
> **HTB mapping:** HTB: Hardware  
> **Techniques:** 2

## Description

Hiding data in embedded interfaces/signals and physically extracting it.

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
| [CTFTTE-HWR-001](../techniques/CTFTTE-HWR-001.md) | USB HID keystroke concealment | [CTFTCTE-HWR-001](../countertechniques/CTFTCTE-HWR-001.md) | Reconstruct keystrokes from captured USB HID traffic | T1056.001 |
| [CTFTTE-HWR-002](../techniques/CTFTTE-HWR-002.md) | Badge / embedded-device firmware concealment | [CTFTCTE-HWR-002](../countertechniques/CTFTCTE-HWR-002.md) | Dump and reverse badge firmware | T1027 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
