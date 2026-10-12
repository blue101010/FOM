# CTFTTE-NET-008 — Anonymous FTP without chroot

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-008`](../countertechniques/CTFTCTE-NET-008.md) — Walk the FTP tree and read outside the root

---

## How the challenge author hides

An anonymous FTP service is configured without a chroot: the interesting files (configuration, dictionaries, operator databases, token material) sit above the anonymous root, reachable by walking out of the jail. The files disclosed are fuel for the next stages, not necessarily the final flag.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078 | Valid Accounts | The anonymous account is the valid credential; the missing chroot is the CTF-specific defect. |

## Tools

- ftp
- curl
- lftp

## References

- Add challenge write-up link
