# CTFTCTE-STE-010 — Detect and decode audio-domain stego

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-010`](../techniques/CTFTTE-STE-010.md) — Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV)

---

## Offensive Recovery (CTF practitioner / solver)

Analyze waveform/spectrum, decode DTMF/SSTV, or extract LSB/phase payloads.

## Forensic / Blue-Team Perspective (DFIR analyst)

Audio analysis plots (waveform/spectrum/spectrogram) expose unnatural carriers; decoder selection follows the carrier type.

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
