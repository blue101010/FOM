# CTFTCTE-JAL-005 — Identify allowed syscalls and pivot around the filter

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Counters technique:** [`CTFTTE-JAL-005`](../techniques/CTFTTE-JAL-005.md) — Seccomp / AppArmor policy confinement

---

## Offensive Recovery (CTF practitioner / solver)

Use `seccomp-tools dump` to disassemble the BPF filter and enumerate permitted syscalls. If `openat` is blocked but `open` is not (or vice versa), use the allowed variant. Alternatively pivot to `mmap`+`read` or use `process_vm_readv` if permitted.

## Forensic / Blue-Team Perspective (DFIR analyst)

The pivot documents incomplete syscall coverage in the seccomp policy; a robust policy should adopt a default-deny allowlist and validate both 32-bit and 64-bit ABI syscall numbers independently.

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
