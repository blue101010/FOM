# CTFTCTE-AIM-001 — Extract tensors and inspect weights

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-001`](../techniques/CTFTTE-AIM-001.md) — Secret embedded in model weights

---

## Offensive Recovery (CTF practitioner / solver)

Load the model, dump tensors, and decode the embedded bytes/strings.

## Forensic / Blue-Team Perspective (DFIR analyst)

Tensor inspection documents non-functional data smuggled into the model file.

## Tools

- numpy
- torch/onnx
- netron

## References

- https://github.com/lutzroeder/netron
- Add challenge write-up link