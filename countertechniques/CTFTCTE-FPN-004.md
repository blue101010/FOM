# CTFTCTE-FPN-004 — Chain service misconfig and container escape to host

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Counters technique:** [`CTFTTE-FPN-004`](../techniques/CTFTTE-FPN-004.md) — Container / service misconfiguration chain

---

## Offensive Recovery (CTF practitioner / solver)

Exploit the exposed service (weak credentials, SSRF, command injection) to gain container-level execution, then apply the appropriate container-escape technique (privileged mode, socket mount, writable host path) to reach the host flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

The two-stage chain documents a defence-in-depth failure: neither the service hardening nor the container isolation was sufficient alone; both must be remediated together to close the attack path.

## Tools

- docker / kubectl
- deepce
- curl / httpie

## References

- https://github.com/stealthcopter/deepce
- Add challenge write-up link
