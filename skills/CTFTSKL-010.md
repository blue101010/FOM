# CTFTSKL-010 — ctf-web-caido

> **Skill ID:** `CTFTSKL-010`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-WEB-001, CTFTCTE-WEB-001, CTFTTE-WEB-002, CTFTCTE-WEB-002, CTFTTE-WEB-003, CTFTCTE-WEB-003, CTFTTE-WEB-009, CTFTCTE-WEB-009

## Description

The decision layer that makes Caido the **default** web workbench in this workspace: a tool ladder
(Caido MCP tools → `caido-cli` → `ctf-web-analyze` Playwright/Edge DevTools), the read-only/mutation
split that the HFCTF no-AI scoreboard rule imposes, and the concrete recipes for HTTPQL triage, request
inspection, replay, parallel access-control sweeps, fuzzing, findings and curl export.

Its value is not "another proxy": it prevents the two recurring failures — rebuilding a request by hand
once the shell is gone, and sweeping a target without an attributable record of what was sent.

## Skill file

- [.github/skills/ctf-web-caido/SKILL.md](../../.github/skills/ctf-web-caido/SKILL.md) — canonical (VS Code Copilot)
- [.codex/skills/ctf-web-caido/SKILL.md](../../.codex/skills/ctf-web-caido/SKILL.md) — Codex mirror (keep in sync)

## When to load

```yaml
artifact_type: url | api | web-app
runtime: caido
evidence:
  - a challenge URL, login form, API endpoint, session cookie or JWT to inspect
  - a Caido instance answering on CAIDO_URL (caido-cli status → Auth OK + Instance OK)
  - caido_* tools present in the session (MCP rung available)
  - a question of the form "what did the app send", "what does this request look like",
    "what happens if I change this header/id", "what happens across these N variations"
```

## FOM pairs

- [CTFTTE-WEB-001](../techniques/CTFTTE-WEB-001.md) / [CTFTCTE-WEB-001](../countertechniques/CTFTCTE-WEB-001.md) — obscured endpoint / source-comment hiding (history + sitemap first)
- [CTFTTE-WEB-002](../techniques/CTFTTE-WEB-002.md) / [CTFTCTE-WEB-002](../countertechniques/CTFTCTE-WEB-002.md) — IDOR (`batch sweep` is the instrument)
- [CTFTTE-WEB-003](../techniques/CTFTTE-WEB-003.md) / [CTFTCTE-WEB-003](../countertechniques/CTFTCTE-WEB-003.md) — JWT misconfiguration (replay/edit, cookie jar)
- [CTFTTE-WEB-009](../techniques/CTFTTE-WEB-009.md) / [CTFTCTE-WEB-009](../countertechniques/CTFTCTE-WEB-009.md) — configuration secret exposure (triage before exploitation)

## Tools

- [CTFTTOU-441](../tools/CTFTTOU-441.md) — Caido: `caido-cli` + `caido-mcp-server`
- [frankysolve-chepy](../../ctf-skills-main/frankysolve-chepy/SKILL.md) — decoding captured values

## Related skills

- `ctf-web-analyze` ([.github/skills/ctf-web-analyze/SKILL.md](../../.github/skills/ctf-web-analyze/SKILL.md)) — fallback rung when no Caido instance answers; no FOM sheet yet
- `web-ctf-resolve` ([.github/skills/web-ctf-resolve/SKILL.md](../../.github/skills/web-ctf-resolve/SKILL.md)) — end-to-end solve
- `ctf-web` ([../../ctf-skills-main/ctf-web/SKILL.md](../../ctf-skills-main/ctf-web/SKILL.md)) — per-vulnerability technique files

## Notes

Added 2026-10-28 with the workspace's Caido installation (`go install` v4.3.0, MCP registered as
`caido` in `.mcp.json`, `.vscode/mcp.json` and `.codex/config.toml`). The skill intentionally encodes
authorization first: read-only triage is unconditional, while replay/sweeps/fuzzing need an explicit
in-scope decision, and the HFCTF no-AI scoreboard forbids the agent from driving requests at all.
Complements rather than replaces `ctf-web-analyze`: same Burp mapping, different capture engine.

## Related Techniques

CTFTTE-WEB-001, CTFTCTE-WEB-001, CTFTTE-WEB-002, CTFTCTE-WEB-002, CTFTTE-WEB-003, CTFTCTE-WEB-003,
CTFTTE-WEB-009, CTFTCTE-WEB-009
