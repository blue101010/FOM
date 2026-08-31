# FOR — Forensics

> **Domain ID:** `CTFT-TA-FOR`  
> **HTB mapping:** HTB: Forensics  
> **Techniques:** 27

## Description

Challenges where the flag survives in an artifact but not in plain sight: tampered file signatures, slack and unallocated space, falsified timestamps, alternate data streams, memory images, packet captures and unusual encodings. Recovery is structural — read what the container actually is, not what it claims to be.

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
| [CTFTTE-FOR-001](../techniques/CTFTTE-FOR-001.md) | Magic-byte / file-signature tampering | [CTFTCTE-FOR-001](../countertechniques/CTFTCTE-FOR-001.md) | Recover the legitimate file signature | T1027 |
| [CTFTTE-FOR-002](../techniques/CTFTTE-FOR-002.md) | Slack-space and unallocated-area concealment | [CTFTCTE-FOR-002](../countertechniques/CTFTCTE-FOR-002.md) | Carve hidden files from slack/unallocated space | T1564 |
| [CTFTTE-FOR-003](../techniques/CTFTTE-FOR-003.md) | Timestomping (MACB manipulation) | [CTFTCTE-FOR-003](../countertechniques/CTFTCTE-FOR-003.md) | Detect and reconstruct true timestamps | T1070.006 |
| [CTFTTE-FOR-004](../techniques/CTFTTE-FOR-004.md) | NTFS Alternate Data Stream hiding | [CTFTCTE-FOR-004](../countertechniques/CTFTCTE-FOR-004.md) | Enumerate and extract Alternate Data Streams | T1564.004 |
| [CTFTTE-FOR-005](../techniques/CTFTTE-FOR-005.md) | Memory-resident artifact concealment | [CTFTCTE-FOR-005](../countertechniques/CTFTCTE-FOR-005.md) | Recover secrets from a memory image | T1014 |
| [CTFTTE-FOR-006](../techniques/CTFTTE-FOR-006.md) | PCAP payload obfuscation | [CTFTCTE-FOR-006](../countertechniques/CTFTCTE-FOR-006.md) | Reassemble and decode hidden network payloads | T1573 |
| [CTFTTE-FOR-007](../techniques/CTFTTE-FOR-007.md) | Modify legitimate header signature of a file | [CTFTCTE-FOR-007](../countertechniques/CTFTCTE-FOR-007.md) | Recover legitimate signature of a file | T1027 |
| [CTFTTE-FOR-008](../techniques/CTFTTE-FOR-008.md) | OpenEXR header-signature tampering | [CTFTCTE-FOR-008](../countertechniques/CTFTCTE-FOR-008.md) | Recover legitimate header signature of an OpenEXR image file | T1027 |
| [CTFTTE-FOR-009](../techniques/CTFTTE-FOR-009.md) | Corrupt Image file magic signature | [CTFTCTE-FOR-009](../countertechniques/CTFTCTE-FOR-009.md) | Repair a corrupted image magic signature | T1027 |
| [CTFTTE-FOR-010](../techniques/CTFTTE-FOR-010.md) | Use special encoding system to hide data with visual, machine-readable form. | [CTFTCTE-FOR-010](../countertechniques/CTFTCTE-FOR-010.md) | Retrieve information from visual machine-readable encodings | T1027 |
| [CTFTTE-FOR-011](../techniques/CTFTTE-FOR-011.md) | Use special encoding system to hide data with QR codes | [CTFTCTE-FOR-011](../countertechniques/CTFTCTE-FOR-011.md) | Retrieve information from QR codes | T1027 |
| [CTFTTE-FOR-012](../techniques/CTFTTE-FOR-012.md) | Use special encoding system to hide data with RMQR codes | [CTFTCTE-FOR-012](../countertechniques/CTFTCTE-FOR-012.md) | Retrieve information from rMQR codes | T1027 |
| [CTFTTE-FOR-013](../techniques/CTFTTE-FOR-013.md) | Conceal information with diagrams encoding | [CTFTCTE-FOR-013](../countertechniques/CTFTCTE-FOR-013.md) | Retrieve information from diagram encodings | T1027 |
| [CTFTTE-FOR-014](../techniques/CTFTTE-FOR-014.md) | Conceal information with Mengenlehreuhr diagrams encoding | [CTFTCTE-FOR-014](../countertechniques/CTFTCTE-FOR-014.md) | Retrieve information from Mengenlehreuhr diagram encodings | T1027 |
| [CTFTTE-FOR-015](../techniques/CTFTTE-FOR-015.md) | Conceal information with packagers | [CTFTCTE-FOR-015](../countertechniques/CTFTCTE-FOR-015.md) | Recover from packager obfuscations | T1027.002 |
| [CTFTTE-FOR-016](../techniques/CTFTTE-FOR-016.md) | Conceal information with date and time representations | [CTFTCTE-FOR-016](../countertechniques/CTFTCTE-FOR-016.md) | Recover information with date and time representations | T1027 |
| [CTFTTE-FOR-017](../techniques/CTFTTE-FOR-017.md) | Conceal text data strings in ELF binary | [CTFTCTE-FOR-017](../countertechniques/CTFTCTE-FOR-017.md) | Recover text data strings from ELF binary | T1027 |
| [CTFTTE-FOR-018](../techniques/CTFTTE-FOR-018.md) | MFT record and attribute tampering | [CTFTCTE-FOR-018](../countertechniques/CTFTCTE-FOR-018.md) | Analyze orphaned MFT records and raw attributes | T1564.001 |
| [CTFTTE-FOR-019](../techniques/CTFTTE-FOR-019.md) | JPEG marker / DCT coefficient corruption | [CTFTCTE-FOR-019](../countertechniques/CTFTCTE-FOR-019.md) | Repair JPEG segments and decode DCT coefficients | T1027 |
| [CTFTTE-FOR-020](../techniques/CTFTTE-FOR-020.md) | LUKS-encrypted volume concealment | [CTFTCTE-FOR-020](../countertechniques/CTFTCTE-FOR-020.md) | Recover LUKS headers/keyslots, bruteforce passphrase | T1486 |
| [CTFTTE-FOR-021](../techniques/CTFTTE-FOR-021.md) | LVM fragment/concat volume labyrinth | [CTFTCTE-FOR-021](../countertechniques/CTFTCTE-FOR-021.md) | Reassemble LVM logical volumes and mount | T1564 |
| [CTFTTE-FOR-022](../techniques/CTFTTE-FOR-022.md) | Deleted-file / open-handle recovery | [CTFTCTE-FOR-022](../countertechniques/CTFTCTE-FOR-022.md) | Recover deleted files via /proc handles, journal, carving | T1070.004 |
| [CTFTTE-FOR-023](../techniques/CTFTTE-FOR-023.md) | SELinux context-based concealment | [CTFTCTE-FOR-023](../countertechniques/CTFTCTE-FOR-023.md) | Analyze SELinux contexts blocking artifacts | T1562 |
| [CTFTTE-FOR-024](../techniques/CTFTTE-FOR-024.md) | Browser-profile artifact concealment | [CTFTCTE-FOR-024](../countertechniques/CTFTCTE-FOR-024.md) | Parse Firefox/SQLite artifacts (places, logins, cookies) | T1217 |
| [CTFTTE-FOR-025](../techniques/CTFTTE-FOR-025.md) | PDF object/stream hiding | [CTFTCTE-FOR-025](../countertechniques/CTFTCTE-FOR-025.md) | Parse PDF xref, streams and filters | T1027 |
| [CTFTTE-FOR-026](../techniques/CTFTTE-FOR-026.md) | Memory-image OS-artifact recovery | [CTFTCTE-FOR-026](../countertechniques/CTFTCTE-FOR-026.md) | Extract registry/services/process artifacts from memory images | T1003 |
| [CTFTTE-FOR-027](../techniques/CTFTTE-FOR-027.md) | Use JAB colour 2D codes to hide data | [CTFTCTE-FOR-027](../countertechniques/CTFTCTE-FOR-027.md) | Retrieve information from JAB colour codes | T1027 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
