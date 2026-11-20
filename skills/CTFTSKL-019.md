# CTFTSKL-019 — ctf-cloud-aws

> **Skill ID:** `CTFTSKL-019`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003, CTFTTE-CLD-004, CTFTCTE-CLD-004, CTFTTE-CLD-005, CTFTCTE-CLD-005, CTFTTE-CLD-006, CTFTCTE-CLD-006, CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011

## Description

Decision workflow for authorized AWS challenges. Given an AWS artefact — an access-key pair or
session token, a shared-credentials profile, a role ARN or trust policy, an instance-metadata
endpoint, a Lambda configuration or layer, a CodeBuild/CodePipeline definition, a Cognito app client,
an S3 URI or presigned URL, a DynamoDB table, a KMS key or a Secrets Manager/SSM path — establish the
acting identity, enumerate the authorisation layer rather than the inventory, and name the single
grant that reaches the flag.

It complements `ctf-cloud-azure` (directory/management-plane work on the Microsoft side) and
`ctf-cloud-kubernetes` (cluster-first challenges) by covering the AWS identity model: the credential
shapes, the policy-evaluation order that decides every read, the escalation candidates with their
prerequisites, and the service-by-service data planes where the value actually sits.

## Skill file

- [ctf-skills-main/ctf-cloud-aws/SKILL.md](../../ctf-skills-main/ctf-cloud-aws/SKILL.md) — canonical
- References: [iam-and-credentials.md](../../ctf-skills-main/ctf-cloud-aws/references/iam-and-credentials.md),
  [compute-and-metadata.md](../../ctf-skills-main/ctf-cloud-aws/references/compute-and-metadata.md),
  [storage-and-data.md](../../ctf-skills-main/ctf-cloud-aws/references/storage-and-data.md),
  [serverless-and-ci.md](../../ctf-skills-main/ctf-cloud-aws/references/serverless-and-ci.md)
- Script: [aws_ctf_inventory.py](../../ctf-skills-main/ctf-cloud-aws/scripts/aws_ctf_inventory.py)
  (`artifacts` / `creds` / `token` / `policy` / `privesc`, stdlib only, no network,
  `selftest` = 34 offline checks)
- Mirrors: [.github/skills/ctf-cloud-aws/SKILL.md](../../.github/skills/ctf-cloud-aws/SKILL.md),
  [.codex/skills/ctf-cloud-aws/SKILL.md](../../.codex/skills/ctf-cloud-aws/SKILL.md)

## When to load

```yaml
artifact_type: credential | role-arn | metadata-endpoint | function-config | pipeline-definition | storage-uri
runtime: aws
evidence:
  - an access key id (AKIA/ASIA…), a 40-char secret, or a session token, in a file, env dump or URL
  - a shared-credentials profile, a credential_process/sso entry, or a role ARN with a trust policy
  - an instance/container metadata endpoint (169.254.169.254, 169.254.170.2,
    AWS_CONTAINER_CREDENTIALS_*, AWS_WEB_IDENTITY_TOKEN_FILE)
  - Lambda environment, layer ARN, function URL or resource policy; CodeBuild/CodePipeline project
  - an S3 URI, presigned URL, bucket policy, DynamoDB table, KMS key id, Secrets Manager/SSM path
  - a Cognito user-pool or identity-pool id, or a story about "too many permissions"
fom_pair: CTFTTE-CLD-002 <-> CTFTCTE-CLD-002
```

## FOM pairs

- [CLD-001](../techniques/CTFTTE-CLD-001.md) / [CTE-CLD-001](../countertechniques/CTFTCTE-CLD-001.md) — misconfigured object-storage exposure
- [CLD-002](../techniques/CTFTTE-CLD-002.md) / [CTE-CLD-002](../countertechniques/CTFTCTE-CLD-002.md) — over-permissive IAM role
- [CLD-003](../techniques/CTFTTE-CLD-003.md) / [CTE-CLD-003](../countertechniques/CTFTCTE-CLD-003.md) — instance metadata service exposure
- [CLD-004](../techniques/CTFTTE-CLD-004.md) / [CTE-CLD-004](../countertechniques/CTFTCTE-CLD-004.md) — secrets in function config / layers
- [CLD-005](../techniques/CTFTTE-CLD-005.md) / [CTE-CLD-005](../countertechniques/CTFTCTE-CLD-005.md) — container image / registry leak
- [CLD-006](../techniques/CTFTTE-CLD-006.md) / [CTE-CLD-006](../countertechniques/CTFTCTE-CLD-006.md) — cross-account role chaining / trust abuse
- [CLD-007](../techniques/CTFTTE-CLD-007.md) / [CTE-CLD-007](../countertechniques/CTFTCTE-CLD-007.md) — cloud NoSQL-store misconfiguration
- [CLD-010](../techniques/CTFTTE-CLD-010.md) / [CTE-CLD-010](../countertechniques/CTFTCTE-CLD-010.md) — secret store reachable by a workload identity
- [CLD-011](../techniques/CTFTTE-CLD-011.md) / [CTE-CLD-011](../countertechniques/CTFTCTE-CLD-011.md) — bearer credential embedded in a storage URL

## Tools

- [CTFTTOU-217](../tools/CTFTTOU-217.md) — AWS CLI v2 (`aws sts`, `aws iam`, service data planes)
- [CTFTTOU-219](../tools/CTFTTOU-219.md) — boto3
- [CTFTTOU-220](../tools/CTFTTOU-220.md) — Pacu
- [CTFTTOU-221](../tools/CTFTTOU-221.md) — cloudfox
- [CTFTTOU-222](../tools/CTFTTOU-222.md) — enumerate-iam
- [CTFTTOU-226](../tools/CTFTTOU-226.md) — ScoutSuite (and Prowler)
- [CTFTTOU-415](../tools/CTFTTOU-415.md) — s3_public_probe.py (anonymous side of CLD-001)

## Related skills

- [ctf-cloud-public-bucket](CTFTSKL-008.md) — the exposure needs no credential at all
- [ctf-cloud-kubernetes](CTFTSKL-006.md) — the foothold becomes a cluster or crosses a workload identity
- [ctf-cloud-azure](CTFTSKL-009.md) — the same decision shape on the Microsoft side
- [ctf-gitlab-cicd](../../ctf-skills-main/ctf-gitlab-cicd/SKILL.md) — when the credential lives in CI, not in AWS

## Notes

Added 2026-11-19 to close the AWS gap in the cloud domain: CLD-001..007 and CLD-010/011 all describe
AWS-shaped behaviour, but no skill covered the identity model that decides every one of them (which
document authorises the read, and which grant is the next hop). The catalogue in the reference file
lists escalation candidates with the prerequisite that turns a matching action into a working path,
so a policy hit is never reported as an exploit.

All pairs used here remain `taxonomy_only`: no attested CTF event record yet. AWS CLI v2 is the
self-contained bundle on Kali; Python tooling goes in `~/.venvs/ctfcloud` (PEP 668 — never a bare
`pip install`). The bundled script is read-only by construction: it never opens a socket and reports
candidates, not results.

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001, CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003,
CTFTTE-CLD-004, CTFTCTE-CLD-004, CTFTTE-CLD-005, CTFTCTE-CLD-005, CTFTTE-CLD-006, CTFTCTE-CLD-006,
CTFTTE-CLD-007, CTFTCTE-CLD-007, CTFTTE-CLD-010, CTFTCTE-CLD-010, CTFTTE-CLD-011, CTFTCTE-CLD-011
