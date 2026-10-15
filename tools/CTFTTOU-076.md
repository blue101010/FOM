# CTFTTOU-076 — inotify-tools

> **Tool ID:** `CTFTTOU-076`  
> **Related techniques/counters:** CTFTTE-FOR-030, CTFTCTE-FOR-030

## Description

`inotifywait`/`inotifywatch` — observe filesystem events (open, access, modify) on a file or
directory in real time. In read-triggered-mutation challenges, watching the flag file proves
the mutation is event-driven (an `OPEN`-triggered `MODIFY` from a guardian process) rather
than corruption, and watching the directory identifies the watcher's own watch descriptor.
Pairs with [mutating-file-watchdog.py](scripts/mutating-file-watchdog.py)
([CTFTTOU-070](CTFTTOU-070.md)), which detects the mutation itself via repeated hashed reads.

## URL

<https://github.com/inotify-tools/inotify-tools>

## Related Techniques

CTFTTE-FOR-030, CTFTCTE-FOR-030
