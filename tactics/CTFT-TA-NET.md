# NET — Network

> **Tactic ID:** `CTFT-TA-NET`  
> **HTB mapping:** HTB: Misc (Network)  
> **Techniques:** 7

## Description

Hiding flags behind network discovery, sniffing, tunneling and protocol-barrier puzzles.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

> Per-entry related ATT&CK IDs are rendered on every technique and
> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).


## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-NET-001](../techniques/CTFTTE-NET-001.md) | Port/service discovery maze | [CTFTCTE-NET-001](../countertechniques/CTFTCTE-NET-001.md) | Systematic port/service enumeration | T1046 |
| [CTFTTE-NET-002](../techniques/CTFTTE-NET-002.md) | DNS covert channel / tunnel | [CTFTCTE-NET-002](../countertechniques/CTFTCTE-NET-002.md) | Detect DNS tunneling and beaconing in PCAPs | T1071.004 |
| [CTFTTE-NET-003](../techniques/CTFTTE-NET-003.md) | SMB enumeration barrier | [CTFTCTE-NET-003](../countertechniques/CTFTCTE-NET-003.md) | Enumerate SMB shares/versions | T1021.002 |
| [CTFTTE-NET-004](../techniques/CTFTTE-NET-004.md) | Wi-Fi capture / handshake concealment | [CTFTCTE-NET-004](../countertechniques/CTFTCTE-NET-004.md) | Crack WPA2 handshakes, decode Wi-Fi captures | T1040 |
| [CTFTTE-NET-005](../techniques/CTFTTE-NET-005.md) | Traffic tunnel / port-forwarding relay | [CTFTCTE-NET-005](../countertechniques/CTFTCTE-NET-005.md) | Pivot via ssh -L/-R, chisel | T1572 / T1090 |
| [CTFTTE-NET-006](../techniques/CTFTTE-NET-006.md) | TTL / protocol-field covert channel | [CTFTCTE-NET-006](../countertechniques/CTFTCTE-NET-006.md) | Decode TTL/ICMP/padding channels | T1095 |
| [CTFTTE-NET-007](../techniques/CTFTTE-NET-007.md) | Packet-capture forensics maze | [CTFTCTE-NET-007](../countertechniques/CTFTCTE-NET-007.md) | Run beaconing/exfil/credential detectors over PCAPs | T1040 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
