# CTFTTE-FPN-014 — Injection through a delegated session configuration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-014`](../countertechniques/CTFTCTE-FPN-014.md) — Constrain delegated endpoints and log session commands

---

## How the challenge author hides

The box is only reachable through a constrained delegation endpoint (JEA) backed
by a custom module. A module parameter is concatenated unsafely into a command,
so the endpoint becomes an injection gate. The module source itself is
distributed through a shared scripts folder, making the review step part of the
challenge.

## Evidence expected

- A startup or deployment script references a constrained session configuration.
- A shared folder exposes the module source used by the endpoint.
- One module parameter is concatenated into an executable command.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1059.001 | Command and Scripting Interpreter: PowerShell | Injection rides the delegated PowerShell endpoint. |
| T1136.001 | Create Account: Local Account | The injection is used to plant local persistence. |

## Tools

- [Enter-PSSession](../tools/CTFTTOU-297.md)
- [New-PSSession](../tools/CTFTTOU-298.md)
- [evil-winrm](../tools/CTFTTOU-024.md)
- [netexec](../tools/CTFTTOU-016.md) (spider_plus module)

## References

- <https://learn.microsoft.com/en-us/powershell/jea/overview>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
