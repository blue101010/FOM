# CTFTTOU-339 — kalibrate-rtl

> **Tool ID:** `CTFTTOU-339`  
> **Related techniques/counters:** CTFTTE-SDR-003, CTFTCTE-SDR-003

## Description

Measures an RTL-SDR dongle's frequency error (PPM) against GSM base-station
carriers (FCCH bursts). The PPM value is then passed to every `rtl_*` tool with
`-p`. It is needed when absolute frequencies matter (narrow channels, matching a
challenge's stated frequency); TCXO dongles such as the NESDR SMArt v5 drift less
than 1 PPM but still benefit. Some Osmocom builds of `rtl_test` lack the `-p` PPM
measurement, which leaves this tool or a known reference beacon.

## URL

<https://github.com/steve-m/kalibrate-rtl>

## Usage

```bash
kal -s GSM900            # scan for strong channels
kal -c 37                # measure the offset on one channel -> "average absolute error: N ppm"
rtl_sdr -p N ...         # apply the correction
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## Related Techniques

CTFTTE-SDR-003, CTFTCTE-SDR-003
