# CTFTCTE-CLD-005 — Pull and inspect image layers

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-CLD`](../tactics/CTFT-TA-CLD.md) — Cloud  
> **Counters technique:** [`CTFTTE-CLD-005`](../techniques/CTFTTE-CLD-005.md) — Container image / registry leak

---

## Offensive Recovery (CTF practitioner / solver)

Pull the image and inspect layer history/filesystem for the artifact.

## Forensic / Blue-Team Perspective (DFIR analyst)

Layer diffing reveals files and history entries containing the secret.

## Tools

- docker
- dive
- skopeo

## References

- https://github.com/wagoodman/dive
- Add challenge write-up link