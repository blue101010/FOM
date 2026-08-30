# CTFTTE-NET-005 — Traffic tunnel / port-forwarding relay

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Paired counter-technique:** [`CTFTCTE-NET-005`](../countertechniques/CTFTCTE-NET-005.md) — Pivot via ssh -L/-R, chisel

---

## How the challenge author hides

The flag service is only reachable through a pivot host; direct connections fail.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1572 | Protocol Tunneling | Tunnel establishment mirrors protocol tunneling. |
| T1090 | Proxy | Relay usage echoes proxy pivoting. |

## Tools

- ssh
- chisel
- socat
- proxychains

## References

- https://github.com/jpillora/chisel
- Add challenge write-up link
