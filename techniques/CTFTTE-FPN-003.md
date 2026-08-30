# CTFTTE-FPN-003 — Multi-hop network pivot

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-003`](../countertechniques/CTFTCTE-FPN-003.md) — Tunnel through compromised hosts to reach the flag

---

## How the challenge author hides

The flag host sits on a network segment not directly reachable from the attacker; reaching it requires traversing one or more intermediate compromised hosts via tunnelling or proxying.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1572 | Protocol Tunneling | Pivot tunnels. |
| T1090 | Proxy | Pivot relays. |

## Tools

- chisel
- proxychains-ng
- socat
- ssh -D / -L / -R

## References

- https://github.com/jpillora/chisel
- Add challenge write-up link
