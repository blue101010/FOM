# CTFTTE-AIM-002 — Prompt-injection-gated flag

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-002`](../countertechniques/CTFTCTE-AIM-002.md) — Extract the flag via crafted prompts

---

## How the challenge author hides

An LLM-backed app holds the flag in its instructions/context behind guardrails.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Prompt-injection is emerging LLM-security craft ATT&CK does not model. |

## Tools

- the target chat interface
- prompt tooling

## References

- Add challenge write-up link