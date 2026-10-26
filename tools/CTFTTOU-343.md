# CTFTTOU-343 — iq_demod.py

> **Tool ID:** `CTFTTOU-343`  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-004, CTFTCTE-SDR-004

## Description

Workspace-authored offline demodulator (Python, NumPy/SciPy). Modes: `wbfm` (75 µs
de-emphasis), `fm`, `am`, `usb`, `lsb`. It selects the signal by `--shift`, `--freq` or
`--auto` (strongest carrier centroid) and writes WAV, or raw s16le that pipes into
`multimon-ng` like `rtl_fm` output. It is the capture-file equivalent of `rtl_fm`, for
pager/APRS/DTMF/voice payloads recorded as IQ.

## URL

Local (workspace): [.agents/ctf/ctf-sdr/scripts/iq_demod.py](../../.agents/ctf/ctf-sdr/scripts/iq_demod.py)

## Usage

```bash
~/.venvs/ctfml/bin/python -I iq_demod.py fm.cu8 --mode wbfm --auto -o fm.wav
~/.venvs/ctfml/bin/python -I iq_demod.py pager.cu8 --freq 152.24M --mode fm --rate 22050 --raw -o - \
  | multimon-ng -t raw -a POCSAG1200 -
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-004, CTFTCTE-SDR-004
