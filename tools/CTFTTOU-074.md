# CTFTTOU-074 — python tarfile

> **Tool ID:** `CTFTTOU-074`  
> **Related techniques/counters:** CTFTTE-PWN-010, CTFTCTE-PWN-010

## Description

Python standard-library module for reading and writing tar archives. The crafting side of
archive-based exploits: build entries with arbitrary names, types (file/dir) and modes
without touching the filesystem, and inspect a suspect archive's entry set before feeding
it to a vulnerable extractor. Used by the CTFT helper scripts
[tar-parent-traversal.py](scripts/tar-parent-traversal.py) ([CTFTTOU-069](CTFTTOU-069.md))
and [tar-symlink-redirect.py](scripts/tar-symlink-redirect.py) ([CTFTTOU-068](CTFTTOU-068.md)).
Distinct from the python interpreter entry ([CTFTTOU-050](CTFTTOU-050.md)).

## URL

<https://docs.python.org/3/library/tarfile.html>

## Related Techniques

CTFTTE-PWN-010, CTFTCTE-PWN-010
