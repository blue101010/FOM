# CTFTCTE-MOB-005 — Hook the app to satisfy runtime checks

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-005`](../techniques/CTFTTE-MOB-005.md) — Runtime/device-conditioned flag

---

## Offensive Recovery (CTF practitioner / solver)

Hook the conditional methods to force the success branch and read the value.

## Forensic / Blue-Team Perspective (DFIR analyst)

Hook traces document which checks gated the flag and how they were satisfied.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1497 | Virtualization/Sandbox Evasion | Runtime/device-conditioned checks echo sandbox evasion. |

## Tools

- Frida
- objection

## References

- <https://frida.re/>
- Add challenge write-up link