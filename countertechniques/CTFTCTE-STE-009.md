# CTFTCTE-STE-009 — Recursively inspect nested metadata containers

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-009`](../techniques/CTFTTE-STE-009.md) — Nested metadata-container embedding

---

## Offensive Recovery (CTF practitioner / solver)

Extract metadata from the supplied artifact and each declared embedded container,
preserving the parent-child relation and checking whether a recovered value
advances the challenge.

## Forensic / Blue-Team Perspective (DFIR analyst)

Treat nested metadata as an artifact graph: retain container provenance, parser
version and extraction result so an apparent clue can be reproduced or rejected.

## Preconditions

- The artifact and any extracted child containers remain read-only inputs.
- Each recursion level has a bounded depth and a recorded parent identifier.

## Indicators

- Embedded preview, attachment, or sidecar metadata is present.
- Top-level metadata references a nested object or inconsistent authoring data.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Nested metadata containers. |

## Tools

- ExifTool
- [CTFTTOU-006](../tools/CTFTTOU-006.md)

## References

- <https://exiftool.org/>