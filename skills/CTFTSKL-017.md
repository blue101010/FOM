# CTFTSKL-017 — ctf-ai-ml

> **Skill ID:** `CTFTSKL-017`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-AIM-001..007, CTFTTE-AIM-009, CTFTCTE-AIM-001..007, CTFTCTE-AIM-009

## Description

Domain skill for AI/ML CTF challenges: model weight attacks and extraction, adversarial
examples, prompt injection and jailbreaking, token smuggling, context-window attacks,
agentic tool-use exploitation, and — since the 2026 company CTFs — direct probing of
player-reachable MCP servers (`mcp-probe.md` + `scripts/mcp_probe.py`, AIM-009).

## Skill file

- [ctf-skills-main/ctf-ai-ml/SKILL.md](../../ctf-skills-main/ctf-ai-ml/SKILL.md) — canonical
  - deep dives: `llm-attacks.md`, `model-attacks.md`, `adversarial-ml.md`, `mcp-probe.md`
  - script: `scripts/mcp_probe.py` (stdlib, `--selftest`)

## When to load

```yaml
artifact_type: model-weights | LLM-backed web service | MCP endpoint | serialized model
evidence:
  - challenge hands you an LLM chat/verdict endpoint, an agent with tools, or a model file
  - an HTTP endpoint answers MCP initialize with serverInfo + SSE frames (AIM-009)
  - the LLM gates on a decision (verdict/score/approval), not on output redaction (AIM-002/007)
  - weights/adapter files (AIM-001/004/005) or a classifier to attack (AIM-003)
fom_pairs: CTFTTE-AIM-001..007, CTFTTE-AIM-009
```

If the LLM instead **sanitizes its own output** and the secret hides in unfiltered
channels, load the fine-grained [CTFTSKL-018](CTFTSKL-018.md) (AIM-008).

## FOM pairs

- [CTFTTE-AIM-002](../techniques/CTFTTE-AIM-002.md) / [CTFTCTE-AIM-002](../countertechniques/CTFTCTE-AIM-002.md) — prompt-injection-gated flag / crafted-prompt extraction
- [CTFTTE-AIM-007](../techniques/CTFTTE-AIM-007.md) / [CTFTCTE-AIM-007](../countertechniques/CTFTCTE-AIM-007.md) — agent tool-calling guardrail bypass
- [CTFTTE-AIM-009](../techniques/CTFTTE-AIM-009.md) / [CTFTCTE-AIM-009](../countertechniques/CTFTCTE-AIM-009.md) — player-reachable MCP server / enumerate and abuse its surface
- plus AIM-001, AIM-003..006 (weights, adversarial input, serialized model, inversion, platform misconfig)

## Tools

- [garak](../tools/CTFTTOU-062.md), [promptfoo](../tools/CTFTTOU-063.md), [PyRIT](../tools/CTFTTOU-064.md), [promptmap](../tools/CTFTTOU-066.md)
- [curl](../tools/CTFTTOU-038.md) / [requests](../tools/CTFTTOU-067.md), [Playwright](../tools/CTFTTOU-008.md)
- [mcp_probe.py](../tools/CTFTTOU-448.md) — MCP enumeration + flag scan (AIM-009)
- [prompt_fuzzer.py](../tools/CTFTTOU-447.md) — sanitizer-bypass ladder runner (AIM-008, used via CTFTSKL-018)

## Related skills

- [ctf-ai-llm-sanitizer-bypass](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/SKILL.md) — CTFTSKL-018, the AIM-008 fine-grained skill

## Notes

Kali WSL venv `~/.venvs/ctfml` (torch + transformers) for the model-weight branches;
the LLM-attack and MCP branches are stdlib-only (`mcp_probe.py --selftest` needs no
venv). HTB Business CTF 2025 aiml challenges (few-shot verdict injection, agentic
tool-misuse file read / DB exfil) are the reference events — see
`v3/evidence.curated.json` EVID-AIM-002 / EVID-AIM-007.

## Related Techniques

CTFTTE-AIM-001..007, CTFTTE-AIM-009, CTFTCTE-AIM-001..007, CTFTCTE-AIM-009
