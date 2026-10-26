# CTFTTOU-337 — dump1090

> **Tool ID:** `CTFTTOU-337`  
> **Related techniques/counters:** CTFTTE-SDR-004, CTFTCTE-SDR-004

## Description

Mode S / ADS-B decoder for 1090 MHz. It does error correction and CRC checking,
decodes aircraft position, altitude, speed and callsign, and offers interactive
and network (`--net`, raw `*hex;` on port 30002) outputs. Many maintained forks
exist (FlightAware `dump1090-fa`, `dump1090-mutability`).

## URL

<https://github.com/antirez/dump1090>

## Installation

```bash
sudo apt install -y dump1090-mutability     # or build dump1090-fa from source
```

## Usage

```bash
dump1090 --interactive                       # live table of aircraft
dump1090 --raw | tee adsb.txt                # raw frames for offline decoding
dump1090 --ifile capture.bin --raw           # 2 MS/s 8-bit IQ file
```

For CRC-filtering raw `rtl_adsb` output offline, see `adsb_crc.py` ([CTFTTOU-345](CTFTTOU-345.md)).

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill (standard-protocol decoding, SDR-004)

## References

- <https://mode-s.org/decode/>

## Related Techniques

CTFTTE-SDR-004, CTFTCTE-SDR-004
