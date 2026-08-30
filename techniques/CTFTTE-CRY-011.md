# CTFTTE-CRY-011 — Protocol implementation flaw (Heartbleed-style)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-011`](../countertechniques/CTFTCTE-CRY-011.md) — Reproduce protocol memory-leak vulnerabilities

---

## How the challenge author hides

The challenge emulates a protocol memory-leak flaw (Heartbleed-style); the flag leaks from server memory.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Public-protocol memory-leak exploitation. |

## Tools

- openssl
- Python socket

## References

- https://heartbleed.com/
- Add challenge write-up link
