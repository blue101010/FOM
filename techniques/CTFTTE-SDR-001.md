# CTFTTE-SDR-001 — RF/SDR signal embedding

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Paired counter-technique:** [`CTFTCTE-SDR-001`](../countertechniques/CTFTCTE-SDR-001.md) — Demodulate and decode RF captures

---

## How the challenge author hides

The flag is transmitted or stored as a modulated RF signal (AM/FM/FSK/PSK), an SDR IQ capture, or a hidden frequency in an audio/RF file; identifying the modulation is the first barrier. This is the umbrella entry. More specific shapes have their own pairs:

- CTFTTE-SDR-002: a line-coded on-off-keyed remote;
- CTFTTE-SDR-003: an unlabelled capture;
- CTFTTE-SDR-004: a standard radio protocol;
- CTFTTE-SDR-005: a transmitter hidden in a live spectrum.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | RF-domain data hiding echoes steganography; ATT&CK omits the demodulation craft. |

## Tools

- [Gqrx](../tools/CTFTTOU-234.md)
- [GNU Radio Companion](../tools/CTFTTOU-233.md)
- [Universal Radio Hacker](../tools/CTFTTOU-235.md)
- [inspectrum](../tools/CTFTTOU-236.md)
- [multimon-ng](../tools/CTFTTOU-237.md)
- [SigDigger](../tools/CTFTTOU-338.md)
- [iq_check.py](../../.agents/ctf/ctf-sdr/scripts/iq_check.py) ([CTFTTOU-341](../tools/CTFTTOU-341.md))
- [iq_demod.py](../../.agents/ctf/ctf-sdr/scripts/iq_demod.py) ([CTFTTOU-343](../tools/CTFTTOU-343.md))
- [rtl_sdr](../tools/CTFTTOU-347.md)
- [rtl_fm](../tools/CTFTTOU-348.md)

## References

- <https://github.com/jopohl/urh>
- <https://projects.osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>
