# CTFTTE-FOR-030 — Read-triggered payload mutation (guardian process)

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-030`](../countertechniques/CTFTCTE-FOR-030.md) — Detect, stop and snapshot a read-triggered mutator

---

## How the challenge author hides

A background guardian process (e.g. `flag-defender`) watches the flag file and re-encrypts it
on every access — XOR with the current time, content doubling in size with each read. The
concealment is the act of reading itself: every observation changes the ciphertext, so
CyberChef magic, hash comparison and format detection all fail, and naive triage burns
instance re-provisionings. The defense punishes the standard forensic loop
(open → inspect → decode) and only reveals itself through repeated identical reads
producing different bytes.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1070 | Indicator Removal on Host | The artifact is altered at the moment of access so each observation destroys the previous state. |

## Tools

- [mutating-file-watchdog.py](../tools/scripts/mutating-file-watchdog.py) ([CTFTTOU-070](../tools/CTFTTOU-070.md))
- [ps / /proc](../tools/CTFTTOU-075.md)
- [inotify-tools](../tools/CTFTTOU-076.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/> (HFCTF 2025 "Tarpit Fall", flag-defender stage)
