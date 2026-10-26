# CTFTTOU-336 — rtl_433

> **Tool ID:** `CTFTTOU-336`  
> **Related techniques/counters:** CTFTTE-SDR-002, CTFTCTE-SDR-002

## Description

Generic decoder for ISM-band (315/433/868/915 MHz) devices: weather sensors,
remotes, key fobs, tyre sensors. It has more than 200 built-in protocols. For CTF
work the useful parts are:

- the pulse analyser `-A`: pulse/gap histograms, a modulation guess and a ready-made
  flex-decoder line;
- the flexible decoder `-X`, covering `OOK_PWM`, `OOK_PPM`, `OOK_MC_ZEROBIT`
  (Manchester), FSK variants and more.

It reads live dongles (also `rtl_tcp`) and capture files (`-r`; `.cu8`/`.cs16`/`.cf32`, rate via `-s`).

## URL

<https://github.com/merbanan/rtl_433>

## Installation

```bash
sudo apt install -y rtl-433
```

## Usage

```bash
rtl_433 -r signal.cf32 -s 2048k -A                              # pulse analysis + flex suggestion
rtl_433 -r signal.cf32 -s 2048k -X 'n=ctf,m=OOK_MC_ZEROBIT,s=439,l=0,r=5300'
rtl_433 -d rtl_tcp:127.0.0.1:1234 -f 433.92M -A                 # live, via a Windows rtl_tcp server
```

`ook_decode.py` ([CTFTTOU-340](CTFTTOU-340.md)) prints a matching `-X` suggestion from its own pulse analysis.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr-ook-line-code](../skills/CTFTSKL-002.md) — fine-grained FOM pair SDR-002
- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## References

- <https://github.com/merbanan/rtl_433/blob/master/docs/ANALYZE.md>

## Related Techniques

CTFTTE-SDR-002, CTFTCTE-SDR-002
