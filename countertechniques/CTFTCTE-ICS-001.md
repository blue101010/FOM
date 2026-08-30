# CTFTCTE-ICS-001 — Read Modbus registers

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-001`](../techniques/CTFTTE-ICS-001.md) — Modbus holding-register concealment

---

## Offensive Recovery (CTF practitioner / solver)

Connect and read the register range, then reassemble the bytes into the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Register reads document the unauthenticated data exposure typical of Modbus.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0861 | Point & Tag Identification | ICS ATT&CK: Modbus register reads. |

## Tools

- pymodbus
- modbus-cli

## References

- <https://github.com/pymodbus-dev/pymodbus>
- Add challenge write-up link