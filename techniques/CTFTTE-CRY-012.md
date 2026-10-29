# CTFTTE-CRY-012 — Hash-cracking maze with constraints

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Cryptography  
> **Paired counter-technique:** [`CTFTCTE-CRY-012`](../countertechniques/CTFTCTE-CRY-012.md) — Crack hashes under masks/rules

---

## How the challenge author hides

The flag is a hash whose preimage satisfies extra constraints (mask, salt, charset).
The hash itself is strong (sha256crypt and peers), so raw brute force is hopeless; the
intended path is that the *shape* of the plaintext is leaked by the challenge story and
the solver must turn that shape into a mask or rule set. A second, harder variant gives
a plaintext that follows an external fixed format — a word address, a date, a serial
number — where each position's character class is known, collapsing the keyspace by
orders of magnitude. The concealment is the missing constraint statement: the solver
must notice that the format is knowable before any attack can succeed.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1110 | Brute Force | Credential-hash brute force; CTFT adds mask/rule craft. |

## Tools

- [hashcat](../tools/CTFTTOU-011.md)
- john
- hashid

## Indicators

- a documented hash format (sha256crypt `$5$`, bcrypt, Kerberos) with a salt, where the flag is the plaintext
- wordlist and rule attacks exhaust without a hit, while the challenge text keeps describing the plaintext's shape
- the plaintext is known to follow an external fixed format (word address, date, serial), so every position's character class is derivable
- challenge text about "three words", a pattern, or a format the answer must match

## References

- <https://hashcat.net/hashcat/>
- <https://hashcat.net/wiki/doku.php?id=mask_attack>
