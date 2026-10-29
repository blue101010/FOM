# CTFTSKL-012 — ctf-wordlists

> **Skill ID:** `CTFTSKL-012`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-CRY-012, CTFTCTE-CRY-012

## Description

Wordlist inventory and cracking-tool quick reference for CTF on Kali WSL.
Operationalises the CTFTCTE-CRY-012 recovery action with a verified inventory
of the host's wordlists (rockyou, SecLists Passwords/Usernames, default
credentials, keyboard walks, cracked-hash plaintexts, English dictionaries),
hashcat/john mechanics (attack modes, rules ladder, masks, pot files), and the
*2john extractors that turn protected artifacts (zip, rar, ssh, KeePass, pdf,
office, gpg, /etc/shadow) into crackable hashes. Companion read-only script
`ctf-skills-main/ctf-wordlists/scripts/wordlist_inventory.sh`.

## Skill file

- [ctf-skills-main/ctf-wordlists/SKILL.md](../../ctf-skills-main/ctf-wordlists/SKILL.md) — canonical

## When to load

```yaml
artifact_type: hash | protected-file
runtime: kali-wsl
evidence:
  - a hash to identify and crack, or a password-protected artifact
  - need to pick/mangle a wordlist instead of brute-forcing
  - challenge hints at human passwords, defaults, dates, leetspeak
```

## FOM pairs

- [CTFTTE-CRY-012](../techniques/CTFTTE-CRY-012.md) / [CTFTCTE-CRY-012](../countertechniques/CTFTCTE-CRY-012.md) — hash-cracking maze / crack under masks and rules

## Tools

- [CTFTTOU-015 hashcat](../tools/CTFTTOU-015.md)
- [CTFTTOU-257 john](../tools/CTFTTOU-257.md)
- [CTFTTOU-061 rockyou](../tools/CTFTTOU-061.md)
- [CTFTTOU-011 name-that-hash](../tools/CTFTTOU-011.md)

## Agents

- (none yet)

## Related skills

- [CTFTSKL-007 ctf-crypto-bounded-exponent-relation](CTFTSKL-007.md) — other CRY fine-grained sheet
- ctf-crypto-hash-cracking-maze — cracking strategy layer above this tool manual

## Notes

- Strategy (constraints, keyspaces, solver hand-off) lives in
  ctf-crypto-hash-cracking-maze; this sheet is the inventory + tool mechanics.
- WSL has no GPU: prefer john for rockyou-scale lists, hashcat for masks/rules.

## Related Techniques

CTFTTE-CRY-012, CTFTCTE-CRY-012
