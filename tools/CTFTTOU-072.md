# CTFTTOU-072 — gosym2src.py

> **Tool ID:** `CTFTTOU-072`  
> **Related techniques/counters:** CTFTTE-REV-010, CTFTCTE-REV-010

## Description

CTFT-authored source-recovery helper (Python, stdlib only). Extracts embedded
code-host package paths (`github.com/<user>/<repo>/...` and peers) from a Go/Rust
binary, groups them by repository root and prints the candidate URLs. `--diff
REPO` inspects an already-local clone: finds challenge-looking branches
(ctf/challenge/flag/pwn) and prints their diff against the checked-out HEAD,
localising the planted flaw without any network access.

## Location

[`tools/scripts/gosym2src.py`](scripts/gosym2src.py) (local CTFT tool, not an external project)

## Related Techniques

CTFTTE-REV-010, CTFTCTE-REV-010
