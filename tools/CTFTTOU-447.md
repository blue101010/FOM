# CTFTTOU-447 — prompt_fuzzer.py

> **Tool ID:** `CTFTTOU-447`  
> **Related techniques/counters:** CTFTTE-AIM-008, CTFTCTE-AIM-008

## Description

Workspace-authored payload fuzzer for LLM output-sanitizer challenges (Python, stdlib
only — no venv, no pip). It fires a payload library at a chat/submit endpoint (POST,
JSON body with a `{{PAYLOAD}}` template) and scans **every** response for
flag-format strings (`[A-Z][A-Z0-9_]{1,15}\{{4,}}`-style regex, configurable) and
sanitizer-leak markers (`removed`, `forensic_ascii`, `debug_pre`, `examples`,
`suppression_ledger`, …). Each attempt is appended to a JSONL transcript
(name, payload, status, flags, leak markers, response excerpt) so multi-turn
escalation has a paper trail.

Payload files use blocks separated by `###` lines with an optional `# name:` header —
see the ready-made ladder in
[ctf-skills-main/ctf-ai-llm-sanitizer-bypass/payloads.md](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/payloads.md).

`--selftest` spins up a mock policy-filtered endpoint (sanitizes `final`, leaks
flag-format examples when asked for `examples`) and asserts the planted flag is
recovered through the examples payload while a direct ask stays clean.

## URL

Local (workspace): [ctf-skills-main/ctf-ai-llm-sanitizer-bypass/scripts/prompt_fuzzer.py](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/scripts/prompt_fuzzer.py)

## Usage

```bash
python3 prompt_fuzzer.py --endpoint http://target:8080/api/chat \
    --payloads ../payloads.md --out transcript.jsonl
python3 prompt_fuzzer.py --endpoint URL --payloads P.txt \
    --body-template '{"msg": {{PAYLOAD}}}' --header 'Authorization: Bearer X'
python3 prompt_fuzzer.py --selftest
```

## Skills

- [ctf-ai-llm-sanitizer-bypass](../skills/CTFTSKL-018.md) — fine-grained FOM pair AIM-008
- [ctf-ai-ml](../skills/CTFTSKL-017.md) — domain skill

## Related Techniques

CTFTTE-AIM-008, CTFTCTE-AIM-008
