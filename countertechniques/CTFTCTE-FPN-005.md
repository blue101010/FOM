# CTFTCTE-FPN-005 — Pivot from on-prem to cloud IAM to retrieve the secret

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-005`](../techniques/CTFTTE-FPN-005.md) — Cloud-integrated fullpwn

---

## Offensive Recovery (CTF practitioner / solver)

After gaining on-premises access, query the cloud instance metadata endpoint (e.g. `169.254.169.254`) for IAM role credentials, enumerate the role's permissions with `aws iam`, and retrieve the flag from the authorised cloud resource (S3, Secrets Manager, Parameter Store).

## Forensic / Blue-Team Perspective (DFIR analyst)

Metadata-endpoint credential theft is a documented cloud attack pattern; AWS IMDSv2 token requirements mitigate it. DFIR analysts correlate CloudTrail API calls (ListBuckets, GetSecretValue) with the on-prem compromise timeline to reconstruct the full attack.

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
