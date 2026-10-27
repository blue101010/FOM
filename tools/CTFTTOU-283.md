# CTFTTOU-283 — bettercap

> **Tool ID:** `CTFTTOU-283`  
> **Related techniques/counters:** CTFTTE-IOT-005, CTFTCTE-IOT-005, CTFTTE-IOT-007, CTFTCTE-IOT-007

## Description

Swiss-army knife for network, Wi-Fi, Bluetooth Low Energy and HID wireless recon and man-in-the-middle attacks, including BLE device enumeration and characteristic read/write.

## URL

<https://github.com/bettercap/bettercap>

## Usage

```bash
bettercap -eval "ble.recon on; ble.show"   # discover BLE peripherals
bettercap -eval "ble.enum <MAC>"           # enumerate a device's services / characteristics / handles
```

## Related Techniques

CTFTTE-IOT-005, CTFTCTE-IOT-005, CTFTTE-IOT-007, CTFTCTE-IOT-007

## References

- [bettercap](https://github.com/bettercap/bettercap)
- [bi0s — BLE CTF Infinity write-up](https://blog.bi0s.in/2026/08/25/Hardware/BLE_CTF_Infinity_Writeup_BIOS/)
