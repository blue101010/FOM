# CTFTCTE-FOR-025 — Parse PDF xref, streams and filters

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-025`](../techniques/CTFTTE-FOR-025.md) — PDF object/stream hiding

---

## Offensive Recovery (CTF practitioner / solver)

Parse the xref, decompress streams (qpdf/pdftk), and dump objects for strings.

## Forensic / Blue-Team Perspective (DFIR analyst)

PDFs are compound artifacts; unparsed objects and post-EOF data are classic hiding spots.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Container-level hiding echoes obfuscation. |

## Tools

- qpdf
- pdftk
- pdf-parser.py
- strings

## References

- <https://blog.didierstevens.com/programs/pdf-tools/>

