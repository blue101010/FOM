# CTFTTE-IOT-005 — Short-range IoT radio concealment (Zigbee/BLE/sub-GHz)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-005`](../countertechniques/CTFTCTE-IOT-005.md) — Sniff and decode the device radio protocol

---

## How the challenge author hides

The flag transits a short-range device radio: a Zigbee sensor network, a BLE GATT
characteristic or advertisement, or a sub-GHz (433/868 MHz) remote. The concealment is the
air interface: the protocol looks opaque, traffic is periodic and low-volume, and the key
material (Zigbee network key, BLE pairing) may be recoverable only from the device firmware.
Distinct from SDR-001 (generic RF puzzles) and NET-004 (Wi-Fi): the subject is the IoT
protocol ecosystem and its device pairing.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Device radios carry their own application protocols over the air. |

## Tools

- [ubertooth / killerbee](../tools/CTFTTOU-277.md)
- [bettercap](../tools/CTFTTOU-283.md)
- [gatttool](../tools/CTFTTOU-416.md)

## References

- <https://github.com/greatscottgadgets/ubertooth>
- [bi0s — BLE CTF Infinity write-up](https://blog.bi0s.in/2026/08/25/Hardware/BLE_CTF_Infinity_Writeup_BIOS/)

> For BLE **GATT client interaction** (read/write handles, pairing, MAC spoof, brute force) see the
> dedicated pair [`CTFTTE-IOT-007`](CTFTTE-IOT-007.md) / [`CTFTCTE-IOT-007`](../countertechniques/CTFTCTE-IOT-007.md).
