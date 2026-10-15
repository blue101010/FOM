# CTFTTE-AIM-006 — Self-hosted LLM platform misconfiguration

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-006`](../countertechniques/CTFTCTE-AIM-006.md) — Audit ollama/oobabooga deployments for exposed endpoints

---

## How the challenge author hides

A self-hosted LLM (ollama/oobabooga) is exposed or misconfigured; the flag hides in model outputs, endpoints, or host files.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Exposed LLM endpoints. |

## Tools

- [ollama](../tools/CTFTTOU-047.md) CLI
- [curl](../tools/CTFTTOU-038.md)
- [nmap](../tools/CTFTTOU-033.md)

## References

- <https://github.com/ollama/ollama>
- Add challenge write-up link
