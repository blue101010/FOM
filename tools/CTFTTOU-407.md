# CTFTTOU-407 — timeline_correlate.py

> **Tool ID:** `CTFTTOU-407`
> **Related techniques/counters:** CTFTTE-FOR-028, CTFTCTE-FOR-028

## Description

Workspace-authored timeline correlator (Python, stdlib). Reads the normalized JSONL, buckets events by host/user in a sliding window and ranks sequences that look like intrusion activity (authentication -> execution -> persistence/defense-evasion -> network), each a window to read closely rather than a verdict. Every event keeps its source artifact + record id for verification.

## URL

Local (workspace): [ctf-skills-main/ctf-windows-artifact-timeline/scripts/timeline_correlate.py](../../ctf-skills-main/ctf-windows-artifact-timeline/scripts/timeline_correlate.py)

## Usage

```bash
python timeline_correlate.py timeline.jsonl --window 10m -o incidents.md
```

## Skills

- [ctf-windows-artifact-timeline](../skills/CTFTSKL-005.md)

## Related Techniques

CTFTTE-FOR-028, CTFTCTE-FOR-028
