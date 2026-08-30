# CTFTCTE-FPN-003 — Tunnel through compromised hosts to reach the flag

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-003`](../techniques/CTFTTE-FPN-003.md) — Multi-hop network pivot

---

## Offensive Recovery (CTF practitioner / solver)

Deploy a lightweight SOCKS5 tunnel (chisel server/client) or SSH dynamic-forward through each compromised host; chain proxychains to route all tool traffic through the tunnel stack until the flag host is reachable.

## Forensic / Blue-Team Perspective (DFIR analyst)

Pivot tunnels leave characteristic artefacts: unexpected outbound SOCKS connections, chisel/socat processes, and unusual SSH port-forwarding entries in auth logs; network segmentation and egress filtering limit the blast radius.

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

- <https://github.com/jpillora/chisel>
- Add challenge write-up link
