# CTFTTOU-411 — cloud_identity_report.py

> **Tool ID:** `CTFTTOU-411`
> **Related techniques/counters:** CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003

## Description

Workspace-authored read-only cloud/cluster identity report (Python, stdlib). Resolves 'who am I and what reads am I allowed' across the footholds you hold (kube, AWS, Azure, GCP) using only identity/whoami and permission-listing calls; it never assumes a role, mints a token or changes anything. --from-file replays a captured bundle for offline use.

## URL

Local (workspace): [ctf-skills-main/ctf-cloud-kubernetes/scripts/cloud_identity_report.py](../../ctf-skills-main/ctf-cloud-kubernetes/scripts/cloud_identity_report.py)

## Usage

```bash
python cloud_identity_report.py --kube --aws --azure --gcp -o identity.json
```

## Skills

- [ctf-cloud-kubernetes](../skills/CTFTSKL-006.md)

## Related Techniques

CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003
