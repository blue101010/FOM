# CTFTTE-FPN-015 — Default database credential enabling command execution

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-015`](../countertechniques/CTFTCTE-FPN-015.md) — Enumerate database defaults and disable dangerous procedures

---

## How the challenge author hides

A server exposes an MSSQL instance whose `sa` account still uses a default
password. The only hint is buried in a service account's description text. Once
the credential is guessed, the solver escalates through `xp_cmdshell`, which the
author left enabled, to run commands as the SQL service account.

## Evidence expected

- Port 1433 is open on a member server.
- An account description or documentation hints at an unchanged default password.
- The database account can execute operating-system commands.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.001 | Valid Accounts: Default Accounts | The `sa` account authenticates with a default secret. |
| T1505.001 | Server Software Component: SQL Stored Procedures | `xp_cmdshell` turns SQL access into command execution. |

## Tools

- [netexec](../tools/CTFTTOU-016.md) (mssql protocol)
- [mssqlclient.py](../tools/CTFTTOU-026.md)
- [SecLists](../tools/CTFTTOU-027.md) default-credential wordlists

## References

- <https://www.thehacker.recipes/ad/movement/mssql>
- <https://medium.com/etticblog/hfctf25-write-up-corporate-digital-soul-df6ad0117a1f>
