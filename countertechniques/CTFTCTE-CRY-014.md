# CTFTCTE-CRY-014 — Derive the XOR key from file mtime

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CRY`](../tactics/CTFT-TA-CRY.md) — Crypto  
> **Counters technique:** [`CTFTTE-CRY-014`](../techniques/CTFTTE-CRY-014.md) — Timestamp-keyed XOR

---

## Offensive Recovery (CTF practitioner / solver)

1. Read the file's last-modification time with full precision
   (`stat`, `date -r`, or `os.stat().st_mtime`).
2. Convert to epoch seconds and use the decimal string as the repeating XOR key over the
   hex-decoded ciphertext.
3. If the mtime was disturbed (guardian still running, tool re-writing the file), sweep a
   ±N-second window around plausible write times and score each candidate key by printable
   ASCII ratio or a flag-format regex.
4. Beware timezone and truncation variants: try local vs UTC parsing, integer vs
   sub-second float, and RFC3339-formatted strings as alternative key spellings.

## Forensic / Blue-Team Perspective (DFIR analyst)

Timestamp-keyed XOR is fragile opsec: the key is recoverable from the artifact's own
metadata, and every re-encryption bumps the mtime, correlating reads with writes. Analysts
break it the same way players do — pair the ciphertext with the last write time before the
snapshot.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Time-derived XOR keys are an obfuscation whose key material lives in filesystem metadata. |

## Tools

- [mtime-xor-recover.py](../tools/scripts/mtime-xor-recover.py) ([CTFTTOU-071](../tools/CTFTTOU-071.md))
- stat
- CyberChef

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/>
