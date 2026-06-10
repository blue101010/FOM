# CTFTTE-AIM-004 — Malicious / opaque serialized model

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-004`](../countertechniques/CTFTCTE-AIM-004.md) — Safely inspect serialized model files

---

## How the challenge author hides

A pickle/serialized model hides logic or data that executes/loads on deserialization.

## ATT\&CK Complementarity

Complements T1204/T1027 conceptually; CTFT adds safe-pickle-inspection procedure.

## Tools

- fickling
- python pickletools

## References

- https://github.com/trailofbits/fickling
- Add challenge write-up link