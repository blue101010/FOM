# CTFTSKL-013 — ctf-urlscan-rulecraft

> **Skill ID:** `CTFTSKL-013`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-OSI-003, CTFTCTE-OSI-003

## Description

Derives exact urlscan.io search rules from stored scan metadata, DOM text, open-directory listings,
resources and response hashes. It distinguishes unquoted URL wildcards from exact title phrases,
counts files separately from subdirectories/navigation links, models indexed text and its prefix
cutoff, records plan-gated validation honestly, and prevents punctuation variants from replacing
evidence.

## Skill file

- [ctf-skills-main/ctf-urlscan-rulecraft/SKILL.md](../../ctf-skills-main/ctf-urlscan-rulecraft/SKILL.md) — canonical

## When to load

```yaml
artifact_type: urlscan-result | stored-dom | urlscan-query
runtime: kali-wsl
evidence:
  - a challenge asks for a URLScan search rule
  - a historical scan preserves a page or resource no longer live
  - page.domain/domain, filename/hash, or text.content semantics decide the query
```

## FOM pairs

- [CTFTTE-OSI-003](../techniques/CTFTTE-OSI-003.md) / [CTFTCTE-OSI-003](../countertechniques/CTFTCTE-OSI-003.md) — historical/cached content recovery

## Tools

- urlscan.io search, result, DOM and Content views (no FOM tool sheet yet)
- bundled `ctf-skills-main/ctf-urlscan-rulecraft/scripts/urlscan_text.py`
- bundled `ctf-skills-main/ctf-urlscan-rulecraft/scripts/urlscan_autoindex.py`

## Agents

- (none yet)

## Related skills

- [CTFTSKL-014 ctf-social-thread-recovery](CTFTSKL-014.md) — recover social seeds before URLScan pivots
- ctf-web-shodan — broader infrastructure clustering after a rule identifies a family

## Notes

- A locally extracted DOM is an approximation; URLScan's stored Content/search representation wins.
- A plan-gated field is unvalidated, not a zero-result query.

## Related Techniques

CTFTTE-OSI-003, CTFTCTE-OSI-003

