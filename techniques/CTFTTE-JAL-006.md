# CTFTTE-JAL-006 — WSL-interop sandbox escape

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-006`](../countertechniques/CTFTCTE-JAL-006.md) — Escape WSL-interop boundaries

---

## How the challenge author hides

The flag is on the Windows host or on the other side of a WSL interop boundary; the WSL shell is confined.

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
- Add challenge write-up link
