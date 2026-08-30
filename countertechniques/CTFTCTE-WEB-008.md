# CTFTCTE-WEB-008 — Reconcile a disclosed short-name namespace

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-008`](../techniques/CTFTTE-WEB-008.md) — Legacy short-name namespace disclosure

---

## Offensive Recovery (CTF practitioner / solver)

Record the disclosed aliases, derive only bounded candidate names from the
declared challenge vocabulary, and mark unresolved aliases as uncertainty.

## Forensic / Blue-Team Perspective (DFIR analyst)

Document the compatibility setting, its exposed aliases, and whether the
deployment should disable legacy name generation or direct disclosure.

## Preconditions

- A lab observation or challenge artifact identifies the alias format.
- The candidate vocabulary is supplied by the challenge, not guessed from an
  external target.

## Indicators

- Legacy aliases expose a stable prefix and ordinal suffix.
- The application inventory contains an ambiguous matching resource family.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | 8.3 short-name disclosure echoes filesystem discovery. |

## References

- <https://learn.microsoft.com/windows/win32/fileio/naming-a-file>
