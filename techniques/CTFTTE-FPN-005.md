# CTFTTE-FPN-005 — Cloud-integrated fullpwn

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-005`](../countertechniques/CTFTCTE-FPN-005.md) — Pivot from on-prem to cloud IAM to retrieve the secret

---

## How the challenge author hides

The flag is stored in a cloud resource (S3 bucket, Secrets Manager, Lambda environment variable) that is reachable only after compromising an on-premises host and pivoting through its attached cloud credentials.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1078.004 | Cloud Accounts | Cloud IAM pivot. |
| T1552.005 | Cloud Instance Metadata API | IMDS credential theft. |

## Tools

- aws cli / azure cli / gcloud
- pacu
- cloudfox

## References

- https://github.com/RhinoSecurityLabs/pacu
- https://github.com/BishopFox/cloudfox
- Add challenge write-up link
