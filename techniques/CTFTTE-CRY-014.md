# CTFTTE-CRY-014 — Timestamp-keyed XOR

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Crypto  
> **Paired counter-technique:** [`CTFTCTE-CRY-014`](../countertechniques/CTFTCTE-CRY-014.md) — Derive the XOR key from file mtime

---

## How the challenge author hides

The ciphertext is a plain repeating-key XOR, but the key is stored nowhere: it is the
decimal string of the epoch timestamp at which the writer touched the file
(e.g. `str(time.Now().Unix())`). Generic decoders fail because the key looks like
arbitrary digits with unknown provenance. The trap is that the key is leaked by the
filesystem itself — the file's last-modification time. A twist: a guardian process may
re-encrypt on every read, so the mtime of the *last* write, not the original one, is the
one that matches the final ciphertext.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Time-derived XOR keys are an obfuscation whose key material lives in filesystem metadata. |

## Tools

- [mtime-xor-recover.py](../tools/scripts/mtime-xor-recover.py) ([CTFTTOU-071](../tools/CTFTTOU-071.md))
- CyberChef XOR bruteforce (baseline failure case)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/> (HFCTF 2025 "Tarpit Fall", flag-defender key schedule)
