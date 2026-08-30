# SDR — Software-Defined Radio

> **Tactic ID:** `CTFT-TA-SDR`  
> **HTB mapping:** HTB: Hardware  
> **Techniques:** 1

## Description

Hiding data in RF captures and modulated signals, and recovering it through
SDR demodulation and decoding. Split from HWR (Hardware), which keeps
embedded-device and physical-interface concealment.

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
| [CTFTTE-SDR-001](../techniques/CTFTTE-SDR-001.md) | RF/SDR signal embedding | [CTFTCTE-SDR-001](../countertechniques/CTFTCTE-SDR-001.md) | Demodulate and decode RF captures | T1001.002 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
