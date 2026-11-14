# CTFTSKL-016 — ctf-threat-report-ioc-pivot

> **Skill ID:** `CTFTSKL-016`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-OSI-005, CTFTCTE-OSI-005, CTFTTE-OSI-008, CTFTCTE-OSI-008

## Description

Extracts raw and normalized indicators from threat reports while preserving source line, context,
defanging and contextual role. It ranks report-backed infrastructure pivots and generates reproducible
questions for Shodan, URLScan, DNS, certificate, repository and malware-intelligence follow-up.

## Skill file

- [ctf-skills-main/ctf-threat-report-ioc-pivot/SKILL.md](../../ctf-skills-main/ctf-threat-report-ioc-pivot/SKILL.md) — canonical

## When to load

```yaml
artifact_type: threat-report | ioc-table | report-html | report-markdown
runtime: kali-wsl
evidence:
  - a challenge starts from a vendor/research report or IOC appendix
  - defanged IPs, domains, URLs or hashes need normalization with provenance
  - report-time indicators must seed infrastructure mapping
```

## FOM pairs

- [CTFTTE-OSI-005](../techniques/CTFTTE-OSI-005.md) / [CTFTCTE-OSI-005](../countertechniques/CTFTCTE-OSI-005.md) — mine public records and repositories
- [CTFTTE-OSI-008](../techniques/CTFTTE-OSI-008.md) / [CTFTCTE-OSI-008](../countertechniques/CTFTCTE-OSI-008.md) — map infrastructure from extracted seeds

## Tools

- [CTFTTOU-093 bbot](../tools/CTFTTOU-093.md)
- [CTFTTOU-421 GitHub Code Search](../tools/CTFTTOU-421.md)
- bundled `ctf-skills-main/ctf-threat-report-ioc-pivot/scripts/report_ioc_extract.py`

## Agents

- (none yet)

## Related skills

- [CTFTSKL-015 ctf-infrastructure-history-correlation](CTFTSKL-015.md)
- [CTFTSKL-013 ctf-urlscan-rulecraft](CTFTSKL-013.md)

## Notes

- Extraction is not attribution; public services, victims and references remain contextual records.
- The normalized field never replaces the raw defanged evidence.

## Related Techniques

CTFTTE-OSI-005, CTFTCTE-OSI-005, CTFTTE-OSI-008, CTFTCTE-OSI-008

