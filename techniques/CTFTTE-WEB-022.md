# CTFTTE-WEB-022 — Public source-map bait

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-022`](../countertechniques/CTFTCTE-WEB-022.md) — Enumerate and triage source maps

---

## How the challenge author hides

Source maps are deliberately public and confirm thematic sections — terminal styles, hidden-file sections, reward animations — while leaking no logic, endpoint or data. The map invites deep source review that yields only vocabulary: structure is disclosed, substance is not.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1213 | Data from Information Repositories | Partial development metadata is exposed on purpose; the substantive logic stays private. |

## Tools

- curl
- browser devtools
- webcrack
- [wget](../tools/CTFTTOU-318.md)

## References

- <https://github.com/j4k0xb/webcrack>
- Add challenge write-up link
