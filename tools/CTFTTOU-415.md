# CTFTTOU-415 — s3_public_probe.py

> **Tool ID:** `CTFTTOU-415`
> **Related techniques/counters:** CTFTTE-CLD-001, CTFTCTE-CLD-001

## Description

Workspace-authored anonymous object-storage probe (Python, stdlib only). Asks one question —
*does this bucket serve data to a caller with no credentials?* — and never signs a request,
never reads `~/.aws/credentials`: it reproduces `aws s3 ls --no-sign-request` from first
principles, which keeps it usable when boto3/awscli venvs are unavailable.

Per bucket:

- **region discovery** — `HEAD https://<bucket>.s3.amazonaws.com/` answers with
  `x-amz-bucket-region` even behind a `403`, so a `301` is not mistaken for a denial;
- **anonymous listing** — `ListObjectsV2` (`?list-type=2&max-keys=1000`) with
  `ContinuationToken` paging;
- **fallbacks** — legacy `?versions` (also reveals *deleted* objects and their `VersionId`)
  and direct `HEAD`/`GET` on guessed keys (`flag.txt`, `secret*.html`, `.env`, …), because
  read-only exposure often coexists with a denied listing;
- **name permutations** — expands a keyword into `-private`, `-public`, `-backup`, year-suffixed
  and prefixed variants (49 names for a single keyword);
- **artefact handling** — optional `--download` of every readable object and `--grep` over the
  bodies, so an exposed `.git` tree or a `secret*.html` page is captured for the next stage.

Related harness: [`s3_probe_selftest.py`](../../ctf-skills-main/ctf-cloud-public-bucket/scripts/s3_probe_selftest.py)
starts a mock S3 endpoint and asserts the four response signatures (public, `403`+`?versions`,
fully private, `NoSuchBucket`) without any network access.

## URL

Local (workspace): [ctf-skills-main/ctf-cloud-public-bucket/scripts/s3_public_probe.py](../../ctf-skills-main/ctf-cloud-public-bucket/scripts/s3_public_probe.py)

## Usage

```bash
# one bucket, scan the bodies for the flag format
python3 s3_public_probe.py --bucket mytarget-bucket --grep 'CTF\{'

# keyword permutations + direct object guesses + download
python3 s3_public_probe.py --permutations ctfbucket --keys flag.txt --download out/

# path-style endpoint (LocalStack/MinIO, or the bundled self-test)
python3 s3_public_probe.py --bucket public-demo --endpoint http://127.0.0.1:9000 --json

# regression (mock server, no network)
python3 s3_probe_selftest.py --verbose
```

## Notes

- Equivalent one-liners for a write-up: `aws s3 ls s3://<bucket>/ --no-sign-request --region <r>`
  and `aws s3 sync s3://<bucket>/ . --no-sign-request`.
- A `403` on both listing and guessed keys means genuinely private, or a grant scoped to any
  authenticated principal — that case needs an account and is out of scope for CLD-001.
- Dotted bucket names break virtual-host TLS; use `--path-style` for those.
- Validated offline by the bundled regression and, live, against the two training writeups
  listed in the paired counter-technique's References. The tool holds no challenge-specific value.

## Skills

- [ctf-cloud-public-bucket](../skills/CTFTSKL-008.md) — public bucket exposure (CLD-001)

## Related Techniques

CTFTTE-CLD-001, CTFTCTE-CLD-001
