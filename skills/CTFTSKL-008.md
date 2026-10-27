# CTFTSKL-008 — ctf-cloud-public-bucket

> **Skill ID:** `CTFTSKL-008`  
> **Kind:** Fine-grained skill (one FOM pair)  
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001

## Description

Solves challenges where object storage is assumed private but is world-readable: an S3/GCS/Azure
bucket whose name or DNS name appears in the prompt, an `s3://` URI, a flag object such as
`flag.txt`, or a "I think I made the bucket private" backstory. Covers region discovery via
`x-amz-bucket-region` (so a `301` is not read as a denial), anonymous `ListObjectsV2`, the legacy
`?versions` fallback that exposes deleted objects, direct object GET when listing is denied, and
the pivot from an exposed bucket to a git repository whose history leaks credentials.

The tell is the negative signature: no credentials are involved at all — if a command needs
`aws configure` first, the challenge belongs to a different pair (a grant scoped to authenticated
callers, CLD-002/003).

## Skill file

- [ctf-skills-main/ctf-cloud-public-bucket/SKILL.md](../../ctf-skills-main/ctf-cloud-public-bucket/SKILL.md) — canonical

## When to load

```yaml
artifact_type: url | bucket-name | cloud-domain
evidence:
  - prompt says the bucket is "private" or asks to "check the permissions"
  - host matches *.s3.amazonaws.com / *.s3.<region>.amazonaws.com / storage.googleapis.com
  - s3:// URI, bucket name in a hint, or a bucket name in a leaked script or JS comment
  - flag object named flag.txt, secret*.html, .env, backup.zip
  - listing returns 403 but a direct object GET returns 200
```

## FOM pairs

- [CTFTTE-CLD-001](../techniques/CTFTTE-CLD-001.md) / [CTFTCTE-CLD-001](../countertechniques/CTFTCTE-CLD-001.md) — misconfigured object-storage exposure / enumerate and list public buckets

## Tools

- [s3_public_probe.py](../tools/CTFTTOU-415.md) — anonymous probe, `?versions` fallback, permutations, download/grep
- `aws` CLI v2 (`/usr/local/bin/aws`) — `s3 ls` / `s3 sync` with `--no-sign-request`
- `cloud_enum` (initstring) — keyword enumeration across AWS/GCP/Azure
- `curl` — raw `ListBucketResult` XML, and the one-liner quoted in write-ups

## Related skills

- [ctf-cloud-kubernetes](../../ctf-skills-main/ctf-cloud-kubernetes/SKILL.md) — once the exposed objects yield credentials or a kubeconfig
- [ctf-web-enumeration](../../ctf-skills-main/ctf-web-enumeration/SKILL.md) — when the bucket name has to be discovered from the web surface first

## Notes

Validated offline by `scripts/s3_probe_selftest.py` (17 assertions across four mock buckets). The
pair is attested by two independent events recorded in `v3/evidence.curated.json`; this skill keeps
to the anonymous-exposure behaviour, and the credential pivot stays with CLD-002.

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001
