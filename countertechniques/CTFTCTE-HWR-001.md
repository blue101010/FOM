# CTFTCTE-HWR-001 — Reconstruct keystrokes from captured USB HID traffic

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-HWR`](../tactics/CTFT-TA-HWR.md) — Hardware  
> **Counters technique:** [`CTFTTE-HWR-001`](../techniques/CTFTTE-HWR-001.md) — USB HID keystroke concealment

---

## Offensive Recovery (CTF practitioner / solver)

Decode the USB HID report descriptor and translate scan codes back into characters, including modifiers and non-US layouts.

## Forensic / Blue-Team Perspective (DFIR analyst)

USB capture analysis treats keyboards as peripheral evidence; scan-code translation is deterministic and can be replayed against capture files.

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

