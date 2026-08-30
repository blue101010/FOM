# CTFTTE-AIM-001 — Secret embedded in model weights

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-001`](../countertechniques/CTFTCTE-AIM-001.md) — Extract tensors and inspect weights

---

## How the challenge author hides

The flag is encoded in a layer's weights/embedding rather than any text field.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Secrets embedded in model artifacts. |

## Tools

- numpy
- torch/onnx
- netron

## References

- <https://github.com/lutzroeder/netron>
- Add challenge write-up link