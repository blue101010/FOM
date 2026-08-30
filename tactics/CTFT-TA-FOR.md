# FOR — Forensics

> **Tactic ID:** `CTFT-TA-FOR`  
> **HTB mapping:** HTB: Forensics  
> **Techniques:** 18

## Description

CTFT forensic techniques complement ATT&CK at the artifact-recovery level (file carving, memory analysis, timestamp forensics, encoding schemes).

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
| [CTFTTE-FOR-001](../techniques/CTFTTE-FOR-001.md) | Magic-byte / file-signature tampering | [CTFTCTE-FOR-001](../countertechniques/CTFTCTE-FOR-001.md) | Recover the legitimate file signature |
| [CTFTTE-FOR-002](../techniques/CTFTTE-FOR-002.md) | Slack-space and unallocated-area concealment | [CTFTCTE-FOR-002](../countertechniques/CTFTCTE-FOR-002.md) | Carve hidden files from slack/unallocated space |
| [CTFTTE-FOR-003](../techniques/CTFTTE-FOR-003.md) | Timestomping (MACB manipulation) | [CTFTCTE-FOR-003](../countertechniques/CTFTCTE-FOR-003.md) | Detect and reconstruct true timestamps |
| [CTFTTE-FOR-004](../techniques/CTFTTE-FOR-004.md) | NTFS Alternate Data Stream hiding | [CTFTCTE-FOR-004](../countertechniques/CTFTCTE-FOR-004.md) | Enumerate and extract Alternate Data Streams |
| [CTFTTE-FOR-005](../techniques/CTFTTE-FOR-005.md) | Memory-resident artifact concealment | [CTFTCTE-FOR-005](../countertechniques/CTFTCTE-FOR-005.md) | Recover secrets from a memory image |
| [CTFTTE-FOR-006](../techniques/CTFTTE-FOR-006.md) | PCAP payload obfuscation | [CTFTCTE-FOR-006](../countertechniques/CTFTCTE-FOR-006.md) | Reassemble and decode hidden network payloads |
| [CTFTTE-FOR-007](../techniques/CTFTTE-FOR-007.md) | Modify legitimate header signature of a file | [CTFTCTE-FOR-007](../countertechniques/CTFTCTE-FOR-007.md) | Recover legitimate signature of a file |
| [CTFTTE-FOR-008](../techniques/CTFTTE-FOR-008.md) | Modify legitimate header signature of a file via python script | [CTFTCTE-FOR-008](../countertechniques/CTFTCTE-FOR-008.md) | Recover legitimate header signature of an OpenEXR image file |
| [CTFTTE-FOR-009](../techniques/CTFTTE-FOR-009.md) | Corrupt Image file magic signature | [CTFTCTE-FOR-009](../countertechniques/CTFTCTE-FOR-009.md) | Counter — Corrupt Image file magic signature |
| [CTFTTE-FOR-010](../techniques/CTFTTE-FOR-010.md) | Use special encoding system to hide data with visual, machine-readable f | [CTFTCTE-FOR-010](../countertechniques/CTFTCTE-FOR-010.md) | Retrieve information from QR codes |
| [CTFTTE-FOR-011](../techniques/CTFTTE-FOR-011.md) | Use special encoding system to hide data with QR codes | [CTFTCTE-FOR-011](../countertechniques/CTFTCTE-FOR-011.md) | Retrieve information from rMQR codes |
| [CTFTTE-FOR-012](../techniques/CTFTTE-FOR-012.md) | Use special encoding system to hide data with RMQR codes | [CTFTCTE-FOR-012](../countertechniques/CTFTCTE-FOR-012.md) | Retrieve information from JAB QR codes (2D color bar code) |
| [CTFTTE-FOR-013](../techniques/CTFTTE-FOR-013.md) | Conceal information with diagrams encoding | [CTFTCTE-FOR-013](../countertechniques/CTFTCTE-FOR-013.md) | Retrieve information from Mengenlehreuhr diagrams encoding |
| [CTFTTE-FOR-014](../techniques/CTFTTE-FOR-014.md) | Conceal information with Mengenlehreuhr diagrams encoding | [CTFTCTE-FOR-014](../countertechniques/CTFTCTE-FOR-014.md) | Counter — Conceal information with Mengenlehreuhr diagrams encoding |
| [CTFTTE-FOR-015](../techniques/CTFTTE-FOR-015.md) | Conceal information with packagers | [CTFTCTE-FOR-015](../countertechniques/CTFTCTE-FOR-015.md) | Recover from packager obfuscations |
| [CTFTTE-FOR-016](../techniques/CTFTTE-FOR-016.md) | Conceal information with date and time representations | [CTFTCTE-FOR-016](../countertechniques/CTFTCTE-FOR-016.md) | Recover information with date and time representations |
| [CTFTTE-FOR-017](../techniques/CTFTTE-FOR-017.md) | Conceal text data strings in ELF binary | [CTFTCTE-FOR-017](../countertechniques/CTFTCTE-FOR-017.md) | Recover text data strings from ELF binary |
| [CTFTTE-FOR-018](../techniques/CTFTTE-FOR-018.md) | MFT record and attribute tampering | [CTFTCTE-FOR-018](../countertechniques/CTFTCTE-FOR-018.md) | Analyze orphaned MFT records and raw attributes |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
