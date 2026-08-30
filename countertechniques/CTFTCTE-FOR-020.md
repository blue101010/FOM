# CTFTCTE-FOR-020 — Recover LUKS headers/keyslots, bruteforce passphrase

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-020`](../techniques/CTFTTE-FOR-020.md) — LUKS-encrypted volume concealment

---

## Offensive Recovery (CTF practitioner / solver)

Identify LUKS headers/keyslots, attack the passphrase (dictionary/bruteforce via luks2john), unlock and mount the volume.

## Forensic / Blue-Team Perspective (DFIR analyst)

Encrypted-media recovery must preserve header integrity; keyslot iteration counts and header backups decide feasibility.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1486 | Data Encrypted for Impact | Adversarial volume encryption; CTFT recovers it. |

## Tools

- cryptsetup
- luks2john
- hashcat
- dd

## References

- <https://gitlab.com/cryptsetup/cryptsetup>

