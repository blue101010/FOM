# CTFTTOU-405 — artifact_inventory.py

> **Tool ID:** `CTFTTOU-405`
> **Related techniques/counters:** CTFTTE-FOR-028, CTFTCTE-FOR-028

## Description

Workspace-authored read-only Windows evidence classifier (Python, stdlib). Walks a KAPE triage ZIP, a mounted image or an extracted profile and reports which artifact classes are present (EVTX, $MFT, USN, Prefetch, Amcache, registry, SRUM, PowerShell history, browser) and the parser for each, so you only run parsers that have input. Opens only directory listings / the ZIP index.

## URL

Local (workspace): [ctf-skills-main/ctf-windows-artifact-timeline/scripts/artifact_inventory.py](../../ctf-skills-main/ctf-windows-artifact-timeline/scripts/artifact_inventory.py)

## Usage

```bash
python artifact_inventory.py /cases/triage.zip -o inventory.json
```

## Skills

- [ctf-windows-artifact-timeline](../skills/CTFTSKL-005.md)

## Related Techniques

CTFTTE-FOR-028, CTFTCTE-FOR-028
