# CTFTCTE-REV-010 — Pivot from binary symbols to upstream source and diff the challenge branch

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Counters technique:** [`CTFTTE-REV-010`](../techniques/CTFTTE-REV-010.md) — Retained build-path symbol-to-source anchor

---

## Offensive Recovery (CTF practitioner / solver)

1. In the decompiler (or a plain `strings` pass), collect full package paths:
   `github.com/<user>/<repo>/...` from function names, build IDs and error strings.
2. Search the code host for the repo; clone it and list all branches — challenge builds
   frequently live on a `ctf-challenge`-style branch.
3. Diff the challenge branch against the default branch; the delta is the planted flaw
   (an added output folder, a dropped validation, an extra handler).
4. Review the diff as code instead of asm, but keep the binary as ground truth: the
   deployed build may lag the branch.

## Forensic / Blue-Team Perspective (DFIR analyst)

Build-path leakage is a real-world attribution vector: malware compiled from Go/Rust
discloses developer module paths, internal repo names and sometimes CI user names.
Analysts use the same symbol-to-repository pivot for clustering samples and identifying
supply-chain provenance.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1596.003 | Search Open Technical Databases: Code Repositories | Retained build paths turn the binary itself into a pointer at a public code repository. |

## Tools

- [gosym2src.py](../tools/scripts/gosym2src.py) ([CTFTTOU-072](../tools/CTFTTOU-072.md))
- strings / grep
- [ghidra](../tools/CTFTTOU-073.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/>
