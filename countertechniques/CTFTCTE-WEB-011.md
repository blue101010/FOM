# CTFTCTE-WEB-011 — Traverse filtered paths (PHP labyrinth)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-011`](../techniques/CTFTTE-WEB-011.md) — Directory-traversal maze

---

## Offensive Recovery (CTF practitioner / solver)

Bypass the filters (encodings, absolute paths, null bytes) and traverse to the flag file.

## Forensic / Blue-Team Perspective (DFIR analyst)

Traversal attempts appear as ../ patterns in access logs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Path-traversal exploitation. |

## Tools

- Burp Suite
- curl
- ffuf

## References

- <https://github.com/ffuf/ffuf>
- Add challenge write-up link
