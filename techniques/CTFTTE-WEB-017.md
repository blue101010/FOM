# CTFTTE-WEB-017 — Host-header / vhost fuzzing

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-017`](../countertechniques/CTFTCTE-WEB-017.md) — Fuzz vhosts and host headers

---

## How the challenge author hides

The flag app is served only under a specific Host header or virtual host.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | Vhost / host-header discovery. |

## Tools

- ffuf
- gobuster
- Burp Intruder

## References

- https://github.com/ffuf/ffuf
- Add challenge write-up link
