# CTFTTE-STE-004 — Metadata / EXIF embedding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-004`](../countertechniques/CTFTCTE-STE-004.md) — Extract concealed metadata fields

---

## How the challenge author hides

The secret sits in EXIF/XMP/ID3 comment, GPS or maker-note fields rather than the visible content.

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