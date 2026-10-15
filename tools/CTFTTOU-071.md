# CTFTTOU-071 — mtime-xor-recover.py

> **Tool ID:** `CTFTTOU-071`  
> **Related techniques/counters:** CTFTTE-CRY-014, CTFTCTE-CRY-014, CTFTCTE-FOR-030

## Description

CTFT-authored recovery helper (Python, stdlib only). Recovers repeating-key XOR
whose key is the writer's timestamp: hex-decodes the ciphertext, derives the
decimal epoch-seconds string from the file's mtime (or a supplied time), XORs and
scores candidates by printable-ASCII ratio with flag-format boosting.
`--window N` sweeps ±N seconds for disturbed mtimes; `--key-str` forces an exact
key. The standard next step after stopping a read-triggered guardian.

## Location

[`tools/scripts/mtime-xor-recover.py`](scripts/mtime-xor-recover.py) (local CTFT tool, not an external project)

## Related Techniques

CTFTTE-CRY-014, CTFTCTE-CRY-014, CTFTCTE-FOR-030
