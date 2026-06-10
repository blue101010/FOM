# CTFTCTE-STE-003 — Reveal data in the audio spectrogram

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-003`](../techniques/CTFTTE-STE-003.md) — Audio spectrogram hiding

---

## Offensive Recovery (CTF practitioner / solver)

Open the file in a spectrogram view and adjust window/contrast to read the embedded content.

## Forensic / Blue-Team Perspective (DFIR analyst)

Spectral analysis exposes synthetic frequency artifacts that natural audio would not contain.

## Tools

- Sonic Visualiser
- Audacity
- sox
- spectrology

## References

- Add challenge write-up link