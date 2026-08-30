# CTFTTE-NET-003 — SMB enumeration barrier

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-003`](../countertechniques/CTFTCTE-NET-003.md) — Enumerate SMB shares/versions

---

## How the challenge author hides

The flag is inside an SMB share whose name or permissions are part of the puzzle; protocol version mismatches hide content.

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

- https://www.samba.org/
- Add challenge write-up link
