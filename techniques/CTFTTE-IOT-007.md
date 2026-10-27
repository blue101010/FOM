# CTFTTE-IOT-007 — BLE GATT characteristic gating (pairing / passkey / MAC allow-list / password)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-007`](../countertechniques/CTFTCTE-IOT-007.md) — Enumerate and drive BLE GATT as a client

---

## How the challenge author hides

The flag sits inside a **BLE GATT characteristic** reachable only after clearing a client-side gate,
not by sniffing the air. Typical gates (as in `BLE CTF Infinity`): the flag handle is read only after
writing a selector to another handle; the peripheral requires **BLE pairing with a passkey**; it bonds
only to a **specific BD_ADDR** (MAC allow-list); or it releases the flag only after the **correct
password is written into a characteristic**. The challenge is GATT interaction and its authentication,
distinct from IOT-005 (sniffing/decoding the device radio) and from SDR RF puzzles.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | GATT is BLE's application protocol; the flag is an attribute value. |
| T1110.001 | Brute Force: Password Guessing | Passkey / characteristic-password gates are brute-forced. |

## Tools

- [gatttool](../tools/CTFTTOU-416.md)
- [bettercap](../tools/CTFTTOU-283.md)
- bluetoothctl
- btmgmt

## References

- [bi0s — BLE CTF Infinity write-up](https://blog.bi0s.in/2026/08/25/Hardware/BLE_CTF_Infinity_Writeup_BIOS/)
- <https://github.com/hackgnar/ble_ctf_infinity>
