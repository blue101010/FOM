# CTFTCTE-OSI-010 — Resolve word addresses to locations and attribution

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Counters technique:** [`CTFTTE-OSI-010`](../techniques/CTFTTE-OSI-010.md) — Word-address geocoding pivot

---

## Offensive Recovery (CTF practitioner / solver)

1. Recognize the shape: three lowercase dictionary words, dot-separated, surfacing as a
   cracked secret, a transmitted string or a phrase in the challenge text.
2. Resolve the words through the word-address geocoding service (web UI or API) to
   coordinates and a country. If the service rejects the words, try the other supported
   languages — the wordlists differ per language.
3. Reverse-geocode the coordinates to a street address with Nominatim/OpenStreetMap.
4. Pivot the address into public records and reporting: facility, organization, unit or
   entity associated with that location. The answer is usually the attribution, not the
   coordinates.
5. Verify the attribution with at least two independent sources before submitting.

## Forensic / Blue-Team Perspective (DFIR analyst)

A word-address pivot is attribution support: document each resolution step (service,
language, date) because the wordlists are versioned and a later resolution can shift.
Geolocation of a subject's location reference feeds the same reporting chain as imagery
geolocation, with the added caveat that the encoding is exact — a resolved square is
evidence of the *reference*, not proof the subject was there.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1132 | Data Encoding | Recovery reverses the word encoding to coordinates before any location work starts. |
| T1589 | Gather Victim Identity Info | The resolved location feeds the public-records identity pivot. |

## Tools

- [what3words](../tools/CTFTTOU-446.md)
- [Nominatim](../tools/CTFTTOU-418.md)
- [OpenStreetMap](../tools/CTFTTOU-324.md)

## References

- <https://developer.what3words.com/>
- <https://nominatim.org/>
