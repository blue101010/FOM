# CTFTTE-STE-009 — Nested metadata-container embedding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-009`](../countertechniques/CTFTCTE-STE-009.md) — Recursively inspect nested metadata containers

---

## How the challenge author hides

The challenge places clues across nested metadata containers, such as embedded
documents, thumbnails, sidecar records, or recursively embedded media, so a
single top-level metadata listing is incomplete.

## ATT\&CK Complementarity

This is carrier-level challenge craft. It does not assert that metadata presence
alone represents malicious behavior.

## Tools

- ExifTool
- [CTFTTOU-006](../tools/CTFTTOU-006.md)

## References

- https://exiftool.org/