# CTFTTOU-348 — rtl_fm

> **Tool ID:** `CTFTTOU-348`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-004, CTFTCTE-SDR-004

## Description

`rtl_fm` is a live demodulator. It produces signed 16-bit mono PCM (s16le) from FM,
wideband FM, AM, USB, LSB, or raw IQ, either to a file or piped into decoders:
- `multimon-ng` for POCSAG, AFSK1200/APRS and DTMF;
- `sox` / `ffplay` to listen.

It can also scan a frequency list or range when squelch is enabled.

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_fm.exe`
- Kali / Debian: `/usr/bin/rtl_fm` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| `-f Hz` | frequency; repeat or use a range `118M:137M:25k` to scan (needs `-l`) |
| `-M mode` | `fm` (default), `wbfm`, `raw`, `am`, `usb`, `lsb` |
| `-s rate` | **channel** rate (default 24k), not the capture rate |
| `-r rate` | resample output rate |
| `-g dB` | tuner gain (default auto) |
| `-l level` | squelch (0 = off) |
| `-p ppm` | frequency correction |
| `-E opt` | `edge`, `dc`, `deemp`, `direct`, `direct2`, `offset` (repeatable) |
| `-F 0\|9` | low-leakage downsample filter |
| `-A std\|fast\|lut` | atan math |
| `-T` | bias-T (RTL-SDR Blog v3 only; the NESDR SMArt v5 has none) |

`wbfm` is shorthand for `-M fm -s 170k -o 4 -A fast -r 32k -l 0 -E deemp`, so its output is 32 kHz. There is **no `-n`**: stop with Ctrl+C.

## Usage

```powershell
rtl_fm.exe -f 100.7M -M wbfm -g 20 fm_32k_s16le.raw
python scripts\s16_to_wav.py fm_32k_s16le.raw --rate 32k -o fm.wav
```

```bash
rtl_fm -f 152.24M -M fm -s 22050 -g 40 - | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -f alpha -
rtl_fm -f 144.39M -M fm -s 22050 -g 40 - | multimon-ng -t raw -a AFSK1200 -a DTMF -
```

Observed on 2026-10-25: for `-f 100.7M` it tuned the dongle to 100.971 MHz. That is
deliberate: it offsets by about a quarter of the capture rate to keep the station away
from the DC spike. For a capture file, use `iq_demod.py` ([CTFTTOU-343](CTFTTOU-343.md)),
which produces the same output offline.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-004, CTFTCTE-SDR-004
