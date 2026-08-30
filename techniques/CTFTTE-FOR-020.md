# CTFTTE-FOR-020 — LUKS-encrypted volume concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-020`](../countertechniques/CTFTCTE-FOR-020.md) — Recover LUKS headers/keyslots, bruteforce passphrase

---

## How the challenge author hides

A partition is LUKS-encrypted and the passphrase (or a keyslot) is part of the puzzle; the flag is inside the decrypted filesystem.

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
- Add challenge write-up link
