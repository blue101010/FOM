# CTFTTE-FOR-024 — Browser-profile artifact concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-024`](../countertechniques/CTFTCTE-FOR-024.md) — Parse Firefox/SQLite artifacts (places, logins, cookies)

---

## How the challenge author hides

The flag is inside a browser profile: bookmarks, history, saved logins, cookies or localStorage.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1217 | Browser Information Discovery | Browser artifact mining; CTFT adds profile-parsing detail. |

## Tools

- sqlite3
- sqlitebrowser
- firefox_decrypt

## References

- https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data
- Add challenge write-up link
