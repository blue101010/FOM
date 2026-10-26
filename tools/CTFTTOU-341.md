# CTFTTOU-341 — iq_check.py

> **Tool ID:** `CTFTTOU-341`  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-003, CTFTCTE-SDR-003

## Description

Workspace-authored first look at an IQ capture (Python, NumPy/SciPy). It reports:

- duration;
- DC offset;
- clipping, including two-rail pile-up detection for float files;
- I/Q imbalance and noise floor;
- the count of distinct sample values: a `cf32` with ≤ 256 levels is flagged as converted from an 8-bit RTL capture, an SDR-003 indicator;
- the strongest carriers, as power-weighted centroid offset, absolute frequency and occupied bandwidth.

`--fm-pilot` WBFM-demodulates carrier #1 and tests for the 19 kHz stereo pilot,
an end-to-end proof of the receive chain on broadcast FM. `--json` gives
machine-readable output.

## URL

Local (workspace): [.agents/ctf/ctf-sdr/scripts/iq_check.py](../../.agents/ctf/ctf-sdr/scripts/iq_check.py)

## Usage

```bash
~/.venvs/ctfml/bin/python -I iq_check.py capture.cu8 --top 5 --fm-pilot
~/.venvs/ctfml/bin/python -I iq_check.py signal.cf32 --fs 2.048M --json
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — script toolkit index

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-003, CTFTCTE-SDR-003
