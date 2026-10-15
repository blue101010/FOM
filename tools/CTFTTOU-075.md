# CTFTTOU-075 — ps / /proc

> **Tool ID:** `CTFTTOU-075`  
> **Related techniques/counters:** CTFTTE-FOR-030, CTFTCTE-FOR-030

## Description

Linux process inventory and the kernel's per-process filesystem. `ps auxww` lists running
processes (find a guardian daemon by name); `/proc/<pid>/cmdline`, `/proc/<pid>/fd` and
`/proc/<pid>/fdinfo` expose each process's open file descriptors and inotify/fanotify
watch descriptors — the direct way to prove which process is holding or watching the
artifact that mutates on read. The `--hunt` mode of
[mutating-file-watchdog.py](scripts/mutating-file-watchdog.py) ([CTFTTOU-070](CTFTTOU-070.md))
automates exactly this scan.

## URL

<https://man7.org/linux/man-pages/man1/ps.1.html> — proc filesystem: <https://docs.kernel.org/filesystems/proc.html>

## Related Techniques

CTFTTE-FOR-030, CTFTCTE-FOR-030
