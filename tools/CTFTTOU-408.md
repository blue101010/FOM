# CTFTTOU-408 — k8s_inventory.sh

> **Tool ID:** `CTFTTOU-408`
> **Related techniques/counters:** CTFTTE-FPN-004, CTFTCTE-FPN-004, CTFTTE-CLD-002, CTFTCTE-CLD-002

## Description

Workspace-authored read-only Kubernetes inventory (bash + kubectl). Collects contexts, namespaces, your effective permissions per namespace (auth can-i --list), workloads, readable secrets/configmaps, service accounts, the images in use and the RBAC export for rbac_graph.py — using only kubectl get / auth can-i, which return exactly what your identity may see. It creates no objects.

## URL

Local (workspace): [ctf-skills-main/ctf-cloud-kubernetes/scripts/k8s_inventory.sh](../../ctf-skills-main/ctf-cloud-kubernetes/scripts/k8s_inventory.sh)

## Usage

```bash
bash k8s_inventory.sh -o k8s_inventory/
```

## Skills

- [ctf-cloud-kubernetes](../skills/CTFTSKL-006.md)

## Related Techniques

CTFTTE-FPN-004, CTFTCTE-FPN-004, CTFTTE-CLD-002, CTFTCTE-CLD-002
