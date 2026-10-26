# CTFTTOU-410 — image_triage.sh

> **Tool ID:** `CTFTTOU-410`
> **Related techniques/counters:** CTFTTE-CLD-005, CTFTCTE-CLD-005

## Description

Workspace-authored read-only container image triage (bash; crane/skopeo/trivy/syft when present). Inspects an image for secrets left in layers (a file removed in a later layer still lives in its own), leaked build ARG/ENV in the history, and the SBOM/vulns that may be the intended foothold. It only pulls/reads the image; it builds and runs nothing.

## URL

Local (workspace): [ctf-skills-main/ctf-cloud-kubernetes/scripts/image_triage.sh](../../ctf-skills-main/ctf-cloud-kubernetes/scripts/image_triage.sh)

## Usage

```bash
bash image_triage.sh registry.example.com/app:latest -o triage/
```

## Skills

- [ctf-cloud-kubernetes](../skills/CTFTSKL-006.md)

## Related Techniques

CTFTTE-CLD-005, CTFTCTE-CLD-005
