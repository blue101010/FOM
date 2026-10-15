# CTFTTOU-068 — tar-symlink-redirect.py

> **Tool ID:** `CTFTTOU-068`  
> **Related techniques/counters:** CTFTTE-PWN-009, CTFTCTE-PWN-009

## Description

CTFT-authored offensive-recovery helper (Python, stdlib only). Builds the archive
half of a fixed-name output symlink redirect: plants a symlink named after the
privileged tool's hard-coded output folder (default `extracted`) pointing at a
directory the user cannot write to, and writes a tar whose single entry (default
`authorized_keys`) is extracted through it. `--dry-run` prints the equivalent
shell commands; `--no-link` builds only the archive.

## Location

[`tools/scripts/tar-symlink-redirect.py`](scripts/tar-symlink-redirect.py) (local CTFT tool, not an external project)

## Related Techniques

CTFTTE-PWN-009, CTFTCTE-PWN-009
