# CTFTCTE-CLD-002 — Enumerate and assume reachable roles

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-002`](../techniques/CTFTTE-CLD-002.md) — Over-permissive IAM role

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate effective permissions and assume the role to reach the protected resource.

## Forensic / Blue-Team Perspective (DFIR analyst)

CloudTrail-style logs show the privilege enumeration and assume-role calls.

## Tools

- enumerate-iam
- awscli
- pacu

## References

- Add challenge write-up link