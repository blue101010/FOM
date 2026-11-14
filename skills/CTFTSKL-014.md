# CTFTSKL-014 — ctf-social-thread-recovery

> **Skill ID:** `CTFTSKL-014`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-OSI-003, CTFTCTE-OSI-003, CTFTTE-OSI-005, CTFTCTE-OSI-005

## Description

Recovers public social-post evidence when the interactive platform is unavailable, login-gated or
throttled. It canonicalises post IDs, merges saved syndication/archival records into a provenance
graph, separates replies from quotes and mentions, preserves media evidence, and pivots to archives,
search indexes, reports and public repositories without attempting account or rate-limit bypasses.

## Skill file

- [ctf-skills-main/ctf-social-thread-recovery/SKILL.md](../../ctf-skills-main/ctf-social-thread-recovery/SKILL.md) — canonical

## When to load

```yaml
artifact_type: social-url | post-id | saved-social-json | social-media
runtime: kali-wsl
evidence:
  - an X/Twitter post, reply, quote-post or media URL seeds the challenge
  - replies are login-gated or the platform returns 429/unavailable
  - archived copies, public records or reports may preserve the missing node
```

## FOM pairs

- [CTFTTE-OSI-003](../techniques/CTFTTE-OSI-003.md) / [CTFTCTE-OSI-003](../countertechniques/CTFTCTE-OSI-003.md) — recover deleted or changed public content
- [CTFTTE-OSI-005](../techniques/CTFTTE-OSI-005.md) / [CTFTCTE-OSI-005](../countertechniques/CTFTCTE-OSI-005.md) — mine public repositories and records for quoted evidence

## Tools

- [CTFTTOU-094 waybackurls](../tools/CTFTTOU-094.md)
- [CTFTTOU-096 Wayback Machine](../tools/CTFTTOU-096.md)
- [CTFTTOU-420 archive.today](../tools/CTFTTOU-420.md)
- [CTFTTOU-421 GitHub Code Search](../tools/CTFTTOU-421.md)
- bundled `ctf-skills-main/ctf-social-thread-recovery/scripts/thread_manifest.py`

## Agents

- (none yet)

## Related skills

- [CTFTSKL-013 ctf-urlscan-rulecraft](CTFTSKL-013.md) — convert recovered infrastructure into URLScan rules

## Notes

- Numeric post IDs are stable join keys; handles can change.
- Counts and mentions are not reply identifiers.
- 429/login checkpoints trigger archive fallback, not repeated retries or credential use.

## Related Techniques

CTFTTE-OSI-003, CTFTCTE-OSI-003, CTFTTE-OSI-005, CTFTCTE-OSI-005

