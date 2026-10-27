# IOT — IoT / Embedded

> **Domain ID:** `CTFT-TA-IOT`  
> **HTB mapping:** HTB: Misc (IoT)  
> **Techniques:** 7

## Description

Hiding/recovering flags inside internet-connected devices: consumer firmware images and their
embedded web stacks, IoT messaging brokers (MQTT/CoAP), on-board serial consoles, short-range
device radio (Zigbee/BLE/sub-GHz), and the emulation of embedded binaries (MIPS/ARM).
Distinct from HWR (electronic badges without a network story), ICS (industrial control
systems) and SDR (generic RF signal puzzles): the subject here is the consumer/connected
device and its firmware-to-cloud chain.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-IOT-001](../techniques/CTFTTE-IOT-001.md) | Vendor firmware image with hardcoded secrets | [CTFTCTE-IOT-001](../countertechniques/CTFTCTE-IOT-001.md) | Unpack the firmware image and grep the rootfs for secrets | T1078.001 |
| [CTFTTE-IOT-002](../techniques/CTFTTE-IOT-002.md) | Device web-admin backdoor / default credential gate | [CTFTCTE-IOT-002](../countertechniques/CTFTCTE-IOT-002.md) | Enumerate the device web stack and abuse its backdoor endpoints | T1190 |
| [CTFTTE-IOT-003](../techniques/CTFTTE-IOT-003.md) | Unauthenticated message-broker topic/queue concealment | [CTFTCTE-IOT-003](../countertechniques/CTFTCTE-IOT-003.md) | Enumerate broker topics/queues and capture service traffic | T1552 |
| [CTFTTE-IOT-004](../techniques/CTFTTE-IOT-004.md) | On-board serial console flag (UART/JTAG exposure) | [CTFTCTE-IOT-004](../countertechniques/CTFTCTE-IOT-004.md) | Identify debug pads and read the serial console | T1200 |
| [CTFTTE-IOT-005](../techniques/CTFTTE-IOT-005.md) | Short-range IoT radio concealment (Zigbee/BLE/sub-GHz) | [CTFTCTE-IOT-005](../countertechniques/CTFTCTE-IOT-005.md) | Sniff and decode the device radio protocol | T1071 |
| [CTFTTE-IOT-006](../techniques/CTFTTE-IOT-006.md) | Embedded-binary exploitation behind device emulation (MIPS/ARM) | [CTFTCTE-IOT-006](../countertechniques/CTFTCTE-IOT-006.md) | Emulate the service and exploit the embedded binary | T1210 |
| [CTFTTE-IOT-007](../techniques/CTFTTE-IOT-007.md) | BLE GATT characteristic gating (pairing / passkey / MAC allow-list / password) | [CTFTCTE-IOT-007](../countertechniques/CTFTCTE-IOT-007.md) | Enumerate and drive BLE GATT as a client | T1071, T1110.001 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
