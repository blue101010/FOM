# CTFTTOU-069 — tar-parent-traversal.py

> **Tool ID:** `CTFTTOU-069`  
> **Related techniques/counters:** CTFTTE-PWN-010, CTFTCTE-PWN-010

## Description

CTFT-authored offensive-recovery helper (Python, stdlib only). Builds the sibling
entry pair that abuses hierarchy-reconstruction path traversal in archive
extractors: a directory entry `<prefix><target-dir>` plus a file entry
`<prefix><target-path>` carrying the payload bytes. `--verify` simulates the
flawed parenting and join logic locally (pure posixpath) and reports where the
write would land, so the `../` prefix can be tuned without burning challenge
instances.

## Location

[`tools/scripts/tar-parent-traversal.py`](scripts/tar-parent-traversal.py) (local CTFT tool, not an external project)

## Related Techniques

CTFTTE-PWN-010, CTFTCTE-PWN-010
