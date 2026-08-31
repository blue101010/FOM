# NET — Network

> **Domain ID:** `CTFT-TA-NET`  
> **HTB mapping:** HTB: Misc (Network)  
> **Techniques:** 7

## Description

Hiding flags behind network discovery, sniffing, tunneling and protocol-barrier puzzles.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-NET-001](../techniques/CTFTTE-NET-001.md) | Port/service discovery maze | [CTFTCTE-NET-001](../countertechniques/CTFTCTE-NET-001.md) | Systematic port/service enumeration | T1046 |
| [CTFTTE-NET-002](../techniques/CTFTTE-NET-002.md) | DNS covert channel / tunnel | [CTFTCTE-NET-002](../countertechniques/CTFTCTE-NET-002.md) | Detect DNS tunneling and beaconing in PCAPs | T1071.004 |
| [CTFTTE-NET-003](../techniques/CTFTTE-NET-003.md) | SMB enumeration barrier | [CTFTCTE-NET-003](../countertechniques/CTFTCTE-NET-003.md) | Enumerate SMB shares/versions | T1021.002 |
| [CTFTTE-NET-004](../techniques/CTFTTE-NET-004.md) | Wi-Fi capture / handshake concealment | [CTFTCTE-NET-004](../countertechniques/CTFTCTE-NET-004.md) | Crack WPA2 handshakes, decode Wi-Fi captures | T1040 |
| [CTFTTE-NET-005](../techniques/CTFTTE-NET-005.md) | Traffic tunnel / port-forwarding relay | [CTFTCTE-NET-005](../countertechniques/CTFTCTE-NET-005.md) | Pivot via ssh -L/-R, chisel | T1572, T1090 |
| [CTFTTE-NET-006](../techniques/CTFTTE-NET-006.md) | TTL / protocol-field covert channel | [CTFTCTE-NET-006](../countertechniques/CTFTCTE-NET-006.md) | Decode TTL/ICMP/padding channels | T1095 |
| [CTFTTE-NET-007](../techniques/CTFTTE-NET-007.md) | Packet-capture forensics maze | [CTFTCTE-NET-007](../countertechniques/CTFTCTE-NET-007.md) | Run beaconing/exfil/credential detectors over PCAPs | T1040 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
