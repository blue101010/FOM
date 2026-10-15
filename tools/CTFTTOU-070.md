# CTFTTOU-070 — mutating-file-watchdog.py

> **Tool ID:** `CTFTTOU-070`  
> **Related techniques/counters:** CTFTTE-FOR-030, CTFTCTE-FOR-030

## Description

CTFT-authored triage helper (Python, stdlib only). Detects read-triggered payload
mutation: reads a file N times, hashes each read and reports whether identical
reads produce different bytes (the guardian-process signature, often with
doubling size). `--hunt` lists processes holding the file open or watching its
directory via /proc (Linux); `--snapshot` preserves the current bytes off the
watched path. Exit code 2 signals a mutating artifact.

## Location

[`tools/scripts/mutating-file-watchdog.py`](scripts/mutating-file-watchdog.py) (local CTFT tool, not an external project)

## Related Techniques

CTFTTE-FOR-030, CTFTCTE-FOR-030
