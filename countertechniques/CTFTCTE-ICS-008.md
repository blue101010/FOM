# CTFTCTE-ICS-008 — Pivot through the controller and brute-force the firewall manager

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Counters technique:** [`CTFTTE-ICS-008`](../techniques/CTFTTE-ICS-008.md) — Industrial firewall weak credential behind a controller pivot

---

## Offensive Recovery (CTF practitioner / solver)

Open an SSH tunnel from the compromised controller to the firewall's
management port, then brute force the web login with a public wordlist and the
obvious administrative usernames. Once authenticated, alter the firewall rules
to admit the player network and retrieve the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

Management interfaces should never sit on the production path with weak or
default credentials. Log failed logons, alert on rule changes, and keep the
management plane separate from the data plane so a single controller
compromise cannot pivot into the firewall.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T0859 | Valid Accounts | The firewall admin account falls to a wordlist attack. |
| T0886 | Remote Services | The controller pivot exposes the remote management service. |

## Tools

- [openssh client](../tools/CTFTTOU-058.md)
- [python](../tools/CTFTTOU-050.md)
- [rockyou](../tools/CTFTTOU-061.md)

## References

- <https://youllou.com/writeups/hackfest_2025/operation_shutdown>
