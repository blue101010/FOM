# STE — Steganography

> **Tactic ID:** `CTFT-TA-STE`  
> **HTB mapping:** HTB: Forensics/Misc (Stego)  
> **Techniques:** 11

## Description

CTFT steganography techniques complement ATT&CK at the carrier-level embedding and extraction detail ATT&CK omits.

## Relation to MITRE ATT\&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

> Per-entry related ATT&CK IDs are rendered on every technique and
> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).


## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name |
| --- | --- | --- | --- |
| [CTFTTE-STE-001](../techniques/CTFTTE-STE-001.md) | LSB image steganography | [CTFTCTE-STE-001](../countertechniques/CTFTCTE-STE-001.md) | Extract least-significant-bit payloads |
| [CTFTTE-STE-002](../techniques/CTFTTE-STE-002.md) | Appended data / polyglot after EOF | [CTFTCTE-STE-002](../countertechniques/CTFTCTE-STE-002.md) | Detect and split appended/embedded files |
| [CTFTTE-STE-003](../techniques/CTFTTE-STE-003.md) | Audio spectrogram hiding | [CTFTCTE-STE-003](../countertechniques/CTFTCTE-STE-003.md) | Reveal data in the audio spectrogram |
| [CTFTTE-STE-004](../techniques/CTFTTE-STE-004.md) | Metadata / EXIF embedding | [CTFTCTE-STE-004](../countertechniques/CTFTCTE-STE-004.md) | Extract concealed metadata fields |
| [CTFTTE-STE-005](../techniques/CTFTTE-STE-005.md) | Zero-width / whitespace text steganography | [CTFTCTE-STE-005](../countertechniques/CTFTCTE-STE-005.md) | Decode invisible-character payloads |
| [CTFTTE-STE-006](../techniques/CTFTTE-STE-006.md) | Conceal information within digital media with **linguistic** steganograp | [CTFTCTE-STE-006](../countertechniques/CTFTCTE-STE-006.md) | Counter — Conceal information within digital media with **linguistic** s |
| [CTFTTE-STE-007](../techniques/CTFTTE-STE-007.md) | Conceal information within digital media with **technical** steganograph | [CTFTCTE-STE-007](../countertechniques/CTFTCTE-STE-007.md) | Counter — Conceal information within digital media with **technical** st |
| [CTFTTE-STE-008](../techniques/CTFTTE-STE-008.md) | Conceal via **technical text** steganography | [CTFTCTE-STE-008](../countertechniques/CTFTCTE-STE-008.md) | Counter — Conceal via **technical text** steganography |
| [CTFTTE-STE-009](../techniques/CTFTTE-STE-009.md) | Nested metadata-container embedding | [CTFTCTE-STE-009](../countertechniques/CTFTCTE-STE-009.md) | Recursively inspect nested metadata containers |
| [CTFTTE-STE-010](../techniques/CTFTTE-STE-010.md) | Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV) | [CTFTCTE-STE-010](../countertechniques/CTFTCTE-STE-010.md) | Detect and decode audio-domain stego | T1001.002 |
| [CTFTTE-STE-011](../techniques/CTFTTE-STE-011.md) | Palette / bitplane LSB tricks | [CTFTCTE-STE-011](../countertechniques/CTFTCTE-STE-011.md) | Analyze bitplanes and palette-based LSB | T1001.002 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
