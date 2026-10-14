# CTFTCTE-FPN-014 — Constrain delegated endpoints and log session commands

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-014`](../techniques/CTFTTE-FPN-014.md) — Injection through a delegated session configuration

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate startup scripts and shared folders for the constrained endpoint's
module source. Audit each module for parameters concatenated into commands,
inject through the unsafe parameter to execute commands as the delegated
principal, and plant a local persistence account before leaving the endpoint.

## Forensic / Blue-Team Perspective (DFIR analyst)

Enable session transcripts and script-block logging for constrained endpoints.
String concatenation into execution primitives inside role-capability modules is
the review signal; unusual local account creation (event 4720) marks abuse.

## Preconditions

- A constrained session endpoint is reachable with valid credentials.
- The module source backing the endpoint is retrievable.

## Indicators

- Startup scripts or shares expose the endpoint's module project.
- A module parameter flows unsanitized into an execution primitive.
- A new local user appears in the local Administrators group.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.001 | Command and Scripting Interpreter: PowerShell | Injection rides the delegated PowerShell endpoint. |
| T1136.001 | Create Account: Local Account | The injection is used to plant local persistence. |

## Tools

- [Enter-PSSession / New-PSSession](../tools/CTFTTOU-025.md)
- [evil-winrm](../tools/CTFTTOU-024.md)

## References

- <https://learn.microsoft.com/en-us/powershell/jea/overview>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
