# CTFTCTE-NET-003 — Enumerate SMB shares/versions

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-003`](../techniques/CTFTTE-NET-003.md) — SMB enumeration barrier

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate shares and dialect with smbclient/nmap scripts, list anonymously, and download the flag file.

## Forensic / Blue-Team Perspective (DFIR analyst)

SMB session logs and share enumeration are standard IR steps; auditing records who listed what and when.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1021.002 | SMB/Windows Admin Shares | Share enumeration mirrors admin-share access patterns. |

## Tools

- smbclient
- enum4linux
- crackmapexec
- nmap

## References

- <https://www.samba.org/>

