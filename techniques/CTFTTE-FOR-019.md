# CTFTTE-FOR-019 — JPEG marker / DCT coefficient corruption

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-019`](../countertechniques/CTFTCTE-FOR-019.md) — Repair JPEG segments and decode DCT coefficients

---

## How the challenge author hides

JPEG structure is tampered: extraneous bytes before the EOI marker, corrupted quantization tables, or DCT-coefficient tricks hide data.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Structural tampering echoes obfuscation; ATT&CK omits the JPEG repair craft. |

## Tools

- xxd
- Python PIL
- jpegio
- binwalk

## References

- https://github.com/corkami/pics
- Add challenge write-up link
