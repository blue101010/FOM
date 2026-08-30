# CTFTTE-MOB-005 — Runtime/device-conditioned flag

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-005`](../countertechniques/CTFTCTE-MOB-005.md) — Hook the app to satisfy runtime checks

---

## How the challenge author hides

The flag only renders when device/root/emulator/time conditions are met.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1497 | Virtualization/Sandbox Evasion | Runtime/device-conditioned checks echo sandbox evasion. |

## Tools

- Frida
- objection

## References

- https://frida.re/
- Add challenge write-up link