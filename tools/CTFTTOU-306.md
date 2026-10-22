# CTFTTOU-306 — CAI (cai-framework)

> **Tool ID:** `CTFTTOU-306`  
> **Related techniques/counters:** CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001

## Description

Open-source cybersecurity agent framework (Alias Robotics): an LLM agent harness whose
agents drive a `generic_linux_command` tool to solve offensive challenges. The default
CTF agent (`one_tool`) executes a strict one-tool-per-turn ReAct loop — plan, act,
observe, adapt — across all CTF categories (Cybench-class performance via agent
scaffolds); ~35 other agents cover red/blue teaming, reverse engineering, DFIR,
network-traffic analysis, SDR. It is a cross-domain scaffold: the recovery-action
executor behind any technique whose solve is shell-driven, with the domain knowledge
supplied by prompt/skills layered on top (OWASP-LLM guardrails, honest-evidence and
untrusted-output rules built into its system prompts).

Public open-source line: `cai-framework` on PyPI (0.5.10, frozen Dec 2025); the
repository is archived (the professional line moved to Alias' commercial CSI offer).
The default agent type is `one_tool_agent` (the CTF agent).

## URL

<https://github.com/aliasrobotics/cai>

## AGENT & SKILLS

- [cai-one-tool](../../ctf-skills-main/cai-one-tool/SKILL.md) — ported discipline: ReAct loop, command hygiene, session management, honest evidence, flag validation; includes the verified Kali WSL install

## Related Techniques

CTFTTE-PWN-001, CTFTCTE-PWN-001, CTFTTE-REV-001, CTFTCTE-REV-001
