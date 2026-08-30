# CTFTCTE-STE-004 — Extract concealed metadata fields

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-004`](../techniques/CTFTTE-STE-004.md) — Metadata / EXIF embedding

---

## Offensive Recovery (CTF practitioner / solver)

Dump all metadata and inspect comment/user fields and GPS tags.

## Forensic / Blue-Team Perspective (DFIR analyst)

Full metadata extraction surfaces author-injected fields and inconsistencies versus the file's apparent origin.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Metadata / EXIF embedding. |

## Tools

- exiftool
- exiv2
- strings

## References

- https://exiftool.org/
- Add challenge write-up link