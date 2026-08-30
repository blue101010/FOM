# CTFTTE-SDR-001 — RF/SDR signal embedding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Paired counter-technique:** [`CTFTCTE-SDR-001`](../countertechniques/CTFTCTE-SDR-001.md) — Demodulate and decode RF captures

---

## How the challenge author hides

The flag is transmitted or stored as a modulated RF signal (AM/FM/FSK/PSK), an SDR IQ capture, or a hidden frequency in an audio/RF file; identifying the modulation is the first barrier.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | RF-domain data hiding echoes steganography; ATT&CK omits the demodulation craft. |

## Tools

- Gqrx
- GNU Radio Companion
- Universal Radio Hacker
- inspectrum
- multimon-ng

## References

- <https://github.com/jopohl/urh>
- Add challenge write-up link
