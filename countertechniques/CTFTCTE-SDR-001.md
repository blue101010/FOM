# CTFTCTE-SDR-001 — Demodulate and decode RF captures

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Counters technique:** [`CTFTTE-SDR-001`](../techniques/CTFTTE-SDR-001.md) — RF/SDR signal embedding

---

## Offensive Recovery (CTF practitioner / solver)

Load the IQ capture in Gqrx/GNU Radio, identify the modulation from the waterfall and constellation, demodulate, and decode the recovered bitstream into the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

RF captures are analyzed like any volatile signal artifact: center frequency, bandwidth and modulation are the recovery keys, and SDR snapshots can be replayed indefinitely.

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

