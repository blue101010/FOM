# CTFTTOU-243 — usbhid-dump (legacy)

> **Tool ID:** `CTFTTOU-243`  
> **Related techniques/counters:** (historical) CTFTTE-HWR-001, CTFTCTE-HWR-001

## Description

Dumps USB HID device report descriptors and streams. LEGACY: upstream
(DIGImend) has been unmaintained for years — do not build a workflow on it. The maintained
equivalents are [usbmon](CTFTTOU-278.md) (kernel capture, read directly by Wireshark/tshark)
for the capture step and the CTFT-authored
[usbhid-keystroke-decode.py](scripts/usbhid-keystroke-decode.py) ([CTFTTOU-279](CTFTTOU-279.md))
for the scan-code-to-text step. Kept only so the identifier is never silently reused.

## URL

<https://github.com/DIGImend/usbhid-dump>

## Related Techniques

(historical) CTFTTE-HWR-001, CTFTCTE-HWR-001
