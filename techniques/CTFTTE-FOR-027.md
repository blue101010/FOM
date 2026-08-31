# CTFTTE-FOR-027 — Use JAB colour 2D codes to hide data

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-027`](../countertechniques/CTFTCTE-FOR-027.md) — Retrieve information from JAB colour codes

---

## How the challenge author hides

The payload is encoded as a JAB Code (Just Another Barcode): a colour 2D matrix symbology whose
modules are coloured squares laid out on square or rectangular grids. Because the data lives in the
colour channel rather than in black-and-white modules, ordinary QR readers ignore the symbol
entirely, and a greyscale conversion or an aggressive JPEG recompression destroys the payload
without any visible sign of damage.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Colour 2D matrix encodings are CTF-specific obfuscation ATT&CK omits. |

## Tools

- jabcode reference encoder

## References

- <https://en.wikipedia.org/wiki/JAB_Code>
- <https://github.com/jabcode/jabcode>
- Add challenge write-up link
