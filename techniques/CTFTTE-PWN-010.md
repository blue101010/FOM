# CTFTTE-PWN-010 — Archive hierarchy-reconstruction path traversal

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Paired counter-technique:** [`CTFTCTE-PWN-010`](../countertechniques/CTFTCTE-PWN-010.md) — Craft sibling entries whose reconstructed parent path traverses

---

## How the challenge author hides

The extractor rebuilds a directory tree in memory from archive entries: each parsed entry is
attached to a previously seen node whose stored path matches the entry's parent directory,
and orphans are re-parented under the root. At write time it joins
`output + stored-parent-path + name` without sanitising the stored path. A single entry
carrying `../` looks harmless (it becomes a root child with a weird name), but a crafted
sibling pair — a directory entry `../../../root/.ssh` followed by a file entry whose parent
portion exactly matches that stored path — makes the tree hold a traversing parent path, so
the final join writes outside the extraction root with the privileged process's rights. The
archive passes naive "no absolute paths, no symlinks" validation and extracts without a
single error message.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Archive-extraction path traversal is the file-write analogue of an input-validation exploit. |

## Tools

- [tar-parent-traversal.py](../tools/scripts/tar-parent-traversal.py) ([CTFTTOU-069](../tools/CTFTTOU-069.md))
- [python tarfile](../tools/CTFTTOU-074.md)
- [ghidra](../tools/CTFTTOU-073.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/> (HFCTF 2025 "Tarpit Fall", unintended path)
- <https://cwe.mitre.org/data/definitions/22.html> (CWE-22: Improper Limitation of a Pathname to a Restricted Directory)
