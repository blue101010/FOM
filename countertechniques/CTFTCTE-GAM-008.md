# CTFTCTE-GAM-008 — Treat the simulated stage as a chained puzzle

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Counters technique:** [`CTFTTE-GAM-008`](../techniques/CTFTTE-GAM-008.md) — In-browser simulated OS / virtual-machine stage

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate the simulated command set and filesystem first, then apply the standard runbooks against the simulated services: walk the fake FTP, inject the simulated login, run the command-injection micro-runbook on the wrapped utility, crack and forge the simulated tokens. The privilege boundaries inside the simulation are part of the puzzle — observe, then exploit each in turn.

## Forensic / Blue-Team Perspective (DFIR analyst)

A client-side simulation leaves no host telemetry; the defence is the same chain of controls as for the real systems it imitates.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1036 | Masquerading | Recovery re-labels the stage as a simulation, then applies the full-pwn chain inside it. |

## Tools

- browser devtools
- JavaScript debugger

## References

- Add challenge write-up link
