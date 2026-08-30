# CTFTCTE-NET-005 — Pivot via ssh -L/-R, chisel

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-NET`](../tactics/CTFT-TA-NET.md) — Network  
> **Counters technique:** [`CTFTTE-NET-005`](../techniques/CTFTTE-NET-005.md) — Traffic tunnel / port-forwarding relay

---

## Offensive Recovery (CTF practitioner / solver)

Relay traffic through the pivot (ssh -L/-R, chisel, socat) and reach the internal service.

## Forensic / Blue-Team Perspective (DFIR analyst)

Tunnel artifacts appear as long-lived SSH/chisel sessions in logs; defenders track them as pivot-chain evidence.

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

- <https://github.com/jpillora/chisel>

