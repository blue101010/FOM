# CTFTCTE-CRY-011 — Reproduce protocol memory-leak vulnerabilities

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Counters technique:** [`CTFTTE-CRY-011`](../techniques/CTFTTE-CRY-011.md) — Protocol implementation flaw (Heartbleed-style)

---

## Offensive Recovery (CTF practitioner / solver)

Craft the malformed heartbeat/request, read the leaked buffer, and extract the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Protocol memory leaks are historical CVE evidence; reproduction is documented safely in labs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Public-protocol memory-leak exploitation. |

## Tools

- openssl
- Python socket

## References

- <https://heartbleed.com/>

