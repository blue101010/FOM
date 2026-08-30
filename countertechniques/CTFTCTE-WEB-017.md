# CTFTCTE-WEB-017 — Fuzz vhosts and host headers

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Counters technique:** [`CTFTTE-WEB-017`](../techniques/CTFTTE-WEB-017.md) — Host-header / vhost fuzzing

---

## Offensive Recovery (CTF practitioner / solver)

Fuzz Host headers and vhost names (ffuf/gobuster) and reach the hidden vhost.

## Forensic / Blue-Team Perspective (DFIR analyst)

Vhost discovery correlates TLS SNI and Host headers in proxy logs.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1083 | File and Directory Discovery | Vhost / host-header discovery. |

## Tools

- ffuf
- gobuster
- Burp Intruder

## References

- <https://github.com/ffuf/ffuf>

