# CTFTTOU-345 — adsb_crc.py

> **Tool ID:** `CTFTTOU-345`  
> **Related techniques/counters:** CTFTTE-SDR-004, CTFTCTE-SDR-004

## Description

Workspace-authored Mode S / ADS-B frame validator and decoder (Python, standard
library only). It reads `rtl_adsb` or `dump1090 --raw` output, checks the CRC-24
(DF17/18; DF11 parity with interrogator code) and drops noise frames. It decodes:

- callsign (TC 1–4);
- barometric altitude (TC 9–18);
- ground speed, heading and vertical rate (TC 19).

Output modes: `--valid-only` and `--json`. The self-test checks it against the
published *1090 MHz Riddle* example frames (KLM1023, 38 000 ft, 159.2 kt / 182.88° / −832 fpm).

## URL

Local (workspace): [.agents/ctf/ctf-sdr/scripts/adsb_crc.py](../../.agents/ctf/ctf-sdr/scripts/adsb_crc.py)

## Usage

```bash
rtl_adsb -g 49.6 adsb.txt          # Ctrl+C after a while
python3 adsb_crc.py adsb.txt       # DF counts, CRC-valid frames, per-aircraft fields
python3 adsb_crc.py adsb.txt --valid-only > clean.txt
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## References

- <https://mode-s.org/decode/>

## Related Techniques

CTFTTE-SDR-004, CTFTCTE-SDR-004
