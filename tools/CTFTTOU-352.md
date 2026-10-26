# CTFTTOU-352 — rtl_adsb

> **Tool ID:** `CTFTTOU-352`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-004, CTFTCTE-SDR-004

## Description

`rtl_adsb` is a minimal Mode S / ADS-B demodulator. It tunes to 1090 MHz at a fixed
2 MS/s and prints every frame candidate as `*<hex>;`. It does **not** filter on CRC, so
its output mixes real frames with noise (DF 19–31 garbage, bad parity). Validate with
`adsb_crc.py` ([CTFTTOU-345](CTFTTOU-345.md)), or use dump1090 ([CTFTTOU-337](CTFTTOU-337.md)) for full decoding.

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_adsb.exe`
- Kali / Debian: `/usr/bin/rtl_adsb` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| `-g dB` | tuner gain (default auto; 49.6 = max on R820T) |
| `-p ppm` | frequency correction |
| `-d index` | device index |
| `-V` | verbose output |
| `-S` | also show short (56-bit) frames |
| `-Q q` | quality: 0 no checks, 0.5 half bit, 1 one bit (default), 2 two bits |
| `-e n` | allowed errors (default 5) |
| `-R` | raw output |
| `filename` | output file (`-` or omitted = stdout) |

## Usage

```powershell
rtl_adsb.exe -g 49.6 adsb.txt              # Ctrl+C after 30 s
python scripts\adsb_crc.py adsb.txt          # CRC-valid frames, ICAO, callsign, altitude, speed
```

Observed on 2026-10-25 (indoor antenna, 30 s): 72 frames, 15 of them CRC-valid DF17
from one aircraft (callsign TSC539). A second run gave 130 frames, 5 CRC-valid, from 3 aircraft.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)

## Related Techniques

CTFTTE-SDR-004, CTFTCTE-SDR-004
