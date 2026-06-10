# CTFTTE-FPN-005 — Cloud-integrated fullpwn

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-005`](../countertechniques/CTFTCTE-FPN-005.md) — Pivot from on-prem to cloud IAM to retrieve the secret

---

## How the challenge author hides

The flag is stored in a cloud resource (S3 bucket, Secrets Manager, Lambda environment variable) that is reachable only after compromising an on-premises host and pivoting through its attached cloud credentials.

## ATT\&CK Complementarity

Complements T1552.005 (Cloud Instance Metadata) and T1537 (Transfer Data to Cloud Account) with CTF-specific on-prem-to-cloud pivot detail.

## Tools

- aws cli / azure cli / gcloud
- pacu
- cloudfox

## References

- https://github.com/RhinoSecurityLabs/pacu
- https://github.com/BishopFox/cloudfox
- Add challenge write-up link
