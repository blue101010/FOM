# CTFTCTE-STE-008 — Decode technical text steganography

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-008`](../techniques/CTFTTE-STE-008.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Text steganography conceals a message inside a piece of text through position and formatting
rather than wording. Check, in order: the first letter of each sentence or line, meaningful
typos, punctuation patterns, trailing whitespace, tab-vs-space runs, and zero-width or
homoglyph characters (see [`CTFTCTE-STE-005`](CTFTCTE-STE-005.md) for the invisible-character
case). Normalise the text and diff against the original to expose non-printing carriers.

## Forensic / Blue-Team Perspective (DFIR analyst)

Copy-paste preserves zero-width and whitespace carriers, so the payload often survives into
tickets, chat logs and documents. Hexdump the raw bytes rather than reading the rendered text.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Technical text steganography. |

## Tools

- xxd
- CyberChef
- unicode normalisation scripts

## References

**Sources**

- (1) [Steganography — Wikipedia](https://en.wikipedia.org/wiki/Steganography)

**Writeups**

- Add challenge write-up link
