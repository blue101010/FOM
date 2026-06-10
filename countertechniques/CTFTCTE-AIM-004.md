# CTFTCTE-AIM-004 — Safely inspect serialized model files

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-004`](../techniques/CTFTTE-AIM-004.md) — Malicious / opaque serialized model

---

## Offensive Recovery (CTF practitioner / solver)

Statically inspect the serialized opcodes without executing them to recover content.

## Forensic / Blue-Team Perspective (DFIR analyst)

Opcode-level inspection documents embedded payloads without triggering them.

## Tools

- fickling
- python pickletools

## References

- https://github.com/trailofbits/fickling
- Add challenge write-up link