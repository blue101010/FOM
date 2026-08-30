# CTFTTE-MOB-003 — Certificate pinning as capture barrier

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-003`](../countertechniques/CTFTCTE-MOB-003.md) — Bypass pinning to observe traffic

---

## How the challenge author hides

TLS pinning prevents intercepting the request/response that carries the flag.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1557 | Man-in-the-Middle | Certificate pinning as a MITM barrier. |

## Tools

- Frida
- objection
- mitmproxy/Burp

## References

- https://frida.re/
- Add challenge write-up link