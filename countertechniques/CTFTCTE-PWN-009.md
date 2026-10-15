# CTFTCTE-PWN-009 — Pre-plant a symlink over a privileged fixed-name output path

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-009`](../techniques/CTFTTE-PWN-009.md) — Fixed-name output symlink redirect

---

## Offensive Recovery (CTF practitioner / solver)

1. Inventory every fixed path the privileged binary writes to (strings, Ghidra, or a
   quick `strace -f` run): default output folders, config paths, temp names.
2. From a writable directory, pre-plant a symlink with that exact name pointing at the
   target you cannot write to directly (classic target: `/root/.ssh` to land an
   `authorized_keys`).
3. Feed the tool an input that makes it write a payload file through the symlink
   (for an archive extractor: a tar whose root entry is `authorized_keys` with your
   public key).
4. Verify with a low-privilege test write first; keep a second payload entry in the
   archive in case ordering matters.

## Forensic / Blue-Team Perspective (DFIR analyst)

Symlink-redirect abuse leaves durable evidence: an `authorized_keys` materializing in a
root-owned directory with a creation time matching a service start, plus auditd/audit
`SYMLINK` and `CREATE` events naming the unprivileged invoking user. Blue teams detect the
pattern by alerting on privileged processes writing through symlinks owned by other UIDs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1222.002 | File and Directory Permissions Modification: Linux and Mac | The privileged write follows an attacker-planted symlink into protected paths. |

## Tools

- [tar-symlink-redirect.py](../tools/scripts/tar-symlink-redirect.py) ([CTFTTOU-068](../tools/CTFTTOU-068.md))
- strace
- [ghidra](../tools/CTFTTOU-073.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/>
