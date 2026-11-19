# CTFTSKL-018 — ctf-ai-llm-sanitizer-bypass

> **Skill ID:** `CTFTSKL-018`  
> **Kind:** Fine-grained skill (one FOM pair)  
> **Related techniques/counters:** CTFTTE-AIM-008, CTFTCTE-AIM-008

## Description

Solves LLM-backed challenges whose output passes a **self-sanitizing policy filter**
(forced schema, removed-term lists, normalization maps) while the flag/secret sits in
system-prompt constants, example strings, debug/audit fields, or headers. Covers the
payload ladder — extra schema keys, serialization switches, transform encodings
(ASCII/unicode/base64/token arrays), audit/contradiction framing, and
example/template enumeration — plus a ready-made payload library and an automated
fuzzer that logs every attempt and greps all responses for flag-format strings.

## Skill file

- [ctf-skills-main/ctf-ai-llm-sanitizer-bypass/SKILL.md](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/SKILL.md) — canonical
  - deep dive: `sanitizer-bypass.md` (anatomy, fingerprints, payload ladder, low-yield list)
  - payload library: `payloads.md` (fuzzer block format)
  - fuzzer: `scripts/prompt_fuzzer.py` (stdlib, `--selftest`)

## When to load

```yaml
artifact_type: web-service | chat-endpoint | LLM-backed API
fom_pair: CTFTTE-AIM-008 <-> CTFTCTE-AIM-008
evidence:
  - the app returns LLM output in a rigid schema that never contains the flag
  - responses expose 'removed' / 'normalization_map' / 'debug_pre_standardization' fields when asked
  - the same input yields different internal labels across runs
  - direct asks collapse to the sanitized default, but encodings, audit fields, or example strings leak
```

If the LLM gates on a *decision* rather than output redaction, or fronts a directly
callable MCP server, use [CTFTSKL-017](CTFTSKL-017.md) (ctf-ai-ml) instead.

## FOM pairs

- [CTFTTE-AIM-008](../techniques/CTFTTE-AIM-008.md) / [CTFTCTE-AIM-008](../countertechniques/CTFTCTE-AIM-008.md) — output-sanitizer / policy-filter gate / leak via structure, serialization, encodings and examples

## Tools

- [prompt_fuzzer.py](../tools/CTFTTOU-447.md) — fire the payload ladder, JSONL transcript, flag scan, `--selftest`
- [garak](../tools/CTFTTOU-062.md), [promptfoo](../tools/CTFTTOU-063.md), [PyRIT](../tools/CTFTTOU-064.md), [promptmap](../tools/CTFTTOU-066.md)
- [curl](../tools/CTFTTOU-038.md) / [requests](../tools/CTFTTOU-067.md), [Playwright](../tools/CTFTTOU-008.md)

## Related skills

- [ctf-ai-ml](../../ctf-skills-main/ctf-ai-ml/SKILL.md) — CTFTSKL-017, the domain skill (AIM-002/007/009)

## Notes

Validated by `scripts/prompt_fuzzer.py --selftest` (mock sanitizer endpoint, planted
flag recovered through the examples payload; direct ask stays clean). Reference
event recorded in `v3/evidence.curated.json` EVID-AIM-008 (2026 company CTF, sanitizer
challenge solved via example/template enumeration).

## Related Techniques

CTFTTE-AIM-008, CTFTCTE-AIM-008
