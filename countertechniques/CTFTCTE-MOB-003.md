# CTFTCTE-MOB-003 — Bypass pinning to observe traffic

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-003`](../techniques/CTFTTE-MOB-003.md) — Certificate pinning as capture barrier

---

## Offensive Recovery (CTF practitioner / solver)

Hook the pinning/validation logic at runtime to allow a proxy to read the traffic.

## Forensic / Blue-Team Perspective (DFIR analyst)

Instrumentation logs show where validation was disabled to enable capture.

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