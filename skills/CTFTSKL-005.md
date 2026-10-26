# CTFTSKL-005 — ctf-windows-artifact-timeline

> **Skill ID:** `CTFTSKL-005`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-FOR-026, CTFTCTE-FOR-026, CTFTTE-FOR-028, CTFTCTE-FOR-028, CTFTTE-FOR-029, CTFTCTE-FOR-029

## Description

Builds a deterministic, UTC-normalized cross-artifact timeline from Windows forensic evidence
(KAPE triage ZIP, disk image, or extracted artifact set) in Kali WSL, then correlates it into
candidate incidents. Where [ctf-evtx](CTFTSKL-003.md) parses a single `.evtx` file deeply, this
skill is the multi-artifact fusion layer: it consumes EVTX, MFT/USN, Prefetch, Amcache,
Shimcache, registry, PowerShell, Defender, SRUM and browser evidence through the right parsers
and merges them into one ordered, provenance-preserving stream so the three events that form the
intrusion stand out of fifty thousand.

## Skill file

- [ctf-skills-main/ctf-windows-artifact-timeline/SKILL.md](../../ctf-skills-main/ctf-windows-artifact-timeline/SKILL.md) — canonical

## When to load

```yaml
artifact_type: windows-evidence         # KAPE ZIP / image / extracted artifacts (multiple classes)
runtime: offline
evidence:
  - several Windows artifact types present (EVTX + MFT + Prefetch + registry ...)
  - task is "when did the attacker X" / reconstruct the sequence across artifacts
  - Hayabusa / Chainsaw / Plaso / Eric Zimmerman tools named
```

## FOM pairs

- [CTFTTE-FOR-026](../techniques/CTFTTE-FOR-026.md) / [CTFTCTE-FOR-026](../countertechniques/CTFTCTE-FOR-026.md) — memory/OS-artifact recovery
- [CTFTTE-FOR-028](../techniques/CTFTTE-FOR-028.md) / [CTFTCTE-FOR-028](../countertechniques/CTFTCTE-FOR-028.md) — Windows event-log timeline reconstruction
- [CTFTTE-FOR-029](../techniques/CTFTTE-FOR-029.md) / [CTFTCTE-FOR-029](../countertechniques/CTFTCTE-FOR-029.md) — registry-hive artifacts

## Tools

- [Chainsaw](../tools/CTFTTOU-156.md)
- [The Sleuth Kit](../tools/CTFTTOU-131.md)
- [volatility3](../tools/CTFTTOU-134.md)
- [artifact_inventory.py](../tools/CTFTTOU-405.md)
- [timeline_normalize.py](../tools/CTFTTOU-406.md)
- [timeline_correlate.py](../tools/CTFTTOU-407.md)
- Hayabusa, Plaso/log2timeline, Regipy, dissect.target, Eric Zimmerman tools (third-party; see references/tool-matrix.md)

## Related skills

- [ctf-evtx](CTFTSKL-003.md) — the single-format EVTX parser this skill builds on
- [ctf-ad-attack-paths](CTFTSKL-004.md) — the offensive inverse when the timeline shows an AD intrusion

## Notes

Added 2026-10-25 as a forward-looking gap-fill for operational Windows DFIR / log-analytics CTF
content (Hackfest 2026 preview lists log-analytics and forensics; the 2025 APT514 workshop
required Zimmerman tooling). The deliverable is the normalized-event schema and the three
bundled scripts; no attested event record yet. Complements, does not duplicate, ctf-forensics
and ctf-evtx.

## Related Techniques

CTFTTE-FOR-026, CTFTCTE-FOR-026, CTFTTE-FOR-028, CTFTCTE-FOR-028, CTFTTE-FOR-029, CTFTCTE-FOR-029
