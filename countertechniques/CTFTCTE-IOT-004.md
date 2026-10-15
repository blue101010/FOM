# CTFTCTE-IOT-004 — Identify debug pads and read the serial console

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-004`](../techniques/CTFTTE-IOT-004.md) — On-board serial console flag (UART/JTAG exposure)

---

## Offensive Recovery (CTF practitioner / solver)

1. Locate the debug interface: continuity-scan for TX/RX/GND pads (TX idles high); typical
   baud rates are 115200, 57600, 38400, 9600.
2. Attach a USB-UART adapter, capture the full boot log — flags are often printed by boot
   scripts before the console is silenced.
3. If the console offers a U-Boot/bootloader shell, dump the environment (`printenv`),
   memory (`md`) and flash; interrupt the boot to reach it.
4. For JTAG exposure, enumerate the chain and read memory via openocd before attempting
   anything invasive.
5. Validate: the boot log, env or dump contains the flag or points to the next stage.

## Forensic / Blue-Team Perspective (DFIR analyst)

Exposed debug interfaces defeat firmware confidentiality entirely: a device audit includes
pad-mapping and bootlog capture for every model, and production devices should have UART
disabled or console output silenced. CWE-1204 anchors the class.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1200 | Hardware Additions | Debug interfaces (UART/JTAG) are the physical entry point to a device. |

## Tools

- [minicom](../tools/CTFTTOU-241.md)
- [flashrom](../tools/CTFTTOU-240.md)
- openocd

## References

- <https://cwe.mitre.org/data/definitions/1204.html>
- Add challenge write-up link
