# CTFTTE-JAL-003 — Docker / container escape

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Paired counter-technique:** [`CTFTCTE-JAL-003`](../countertechniques/CTFTCTE-JAL-003.md) — Break out of the container to the host

---

## How the challenge author hides

The flag resides on the host filesystem; the player lands inside a container with a deliberate misconfiguration (privileged mode, exposed Docker socket, writable host mount, excessive Linux capability).

## ATT\&CK Complementarity

Complements T1611 (Escape to Host) with CTF-specific misconfiguration paths (e.g. `--privileged`, socket mount) that ATT&CK describes generically.

## Tools

- docker
- deepce
- amicontained

## References

- https://github.com/stealthcopter/deepce
- Add challenge write-up link
