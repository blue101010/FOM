# CTFTTE-WEB-021 — OS command injection in a wrapped utility

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-021`](../countertechniques/CTFTCTE-WEB-021.md) — Run the command-injection micro-runbook

---

## How the challenge author hides

A utility program (login prompt, ping wrapper, report generator) concatenates user input into a shell command line, and the flag or the token it protects sits in files readable only through that concatenation. The wrapper's privilege context is part of the puzzle: the injection is the gate, not the goal.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059 | Command and Scripting Interpreter | Direct echo; CTFT adds the wrapped-utility and privilege-context craft. |

## Tools

- manual probing (apostrophe, separators, no-op command)
- sqlmap only after a reproducible manual signal
- [commix](../tools/CTFTTOU-316.md)

## References

- <https://owasp.org/www-community/attacks/Command_Injection>
- Add challenge write-up link
