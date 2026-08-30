# CTFTTE-HWR-001 — USB HID keystroke concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-HWR`](../tactics/CTFT-TA-HWR.md) — Hardware  
> **Paired counter-technique:** [`CTFTCTE-HWR-001`](../countertechniques/CTFTCTE-HWR-001.md) — Reconstruct keystrokes from captured USB HID traffic

---

## How the challenge author hides

Flag text is typed by a (simulated) USB keyboard; only HID report bytes — scan codes, not characters — are captured, hiding the keystrokes behind the HID protocol.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1056.001 | Keylogging | Captured HID traffic echoes keylogging data sources; ATT&CK omits the scan-code recovery detail. |

## Tools

- usbmon
- Wireshark
- usbhid-dump
- tshark

## References

- <https://wiki.wireshark.org/CaptureSetup/USB>
- Add challenge write-up link
