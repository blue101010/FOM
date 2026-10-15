# CTFTCTE-IOT-002 — Enumerate the device web stack and abuse its backdoor endpoints

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-002`](../techniques/CTFTTE-IOT-002.md) — Device web-admin backdoor / default credential gate

---

## Offensive Recovery (CTF practitioner / solver)

1. Fingerprint the embedded server from banners and error pages (lighttpd, uhttpd, Goahead,
   BusyBox httpd); each has known debug/maintenance routes.
2. Map routes beyond the UI: content discovery with embedded-device wordlists
   (`cgi-bin/`, `debug`, `admin`, `api`, `factory`, `ota`), plus parameter fuzzing for
   magic switches.
3. Try the vendor's documented default credentials on the login; check the firmware image
   (IOT-001) for the exact credential if login resists.
4. Validate: the backdoor route or debug page yields the flag or the next stage.

## Forensic / Blue-Team Perspective (DFIR analyst)

Backdoor routes in embedded web stacks are a firmware-audit finding: diff each release's
CGI list against the UI's documented routes, and alert on any endpoint reachable without
authentication. CWE-912 and CWE-798 anchor the class.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Embedded web stacks ship backdoor and debug routes that never got removed. |

## Tools

- [nmap](../tools/CTFTTOU-033.md)
- [ffuf](../tools/CTFTTOU-013.md)
- curl ([CTFTTOU-038](../tools/CTFTTOU-038.md))

## References

- <https://cwe.mitre.org/data/definitions/912.html>
- Add challenge write-up link
