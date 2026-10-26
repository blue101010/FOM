# CTFTTOU-346 — rtl_test

> **Tool ID:** `CTFTTOU-346`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-003, CTFTCTE-SDR-003

## Description

`rtl_test` is the RTL-SDR benchmark and detection tool. It lists the dongles,
identifies the tuner and its gain table, then streams samples at a given rate and
prints `lost at least N bytes` whenever USB transfers drop data. Use it before any
capture to pick a loss-free sample rate for this host and port.

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_test.exe` (Osmocom MinGW64 build)
- Kali / Debian: `/usr/bin/rtl_test` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| `-s rate` | sample rate (default 2048000) |
| `-d index` | device index (default 0) |
| `-t` | Elonics E4000 benchmark only; on an R820T it prints the device info then `No E4000 tuner found, aborting.` |
| `-b size` | output block size (default 16 × 16384) |
| `-S` | force sync output (default async) |

This build has **no `-p` PPM measurement**: use kalibrate-rtl ([CTFTTOU-339](CTFTTOU-339.md)).

## Usage

```powershell
rtl_test.exe -t                       # detect: device, tuner, 29 gains
rtl_test.exe -s 2400000               # Ctrl+C after ~10 s, count "lost" lines
python scripts\rate_sweep.py --secs 10    # whole sweep, stops each run cleanly
```

Measured with a NESDR SMArt v5 on 2026-10-25:
- 0.25–2.56 MS/s lost nothing;
- 2.88 MS/s lost about 158 KB in 10 s, and 3.2 MS/s about 227 KB;
- 500 kS/s was rejected (`Invalid sample rate`; valid rates are 225 001–300 000 and 900 001–3 200 000 S/s).

`[R82XX] PLL not locked!` at open is harmless. Under redirection, stop with Ctrl+C:
killing the process loses the buffered `lost` lines.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — hardware profile, verified results, `hwtest.ps1`

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)

## Related Techniques

CTFTTE-SDR-003, CTFTCTE-SDR-003
