# CTFTTE-STE-003 — Audio spectrogram hiding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Paired counter-technique:** [`CTFTCTE-STE-003`](../countertechniques/CTFTCTE-STE-003.md) — Reveal data in the audio spectrogram

---

## How the challenge author hides

Text or a QR is drawn into frequency content so it is inaudible but visible in a spectrogram.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Spectrogram embedding. |

## Tools

- Sonic Visualiser
- Audacity
- sox
- spectrology

## References

- Add challenge write-up link