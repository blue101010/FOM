# CTFTCTE-NET-008 — Walk the FTP tree and read outside the root

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-008`](../techniques/CTFTTE-NET-008.md) — Anonymous FTP without chroot

---

## Offensive Recovery (CTF practitioner / solver)

Log in anonymously, list recursively, then attempt traversal out of the anonymous root. Harvest the configuration, dictionaries and databases disclosed — they are the fuel for the following stages, not the flag itself.

## Forensic / Blue-Team Perspective (DFIR analyst)

FTP server logs expose anonymous logins, out-of-root reads and bulk downloads; the controls are disabling anonymous access, enforcing chroot, and segmenting file ACLs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078 | Valid Accounts | Recovery uses the anonymous credential, then exceeds its intended directory scope. |

## Tools

- ftp
- curl
- lftp

## References

- Add challenge write-up link
