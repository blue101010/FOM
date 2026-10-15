# CTFTTE-REV-010 — Retained build-path symbol-to-source anchor

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-REV`](../tactics/CTFT-TA-REV.md) — Reverse Engineering  
> **Paired counter-technique:** [`CTFTCTE-REV-010`](../countertechniques/CTFTCTE-REV-010.md) — Pivot from binary symbols to upstream source and diff the challenge branch

---

## How the challenge author hides

A Go (or Rust/Java) binary keeps full package paths in its symbol table and pclntab even
when the challenge ships no source: decompiled frames read
`github.com/<user>/<repo>/cmd.Execute()`. The author effectively publishes the challenge's
own source — the upstream repo, sometimes with a dedicated branch (`ctf-challenge`) holding
only the introduced flaw. The concealment relies on players grinding the decompilation
instead of correlating binary symbols with public code hosts; a five-minute strings pass
collapses the whole RE stage into a branch diff.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1596.003 | Search Open Technical Databases: Code Repositories | Retained build paths turn the binary itself into a pointer at a public code repository. |

## Tools

- [gosym2src.py](../tools/scripts/gosym2src.py) ([CTFTTOU-072](../tools/CTFTTOU-072.md))
- strings / grep
- [ghidra](../tools/CTFTTOU-073.md)

## References

- <https://blog.linkster78.dev/posts/hfctf25-tarpit-fall/> (HFCTF 2025 "Tarpit Fall", guntar → github.com/franciscolkdo/guntar)
- <https://go.dev/doc/install/source> (why Go builds retain package paths)
