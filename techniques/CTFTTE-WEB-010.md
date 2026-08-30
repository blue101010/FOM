# CTFTTE-WEB-010 — LFI / log poisoning / php-filter chains

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-010`](../countertechniques/CTFTCTE-WEB-010.md) — Exploit LFI to RCE or flag read

---

## How the challenge author hides

A local file include lets the solver read the flag or reach RCE through log poisoning or PHP filter chains.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Public-app LFI exploitation. |

## Tools

- Burp Suite
- curl
- php filter-chain generator

## References

- <https://github.com/synacktiv/php_filter_chain_generator>
- Add challenge write-up link
