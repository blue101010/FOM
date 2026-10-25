# CTFTTE-MOB-006 — Native code anti-hooking

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-006`](../countertechniques/CTFTCTE-MOB-006.md) — Bypass anti-hooking with Frida

---

## How the challenge author hides

Native library code contains the flag but implements anti-hooking checks that detect and evade dynamic instrumentation attempts.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1406 | Obfuscated Files or Information (Mobile) | Native code anti-hooking. |

## Tools

- Frida
- objection
- [Ghidra](../tools/CTFTTOU-073.md)

## References

- <https://frida.re/>
- Add challenge write-up link
