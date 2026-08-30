# CTFTTE-STE-009 — Nested metadata-container embedding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-009`](../countertechniques/CTFTCTE-STE-009.md) — Recursively inspect nested metadata containers

---

## How the challenge author hides

The challenge places clues across nested metadata containers, such as embedded
documents, thumbnails, sidecar records, or recursively embedded media, so a
single top-level metadata listing is incomplete.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Nested metadata containers. |

## Tools

- ExifTool
- [CTFTTOU-006](../tools/CTFTTOU-006.md)

## References

- https://exiftool.org/