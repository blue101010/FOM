# CTFTTOU-409 — rbac_graph.py

> **Tool ID:** `CTFTTOU-409`
> **Related techniques/counters:** CTFTTE-FPN-004, CTFTCTE-FPN-004, CTFTTE-CLD-002, CTFTCTE-CLD-002

## Description

Workspace-authored read-only Kubernetes RBAC analyzer (Python, stdlib). Turns the JSON of kubectl get clusterroles,roles,clusterrolebindings,rolebindings into subject -> verbs/resources paths, flagging the grants that matter for a pivot: secret reads, pod / pod-exec / workload creation and the escalation verbs (* , escalate, bind, impersonate). Parses collected JSON; never contacts the cluster.

## URL

Local (workspace): [ctf-skills-main/ctf-cloud-kubernetes/scripts/rbac_graph.py](../../ctf-skills-main/ctf-cloud-kubernetes/scripts/rbac_graph.py)

## Usage

```bash
kubectl get clusterroles,roles,clusterrolebindings,rolebindings -A -o json > rbac.json; python rbac_graph.py rbac.json --dangerous-only
```

## Skills

- [ctf-cloud-kubernetes](../skills/CTFTSKL-006.md)

## Related Techniques

CTFTTE-FPN-004, CTFTCTE-FPN-004, CTFTTE-CLD-002, CTFTCTE-CLD-002
