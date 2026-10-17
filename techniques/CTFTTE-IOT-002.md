# CTFTTE-IOT-002 — Device web-admin backdoor / default credential gate

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-002`](../countertechniques/CTFTCTE-IOT-002.md) — Enumerate the device web stack and abuse its backdoor endpoints

---

## How the challenge author hides

The device exposes an embedded web stack (lighttpd/uhttpd/Goahead CGI, BusyBox httpd) with a
hidden admin route, a magic parameter, or a login that accepts a default credential the UI
never mentions. The flag sits behind the backdoor endpoint or a hidden debug page; the
concealment is the assumption that players will only interact with the visible interface and
never map the embedded server's routes.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1190 | Exploit Public-Facing Application | Embedded web stacks ship backdoor and debug routes that never got removed. |

## Tools

- [nmap](../tools/CTFTTOU-033.md)
- [ffuf](../tools/CTFTTOU-013.md)
- [curl](../tools/CTFTTOU-038.md)

## References

- <https://cwe.mitre.org/data/definitions/912.html> (CWE-912: Hidden Functionality)
- Add challenge write-up link
