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
| [CTFTSKL-007](CTFTSKL-007.md) | ctf-crypto-bounded-exponent-relation | Fine-grained skill | [ctf-skills-main/ctf-crypto-bounded-exponent-relation/SKILL.md](../../ctf-skills-main/ctf-crypto-bounded-exponent-relation/SKILL.md) | CRY-015 |
| [CTFTSKL-008](CTFTSKL-008.md) | ctf-cloud-public-bucket | Fine-grained skill | [ctf-skills-main/ctf-cloud-public-bucket/SKILL.md](../../ctf-skills-main/ctf-cloud-public-bucket/SKILL.md) | CLD-001 |
| [CTFTSKL-009](CTFTSKL-009.md) | ctf-cloud-azure | Domain skill | [ctf-skills-main/ctf-cloud-azure/SKILL.md](../../ctf-skills-main/ctf-cloud-azure/SKILL.md) | CLD-001/002/003/005/007/008/009/010/011 |
| [CTFTSKL-010](CTFTSKL-010.md) | ctf-web-caido | Tool manual | [.github/skills/ctf-web-caido/SKILL.md](../../.github/skills/ctf-web-caido/SKILL.md) | WEB-001/002/003/004/007/009/012/014/018/020/022/024..029 |
| [CTFTSKL-011](CTFTSKL-011.md) | ctf-stego-lsb | Fine-grained skill | [ctf-skills-main/ctf-stego-lsb/SKILL.md](../../ctf-skills-main/ctf-stego-lsb/SKILL.md) | STE-001 |
| [CTFTSKL-012](CTFTSKL-012.md) | ctf-wordlists | Tool manual | [ctf-skills-main/ctf-wordlists/SKILL.md](../../ctf-skills-main/ctf-wordlists/SKILL.md) | CRY-012 |
| [CTFTSKL-013](CTFTSKL-013.md) | ctf-urlscan-rulecraft | Tool manual | [ctf-skills-main/ctf-urlscan-rulecraft/SKILL.md](../../ctf-skills-main/ctf-urlscan-rulecraft/SKILL.md) | OSI-003 |
| [CTFTSKL-014](CTFTSKL-014.md) | ctf-social-thread-recovery | Tool manual | [ctf-skills-main/ctf-social-thread-recovery/SKILL.md](../../ctf-skills-main/ctf-social-thread-recovery/SKILL.md) | OSI-003/005 |
| [CTFTSKL-015](CTFTSKL-015.md) | ctf-infrastructure-history-correlation | Domain skill | [ctf-skills-main/ctf-infrastructure-history-correlation/SKILL.md](../../ctf-skills-main/ctf-infrastructure-history-correlation/SKILL.md) | OSI-003/008/009 |
| [CTFTSKL-016](CTFTSKL-016.md) | ctf-threat-report-ioc-pivot | Tool manual | [ctf-skills-main/ctf-threat-report-ioc-pivot/SKILL.md](../../ctf-skills-main/ctf-threat-report-ioc-pivot/SKILL.md) | OSI-005/008 |
| [CTFTSKL-017](CTFTSKL-017.md) | ctf-ai-ml | Domain skill | [ctf-skills-main/ctf-ai-ml/SKILL.md](../../ctf-skills-main/ctf-ai-ml/SKILL.md) | AIM-001..007, AIM-009 |
| [CTFTSKL-018](CTFTSKL-018.md) | ctf-ai-llm-sanitizer-bypass | Fine-grained skill | [ctf-skills-main/ctf-ai-llm-sanitizer-bypass/SKILL.md](../../ctf-skills-main/ctf-ai-llm-sanitizer-bypass/SKILL.md) | AIM-008 |
| [CTFTSKL-019](CTFTSKL-019.md) | ctf-cloud-aws | Domain skill | [ctf-skills-main/ctf-cloud-aws/SKILL.md](../../ctf-skills-main/ctf-cloud-aws/SKILL.md) | CLD-001/002/003/004/005/006/007/010/011 |

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
