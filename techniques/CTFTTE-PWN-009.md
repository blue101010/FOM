# CTFTTE-PWN-009 — Fixed-name output symlink redirect

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-009`](../countertechniques/CTFTCTE-PWN-009.md) — Pre-plant a symlink over a privileged fixed-name output path

---

## How the challenge author hides

A privileged helper (SUID binary, root-owned service) writes its results to a hard-coded,
predictable relative path such as `./extracted`, created relative to the caller's current
working directory. The bug is not a memory corruption but a filesystem redirect: any user can
pre-plant a symlink with that fixed name pointing anywhere on the filesystem, and the
privileged process follows it when creating the directory or writing files through it. The
flag is never reachable directly — the player is steered toward reverse-engineering the
binary while the actual win condition is a two-line symlink plus a crafted archive.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1222.002 | File and Directory Permissions Modification: Linux and Mac | The privileged write follows an attacker-planted symlink into protected paths. |

## Tools

- [tar-symlink-redirect.py](../tools/scripts/tar-symlink-redirect.py) ([CTFTTOU-068](../tools/CTFTTOU-068.md))
- ln / os.symlink
- [ghidra](../tools/CTFTTOU-073.md) (locate the fixed output-folder constant)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/> (HFCTF 2025 "Tarpit Fall", intended path)
- <https://cwe.mitre.org/data/definitions/59.html> (CWE-59: Improper Link Resolution Before File Access)
