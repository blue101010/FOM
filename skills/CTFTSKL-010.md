# CTFTSKL-010 — ctf-web-caido

> **Skill ID:** `CTFTSKL-010`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-WEB-001, CTFTCTE-WEB-001, CTFTTE-WEB-002, CTFTCTE-WEB-002, CTFTTE-WEB-003, CTFTCTE-WEB-003, CTFTTE-WEB-004, CTFTCTE-WEB-004, CTFTTE-WEB-007, CTFTCTE-WEB-007, CTFTTE-WEB-009, CTFTCTE-WEB-009, CTFTTE-WEB-012, CTFTCTE-WEB-012, CTFTTE-WEB-014, CTFTCTE-WEB-014, CTFTTE-WEB-018, CTFTCTE-WEB-018, CTFTTE-WEB-020, CTFTCTE-WEB-020, CTFTTE-WEB-022, CTFTCTE-WEB-022, CTFTTE-WEB-024, CTFTCTE-WEB-024, CTFTTE-WEB-025, CTFTCTE-WEB-025, CTFTTE-WEB-026, CTFTCTE-WEB-026, CTFTTE-WEB-027, CTFTCTE-WEB-027, CTFTTE-WEB-028, CTFTCTE-WEB-028, CTFTTE-WEB-029, CTFTCTE-WEB-029

## Description

The decision layer that makes Caido the **default** web workbench in this workspace: a tool ladder
(Caido MCP tools → `caido-cli` → `ctf-web-analyze` Playwright/Edge DevTools), the read-only/mutation
split that the HFCTF no-AI scoreboard rule imposes, and the concrete recipes for HTTPQL triage, request
inspection, replay, parallel access-control sweeps, fuzzing, findings and curl export.

Its value is not "another proxy": it prevents the two recurring failures — rebuilding a request by hand
once the shell is gone, and sweeping a target without an attributable record of what was sent.

Beyond traffic, the state side carries the capabilities that decide which technique applies: raw
last-byte-synchronized bursts (state-change races), per-identity cookie jars swept in parallel
(access-control matrices), body re-rendering across formats (parser differentials), verbatim byte
sending (framing desync), a passive rule set over every proxied response with findings tied to a request
id (signal buried in volume), and a sitemap as the routed-resource inventory (unlinked privileged
functions). Two rules govern the whole set: passive rules only observe **proxied** traffic, and they
only behave if the challenge host is **in scope**.

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
- [CTFTTE-WEB-024](../techniques/CTFTTE-WEB-024.md) / [CTFTCTE-WEB-024](../countertechniques/CTFTCTE-WEB-024.md) — race window in a state-changing flow (last-byte-synchronized bursts)
- [CTFTTE-WEB-025](../techniques/CTFTTE-WEB-025.md) / [CTFTCTE-WEB-025](../countertechniques/CTFTCTE-WEB-025.md) — server-trusted client-computed state (edit one field, diff the outcome)
- [CTFTTE-WEB-026](../techniques/CTFTTE-WEB-026.md) / [CTFTCTE-WEB-026](../countertechniques/CTFTCTE-WEB-026.md) — signal buried in a high-volume response corpus (passive rules plus findings triage)
- [CTFTTE-WEB-027](../techniques/CTFTTE-WEB-027.md) / [CTFTCTE-WEB-027](../countertechniques/CTFTCTE-WEB-027.md) — representation differential across body formats (convert then replay)
- [CTFTTE-WEB-028](../techniques/CTFTTE-WEB-028.md) / [CTFTCTE-WEB-028](../countertechniques/CTFTCTE-WEB-028.md) — function-level authorization gap (sweep across session jars, anonymous included)
- [CTFTTE-WEB-029](../techniques/CTFTTE-WEB-029.md) / [CTFTCTE-WEB-029](../countertechniques/CTFTCTE-WEB-029.md) — desynchronized request framing (bytes sent verbatim)

## Tool inventory

- `report2.md` in the skill directory lists all 66 MCP tools by capability group, generated from the
  server's own `tools/list` — use it instead of guessing a tool name.
- `scripts/caido_mcp_client.py` is the rung-1b bridge for sessions whose tool picker hides `caido_*`:
  it performs the MCP handshake over stdio and calls one tool. `--list` reproduces the inventory.
- When the picker disables the findings tools, the state surface is still reachable over GraphQL with
  the same token; that path is documented in the skill's findings section.

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
