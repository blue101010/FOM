# CTFTSKL-006 — ctf-cloud-kubernetes

> **Skill ID:** `CTFTSKL-006`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003, CTFTTE-CLD-005, CTFTCTE-CLD-005, CTFTTE-CLD-006, CTFTCTE-CLD-006, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-FPN-004, CTFTCTE-FPN-004, CTFTTE-FPN-005, CTFTCTE-FPN-005

## Description

Decision workflow for authorized cloud-native CTF challenges — Kubernetes clusters and
AWS/Azure/GCP identity. Given a kubeconfig, a service-account token, in-cluster access, a
container image, or cloud credentials, enumerate what the identity can actually do (read-only),
model it as principal → permission → resource, and pick the one misconfiguration that reaches a
secret or flag: read secrets, schedule a pod that mounts a target, escape a privileged pod,
abuse an over-broad IAM role or workload identity, or extract a secret from an image layer. It
expands the single RBAC/hostPath note in `ctf-misc` into a full enumeration-to-pivot workflow.

## Skill file

- [ctf-skills-main/ctf-cloud-kubernetes/SKILL.md](../../ctf-skills-main/ctf-cloud-kubernetes/SKILL.md) — canonical

## When to load

```yaml
artifact_type: cloud-foothold           # kubeconfig / SA token / cloud creds / image ref
runtime: kubernetes | aws | azure | gcp
evidence:
  - kubectl works, or a pod you can exec, or a raw SA-token JWT
  - over-permissive RBAC grant (get secrets, create pods, escalate/bind)
  - IMDS/metadata reachable, or workload identity (IRSA / AAD WI / GKE WI)
  - a container image/registry to triage for layer secrets
```

## FOM pairs

- [CTFTTE-CLD-002](../techniques/CTFTTE-CLD-002.md) / [CTFTCTE-CLD-002](../countertechniques/CTFTCTE-CLD-002.md) — over-permissive IAM role
- [CTFTTE-CLD-003](../techniques/CTFTTE-CLD-003.md) / [CTFTCTE-CLD-003](../countertechniques/CTFTCTE-CLD-003.md) — instance metadata (IMDS) exposure
- [CTFTTE-CLD-005](../techniques/CTFTTE-CLD-005.md) / [CTFTCTE-CLD-005](../countertechniques/CTFTCTE-CLD-005.md) — container image / registry leak
- [CTFTTE-CLD-006](../techniques/CTFTTE-CLD-006.md) / [CTFTCTE-CLD-006](../countertechniques/CTFTCTE-CLD-006.md) — cross-account role chaining
- [CTFTTE-CLD-008](../techniques/CTFTTE-CLD-008.md) / [CTFTCTE-CLD-008](../countertechniques/CTFTCTE-CLD-008.md) — Azure management-plane misconfiguration
- [CTFTTE-FPN-004](../techniques/CTFTTE-FPN-004.md) / [CTFTCTE-FPN-004](../countertechniques/CTFTCTE-FPN-004.md) — container/service misconfiguration chain
- [CTFTTE-FPN-005](../techniques/CTFTTE-FPN-005.md) / [CTFTCTE-FPN-005](../countertechniques/CTFTCTE-FPN-005.md) — cloud-integrated fullpwn

## Tools

- [k8s_inventory.sh](../tools/CTFTTOU-408.md)
- [rbac_graph.py](../tools/CTFTTOU-409.md)
- [image_triage.sh](../tools/CTFTTOU-410.md)
- [cloud_identity_report.py](../tools/CTFTTOU-411.md)
- kubectl, Helm, jq/yq, rakkess, kubectl-who-can, Trivy, Syft, Grype, Kubescape, skopeo, aws/az/gcloud, ScoutSuite/Prowler (third-party; see references/)

## Related skills

- [ctf-ad-attack-paths](CTFTSKL-004.md) — when the path runs into on-prem AD / hybrid identity

## Notes

Added 2026-10-25 as a forward-looking gap-fill for cloud-native CTF content (Hackfest 2026
preview lists Kubernetes, Azure pentest, cloud/levelup and SDLC/DevOps challenges). FOM already
modelled the CLD and FPN-004/005 pairs as taxonomy-only; this skill is the executable workflow.
No attested event record yet.

## Related Techniques

CTFTTE-CLD-002, CTFTCTE-CLD-002, CTFTTE-CLD-003, CTFTCTE-CLD-003, CTFTTE-CLD-005, CTFTCTE-CLD-005, CTFTTE-CLD-006, CTFTCTE-CLD-006, CTFTTE-CLD-008, CTFTCTE-CLD-008, CTFTTE-FPN-004, CTFTCTE-FPN-004, CTFTTE-FPN-005, CTFTCTE-FPN-005
