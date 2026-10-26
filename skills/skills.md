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
| [CTFTSKL-003](CTFTSKL-003.md) | ctf-evtx | Tool manual | [ctf-skills-main/ctf-evtx/SKILL.md](../../ctf-skills-main/ctf-evtx/SKILL.md) | CTFTTE-FOR-028 |
| [CTFTSKL-004](CTFTSKL-004.md) | ctf-ad-attack-paths | Domain skill | [ctf-skills-main/ctf-ad-attack-paths/SKILL.md](../../ctf-skills-main/ctf-ad-attack-paths/SKILL.md) | FPN-002/011/012/013/014/017/018 |
| [CTFTSKL-005](CTFTSKL-005.md) | ctf-windows-artifact-timeline | Domain skill | [ctf-skills-main/ctf-windows-artifact-timeline/SKILL.md](../../ctf-skills-main/ctf-windows-artifact-timeline/SKILL.md) | FOR-026/028/029 |
| [CTFTSKL-006](CTFTSKL-006.md) | ctf-cloud-kubernetes | Domain skill | [ctf-skills-main/ctf-cloud-kubernetes/SKILL.md](../../ctf-skills-main/ctf-cloud-kubernetes/SKILL.md) | CLD-002/003/005/006/008, FPN-004/005 |

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
