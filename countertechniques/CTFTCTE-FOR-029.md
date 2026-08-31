# CTFTCTE-FOR-029 — Extract and analyse registry hives from a forensic image

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-029`](../techniques/CTFTTE-FOR-029.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Open the container first: AD1 is AccessData's logical image format and FTK Imager exports its tree
directly; for E01 use `ewfmount`, for raw images mount read-only. Extract `SOFTWARE`, `SYSTEM`,
`NTUSER.DAT` and their transaction logs, then parse offline with Registry Explorer or
`python-registry`. Go straight to the autostart surface — `Run`, `RunOnce`, `Services`, scheduled
task caches — and decode every value that is not plain text. A base64 blob in a `Run` value is the
payload, not the answer: decode it and read what it does.

## Forensic / Blue-Team Perspective (DFIR analyst)

Replay the `.LOG1`/`.LOG2` transaction logs before parsing, otherwise the hive you analyse is the
last flushed state and the most recent write — often the persistence itself — is missing. Key
last-write timestamps date the persistence and anchor it in the timeline.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1547.001 | Registry Run Keys / Startup Folder | Recovering the persistence entry offline. |
| T1027.010 | Command Obfuscation | Decoding the stored stager. |
| T1562.001 | Impair Defenses | Identifying AMSI/ETW tampering inside the decoded payload. |

## Tools

- FTK Imager
- Registry Explorer
- hivex / python-registry
- CyberChef

## References

**Sources**

- (1) [Registry hive file format](https://learn.microsoft.com/windows/win32/sysinfo/registry-hives)

**Writeups**

- Add challenge write-up link
