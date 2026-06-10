# CTFTTE-CLD-002 — Over-permissive IAM role

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-002`](../countertechniques/CTFTCTE-CLD-002.md) — Enumerate and assume reachable roles

---

## How the challenge author hides

A role/policy grants more than intended, letting solvers pivot to the flag resource.

## ATT\&CK Complementarity

Complements T1078.004 (Cloud Accounts) with CTF permission-mapping steps.

## Tools

- enumerate-iam
- awscli
- pacu

## References

- Add challenge write-up link