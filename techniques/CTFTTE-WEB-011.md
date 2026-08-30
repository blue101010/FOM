# CTFTTE-WEB-011 — Directory-traversal maze

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-011`](../countertechniques/CTFTCTE-WEB-011.md) — Traverse filtered paths (PHP labyrinth)

---

## How the challenge author hides

Path filters block traversal; the flag file is reachable only through filter quirks.

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
