# CTFTTOU-351 — rtl_eeprom

> **Tool ID:** `CTFTTOU-351`  
> **Part of:** [`CTFTTOU-335`](CTFTTOU-335.md) — rtl-sdr  
> **Related techniques/counters:** CTFTTE-SDR-003, CTFTCTE-SDR-003

## Description

`rtl_eeprom` reads and writes the RTL2832U USB EEPROM:
- vendor/product IDs;
- manufacturer, product and serial strings;
- the IR endpoint and remote-wakeup flags.

Reading identifies the exact dongle (useful in evidence and when several dongles share
one host). Writing (`-s`, `-m`, `-p`, `-g`, `-w`) changes the device and is only for an
explicit operator decision, typically giving each of several dongles a unique serial so
`-d` stays stable.

## Binary

- Windows: `.agents/ctf/ctf-sdr/rtl-sdr-64bit-20261018/rtl_eeprom.exe`
- Kali / Debian: `/usr/bin/rtl_eeprom` (package `rtl-sdr`)

## Options (this build)

| Option | Meaning |
| --- | --- |
| *(none)* | print the current configuration (read-only) |
| `-r file` | dump the EEPROM to a file (read-only) |
| `-d index` | device index |
| `-m` / `-p` / `-s str` | **write** manufacturer / product / serial string |
| `-i 0\|1` | **write** IR endpoint off/on |
| `-g conf` | **write** a default config (`realtek`, `realtek_oem`, `noxon`, `terratec_black`, `terratec_plus`) |
| `-w file` | **write** a dumped file back ("use on your own risk") |

## Usage

```powershell
rtl_eeprom.exe                        # read-only: VID/PID, strings, serial, IR flag
rtl_eeprom.exe -r eeprom_dump.bin     # 256-byte read-only dump for the evidence folder
```

Read on 2026-10-25: VID `0x0bda`, PID `0x2838`, Nooelec, NESDR SMArt v5, serial
`00000001`, IR endpoint enabled. PID 0x2838 ("RTL2838") devices contain an RTL2832U;
no RTL2838 chip exists.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — read-only rule, EEPROM profile

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md)

## Related Techniques

CTFTTE-SDR-003, CTFTCTE-SDR-003
