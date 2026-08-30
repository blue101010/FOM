# CTFTTE-JAL-005 — Seccomp / AppArmor policy confinement

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-005`](../countertechniques/CTFTCTE-JAL-005.md) — Identify allowed syscalls and pivot around the filter

---

## How the challenge author hides

A seccomp BPF profile or AppArmor policy blocks the direct syscalls (e.g. `execve`, `open`) needed to read the flag, forcing the solver to find an equivalent permitted path.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1055 | Process Injection | Seccomp/AppArmor filter-bypass detail ATT&CK omits. |

## Tools

- seccomp-tools
- strace
- python ctypes

## References

- <https://github.com/david942j/seccomp-tools>
- Add challenge write-up link
