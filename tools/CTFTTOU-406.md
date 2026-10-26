# CTFTTOU-406 — timeline_normalize.py

> **Tool ID:** `CTFTTOU-406`
> **Related techniques/counters:** CTFTTE-FOR-028, CTFTCTE-FOR-028

## Description

Workspace-authored timeline normalizer (Python, stdlib). Converts Hayabusa, Chainsaw and Plaso l2tcsv output into one UTC-sorted event stream in a shared schema, preserving the original timestamp, the timezone assumption used to convert it, the source artifact, the tool and the record id for every event — so the timeline stays auditable and never silently coerces local time. Emits JSONL and CSV.

## URL

Local (workspace): [ctf-skills-main/ctf-windows-artifact-timeline/scripts/timeline_normalize.py](../../ctf-skills-main/ctf-windows-artifact-timeline/scripts/timeline_normalize.py)

## Usage

```bash
python timeline_normalize.py --hayabusa h.csv --chainsaw c.csv --plaso s.csv -o timeline.jsonl
```

## Skills

- [ctf-windows-artifact-timeline](../skills/CTFTSKL-005.md)

## Related Techniques

CTFTTE-FOR-028, CTFTCTE-FOR-028
