# CTFTCTE-NET-004 — Crack WPA2 handshakes, decode Wi-Fi captures

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-004`](../techniques/CTFTTE-NET-004.md) — Wi-Fi capture / handshake concealment

---

## Offensive Recovery (CTF practitioner / solver)

Extract the EAPOL 4-way handshake, run dictionary attacks (aircrack/hashcat mode 22000), then decrypt frames to read the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Wireless captures preserve association, handshake and traffic timing; cracking is governed by lab scope.

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

- <https://www.aircrack-ng.org/>

