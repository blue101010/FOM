# CTFTCTE-FOR-024 — Parse Firefox/SQLite artifacts (places, logins, cookies)

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-024`](../techniques/CTFTTE-FOR-024.md) — Browser-profile artifact concealment

---

## Offensive Recovery (CTF practitioner / solver)

Open the profile's SQLite databases (places.sqlite, logins.json, cookies) and extract the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Browser artifacts are first-class DFIR evidence; parsing must preserve WAL/uncommitted rows.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1217 | Browser Information Discovery | Browser artifact mining; CTFT adds profile-parsing detail. |

## Tools

- sqlite3
- sqlitebrowser
- firefox_decrypt

## References

- <https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data>

