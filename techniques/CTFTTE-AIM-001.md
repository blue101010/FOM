# CTFTTE-AIM-001 — Secret embedded in model weights

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-001`](../countertechniques/CTFTCTE-AIM-001.md) — Extract tensors and inspect weights

---

## How the challenge author hides

The flag is encoded in a layer's weights/embedding rather than any text field.

## ATT\&CK Complementarity

No ATT&CK equivalent.

## Tools

- numpy
- torch/onnx
- netron

## References

- https://github.com/lutzroeder/netron
- Add challenge write-up link