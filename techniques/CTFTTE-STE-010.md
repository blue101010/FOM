# CTFTTE-STE-010 — Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-010`](../countertechniques/CTFTCTE-STE-010.md) — Detect and decode audio-domain stego

---

## How the challenge author hides

Data hides in audio beyond the spectrogram: LSB of samples, phase coding, DTMF tones, or SSTV frames.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Audio-domain data hiding. |

## Tools

- Audacity
- sox
- multimon-ng
- qsstv

## References

- <https://github.com/EliasOenal/multimon-ng>
- Add challenge write-up link
