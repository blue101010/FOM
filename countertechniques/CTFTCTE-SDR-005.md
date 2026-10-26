# CTFTCTE-SDR-005 — Baseline the band and diff live sweeps

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Counters technique:** [`CTFTTE-SDR-005`](../techniques/CTFTTE-SDR-005.md) — Flag transmitter hidden in a live spectrum

---

## Offensive Recovery (CTF practitioner / solver)

1. Record a baseline sweep away from the venue, or before the transmitters start (`rtl_power -f 30M:1.7G:1M -i 5m -1 base.csv`).
2. Record live sweeps on site with a shorter interval so intermittent carriers are caught (`-P` peak hold helps).
3. Diff live against baseline per bin and rank the bins that rose. A waterfall of repeated sweeps exposes duty-cycled or hopping transmitters.
4. `rtl_power` bins are coarse. Confirm each candidate with a narrow IQ capture at the exact frequency, then decode the payload with the matching SDR recovery (modulation, line code or standard protocol).
5. Move to localise the emitter when the challenge requires it (signal strength versus position).

## Forensic / Blue-Team Perspective (DFIR analyst)

Spectrum baselining is how rogue transmitters are found: a reference survey per site, periodic re-sweeps, and alerts on new or changed carriers. Each detection is kept with its time, frequency, level and a short IQ capture.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001 | Data Obfuscation | Recovery separates the flag carrier from normal spectrum occupancy by differencing. |

## Tools

- [rtl-sdr](../tools/CTFTTOU-335.md)
- [power_peaks.py](../../.agents/ctf/ctf-sdr/scripts/power_peaks.py) ([CTFTTOU-344](../tools/CTFTTOU-344.md))
- [Gqrx](../tools/CTFTTOU-234.md)
- [SigDigger](../tools/CTFTTOU-338.md)
- [rtl_power](../tools/CTFTTOU-349.md)
- [rtl_sdr](../tools/CTFTTOU-347.md)

## References

- <https://wctf.us/>
- <https://projects.osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>
