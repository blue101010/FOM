# CTFTCTE-WEB-021 — Run the command-injection micro-runbook

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-021`](../techniques/CTFTTE-WEB-021.md) — OS command injection in a wrapped utility

---

## Offensive Recovery (CTF practitioner / solver)

Identify the concatenation; find the minimal working separator; prove execution with a no-op command; then perform a single targeted read. Note the wrapper's privilege context and use it rather than aiming for broad execution. Automate only after a reproducible manual difference.

## Forensic / Blue-Team Perspective (DFIR analyst)

Process-tree and command-line telemetry expose child-shell spawns and argument separators; wrappers should call APIs, not shells.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059 | Command and Scripting Interpreter | The recovery is the minimal-test escalation of ATT&CK's own interpretation. |

## Tools

- manual probing
- process-spawn logging
- [commix](../tools/CTFTTOU-316.md)

## References

- <https://owasp.org/www-community/attacks/Command_Injection>
- Add challenge write-up link
