# CTFTTOU-342 — iq_segments.py

> **Tool ID:** `CTFTTOU-342`  
> **Related techniques/counters:** CTFTTE-SDR-002, CTFTCTE-SDR-002

## Description

Workspace-authored time-sliced view of an IQ capture (Python, NumPy). For each
segment it gives power, clipping and the strongest carrier. `--active DB` keeps the
segments DB above the noise floor (10th percentile, which stays valid when the signal
is on most of the time) and merges them into bursts with start, end and length.
That gives pulse timing for OOK/ASK remotes, and shows retune/AGC transients and
hopping carriers. On HTB "RFlag" (0.1 ms segments, `--active 10`) it isolates the
185 on-pulses.

## URL

Local (workspace): [.agents/ctf/ctf-sdr/scripts/iq_segments.py](../../.agents/ctf/ctf-sdr/scripts/iq_segments.py)

## Usage

```bash
~/.venvs/ctfml/bin/python -I iq_segments.py keyfob.cu8 --seg 0.0005 --active 10
~/.venvs/ctfml/bin/python -I iq_segments.py capture.cu8 --seg 0.25 --csv segs.csv
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr-ook-line-code](../skills/CTFTSKL-002.md) — fine-grained FOM pair SDR-002
- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## Related Techniques

CTFTTE-SDR-002, CTFTCTE-SDR-002
