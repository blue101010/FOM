# CTFTTE-FOR-023 — SELinux context-based concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-023`](../countertechniques/CTFTCTE-FOR-023.md) — Analyze SELinux contexts blocking artifacts

---

## How the challenge author hides

Files are labeled with SELinux contexts that deny access; the flag is present but context-blocked.

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
- Add challenge write-up link
