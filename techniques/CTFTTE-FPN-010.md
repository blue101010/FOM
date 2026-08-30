# CTFTTE-FPN-010 — Reverse-shell delivery & listener operations

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-010`](../countertechniques/CTFTCTE-FPN-010.md) — Catch, upgrade and persist reverse shells

---

## How the challenge author hides

The flag requires a stable reverse shell through restricted channels (firewalls, encodings).

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059 | Command and Scripting Interpreter | Command-shell channel establishment. |

## Tools

- netcat
- pwncat
- socat

## References

- https://github.com/calebstewart/pwncat
- Add challenge write-up link
