# CTFTCTE-COD-002 — Implement an efficient algorithm to satisfy the server

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-COD`](../tactics/CTFT-TA-COD.md) — Coding / Programming Puzzle  
> **Counters technique:** [`CTFTTE-COD-002`](../techniques/CTFTTE-COD-002.md) — Algorithm optimisation challenge

---

## Offensive Recovery (CTF practitioner / solver)

Identify the problem class (shortest-path, dynamic programming, number theory), implement the correct algorithm in PyPy or C, and submit the answer within the server's time budget.

## Forensic / Blue-Team Perspective (DFIR analyst)

Timing-bounded server challenges verify that the client has sufficient computational capability; the pattern also appears in legitimate proof-of-work anti-spam schemes and rate-limiting systems.

## Tools

- python / pypy
- numpy / scipy
- z3-solver (for combinatorial instances)

## References

- Add challenge write-up link
