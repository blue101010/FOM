# CTFTCTE-MOB-008 — Use anti-anti-Frida techniques

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-008`](../techniques/CTFTTE-MOB-008.md) — Frida detection

---

## Offensive Recovery (CTF practitioner / solver)

Use spawn-based injection, early injection before detection checks, or embed Frida gadget to evade detection. Modify detection logic at runtime with Frida itself.

## Forensic / Blue-Team Perspective (DFIR analyst)

Anti-anti instrumentation traces document which detection mechanisms were bypassed and how persistent access was established.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1622 | Debugger Evasion | Frida detection as a debugger evasion mechanism. |

## Tools

- [Frida](../tools/CTFTTOU-169.md)
- [objection](../tools/CTFTTOU-170.md)

## References

- <https://frida.re/>
- Add challenge write-up link
