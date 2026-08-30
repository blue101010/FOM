# CTFTTE-STE-011 — Palette / bitplane LSB tricks

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-011`](../countertechniques/CTFTCTE-STE-011.md) — Analyze bitplanes and palette-based LSB

---

## How the challenge author hides

The flag hides in bitplanes or palette indexes of an image (LSB across planes, palette reordering).

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Image-domain data hiding. |

## Tools

- zsteg
- ImageMagick
- Stegsolve

## References

- <https://github.com/zed-0xff/zsteg>
- Add challenge write-up link
