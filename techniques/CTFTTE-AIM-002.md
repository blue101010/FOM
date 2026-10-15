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

- [curl](../tools/CTFTTOU-038.md) / [requests](../tools/CTFTTOU-067.md)
- [garak](../tools/CTFTTOU-062.md)
- [promptfoo](../tools/CTFTTOU-063.md)
- [PyRIT](../tools/CTFTTOU-064.md)
- [Pandoras Box](../tools/CTFTTOU-065.md)
- [promptmap](../tools/CTFTTOU-066.md)
- [ollama](../tools/CTFTTOU-047.md)
- [Playwright](../tools/CTFTTOU-008.md)

## References

- <https://genai.owasp.org/llm-top-10/>
- <https://simonwillison.net/series/prompt-injection/>
- <https://github.com/NVIDIA/garak>