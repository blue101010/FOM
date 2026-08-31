# STE — Steganography

> **Domain ID:** `CTFT-TA-STE`  
> **HTB mapping:** HTB: Forensics/Misc (Stego)  
> **Techniques:** 11

## Description

Challenges where a payload is embedded inside an otherwise valid carrier — image bitplanes, audio spectrograms, metadata containers, invisible characters or the wording of a text — so that the carrier stays openable and looks untouched. Recovery works on the carrier's representation rather than its content.

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
| [CTFTTE-STE-001](../techniques/CTFTTE-STE-001.md) | LSB image steganography | [CTFTCTE-STE-001](../countertechniques/CTFTCTE-STE-001.md) | Extract least-significant-bit payloads | T1001.002 |
| [CTFTTE-STE-002](../techniques/CTFTTE-STE-002.md) | Appended data / polyglot after EOF | [CTFTCTE-STE-002](../countertechniques/CTFTCTE-STE-002.md) | Detect and split appended/embedded files | T1001.002 |
| [CTFTTE-STE-003](../techniques/CTFTTE-STE-003.md) | Audio spectrogram hiding | [CTFTCTE-STE-003](../countertechniques/CTFTCTE-STE-003.md) | Reveal data in the audio spectrogram | T1001.002 |
| [CTFTTE-STE-004](../techniques/CTFTTE-STE-004.md) | Metadata / EXIF embedding | [CTFTCTE-STE-004](../countertechniques/CTFTCTE-STE-004.md) | Extract concealed metadata fields | T1001.002 |
| [CTFTTE-STE-005](../techniques/CTFTTE-STE-005.md) | Zero-width / whitespace text steganography | [CTFTCTE-STE-005](../countertechniques/CTFTCTE-STE-005.md) | Decode invisible-character payloads | T1001.002 |
| [CTFTTE-STE-006](../techniques/CTFTTE-STE-006.md) | Conceal information within digital media with **linguistic** steganography | [CTFTCTE-STE-006](../countertechniques/CTFTCTE-STE-006.md) | Detect and decode linguistic steganography | T1001.002 |
| [CTFTTE-STE-007](../techniques/CTFTTE-STE-007.md) | Conceal information within digital media with **technical** steganography | [CTFTCTE-STE-007](../countertechniques/CTFTCTE-STE-007.md) | Detect and extract technical steganography | T1001.002 |
| [CTFTTE-STE-008](../techniques/CTFTTE-STE-008.md) | Conceal via **technical text** steganography | [CTFTCTE-STE-008](../countertechniques/CTFTCTE-STE-008.md) | Decode technical text steganography | T1001.002 |
| [CTFTTE-STE-009](../techniques/CTFTTE-STE-009.md) | Nested metadata-container embedding | [CTFTCTE-STE-009](../countertechniques/CTFTCTE-STE-009.md) | Recursively inspect nested metadata containers | T1001.002 |
| [CTFTTE-STE-010](../techniques/CTFTTE-STE-010.md) | Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV) | [CTFTCTE-STE-010](../countertechniques/CTFTCTE-STE-010.md) | Detect and decode audio-domain stego | T1001.002 |
| [CTFTTE-STE-011](../techniques/CTFTTE-STE-011.md) | Palette / bitplane LSB tricks | [CTFTCTE-STE-011](../countertechniques/CTFTCTE-STE-011.md) | Analyze bitplanes and palette-based LSB | T1001.002 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
