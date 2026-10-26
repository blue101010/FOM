# CTFTTOU-403 — bh_path_report.py

> **Tool ID:** `CTFTTOU-403`
> **Related techniques/counters:** CTFTTE-FPN-002, CTFTCTE-FPN-002

## Description

Workspace-authored read-only BloodHound path summarizer (Python, stdlib). Parses a BloodHound CE collector ZIP/JSON, walks the outbound control edges reachable from the owned principal, and prints each with the technique it enables, the tool to use, whether it is reversible, and the full path — ranking reversible high-value edges first. It only reads the collected JSON; it never contacts the domain.

## URL

Local (workspace): [ctf-skills-main/ctf-ad-attack-paths/scripts/bh_path_report.py](../../ctf-skills-main/ctf-ad-attack-paths/scripts/bh_path_report.py)

## Usage

```bash
python bh_path_report.py bloodhound_*.zip --owned 'USER@CORP.LOCAL'
```

## Skills

- [ctf-ad-attack-paths](../skills/CTFTSKL-004.md)

## Related Techniques

CTFTTE-FPN-002, CTFTCTE-FPN-002
