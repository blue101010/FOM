# CTFTTOU-335 — rtl-sdr

> **Tool ID:** `CTFTTOU-335`  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-003, CTFTCTE-SDR-003, CTFTTE-SDR-004, CTFTCTE-SDR-004, CTFTTE-SDR-005, CTFTCTE-SDR-005

## Description

Osmocom `librtlsdr` and its command-line suite (`rtl_test`, `rtl_sdr`, `rtl_fm`, `rtl_power`, `rtl_tcp`, `rtl_eeprom`, `rtl_adsb`). They drive RTL2832U DVB-T dongles as receive-only SDRs:

- R820T/R828D tuners cover 24–1766 MHz, with HF through direct sampling;
- samples are 8-bit IQ;
- the maximum rate is 3.2 MS/s, but 2.4 MS/s is the usual loss-free maximum on ordinary USB hosts.

Each binary has its own sheet, listed under Binaries.

## Binaries

Windows build `rtl-sdr-64bit-20261018` in `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/`:

- [rtl_test](CTFTTOU-346.md) — `rtl_test.exe`: detect the dongle and tuner, gain table, sample-loss test per rate
- [rtl_sdr](CTFTTOU-347.md) — `rtl_sdr.exe`: raw `cu8` I/Q capture to a file or stdout
- [rtl_fm](CTFTTOU-348.md) — `rtl_fm.exe`: FM/WBFM/AM/USB/LSB demodulation to s16le PCM, scanning
- [rtl_power](CTFTTOU-349.md) — `rtl_power.exe`: wideband FFT sweep logger to CSV
- [rtl_tcp](CTFTTOU-350.md) — `rtl_tcp.exe`: I/Q server on TCP 1234 (WSL / remote clients)
- [rtl_eeprom](CTFTTOU-351.md) — `rtl_eeprom.exe`: read (and carefully write) the USB EEPROM
- [rtl_adsb](CTFTTOU-352.md) — `rtl_adsb.exe`: basic 1090 MHz Mode S demodulation
- `librtlsdr.dll`, `libusb-1.0.dll`, `libwinpthread-1.dll` — runtime libraries; keep them next to the `.exe` files

Kali / Debian: `sudo apt install -y rtl-sdr` installs the same tools in `/usr/bin`.

Pitfalls seen in practice:

- `[R82XX] PLL not locked!` at device open is harmless;
- killing a tool under redirection loses its buffered output, so stop it with Ctrl+C;
- `rtl_power` peaks are bin-quantised;
- `rtl_tcp` streams samples taken before a retune;
- this build's `rtl_test` has no `-p` PPM measurement, and `rtl_fm` has no `-n`.

## URL

<https://osmocom.org/projects/rtl-sdr/wiki/Rtl-sdr>

Windows builds: <https://ftp.osmocom.org/binaries/windows/rtl-sdr/>

## Installation

```bash
sudo apt install -y rtl-sdr          # Kali / Debian
```

Windows: unpack the Osmocom build and install the WinUSB driver for the dongle (Zadig).
Verify with `rtl_test.exe -t`, then sweep rates with `scripts\rate_sweep.py`.

## Usage

```bash
rtl_test -s 2400000                                   # Ctrl+C after ~10 s, read "lost" lines
rtl_power -f 430M:440M:10k -g 30 -i 5 -1 ism.csv      # survey
rtl_sdr -f 433.92e6 -s 2400000 -g 30 -n 24000000 cap.cu8
rtl_fm -f 152.24M -M fm -s 22050 -g 40 - | multimon-ng -t raw -a POCSAG1200 -
rtl_tcp -a 127.0.0.1                                  # then: rtl_433 -d rtl_tcp:127.0.0.1:1234
```

Whole-chain hardware check (receive-only, PASS/FAIL table):
`scripts\hwtest.ps1 -OutDir <evidence>\hwtest`. On 2026-10-25 it passed 14/14 with a NESDR SMArt v5.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — NESDR SMArt v5 / WinUSB profile, options verified for this build, test results, evidence and safety rules
- [ctf-solver agent](../../.agents/ctf/ctf-solver/AGENT.md) — generic solver; routes RF/SDR work to the ctf-sdr agent

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill: receive chain, FOM SDR pairs, toolkit
- [ctf-sdr-ook-line-code](../skills/CTFTSKL-002.md) — OOK/ASK remotes with Manchester/PWM/PPM (SDR-002)

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-003, CTFTCTE-SDR-003, CTFTTE-SDR-004, CTFTCTE-SDR-004, CTFTTE-SDR-005, CTFTCTE-SDR-005
