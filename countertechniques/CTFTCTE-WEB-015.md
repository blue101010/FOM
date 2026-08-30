# CTFTCTE-WEB-015 — Enumerate and exploit WordPress (wpscan)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-015`](../techniques/CTFTTE-WEB-015.md) — CMS / WordPress plugin flaw

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate plugins/users with wpscan, exploit the flaw or crack the login, and read the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

CMS logs record plugin-abuse patterns; version banners pin the vulnerable surface.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | CMS exploitation. |

## Tools

- wpscan
- curl
- hydra

## References

- https://wpscan.com/wordpress-security-scanner
- Add challenge write-up link
