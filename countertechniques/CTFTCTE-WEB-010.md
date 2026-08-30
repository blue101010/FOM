# CTFTCTE-WEB-010 — Exploit LFI to RCE or flag read

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-010`](../techniques/CTFTTE-WEB-010.md) — LFI / log poisoning / php-filter chains

---

## Offensive Recovery (CTF practitioner / solver)

Use wrapper/filter chains (php://filter), poison logs with payloads, and include the flag or a shell.

## Forensic / Blue-Team Perspective (DFIR analyst)

Web logs retain LFI probe fingerprints; filter-chain requests are distinctive.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Public-app LFI exploitation. |

## Tools

- Burp Suite
- curl
- php filter-chain generator

## References

- https://github.com/synacktiv/php_filter_chain_generator
- Add challenge write-up link
