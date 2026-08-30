# CTFTCTE-AIM-002 — Extract the flag via crafted prompts

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-002`](../techniques/CTFTTE-AIM-002.md) — Prompt-injection-gated flag

---

## Offensive Recovery (CTF practitioner / solver)

Craft inputs that bypass the guardrails to make the model reveal the protected content.

## Forensic / Blue-Team Perspective (DFIR analyst)

Logged prompts/responses document the injection that defeated the controls.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Prompt-injection is emerging LLM-security craft ATT&CK does not model. |

## Tools

- the target chat interface
- prompt tooling

## References

- Add challenge write-up link