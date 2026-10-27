# CTFTTE-FOR-010 — Use special encoding system to hide data with visual, machine-readable form.

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-010`](../countertechniques/CTFTCTE-FOR-010.md)  

---

## How the challenge author hides

Use special encoding system to hide data with visual, machine-readable form

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Visual machine-readable encodings (QR) are CTF-specific obfuscation ATT&CK omits. |

## Tools

- [ZXingReader](../tools/CTFTTOU-004.md) — multi-format 1D/2D (QR, Data Matrix, Aztec, PDF417, rMQR)
- [zbar](../tools/CTFTTOU-423.md) — `zbarimg` / `pyzbar`, fast first-pass QR + 1D barcodes
- [OpenCV](../tools/CTFTTOU-424.md) — scriptable QR/barcode detection, robust to rotation/noise; preprocessing
- [libdmtx](../tools/CTFTTOU-425.md) — Data Matrix (`dmtxread`)
- [QRazyBox](../tools/CTFTTOU-426.md) — recover a **damaged / cropped / masked** QR (grid editor, Reed-Solomon, format brute-force)
- [jabcode decoder](../tools/CTFTTOU-260.md) — JAB colour codes (see `CTFTTE-FOR-027`)

> Symbology-specific decoders live on the child techniques: QR [`CTFTTE-FOR-011`](CTFTTE-FOR-011.md),
> rMQR [`CTFTTE-FOR-012`](CTFTTE-FOR-012.md), JAB [`CTFTTE-FOR-027`](CTFTTE-FOR-027.md).

## References

## Tactics

[CTFT correlation matrix](../CORRELATION.md)

| FOM related tactics  |
| --------------------------------------- |
| `FOMTA007` (FOM) -> [CTFT-TA-FOR](../tactics/CTFT-TA-FOR.md) - Use special encoding system to hide data   |

## Fom Related Techniques (St)

| FOM Sub-techniques ID and description  |
| --------------------------------------- |
| `FOMTE010` (FOM) -> [CTFTTE-FOR-013](CTFTTE-FOR-013.md) - Conceal information with diagrams encoding |

## Fom Related Sub-Techniques (St)

| FOM Sub-techniques ID and description  |
| --------------------------------------- |
| `FOMTE007.001` (FOM) -> [CTFTTE-FOR-011](CTFTTE-FOR-011.md) - Hide data with QR codes   |
| `FOMTE010.001` (FOM) -> [CTFTTE-FOR-014](CTFTTE-FOR-014.md) - Conceal information with Mengenlehreuhr diagrams encoding |

## Fom Counter-Techniques (Ct)

| FOM Sub-techniques ID  and description  |
| --------------------------------------- |
| xxxx   |

**Sources**

- (1) [Jason (jxb5151). (2021, January 28). findapihash.py. Retrieved August 22, 2022.](https://github.com/MITRECND/malchive/blob/main/malchive/utilities/findapihash.py)

**Writeups**

- (1) [QRRRRRRRR — NahamCon CTF](https://medium.com/@inferiorak/qrrrrrrrr-nahamcon-ctf-2024-writeup-by-inferiorak-063406df187e)
- (2) Local write-up — QR/rMQR grid recovery (alignment-pattern maths, `galois.py`, `rmqrdecode*.py`, QRazyBox): `C:\DATA\GIT\writeups\2024\NAHAMCONF\qrrrrrr`
