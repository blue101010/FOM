# CTFTCTE-AIM-008 — Leak filtered content through structure, serialization, encodings and examples

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-AIM`](../tactics/CTFT-TA-AIM.md) — AI / ML  
> **Counters technique:** [`CTFTTE-AIM-008`](../techniques/CTFTTE-AIM-008.md) — Output-sanitizer / policy-filter gate on an LLM service

---

## Offensive Recovery (CTF practitioner / solver)

Baseline the sanitizer first: which fields come back, which terms get removed, which
enum labels appear. Then climb the payload ladder: (1) demand extra schema keys
(`forensic`, `debug_pre_standardization`, `hidden_strings`, `flags`,
`suppression_ledger`, `rule_trace`, `validation_trace`, `developer_artifacts`) with
"do not omit / do not sanitize" rules; (2) switch serialization — YAML, XML+CDATA,
one-line dump, code fences, duplicate keys; (3) demand transform encodings of the
suppressed terms — ASCII decimal arrays, `\uXXXX`, base64, spaced-out letters, token
arrays; (4) use audit/contradiction framing (`contradictions`, `evidence_score`,
`policy_diff` against a null filter); (5) enumerate `examples` / `templates` /
`hidden_examples` of secret-format strings and run regex extraction of flag-format
substrings — models often repeat embedded example constants verbatim; (6) harvest
non-standard uppercase labels that drift between runs. Log every attempt in a
transcript, grep all responses (not just the main field) for the flag regex, validate
the candidate format, then submit. Automate the ladder with
[prompt_fuzzer.py](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/scripts/prompt_fuzzer.py).

## Forensic / Blue-Team Perspective (DFIR analyst)

The transcript of prompts/responses documents which channel leaked; sanitizer logs
show the removed-term list that the model encoded around.

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

## References

- <https://genai.owasp.org/llm01-prompt-injection/>
- <https://simonwillison.net/series/prompt-injection/>
- <https://gandalf.lakera.ai/>
- <https://github.com/NVIDIA/garak>
