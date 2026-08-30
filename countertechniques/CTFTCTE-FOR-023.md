# CTFTCTE-FOR-023 — Analyze SELinux contexts blocking artifacts

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-023`](../techniques/CTFTTE-FOR-023.md) — SELinux context-based concealment

---

## Offensive Recovery (CTF practitioner / solver)

Inspect contexts (ls -Z), identify the blocking policy, and read the file through allowed contexts or policy relaxation.

## Forensic / Blue-Team Perspective (DFIR analyst)

Label forensics shows what a process could touch; context anomalies point at hidden artifacts.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1562 | Impair Defenses | Policy-based hiding echoes defense impairment. |

## Tools

- ls -Z
- semanage
- audit2allow
- setenforce

## References

- <https://selinuxproject.org/>

