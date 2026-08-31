# CTFTCTE-FOR-011 — Retrieve information from QR codes

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-011`](../techniques/CTFTTE-FOR-011.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Retrieve information from QR codes based on the legitimate specifications and extra methods
(like steganography or specific algorithms). Damaged symbols often still decode: Reed-Solomon
error correction tolerates up to 30% loss at level H, so repair the finder patterns and retry
before assuming the payload is unrecoverable.

## Forensic / Blue-Team Perspective (DFIR analyst)

A decoded QR payload is attacker-controlled input. Record the raw modules alongside the decoded
string so the decode can be reproduced independently.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | QR-code encodings are CTF-specific obfuscation ATT&CK omits. |

## Tools

Use [FOMTOU004 - ZXingReader](https://github.com/blue101010/FOM/blob/main/tools/FOMTOU004.md) like in CTF Writeup ref (1)

## References

**Sources**

- (1) [QR Code Model 2 Structure and Algorithms](https://franckybox.com/wp-content/uploads/qrcode.pdf)

**Writeups**

- (1) [NAHAMCONF 2024 RMQR challenge](https://github.com/blue101010/writeups/blob/main/2024/NAHAMCONF/qrrrrrr/README.md)
- (2) [QR Code Model 2 Structure and Algorithms](https://franckybox.com/wp-content/uploads/qrcode.pdf)
- (3) [QRRRRRRRR — NahamCon CTF](https://medium.com/@inferiorak/qrrrrrrrr-nahamcon-ctf-2024-writeup-by-inferiorak-063406df187e)
