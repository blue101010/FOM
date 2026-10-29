# CTFTTE-OSI-010 — Word-address geocoding pivot

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-OSI`](../tactics/CTFT-TA-OSI.md) — OSINT  
> **Paired counter-technique:** [`CTFTCTE-OSI-010`](../countertechniques/CTFTCTE-OSI-010.md) — Resolve word addresses to locations and attribution

---

## How the challenge author hides

The location is encoded as a word address: three dictionary words drawn from a fixed,
versioned wordlist that resolve through a public geocoding service to a square of a few
metres. The words arrive as a cracked secret, a transmitted string or a challenge phrase,
and they look like a passphrase or a red herring — nothing in the string itself suggests
coordinates. Only resolving the words through the service reveals a physical location, and
the location is rarely the answer: it is the pivot into public records (a street address,
a facility, an organization) that holds the flag. Distinct from CTFTTE-OSI-004, where the
location must be deduced from imagery by visual reasoning, and from CTFTTE-OSI-001, where
it leaks through metadata fields.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1132 | Data Encoding | A word address is a reversible encoding of coordinates; ATT&CK has no geolocation technique, so the encoding anchor carries the pair. |
| T1589 | Gather Victim Identity Info | The resolved location feeds the same public-records pivot that identity gathering uses. |

## Tools

- [what3words](../tools/CTFTTOU-446.md)
- [Nominatim](../tools/CTFTTOU-418.md)
- [OpenStreetMap](../tools/CTFTTOU-324.md)

## Indicators

- a recovered secret or challenge string shaped `word.word.word` — three lowercase dictionary words, dot-separated
- challenge text about "three words", a location format, or an address with no coordinates anywhere
- the words resolve through a public word-address service to a specific square on the map
- the resolved street address is the pivot into public records or reporting about a facility or organization

## References

- <https://developer.what3words.com/>
- <https://nominatim.org/>
