# CTFTSKL-004 — ctf-ad-attack-paths

> **Skill ID:** `CTFTSKL-004`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-FPN-002, CTFTCTE-FPN-002, CTFTTE-FPN-011, CTFTCTE-FPN-011, CTFTTE-FPN-012, CTFTCTE-FPN-012, CTFTTE-FPN-013, CTFTCTE-FPN-013, CTFTTE-FPN-014, CTFTCTE-FPN-014, CTFTTE-FPN-017, CTFTCTE-FPN-017, CTFTTE-FPN-018, CTFTCTE-FPN-018

## Description

Decision workflow for authorized Active Directory CTF challenges: turn BloodHound edges,
Kerberos ticket state, AD CS templates, ACL rights, delegation and coercion into a concrete
path to Domain Admin or a cross-domain flag. Where `ctf-fpn` is the broad NetExec/BloodHound
command reference, this skill is the decision layer: observe the current identity's rights, map
the shortest BloodHound path, and pick the one edge whose preconditions you satisfy. Discovery
is read-only; password changes, template edits, coercion and relay are explicit gated mutations.

## Skill file

- [ctf-skills-main/ctf-ad-attack-paths/SKILL.md](../../ctf-skills-main/ctf-ad-attack-paths/SKILL.md) — canonical

## When to load

```yaml
artifact_type: domain-foothold          # kubeconfig-equivalent: creds, ticket, BloodHound data
runtime: ad-domain
evidence:
  - domain-joined hosts / AD credentials / a BloodHound dataset
  - BloodHound edge you hold (GenericWrite, AddKeyCredentialLink, AllowedToAct, ...)
  - vulnerable cert template (ESC1-16) or coercible DC (PrinterBug/PetitPotam)
  - a second domain / forest trust visible
```

## FOM pairs

- [CTFTTE-FPN-002](../techniques/CTFTTE-FPN-002.md) / [CTFTCTE-FPN-002](../countertechniques/CTFTCTE-FPN-002.md) — AD fullpwn
- [CTFTTE-FPN-011](../techniques/CTFTTE-FPN-011.md) / [CTFTCTE-FPN-011](../countertechniques/CTFTCTE-FPN-011.md) — key-credential backdoor (shadow creds)
- [CTFTTE-FPN-012](../techniques/CTFTTE-FPN-012.md) / [CTFTCTE-FPN-012](../countertechniques/CTFTCTE-FPN-012.md) — PKINIT / certificate Kerberos
- [CTFTTE-FPN-013](../techniques/CTFTTE-FPN-013.md) / [CTFTCTE-FPN-013](../countertechniques/CTFTCTE-FPN-013.md) — certificate template reconfiguration (ESC4)
- [CTFTTE-FPN-014](../techniques/CTFTTE-FPN-014.md) / [CTFTCTE-FPN-014](../countertechniques/CTFTCTE-FPN-014.md) — delegated-session injection (JEA)
- [CTFTTE-FPN-017](../techniques/CTFTTE-FPN-017.md) / [CTFTCTE-FPN-017](../countertechniques/CTFTCTE-FPN-017.md) — coerced DC authentication
- [CTFTTE-FPN-018](../techniques/CTFTTE-FPN-018.md) / [CTFTCTE-FPN-018](../countertechniques/CTFTCTE-FPN-018.md) — cross-domain credential reuse

## Tools

- [NetExec](../tools/CTFTTOU-016.md)
- [BloodHound / SharpHound](../tools/CTFTTOU-017.md)
- [impacket](../tools/CTFTTOU-116.md)
- [certipy](../tools/CTFTTOU-020.md)
- [kerbrute](../tools/CTFTTOU-115.md)
- [evil-winrm](../tools/CTFTTOU-024.md)
- [hashcat](../tools/CTFTTOU-015.md)
- [ad_inventory.py](../tools/CTFTTOU-402.md)
- [bh_path_report.py](../tools/CTFTTOU-403.md)
- [ticket_check.sh](../tools/CTFTTOU-404.md)
- bloodyAD, PyWhisker, PKINITtools, Coercer (third-party; see the skill's references/tooling.md)

## Related skills

- [ctf-cloud-kubernetes](CTFTSKL-006.md) — when the path runs on to cloud IAM / Entra
- [ctf-windows-artifact-timeline](CTFTSKL-005.md) — the defensive inverse (reconstructing the same attack from logs)

## Notes

Added 2026-10-25 as a forward-looking gap-fill for enterprise-AD CTF content (Hackfest 2026
preview lists Active Directory). Not yet backed by a reproduced local writeup — no attested
evidence record. The design mirrors public 2025 AD fullpwn chains (shadow creds → PKINIT →
ESC4 → coercion → cross-domain).

## Related Techniques

CTFTTE-FPN-002, CTFTCTE-FPN-002, CTFTTE-FPN-011, CTFTCTE-FPN-011, CTFTTE-FPN-012, CTFTCTE-FPN-012, CTFTTE-FPN-013, CTFTCTE-FPN-013, CTFTTE-FPN-014, CTFTCTE-FPN-014, CTFTTE-FPN-017, CTFTCTE-FPN-017, CTFTTE-FPN-018, CTFTCTE-FPN-018
