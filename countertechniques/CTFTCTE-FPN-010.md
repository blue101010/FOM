# CTFTCTE-FPN-010 — Catch, upgrade and persist reverse shells

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-010`](../techniques/CTFTTE-FPN-010.md) — Reverse-shell delivery & listener operations

---

## Offensive Recovery (CTF practitioner / solver)

Deliver a reverse shell (bash/python/php), catch it with a listener, upgrade to a PTY, and persist.

## Forensic / Blue-Team Perspective (DFIR analyst)

Reverse shells leave outbound connection signatures; listener-side artifacts document the callback.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059 | Command and Scripting Interpreter | Command-shell channel establishment. |

## Tools

- netcat
- pwncat
- socat

## References

- <https://github.com/calebstewart/pwncat>

