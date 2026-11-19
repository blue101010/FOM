# CTFTTE-AIM-008 — Output-sanitizer / policy-filter gate on an LLM service

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Paired counter-technique:** [`CTFTCTE-AIM-008`](../countertechniques/CTFTCTE-AIM-008.md) — Leak filtered content through structure, serialization, encodings and examples

---

## How the challenge author hides

An LLM-backed service is instructed (system prompt) to sanitize its own output:
normalize free text into a fixed schema, replace colloquial or alarming words with
technical enum codes, move forbidden terms into a `removed` list, and never reveal
the flag or internal constants. The secret sits in the model's context — system-prompt
constants, example strings, audit/debug labels, sometimes response headers — i.e. in
channels the policy never marks as user-facing. Direct asks collapse to the sanitized
default, but any channel the filter does not model (an extra JSON key, another
serialization, an encoding of a suppressed term, an "example" of a flag-format string)
is unsupervised. Distinct from CTFTTE-AIM-002, where the guardrail blocks revealing the
flag outright; here the gate is a structural output policy and the bypass is
structural, not semantic.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Prompt-injection is emerging LLM-security craft ATT&CK does not model. |

## Tools

- [curl](../tools/CTFTTOU-038.md) / [requests](../tools/CTFTTOU-067.md)
- [garak](../tools/CTFTTOU-062.md)
- [promptfoo](../tools/CTFTTOU-063.md)
- [PyRIT](../tools/CTFTTOU-064.md)
- [promptmap](../tools/CTFTTOU-066.md)
- [Playwright](../tools/CTFTTOU-008.md)
- [prompt_fuzzer.py](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/scripts/prompt_fuzzer.py) ([CTFTTOU-447](../tools/CTFTTOU-447.md))

## Indicators

- rigid output schema (fixed keys, uppercase enums, auto-generated IDs) that never contains the flag
- responses expose `removed` / `normalization_map` / `debug_pre_standardization`-style fields when asked
- the same input yields different internal labels across runs (probabilistic policy)
- asking for "pre-standardization" text without naming a field and format collapses to the default
- header-prefixed or example-format strings leak when the model is asked for examples/templates of secret-format strings

## References

- <https://genai.owasp.org/llm01-prompt-injection/>
- <https://simonwillison.net/series/prompt-injection/>
- <https://gandalf.lakera.ai/>
- <https://github.com/NVIDIA/garak>
