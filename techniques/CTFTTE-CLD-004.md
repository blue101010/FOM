# CTFTTE-CLD-004 — Secrets in function config / layers

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Paired counter-technique:** [`CTFTCTE-CLD-004`](../countertechniques/CTFTCTE-CLD-004.md) — Dump serverless configuration and layers

---

## How the challenge author hides

Secrets/flags live in environment variables, layers, or build artifacts of a function.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Secrets in serverless configuration. |

## Tools

- awscli
- cloud SDKs

## References

- Add challenge write-up link