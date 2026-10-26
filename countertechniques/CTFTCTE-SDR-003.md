# CTFTCTE-SDR-003 — Fingerprint the IQ format and recover rate and centre

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Counters technique:** [`CTFTTE-SDR-003`](../techniques/CTFTTE-SDR-003.md) — Unlabelled IQ capture (format, sample rate and centre withheld)

---

## Offensive Recovery (CTF practitioner / solver)

1. Infer the sample format from the bytes:
   - size divisibility;
   - byte histogram (`uint8` centred on 127.5 → `cu8`);
   - plausible float ranges (`cf32`);
   - for floats, the count of distinct values (≤ 256 → an 8-bit origin).
2. Load each candidate format in inspectrum or URH. The right one shows clean carriers and bursts; the wrong ones show noise or mirrored images.
3. Recover the sample rate from structure that has a known timing: a standard channel width, a protocol's fixed symbol rate, or round pulse widths. Common RTL-SDR rates are 1.024, 2.048 and 2.4 MS/s.
4. Take the centre frequency from the challenge story, the filename, or the band a recognised protocol must occupy. Record every assumption, because timings and absolute frequencies are only as good as the rate and centre chosen.

## Forensic / Blue-Team Perspective (DFIR analyst)

An IQ file without metadata is unprovable evidence. Acquisition writes the format, rate, centre, gain and tool command next to the samples (for example a JSON sidecar with a hash). A report states which parameters were inferred rather than recorded.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Recovery re-derives the stripped encoding parameters before analysis. |

## Tools

- [iq_check.py](../../.agents/ctf/ctf-sdr/scripts/iq_check.py) ([CTFTTOU-341](../tools/CTFTTOU-341.md))
- [inspectrum](../tools/CTFTTOU-236.md)
- [Universal Radio Hacker](../tools/CTFTTOU-235.md)
- [GNU Radio Companion](../tools/CTFTTOU-233.md)
- [kalibrate-rtl](../tools/CTFTTOU-339.md)
- [rtl_test](../tools/CTFTTOU-346.md)
- [rtl_eeprom](../tools/CTFTTOU-351.md)
- [rtl-sdr](../tools/CTFTTOU-335.md)

## References

- <https://github.com/miek/inspectrum>
- <https://projects.osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>
