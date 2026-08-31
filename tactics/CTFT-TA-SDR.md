# SDR — Software-Defined Radio

> **Domain ID:** `CTFT-TA-SDR`  
> **HTB mapping:** HTB: Hardware  
> **Techniques:** 1

## Description

Hiding data in RF captures and modulated signals, and recovering it through
SDR demodulation and decoding. Split from HWR (Hardware), which keeps
embedded-device and physical-interface concealment.

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
| [CTFTTE-SDR-001](../techniques/CTFTTE-SDR-001.md) | RF/SDR signal embedding | [CTFTCTE-SDR-001](../countertechniques/CTFTCTE-SDR-001.md) | Demodulate and decode RF captures | T1001.002 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
