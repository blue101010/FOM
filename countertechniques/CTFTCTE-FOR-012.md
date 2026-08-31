# CTFTCTE-FOR-012 — Retrieve information from rMQR codes

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-012`](../techniques/CTFTTE-FOR-012.md)  

---

## Offensive Recovery (CTF practitioner / solver)

rMQR (rectangular Micro QR) uses a rectangular grid that most consumer decoders reject. Use a
reader that implements the ISO/IEC 23941 layout — ZXingReader decodes rMQR where zbarimg does
not — or reconstruct the module grid manually and apply the rMQR version table.

## Forensic / Blue-Team Perspective (DFIR analyst)

An rMQR symbol in evidence is a strong authorship signal: the format is rare outside deliberate
concealment, and its presence is itself worth recording.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | rMQR encodings are CTF-specific obfuscation ATT&CK omits. |

## Tools

Use `FOMTOU004` (FOM) -> [CTFTTOU-004](../tools/CTFTTOU-004.md) - ZXingReader like in CTF Writeup ref (1)

## References

**Writeups**

- (1) [NAHAMCONF 2024 RMQR challenge](https://github.com/blue101010/writeups/blob/main/2024/NAHAMCONF/qrrrrrr/README.md)
- (2) [QRRRRRRRR — NahamCon CTF](https://medium.com/@inferiorak/qrrrrrrrr-nahamcon-ctf-2024-writeup-by-inferiorak-063406df187e)

**Sources**

- (1) [QR Code Model 2 Structure and Algorithms](https://franckybox.com/wp-content/uploads/qrcode.pdf)

<https://en.wikipedia.org/wiki/JAB_Code>
