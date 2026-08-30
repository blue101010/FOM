# CTFTCTE-AIM-007 — Bypass agent tool policies

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-007`](../techniques/CTFTTE-AIM-007.md) — Agent / tool-calling guardrail bypass

---

## Offensive Recovery (CTF practitioner / solver)

Craft prompts/tool-call sequences that bypass the guardrails and retrieve the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Agent logs replay the tool-call trace; guardrail violations are auditable events.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; emerging LLM-security craft. |

## Tools

- Python
- agent CLIs

## References

- <https://github.com/microsoft/autogen>
