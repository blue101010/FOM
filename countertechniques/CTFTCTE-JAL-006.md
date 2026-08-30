# CTFTCTE-JAL-006 — Escape WSL-interop boundaries

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Counters technique:** [`CTFTTE-JAL-006`](../techniques/CTFTTE-JAL-006.md) — WSL-interop sandbox escape

---

## Offensive Recovery (CTF practitioner / solver)

Abuse WSL interop (interop binaries, mounts) to cross the boundary and read the host flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

WSL interop activity maps to process and mount artifacts on both OS sides.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1611 | Escape to Host | WSL-to-host boundary escape. |

## Tools

- wsl.exe
- bash
- interop binaries

## References

- <https://learn.microsoft.com/en-us/windows/wsl/>

