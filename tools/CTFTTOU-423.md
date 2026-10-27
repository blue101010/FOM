# CTFTTOU-423 — zbar (zbarimg / pyzbar)

> **Tool ID:** `CTFTTOU-423`  
> **Related techniques/counters:** CTFTTE-FOR-010, CTFTCTE-FOR-010, CTFTTE-FOR-011, CTFTCTE-FOR-011

## Description

Fast C barcode/QR reader. The `zbarimg` CLI decodes QR, Code 128/39/93, EAN-13/8, UPC, Interleaved
2-of-5, Codabar and PDF417 directly from an image; `pyzbar` is the Python binding. Usually the first
decoder to try on a CTF QR/barcode image — quick, scriptable and installed on Kali.

## URL

- <https://github.com/mchehab/zbar>

## Installation

```bash
sudo apt install zbar-tools        # provides zbarimg / zbarcam
pip install pyzbar                 # Python binding (needs libzbar0)
```

## Usage

```bash
zbarimg --raw qr.png                               # print the decoded payload only
zbarimg -q --raw -Sdisable -Sqrcode.enable in.png  # restrict to QR symbology
python3 -c "from pyzbar.pyzbar import decode; from PIL import Image; \
print([d.data for d in decode(Image.open('qr.png'))])"
```

## Related Techniques

CTFTTE-FOR-010, CTFTCTE-FOR-010, CTFTTE-FOR-011, CTFTCTE-FOR-011

## References

- [zbar (mchehab fork)](https://github.com/mchehab/zbar)
- [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar)
