# CTFTTE-GAM-008 — In-browser simulated OS / virtual-machine stage

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Paired counter-technique:** [`CTFTCTE-GAM-008`](../countertechniques/CTFTCTE-GAM-008.md) — Treat the simulated stage as a chained puzzle

---

## How the challenge author hides

The author ships a fake operating system — a FreeDOS-style filesystem and command set — implemented in JavaScript inside the page. The whole flag chain runs against simulated services and simulated files (an internal FTP, a vulnerable login utility, a token file), not against the host. Every attack is performed on in-simulation logic, whose privilege boundaries are part of the puzzle.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1036 | Masquerading | A client-side simulation masquerades as a system stage, redirecting exploit effort inside a sandbox. |

## Tools

- browser devtools
- JavaScript debugger

## References

- Add challenge write-up link
