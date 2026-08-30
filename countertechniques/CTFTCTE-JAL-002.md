# CTFTCTE-JAL-002 — Escape the restricted shell

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Counters technique:** [`CTFTTE-JAL-002`](../techniques/CTFTTE-JAL-002.md) — Restricted-shell confinement

---

## Offensive Recovery (CTF practitioner / solver)

Use GTFOBins to find a binary permitted by the shell that spawns an unrestricted subshell, or abuse PATH manipulation, editor shell-escape (`:!/bin/sh`), or SUID binaries to bypass the restriction.

## Forensic / Blue-Team Perspective (DFIR analyst)

A restricted shell escape reveals that the confinement relied on a blocklist rather than an allowlist; any permitted binary with shell-spawning capability (vi, awk, python) breaks the model.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059 | Command and Scripting Interpreter | Restricted-shell escape details ATT&CK omits. |

## Tools

- GTFOBins references
- standard shells

## References

- <https://gtfobins.github.io/>
- Add challenge write-up link
