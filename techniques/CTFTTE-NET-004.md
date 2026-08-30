# CTFTTE-NET-004 — Wi-Fi capture / handshake concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-004`](../countertechniques/CTFTCTE-NET-004.md) — Crack WPA2 handshakes, decode Wi-Fi captures

---

## How the challenge author hides

The flag rides over Wi-Fi: the challenge ships a .cap with a WPA handshake or encrypted frames, and the passphrase is the gate.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1040 | Network Sniffing | Wi-Fi capture echoes network sniffing; ATT&CK omits the handshake-cracking craft. |

## Tools

- aircrack-ng
- hashcat
- hcxdumptool
- Wireshark

## References

- https://www.aircrack-ng.org/
- Add challenge write-up link
