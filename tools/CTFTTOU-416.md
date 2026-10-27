# CTFTTOU-416 — gatttool

> **Tool ID:** `CTFTTOU-416`  
> **Related techniques/counters:** CTFTTE-IOT-005, CTFTCTE-IOT-005, CTFTTE-IOT-007, CTFTCTE-IOT-007

## Description

BlueZ command-line **GATT client** for Bluetooth Low Energy. Connects to a peripheral and reads/writes
GATT characteristics by handle or UUID, enumerates the attribute table, and subscribes to
notifications/indications — the primary way to interact with a BLE device from Linux when solving a
GATT-gated challenge. Ships with BlueZ (deprecated upstream in favour of `bluetoothctl`'s GATT menu and
D-Bus, but still bundled and widely used in CTF write-ups). Installed on Kali (`/usr/bin/gatttool`).

## URL

- <https://github.com/bluez/bluez>

## Usage

```bash
gatttool -b <MAC> --characteristics              # enumerate char handles / properties / UUIDs
gatttool -b <MAC> --char-read -a 0x0016          # read a characteristic by handle
gatttool -b <MAC> --char-read -a 0x0016 | awk -F': ' '{print $2}' | xxd -r -p   # decode hex value
gatttool -b <MAC> --char-write-req -a 0x002e -n $(echo -n "value" | xxd -ps)    # write (ack'd)
gatttool -b <MAC> -I                             # interactive mode (connect; primary; char-read-hnd …)
```

## Related Techniques

CTFTTE-IOT-005, CTFTCTE-IOT-005, CTFTTE-IOT-007, CTFTCTE-IOT-007

## References

- [BlueZ (gatttool)](https://github.com/bluez/bluez)
- [bi0s — BLE CTF Infinity write-up](https://blog.bi0s.in/2026/08/25/Hardware/BLE_CTF_Infinity_Writeup_BIOS/)
- <https://github.com/hackgnar/ble_ctf_infinity>
