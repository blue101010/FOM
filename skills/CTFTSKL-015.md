# CTFTSKL-015 — ctf-infrastructure-history-correlation

> **Skill ID:** `CTFTSKL-015`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-OSI-003, CTFTCTE-OSI-003, CTFTTE-OSI-008, CTFTCTE-OSI-008, CTFTTE-OSI-009, CTFTCTE-OSI-009

## Description

Normalizes saved Shodan, URLScan, DNS and certificate observations into provenance-preserving events,
orders them by provider observation time, and builds conservative clusters using strong pivots. It
separates current banners from historical services and prevents generic titles, ports or ASNs from
becoming unsupported attribution edges.

## Skill file

- [ctf-skills-main/ctf-infrastructure-history-correlation/SKILL.md](../../ctf-skills-main/ctf-infrastructure-history-correlation/SKILL.md) — canonical

## When to load

```yaml
artifact_type: shodan-history | urlscan-results | dns-history | certificate-history
runtime: kali-wsl
evidence:
  - current infrastructure differs from a historical scan or report
  - an IP changed title, port, certificate or service over time
  - several provider exports must be joined into one cluster timeline
```

## FOM pairs

- [CTFTTE-OSI-003](../techniques/CTFTTE-OSI-003.md) / [CTFTCTE-OSI-003](../countertechniques/CTFTCTE-OSI-003.md) — historical/cached observations
- [CTFTTE-OSI-008](../techniques/CTFTTE-OSI-008.md) / [CTFTCTE-OSI-008](../countertechniques/CTFTCTE-OSI-008.md) — infrastructure mapping
- [CTFTTE-OSI-009](../techniques/CTFTTE-OSI-009.md) / [CTFTCTE-OSI-009](../countertechniques/CTFTCTE-OSI-009.md) — gate historical leads behind current attribution

## Tools

- [CTFTTOU-090 subfinder](../tools/CTFTTOU-090.md)
- [CTFTTOU-095 crt.sh](../tools/CTFTTOU-095.md)
- [CTFTTOU-111 dig](../tools/CTFTTOU-111.md)
- Shodan and URLScan exports (no dedicated FOM tool sheets yet)
- bundled `ctf-skills-main/ctf-infrastructure-history-correlation/scripts/infra_timeline.py`

## Agents

- (none yet)

## Related skills

- [CTFTSKL-013 ctf-urlscan-rulecraft](CTFTSKL-013.md)
- [CTFTSKL-016 ctf-threat-report-ioc-pivot](CTFTSKL-016.md)
- ctf-web-shodan — provider-specific collection and facet logic

## Notes

- Observation time, report time and retrieval time are separate.
- Exact generic titles and ports never form an automatic cluster edge.

## Related Techniques

CTFTTE-OSI-003, CTFTCTE-OSI-003, CTFTTE-OSI-008, CTFTCTE-OSI-008, CTFTTE-OSI-009, CTFTCTE-OSI-009

