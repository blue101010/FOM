# CTFTCTE-ICS-002 — Read S7 data blocks

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-002`](../techniques/CTFTTE-ICS-002.md) — S7comm PLC memory hiding

---

## Offensive Recovery (CTF practitioner / solver)

Use an S7 client to read the relevant data block and extract the value.

## Forensic / Blue-Team Perspective (DFIR analyst)

Data-block reads document the accessible memory regions of the device.

## Tools

- snap7
- python-snap7

## References

- Add challenge write-up link