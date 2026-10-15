# CTFTCTE-IOT-005 — Sniff and decode the device radio protocol

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-005`](../techniques/CTFTTE-IOT-005.md) — Short-range IoT radio concealment (Zigbee/BLE/sub-GHz)

---

## Offensive Recovery (CTF practitioner / solver)

1. Identify the band and protocol from the challenge story and hardware (Zigbee 2.4 GHz
   OQPSK, BLE advertisements, 433/868 MHz ASK/OOK remotes).
2. Capture: killerbee/ubertooth for Zigbee/BLE, bettercap for BLE GATT, an SDR or
   rtl_433 for sub-GHz remotes.
3. Recover the link keys: Zigbee network keys often ship in the firmware (IOT-001) or
   via well-known Trust Center defaults; BLE pairing traffic is sniffeable only if
   captured during pairing — force a re-pair when possible.
4. Decode the frames to application payloads; sensor values and remotes often encode the
   flag in plain structured bytes.
5. Validate: the decoded payload satisfies the flag format.

## Forensic / Blue-Team Perspective (DFIR analyst)

Short-range device traffic is an exfiltration channel that never crosses the network
boundary: radio-audit devices on-site, inventory every radio-enabled product, and treat
firmware-shipped network keys as compromised by default.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Device radios carry their own application protocols over the air. |

## Tools

- ubertooth / killerbee ([CTFTTOU-277](../tools/CTFTTOU-277.md))
- bettercap
- rtl_433

## References

- <https://github.com/greatscottgadgets/ubertooth>
- <https://github.com/merbanan/rtl_433>
- Add challenge write-up link
