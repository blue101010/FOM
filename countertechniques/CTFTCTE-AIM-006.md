# CTFTCTE-AIM-006 — Audit ollama/oobabooga deployments for exposed endpoints

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-006`](../techniques/CTFTTE-AIM-006.md) — Self-hosted LLM platform misconfiguration

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate the exposed endpoints/APIs, query the model, and pivot to the host if the deployment is over-permissive.

## Forensic / Blue-Team Perspective (DFIR analyst)

LLM deployment logs record queries and endpoints; exposure scanning is the same as any service audit.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Exposed LLM endpoints. |

## Tools

- ollama CLI
- curl
- nmap

## References

- <https://github.com/ollama/ollama>

