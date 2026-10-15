# CTFTTE-ICS-008 — Industrial firewall weak credential behind a controller pivot

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-ICS`](../tactics/CTFT-TA-ICS.md) — ICS / SCADA  
> **Paired counter-technique:** [`CTFTCTE-ICS-008`](../countertechniques/CTFTCTE-ICS-008.md) — Pivot through the controller and brute-force the firewall manager

---

## How the challenge author hides

The industrial firewall guarding the next flag is unreachable from the player
network; only the already-compromised controller can reach it. Its web manager
sits behind that pivot with a weak administrative password that happens to be
in every public wordlist, so the stage is a tunnel-plus-brute-force exercise.

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
