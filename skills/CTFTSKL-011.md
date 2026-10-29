# CTFTSKL-011 — ctf-stego-lsb

> **Skill ID:** `CTFTSKL-011`  
> **Kind:** Fine-grained skill (one FOM pair)  
> **Related techniques/counters:** CTFTTE-STE-001, CTFTCTE-STE-001

## Description

Extraction workflow for flags hidden in the least-significant bits of image
pixels (PNG/BMP carriers). Operationalises the CTFTCTE-STE-001 recovery action
("run LSB extractors across channels/bit-planes") with FrankySolve's always-on
LSB analysis (null-padded and heuristic-evading payload tolerant), zsteg and
stegsolve as second opinions, and standalone PowerShell/Python one-liners that
pack channel LSBs row-major MSB-first and keep the printable run.

## Skill file

- [ctf-skills-main/ctf-stego-lsb/SKILL.md](../../ctf-skills-main/ctf-stego-lsb/SKILL.md) — canonical

## When to load

```yaml
artifact_type: image                  # .png / .bmp lossless carrier
runtime: offline
evidence:
  - image visually unchanged, no EXIF/outguess hit
  - challenge mentions LSB / stegosaurus-wrecks / RGB LSB prompt-injection filename
  - payload may be null-padded or heuristic-evading (short flag, large clean image)
```

## FOM pairs

- [CTFTTE-STE-001](../techniques/CTFTTE-STE-001.md) / [CTFTCTE-STE-001](../countertechniques/CTFTCTE-STE-001.md) — LSB image steganography / extract least-significant-bit payloads

## Tools

- [CTFTTOU-139 zsteg](../tools/CTFTTOU-139.md)
- [CTFTTOU-138 stegsolve](../tools/CTFTTOU-138.md)
- FrankySolve LSB analysis (`franckysolve/app.py`, `ForensicAnalyzer.lsb_analysis`; regression `franckysolve/tests/test_lsb_extraction.py`)

## Agents

- (none yet)

## Related skills

- [CTFTSKL-003 ctf-evtx](CTFTSKL-003.md) — other fine-grained extraction skill
- frankysolve-chepy — post-extraction decode chains

## Notes

- FrankySolve extraction is unconditional (no LSB-ratio/chi-square gate) and
  scans printable runs, so null-padded prefixes and low-ratio heuristic-evading
  payloads are recovered.
- Palette/bitplane tricks are pair STE-011, not this sheet; audio LSB is STE-010.

## Related Techniques

CTFTTE-STE-001, CTFTCTE-STE-001
