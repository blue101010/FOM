# CTFTCTE-FPN-015 — Enumerate database defaults and disable dangerous procedures

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-015`](../techniques/CTFTTE-FPN-015.md) — Default database credential enabling command execution

---

## Offensive Recovery (CTF practitioner / solver)

Read account descriptions for password hints, then brute force the database
admin account with default-credential wordlists. Once authenticated, enable or
abuse `xp_cmdshell` to execute operating-system commands as the service
account and inspect its privileges.

## Forensic / Blue-Team Perspective (DFIR analyst)

Audit failed and successful SQL logons, and alert on `sp_configure`
modifications enabling dangerous procedures. Default service passwords are a
configuration-audit finding; restrict SQL service accounts to least privilege.

## Preconditions

- The database service is reachable (1433/tcp).
- A default or weak credential authenticates as an administrator account.

## Indicators

- An account description hints at an unchanged default password.
- A series of failed logons precedes a successful `sa` logon.
- `xp_cmdshell` is enabled and executes operating-system commands.

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
