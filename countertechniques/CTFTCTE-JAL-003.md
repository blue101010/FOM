# CTFTCTE-JAL-003 — Break out of the container to the host

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-JAL`](../tactics/CTFT-TA-JAL.md) — Jail / Sandbox Escape  
> **Counters technique:** [`CTFTTE-JAL-003`](../techniques/CTFTTE-JAL-003.md) — Docker / container escape

---

## Offensive Recovery (CTF practitioner / solver)

Enumerate container capabilities with `amicontained`; if `--privileged`, mount the host filesystem or load a kernel module. If the Docker socket is mounted, use it to spin up a new container with a host-root bind-mount. If a writable host path is mounted, write an SUID binary or modify a cron job.

## Forensic / Blue-Team Perspective (DFIR analyst)

The escape documents a deliberate misconfiguration (excessive capability, exposed socket, writable mount); in production, containers should run with the minimum capability set and no host socket exposure.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1611 | Escape to Host | Container escape paths ATT&CK describes generically. |

## Tools

- docker
- deepce
- amicontained

## References

- https://github.com/stealthcopter/deepce
- Add challenge write-up link
