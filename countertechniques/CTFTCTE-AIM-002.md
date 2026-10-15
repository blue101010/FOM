# CTFTCTE-AIM-002 — Extract the flag via crafted prompts

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-002`](../techniques/CTFTTE-AIM-002.md) — Prompt-injection-gated flag

---

## Offensive Recovery (CTF practitioner / solver)

Craft inputs that bypass the guardrails: recover the system prompt first, then
use role shifts, encoding tricks and indirect context (retrieved documents) to
make the model reveal the protected content. Probe the raw API directly, and
iterate payloads against a local model before replaying them on the target.

## Forensic / Blue-Team Perspective (DFIR analyst)

Logged prompts/responses document the injection that defeated the controls.

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