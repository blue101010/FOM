# CTFTTE-JAL-002 — Restricted-shell confinement

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-002`](../countertechniques/CTFTCTE-JAL-002.md) — Escape the restricted shell

---

## How the challenge author hides

A limited shell (rbash, menu shell, or custom restricted interpreter) is placed between the player and the flag, blocking path traversal and forbidden commands.

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
