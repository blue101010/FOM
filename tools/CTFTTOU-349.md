# CTFTTOU-349 — rtl_power

> **Tool ID:** `CTFTTOU-349`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-005, CTFTCTE-SDR-005

## Description

`rtl_power` is a wideband FFT logger. It hops the tuner across a range far wider than
the 2–3 MHz instantaneous bandwidth, integrates power per bin, and appends CSV rows.
That gives band surveys, waterfalls over time, and the baseline-versus-live diff used to
find a hidden transmitter. Peaks are bin-quantised; confirm each one with an IQ capture.

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_power.exe`
- Kali / Debian: `/usr/bin/rtl_power` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| `-f lo:hi:bin` | range and maximum bin size (1 Hz – 2.8 MHz) |
| `-i interval` | integration interval (default 10 s; buggy if one sweep takes longer) |
| `-1` | single shot |
| `-e timer` | exit after a duration (`1h`, `30m`) |
| `-g dB` | tuner gain (default auto) |
| `-p ppm` | frequency correction |
| `-w window` | hamming, blackman, blackman-harris, hann-poisson, bartlett, youssef |
| `-c percent` | crop hop edges (recommended 20–50 %) |
| `-F 0\|9` | low-leakage downsample filter |
| `-P` | peak hold |
| `-D` / `-O` | direct sampling / offset tuning |

CSV columns: `date, time, Hz low, Hz high, Hz step, samples, dB, dB, …`, one row per hop.

## Usage

```powershell
rtl_power.exe -f 88M:108M:100k -g 20 -i 3 -1 fm.csv              # 8 hops, 78.125 kHz bins
rtl_power.exe -f 30M:1.7G:1M -i 5m -1 base.csv                    # baseline survey
rtl_power.exe -D -f 500k:24M:50k -g 20 -i 2 -1 hf.csv             # HF, direct sampling
scripts\sdrpy.ps1 power_peaks.py fm.csv --top 10 --png fm.png
scripts\sdrpy.ps1 power_peaks.py live.csv --baseline base.csv --min-snr 6
```

Observed on 2026-10-25:
- the FM survey wrote `nan` in 20 hop-edge bins;
- the "strongest" 100.9 MHz bin was really a station at 100.7 MHz.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)

## Related Techniques

CTFTTE-SDR-005, CTFTCTE-SDR-005
