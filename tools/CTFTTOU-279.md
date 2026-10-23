# CTFTTOU-279 — usbhid-keystroke-decode.py

> **Tool ID:** `CTFTTOU-279`  
> **Related techniques/counters:** CTFTTE-HWR-001, CTFTCTE-HWR-001

## Description

CTFT-authored HID boot-keyboard decoder (Python, standard library only — no pip install,
safe on Kali under PEP 668). Translates captured 8-byte HID reports (space-separated hex,
continuous hex, or tshark `usb.capdata`/`usbhid.data` exports) into typed text: modifier
handling (Shift), press/repeat suppression, and `--layout` for non-US keymaps
(one line per usage: `<usage> <normal> [<shifted>]`). `--selftest` runs synthetic reports.

Replaces the unmaintained `usbhid-dump` ([CTFTTOU-243](CTFTTOU-243.md)) for the decode step;
capture itself stays with [usbmon](CTFTTOU-278.md) and Wireshark/tshark.

## URL

<https://github.com/blue101010/FOM/blob/main/tools/scripts/usbhid-keystroke-decode.py>

Local copy: [scripts/usbhid-keystroke-decode.py](scripts/usbhid-keystroke-decode.py)

## Related Techniques

CTFTTE-HWR-001, CTFTCTE-HWR-001
