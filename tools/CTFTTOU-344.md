# CTFTTOU-344 — power_peaks.py

> **Tool ID:** `CTFTTOU-344`  
> **Related techniques/counters:** CTFTTE-SDR-005, CTFTCTE-SDR-005

## Description

Workspace-authored `rtl_power` CSV analyser (Python, NumPy; matplotlib for PNG).
It gives:

- a peak list over the median floor (NaN hop-edge bins skipped);
- multi-sweep aggregation (`--agg mean|max|last`);
- a baseline diff (`--baseline base.csv`) ranking the bins that rose;
- a waterfall PNG.

The diff is the core step of the SDR-005 recovery: baseline away from the venue,
sweep on site, rank what is new, then confirm with a narrow IQ capture.

## URL

Local (workspace): [.agents/ctf/ctf-sdr/scripts/power_peaks.py](../../.agents/ctf/ctf-sdr/scripts/power_peaks.py)

## Usage

```bash
rtl_power -f 30M:1.7G:1M -i 5m -1 base.csv        # away from the venue
rtl_power -f 30M:1.7G:1M -i 30 -e 30m live.csv    # on site
~/.venvs/ctfml/bin/python -I power_peaks.py live.csv --baseline base.csv --min-snr 6 --png wf.png
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Skills

- [ctf-sdr](../skills/CTFTSKL-001.md) — domain skill

## Related Techniques

CTFTTE-SDR-005, CTFTCTE-SDR-005
