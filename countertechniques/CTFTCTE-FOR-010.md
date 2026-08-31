# CTFTCTE-FOR-010 — Retrieve information from visual machine-readable encodings

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-010`](../techniques/CTFTTE-FOR-010.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Identify which visual symbology carries the payload before attempting any decode: matrix
geometry (square vs rectangular), module count, finding/alignment patterns, colour depth and
quiet-zone geometry each narrow the family. Once the symbology is known, delegate to the
specific counter-technique: QR ([`CTFTCTE-FOR-011`](CTFTCTE-FOR-011.md)), rMQR
([`CTFTCTE-FOR-012`](CTFTCTE-FOR-012.md)) or JAB colour codes
([`CTFTCTE-FOR-027`](CTFTCTE-FOR-027.md)). When no decoder recognises the symbol, treat the
grid as raw bits and reconstruct the encoding from the published specification.

## Forensic / Blue-Team Perspective (DFIR analyst)

Visual encodings survive re-photography and screenshotting, so the carrier image often
outlives the artifact it came from. Preserve the original raster before any enhancement:
resampling destroys module boundaries and makes later decoding impossible.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Visual machine-readable encodings are CTF-specific obfuscation ATT&CK omits. |

## Tools

_Symbology-dependent — see the child counter-techniques._

## References

**Sources**

- (1) [QR Code Model 2 Structure and Algorithms](https://franckybox.com/wp-content/uploads/qrcode.pdf)
- (2) [JAB Code specification](https://github.com/jabcode/jabcode)
