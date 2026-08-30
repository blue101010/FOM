# CTFTTE-FPN-004 — Container / service misconfiguration chain

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-004`](../countertechniques/CTFTCTE-FPN-004.md) — Chain service misconfig and container escape to host

---

## How the challenge author hides

The flag requires chaining a service-level misconfiguration (weak credentials, exposed API, SSRF) with a container-escape technique to break out to the host filesystem.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1611 | Escape to Host | Container escape. |
| T1190 | Exploit Public-Facing Application | Service exploitation. |

## Tools

- docker / kubectl
- deepce
- curl / httpie

## References

- https://github.com/stealthcopter/deepce
- Add challenge write-up link
