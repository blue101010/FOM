# CTFTTOU-300 — /proc (procfs)

> **Tool ID:** `CTFTTOU-300`  
> **Related techniques/counters:** CTFTTE-FOR-022, CTFTCTE-FOR-022, CTFTTE-FOR-030, CTFTCTE-FOR-030

## Description

The kernel's per-process pseudo-filesystem: `/proc/<pid>/cmdline`, `/proc/<pid>/fd` and `/proc/<pid>/fdinfo` show what each process has open or watches (inotify/fanotify). The `--hunt` mode of [mutating-file-watchdog.py](scripts/mutating-file-watchdog.py) ([CTFTTOU-070](CTFTTOU-070.md)) automates this scan.

## URL

<https://docs.kernel.org/filesystems/proc.html>

## Related Techniques

CTFTTE-FOR-022, CTFTCTE-FOR-022, CTFTTE-FOR-030, CTFTCTE-FOR-030
