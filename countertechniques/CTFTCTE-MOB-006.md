# CTFTCTE-MOB-006 — Bypass anti-hooking with Frida

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-006`](../techniques/CTFTTE-MOB-006.md) — Native code anti-hooking

---

## Offensive Recovery (CTF practitioner / solver)

Use Frida to hook functions before anti-hooking checks trigger, or patch the checks in memory to allow instrumentation.

## Forensic / Blue-Team Perspective (DFIR analyst)

Hook traces document which anti-hooking checks were bypassed and how instrumentation was established.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1406 | Obfuscated Files or Information (Mobile) | Native code anti-hooking. |

## Tools

- [Frida](../tools/CTFTTOU-169.md)
- [objection](../tools/CTFTTOU-170.md)
- [Ghidra](../tools/CTFTTOU-073.md)

## References

- <https://frida.re/>
- Add challenge write-up link
