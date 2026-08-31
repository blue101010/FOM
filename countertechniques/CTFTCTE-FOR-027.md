# CTFTCTE-FOR-027 — Retrieve information from JAB colour codes

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-027`](../techniques/CTFTTE-FOR-027.md)  

---

## Offensive Recovery (CTF practitioner / solver)

JAB Code (Just Another Barcode) is a colour 2D matrix symbology made of colour squares arranged in
either square or rectangular grids. Decode with the reference `jabcode` reader rather than a QR
library. Work from the highest-fidelity copy available: the colour palette carries data, so any
greyscale conversion, palette reduction or lossy recompression is destructive.

## Forensic / Blue-Team Perspective (DFIR analyst)

The symbology is uncommon enough that its presence is itself an authorship signal. Preserve the
original raster and record the palette before enhancement.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Colour 2D matrix encodings are CTF-specific obfuscation ATT&CK omits. |

## Tools

- jabcode reference decoder

## References

**Sources**

- (1) <https://en.wikipedia.org/wiki/JAB_Code>
- (2) <https://github.com/jabcode/jabcode>

**Writeups**

- Add challenge write-up link
