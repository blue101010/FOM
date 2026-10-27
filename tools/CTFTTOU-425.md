# CTFTTOU-425 — libdmtx (dmtxread / pylibdmtx)

> **Tool ID:** `CTFTTOU-425`  
> **Related techniques/counters:** CTFTTE-FOR-010, CTFTCTE-FOR-010

## Description

Data Matrix 2D barcode reader/writer. `dmtxread` decodes Data Matrix symbols from an image where
zbar or ZXing may fail, and `dmtxwrite` generates them; `pylibdmtx` is the Python binding. The
specialist tool to reach for once the symbology is identified as **Data Matrix** (square or
rectangular finder "L", dotted timing edges).

## URL

- <https://github.com/dmtx/libdmtx>

## Installation

```bash
sudo apt install libdmtx-utils     # dmtxread / dmtxwrite
pip install pylibdmtx              # Python binding (needs libdmtx0)
```

## Usage

```bash
dmtxread -N1 datamatrix.png                         # decode first symbol
python3 -c "from pylibdmtx.pylibdmtx import decode; from PIL import Image; \
print(decode(Image.open('dm.png')))"
```

## Related Techniques

CTFTTE-FOR-010, CTFTCTE-FOR-010

## References

- [libdmtx](https://github.com/dmtx/libdmtx)
- [pylibdmtx](https://github.com/NaturalHistoryMuseum/pylibdmtx)
