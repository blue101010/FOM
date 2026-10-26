# CTFTTE-SDR-005 — Flag transmitter hidden in a live spectrum

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Paired counter-technique:** [`CTFTCTE-SDR-005`](../countertechniques/CTFTCTE-SDR-005.md) — Baseline the band and diff live sweeps

---

## How the challenge author hides

In an on-site RF CTF (conference wireless villages, fox hunts), a low-power transmitter sends the flag on an unannounced frequency. It may transmit only intermittently, or hop between channels. It sits among legitimate signals (broadcast, Wi-Fi, pagers, ISM traffic), so the target is one carrier among hundreds. Its presence, not its encoding, is the first barrier. The payload is then usually one of the encodings of CTFTTE-SDR-001, -002 or -004.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001 | Data Obfuscation | The flag signal blends into normal spectrum occupancy; ATT&CK has no radio-spectrum equivalent. |

## Tools

- [rtl-sdr](../tools/CTFTTOU-335.md)
- [power_peaks.py](../../.agents/ctf/ctf-sdr/scripts/power_peaks.py) ([CTFTTOU-344](../tools/CTFTTOU-344.md))
- [Gqrx](../tools/CTFTTOU-234.md)
- [SigDigger](../tools/CTFTTOU-338.md)
- [rtl_power](../tools/CTFTTOU-349.md)
- [rtl_sdr](../tools/CTFTTOU-347.md)

## Indicators

- live, on-site challenge with a receiver allowed but no frequency given
- carriers present in the venue sweep that are absent from a sweep taken elsewhere, or that appear and disappear on a schedule
- organiser hints about bands, power or a physical area to search

## References

- <https://wctf.us/>
- <https://rfhs.io/>
