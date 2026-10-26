# CTFT Skills

Skill sheets: one fiche per agent skill (`SKILL.md`) that operationalises CTFT
techniques. Each fiche gives:
- the canonical skill file;
- when to load the skill (fingerprint);
- the FOM pairs it resolves;
- the tool sheets it drives;
- the agents that use it.

Tool sheets link here from their `## Skills` section, and FOM Nav opens these fiches
when a skill chip is clicked.

| Skill ID | Name | Kind | Skill file | FOM pairs |
| --- | --- | --- | --- | --- |
| [CTFTSKL-001](CTFTSKL-001.md) | ctf-sdr | Domain skill | [ctf-skills-main/ctf-sdr/SKILL.md](../../ctf-skills-main/ctf-sdr/SKILL.md) | CTFTTE-SDR-001..005 |
| [CTFTSKL-002](CTFTSKL-002.md) | ctf-sdr-ook-line-code | Fine-grained skill | [ctf-skills-main/ctf-sdr-ook-line-code/SKILL.md](../../ctf-skills-main/ctf-sdr-ook-line-code/SKILL.md) | CTFTTE-SDR-002 |

Fiche format (parsed by `franckysolve/fom_nav.py`):

```markdown
# CTFTSKL-NNN — <skill-name>
> **Skill ID:** `CTFTSKL-NNN`
> **Kind:** Domain skill | Fine-grained skill (one FOM pair) | Tool manual
> **Related techniques/counters:** ...
## Description
## Skill file            (first link = the SKILL.md)
## When to load          (fingerprint block)
## FOM pairs             (links to techniques / countertechniques)
## Tools                 (links to tool sheets)
## Agents                (links to .agents/**/AGENT.md)
## Related skills        (links to other CTFTSKL sheets)
## Notes
## Related Techniques
```
