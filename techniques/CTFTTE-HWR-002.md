# CTFTTE-HWR-002 — Badge / embedded-device firmware concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-HWR`](../tactics/CTFT-TA-HWR.md) — Hardware  
> **Paired counter-technique:** [`CTFTCTE-HWR-002`](../countertechniques/CTFTCTE-HWR-002.md) — Dump and reverse badge firmware

---

## How the challenge author hides

The flag lives in an electronic badge or embedded device: in firmware, EEPROM, or behind a hidden UART/JTAG/SPI interface.

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

- https://github.com/ReFirmLabs/binwalk
- Add challenge write-up link
