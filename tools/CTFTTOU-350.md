# CTFTTOU-350 — rtl_tcp

> **Tool ID:** `CTFTTOU-350`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-004, CTFTCTE-SDR-004

## Description

`rtl_tcp` is an I/Q server. It owns the dongle and streams `cu8` samples over TCP
(default port 1234), while clients retune it remotely: GNU Radio/gr-osmosdr, SDR#,
`rtl_433 -d rtl_tcp:host:port`, or the `tcp_client.py` script. It is how Linux-only
tools in WSL Kali use a dongle attached to Windows with WinUSB.

Protocol:
- on connect, the server sends 12 bytes: `"RTL0"` + u32 tuner type + u32 gain count (big-endian);
- each client command is 5 bytes: u8 command + u32 value. Codes: `0x01` freq, `0x02` rate, `0x03` gain mode, `0x04` gain (tenths of dB), `0x05` ppm, `0x08` AGC, `0x09` direct sampling, `0x0a` offset tuning, `0x0d` gain by index, `0x0e` bias tee.

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_tcp.exe`
- Kali / Debian: `/usr/bin/rtl_tcp` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| `-a addr` | listen address (use `127.0.0.1`; `0.0.0.0` exposes the receiver to the LAN) |
| `-p port` | listen port (default 1234) |
| `-f Hz` / `-g dB` / `-s rate` | initial frequency (default 100 MHz), gain (default auto), rate (default 2048000) |
| `-b n` / `-n n` | buffers / max linked-list buffers (default 500) |
| `-d index` | device index |
| `-P ppm` | frequency correction (capital P here) |
| `-D` | direct sampling |

## Usage

```powershell
rtl_tcp.exe -a 127.0.0.1 -p 1234
python scripts\tcp_client.py -f 100.7M -s 2.048M -g 19.7 --secs 3 -o fm.cu8
```

```bash
rtl_433 -d rtl_tcp:127.0.0.1:1234 -f 433.92M -A          # from WSL Kali (mirrored networking)
```

Verified on 2026-10-25:
- the header reads `RTL0`, tuner 5 (R820T), 29 gains;
- throughput was 2.042 MS/s from a Windows client and 2.002 MS/s from Kali;
- a capture taken over TCP showed the 19 kHz pilot 53 dB over the floor.

The server streams samples taken before a retune (100 MHz, auto gain, about 25 %
clipping seen), so drop at least 0.5 s after sending commands.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — WSL bridge, `tcp_client.py`, `hwtest.ps1`

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)

## Related Techniques

CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-004, CTFTCTE-SDR-004
