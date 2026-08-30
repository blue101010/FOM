# CTFTTE-ICS-001 — Modbus holding-register concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-001`](../countertechniques/CTFTCTE-ICS-001.md) — Read Modbus registers

---

## How the challenge author hides

The flag is stored across Modbus holding/input registers on a simulated PLC.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0861 | Point & Tag Identification | ICS ATT&CK: Modbus register reads. |

## Tools

- pymodbus
- modbus-cli

## References

- https://github.com/pymodbus-dev/pymodbus
- Add challenge write-up link