# CTFTTE-FOR-025 — PDF object/stream hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-025`](../countertechniques/CTFTCTE-FOR-025.md) — Parse PDF xref, streams and filters

---

## How the challenge author hides

The flag is inside PDF objects/streams (FlateDecode), hidden annotations, or appended after %%EOF.

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

- https://blog.didierstevens.com/programs/pdf-tools/
- Add challenge write-up link
