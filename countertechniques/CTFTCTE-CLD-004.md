# CTFTCTE-CLD-004 — Dump serverless configuration and layers

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-004`](../techniques/CTFTTE-CLD-004.md) — Secrets in function config / layers

---

## Offensive Recovery (CTF practitioner / solver)

Read the function configuration, environment and layers to extract embedded secrets.

## Forensic / Blue-Team Perspective (DFIR analyst)

Configuration extraction documents secrets shipped in the deployment package.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Secrets in serverless configuration. |

## Tools

- awscli
- cloud SDKs

## References

- Add challenge write-up link