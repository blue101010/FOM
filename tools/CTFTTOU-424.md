# CTFTTOU-424 — OpenCV (QR / barcode detection)

> **Tool ID:** `CTFTTOU-424`  
> **Related techniques/counters:** CTFTTE-FOR-010, CTFTCTE-FOR-010, CTFTTE-FOR-011, CTFTCTE-FOR-011

## Description

OpenCV computer-vision library. Its `cv2.QRCodeDetector` (and `cv2.barcode.BarcodeDetector`) detect
and decode QR/barcodes directly, and are more robust to rotation, perspective distortion, blur and
multiple codes in one image than a plain CLI reader. Equally valuable to **preprocess** a damaged
symbol — grayscale, threshold/Otsu, resize, perspective-correct — before handing it to another
decoder (zbar/ZXing).

## URL

- <https://opencv.org/>

## Installation

```bash
pip install opencv-python
```

## Usage

```python
import cv2
img = cv2.imread('qr.png')
data, pts, _ = cv2.QRCodeDetector().detectAndDecode(img)   # single QR
print(data)
# multiple / curved QR:
ok, decoded, pts, _ = cv2.QRCodeDetector().detectAndDecodeMulti(img)
# preprocess a faint symbol before another decoder:
g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bw = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite('clean.png', bw)
```

## Related Techniques

CTFTTE-FOR-010, CTFTCTE-FOR-010, CTFTTE-FOR-011, CTFTCTE-FOR-011

## References

- [OpenCV](https://opencv.org/)
- [QRCodeDetector docs](https://docs.opencv.org/4.x/de/dc3/classcv_1_1QRCodeDetector.html)
