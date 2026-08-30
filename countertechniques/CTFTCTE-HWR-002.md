# CTFTCTE-HWR-002 — Dump and reverse badge firmware

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-HWR`](../tactics/CTFT-TA-HWR.md) — Hardware  
> **Counters technique:** [`CTFTTE-HWR-002`](../techniques/CTFTTE-HWR-002.md) — Badge / embedded-device firmware concealment

---

## Offensive Recovery (CTF practitioner / solver)

Identify the exposed interfaces (UART/JTAG/SPI), dump firmware or memory, and reverse it for strings and logic.

## Forensic / Blue-Team Perspective (DFIR analyst)

Hardware triage records pinouts and interface activity; firmware dumps are hashed and preserved as evidence before analysis.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Firmware-level hiding echoes obfuscated payloads. |

## Tools

- minicom
- flashrom
- binwalk
- ghidra

## References

- <https://github.com/ReFirmLabs/binwalk>

