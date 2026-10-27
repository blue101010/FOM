# CTFTTOU-426 — QRazyBox

> **Tool ID:** `CTFTTOU-426`  
> **Related techniques/counters:** CTFTTE-FOR-010, CTFTCTE-FOR-010, CTFTTE-FOR-011, CTFTCTE-FOR-011, CTFTTE-FOR-012, CTFTCTE-FOR-012

## Description

Browser-based QR code **analysis and recovery** toolkit (by merricx). The go-to CTF tool when a QR is
cropped, masked, partially destroyed or otherwise undecodable by off-the-shelf readers: draw/erase the
module grid by hand, read and brute-force the **format & version info**, apply/remove data masks, and
run the **Reed-Solomon decoder** to recover the payload from an incomplete symbol. Runs entirely
client-side (usable offline from a local checkout).

## URL

- <https://merricx.github.io/qrazybox/>
- <https://github.com/merricx/qrazybox>

## Usage

```text
# Load the image (or draw modules), then use the Tools menu:
#   Extract QR Information   — version, format, mask, ECC level
#   Data Recovery            — fill unknown modules, try masks
#   Reed-Solomon Decoder     — recover data/ECC codewords from a damaged grid
#   Brute-force Format Info  — when the format bits are gone
# Offline: open the local index.html from a qrazybox checkout in a browser.
```

## Related Techniques

CTFTTE-FOR-010, CTFTCTE-FOR-010, CTFTTE-FOR-011, CTFTCTE-FOR-011, CTFTTE-FOR-012, CTFTCTE-FOR-012

## References

- [QRazyBox](https://merricx.github.io/qrazybox/)
- [QRazyBox source](https://github.com/merricx/qrazybox)
- [QRRRRRRRR — NahamCon CTF write-up](https://medium.com/@inferiorak/qrrrrrrrr-nahamcon-ctf-2024-writeup-by-inferiorak-063406df187e)
