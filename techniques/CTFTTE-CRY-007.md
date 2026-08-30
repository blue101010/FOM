# CTFTTE-CRY-007 — Deliberately predictable stateful pseudo-random generator

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-007`](../countertechniques/CTFTCTE-CRY-007.md) — Assess and predict recoverable PRNG state

---

## How the challenge author hides

The challenge derives a token, ordering, or key material from a deliberately
predictable stateful pseudo-random generator and exposes enough declared output
to make the generator family testable.

## ATT\&CK Complementarity

This is a challenge-construction weakness in randomness, not a claim about an
ATT\&CK procedure.

## Tools

- SageMath
- Z3
- Python reference implementations

## References

- https://csrc.nist.gov/pubs/sp/800/90/a/r1/final
- https://docs.python.org/3/library/random.html