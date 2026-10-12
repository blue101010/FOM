# CTFTCTE-WEB-019 — Timeboxed deobfuscation triage

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-019`](../techniques/CTFTTE-WEB-019.md) — Decoy obfuscated asset / empty-safe lure

---

## Offensive Recovery (CTF practitioner / solver)

Pipeline per asset: hash, size and provenance; grep for URLs, Web APIs and high-entropy strings; fetch the source map when referenced; run webcrack; scan the formatted AST for fetch/XHR/WebSocket/import/storage/crypto/DOM side effects. Promote the asset only on a page-specific or observable effect; otherwise close it within a bounded budget — obfuscation alone earns no deep-RE time.

## Forensic / Blue-Team Perspective (DFIR analyst)

Decoy assets inflate analyst time; timeboxing and side-effect evidence are the defences against investigation burnout.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The recovery decides when deobfuscation is worth the effort. |

## Tools

- webcrack
- ripgrep
- browser devtools

## References

- <https://github.com/j4k0xb/webcrack>
- Add challenge write-up link
