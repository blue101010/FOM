# CTFTCTE-FOR-030 — Detect, stop and snapshot a read-triggered mutator

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-030`](../techniques/CTFTTE-FOR-030.md) — Read-triggered payload mutation (guardian process)

---

## Offensive Recovery (CTF practitioner / solver)

1. Read the file twice with no other access in between; diff the two reads. Growth or
   change on identical reads proves a mutator — do not waste re-provisionings on decoding.
2. Find the guardian: process inventory (`ps auxww`), open handles (`/proc/*/fd` pointing at
   the file or its directory), and inotify/fanotify watchers (`/proc/*/fdinfo`).
3. Terminate the guardian (as root if needed) and immediately snapshot the file to a
   timestamped copy outside its watch path.
4. Treat the last-written state as the stable ciphertext and move to key recovery —
   the mutation often re-encrypts with a time-derived key, so the file's mtime is the
   next lead (see [`CTFTCTE-CRY-014`](CTFTCTE-CRY-014.md)).

## Forensic / Blue-Team Perspective (DFIR analyst)

Guardian daemons are an anti-forensic control also seen in the wild as watchdog-driven
timestomping and self-wiping logs. Analysts preserve evidence with out-of-band imaging
(memory first, then block-level copy) rather than live reads, and hunt for the watcher by
correlating file mtime updates with unrelated process activity.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1070 | Indicator Removal on Host | The artifact is altered at the moment of access so each observation destroys the previous state. |

## Tools

- [mutating-file-watchdog.py](../tools/scripts/mutating-file-watchdog.py) ([CTFTTOU-070](../tools/CTFTTOU-070.md))
- [mtime-xor-recover.py](../tools/scripts/mtime-xor-recover.py) ([CTFTTOU-071](../tools/CTFTTOU-071.md))
- [ps / /proc](../tools/CTFTTOU-075.md)
- [inotify-tools](../tools/CTFTTOU-076.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/>
