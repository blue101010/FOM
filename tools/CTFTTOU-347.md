# CTFTTOU-347 — rtl_sdr

> **Tool ID:** `CTFTTOU-347`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-005, CTFTCTE-SDR-005

## Description

`rtl_sdr` is the raw I/Q recorder. It tunes the dongle and writes interleaved
unsigned 8-bit I,Q samples (`cu8`, midpoint 127.5) to a file or to stdout (`-`).
Every offline analysis (inspectrum, URH, `rtl_433 -r`, the ctf-sdr scripts) starts
from such a capture. It records no metadata, so the frequency, rate and gain must
be kept alongside the file (see SDR-003).

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_sdr.exe`
- Kali / Debian: `/usr/bin/rtl_sdr` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| `-f Hz` | centre frequency (required) |
| `-s rate` | sample rate (default 2048000) |
| `-g dB` | tuner gain, `0` = auto (default) |
| `-p ppm` | frequency correction |
| `-n samples` | number of samples to read (default 0 = until Ctrl+C) |
| `-d index` | device index |
| `-b size` | output block size |
| `-S` | force sync output |
| `-D` | direct sampling (HF below 25 MHz) |
| `filename` | output file, `-` for stdout |

## Usage

```powershell
rtl_sdr.exe -f 433.92e6 -s 2400000 -g 30 -n 24000000 keyfob_433.92M_2400k_g30.cu8   # 10 s
rtl_sdr.exe -f 100.9e6 -s 2048000 -g 20 -n 4096000 iq_100.9M_2048k_g20_2s.cu8      # 2 s, 8 192 000 bytes
python scripts\capture.py --freq 433.92M --rate 2.4M --gain 30 --secs 10 --label chal --dir C:\CTF\ev
```

`capture.py` wraps `rtl_sdr` and writes a `.json` sidecar (settings, exact command,
tool output, SHA-256) that the analysis scripts read automatically. On 2026-10-25 a
2 s capture at 100.9 MHz had 0 % clipping, and a software FM demodulation of it
showed the 19 kHz stereo pilot 52 dB over the floor.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — evidence rules, naming, `capture.py`

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)
- [ctf-sdr-ook-line-code](../skills/CTFTSKL-002.md)

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-005, CTFTCTE-SDR-005
