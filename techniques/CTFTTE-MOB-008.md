# CTFTTE-MOB-008 — Frida detection

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-008`](../countertechniques/CTFTCTE-MOB-008.md) — Use anti-anti-Frida techniques

---

## How the challenge author hides

The app implements Frida detection mechanisms (library checks, port scans, thread enumeration, etc.) and alters behavior or refuses to reveal the flag when Frida is detected.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1622 | Debugger Evasion | Frida detection as a debugger evasion mechanism. |

## Tools

- Frida
- objection

## References

- <https://frida.re/>
- Add challenge write-up link
