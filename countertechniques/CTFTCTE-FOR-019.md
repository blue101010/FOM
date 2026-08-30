# CTFTCTE-FOR-019 — Repair JPEG segments and decode DCT coefficients

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-019`](../techniques/CTFTTE-FOR-019.md) — JPEG marker / DCT coefficient corruption

---

## Offensive Recovery (CTF practitioner / solver)

Parse JPEG segments (SOI..EOI), locate the real image data, repair markers and quantization tables, and decode DCT coefficients.

## Forensic / Blue-Team Perspective (DFIR analyst)

JPEG repair is carving-adjacent: structural anomalies pinpoint the tampered region and often reveal embedded data.

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

- <https://github.com/corkami/pics>

