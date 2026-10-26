# CTFTTOU-338 — SigDigger

> **Tool ID:** `CTFTTOU-338`  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-005, CTFTCTE-SDR-005

## Description

Qt signal analyser built on the Suscan library: waterfall and FFT, channel
inspectors with PSK/FSK/ASK demodulators, symbol-rate estimation, constellation and
time-domain views, and recording. It works live (RTL-SDR via SoapySDR) and on IQ
files. Useful to characterise an unknown modulation before writing a decoder, and
to watch a band for intermittent carriers.

## URL

<https://github.com/BatchDrake/SigDigger>

## Installation

Download the AppImage (Linux) or installer (Windows/macOS) from the GitHub releases page; RTL-SDR support needs SoapyRTLSDR.

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-005, CTFTCTE-SDR-005
