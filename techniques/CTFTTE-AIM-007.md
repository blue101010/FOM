# CTFTTE-AIM-007 — Agent / tool-calling guardrail bypass

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-007`](../countertechniques/CTFTCTE-AIM-007.md) — Bypass agent tool policies

---

## How the challenge author hides

An agent is constrained by guardrails over its tools; the flag requires coaxing it past the policy.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| — | — | No ATT&CK equivalent; emerging LLM-security craft. |

## Tools

- [python](../tools/CTFTTOU-050.md)
- [AutoGen](../tools/CTFTTOU-273.md)
- [LangChain](../tools/CTFTTOU-274.md)
- [CrewAI](../tools/CTFTTOU-275.md)
- [garak](../tools/CTFTTOU-062.md)
- [PyRIT](../tools/CTFTTOU-064.md)

## References

- <https://github.com/microsoft/autogen>
- Add challenge write-up link
