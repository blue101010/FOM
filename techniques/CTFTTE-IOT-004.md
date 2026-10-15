# CTFTTE-IOT-004 — On-board serial console flag (UART/JTAG exposure)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-004`](../countertechniques/CTFTCTE-IOT-004.md) — Identify debug pads and read the serial console

---

## How the challenge author hides

The flag is only reachable through the device's debug interface: a UART console printing it
at boot, a U-Boot shell over serial, or a JTAG-exposed memory region. The concealment is
physical — unlabelled pads, an uncommon baud rate, a bootlog that scrolls past — and the
assumption that players will not pick up a serial adapter.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1200 | Hardware Additions | Debug interfaces (UART/JTAG) are the physical entry point to a device. |

## Tools

- [minicom](../tools/CTFTTOU-241.md)
- [flashrom](../tools/CTFTTOU-240.md)
- multimeter / logic analyzer

## References

- <https://cwe.mitre.org/data/definitions/1204.html> (CWE-1204: Internal Network interfaces)
- Add challenge write-up link
