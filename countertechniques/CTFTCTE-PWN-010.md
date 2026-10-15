# CTFTCTE-PWN-010 — Craft sibling entries whose reconstructed parent path traverses

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-PWN`](../tactics/CTFT-TA-PWN.md) — Binary Exploitation  
> **Counters technique:** [`CTFTTE-PWN-010`](../techniques/CTFTTE-PWN-010.md) — Archive hierarchy-reconstruction path traversal

---

## Offensive Recovery (CTF practitioner / solver)

1. Reverse (or read, if source is recoverable) the parser's parenting rule: which stored
   node path must a later entry's parent portion match for the child to attach to it.
2. Craft a sibling pair per target file: first a directory entry whose path is
   `<traversal-prefix><target-dir>`, then a file entry whose path is
   `<traversal-prefix><target-dir>/<name>`. The traversal prefix must absorb the output
   folder depth (e.g. `../../../root/.ssh` then `../../../root/.ssh/authorized_keys`
   for a one-level `extracted` folder).
3. Extract with the privileged tool and verify the write landed outside the output root;
   then aim the pair at a privileged target (`authorized_keys`, cron files, a SUID
   launcher).
4. Count the `../` components from the observed write location — an off-by-one prefix
   fails silently inside the extraction folder.

## Forensic / Blue-Team Perspective (DFIR analyst)

Extraction traversal leaves a signature: an archive entry set whose first path components
are all `..`, and files materialising outside the extraction directory with the service's
owner. Detection: flag any archive containing entries with parent components that normalize
above the extraction root before writing.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Archive-extraction path traversal is the file-write analogue of an input-validation exploit. |

## Tools

- [tar-parent-traversal.py](../tools/scripts/tar-parent-traversal.py) ([CTFTTOU-069](../tools/CTFTTOU-069.md))
- [python tarfile](../tools/CTFTTOU-074.md)
- [ghidra](../tools/CTFTTOU-073.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/>
