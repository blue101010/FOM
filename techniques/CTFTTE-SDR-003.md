# CTFTTE-SDR-003 — Unlabelled IQ capture (format, sample rate and centre withheld)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Paired counter-technique:** [`CTFTCTE-SDR-003`](../countertechniques/CTFTCTE-SDR-003.md) — Fingerprint the IQ format and recover rate and centre

---

## How the challenge author hides

The recording is handed over as a bare sample file (`.bin`, `.raw`, `.iq`, `.dat`, or a `.cf32` with no sidecar). Its sample format, sample rate and centre frequency are not stated, or the extension is misleading. Read with the wrong format, the file looks like noise. With the wrong sample rate, every timing (baud, pulse width, audio pitch) is off by the same factor. Without the centre frequency, the signal cannot be tied to a band or a protocol. The barrier comes before demodulation: the file has to be read correctly first.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Stripping the format metadata makes a plain recording unreadable until its encoding is inferred. |

## Tools

- [iq_check.py](../../.agents/ctf/ctf-sdr/scripts/iq_check.py) ([CTFTTOU-341](../tools/CTFTTOU-341.md))
- [inspectrum](../tools/CTFTTOU-236.md)
- [Universal Radio Hacker](../tools/CTFTTOU-235.md)
- [GNU Radio Companion](../tools/CTFTTOU-233.md)
- [kalibrate-rtl](../tools/CTFTTOU-339.md)
- [rtl_test](../tools/CTFTTOU-346.md)
- [rtl_eeprom](../tools/CTFTTOU-351.md)
- [rtl-sdr](../tools/CTFTTOU-335.md)

## Indicators

- file size divisible by 2 (cu8/cs8), 4 (cs16) or 8 (cf32) bytes per complex sample, with no header
- `uint8` byte mean close to 127.5 → RTL-SDR `cu8`; float32 pairs with |values| near 1 → `cf32`
- a `cf32` holding at most 256 distinct values → converted from an 8-bit RTL capture (its rails are the 8-bit rails)
- symbol timings that become round numbers (for example 1 µs ADS-B pulses or a 200 kHz FM channel) only under one candidate sample rate

## References

- <https://github.com/miek/inspectrum>
- <https://github.com/jopohl/urh>
- <https://projects.osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>
