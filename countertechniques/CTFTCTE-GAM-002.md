# CTFTCTE-GAM-002 — Hex-edit the save file or patch in-memory values

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-GAM`](../tactics/CTFT-TA-GAM.md) — Game / Protocol Automation (GamePwn)  
> **Counters technique:** [`CTFTTE-GAM-002`](../techniques/CTFTTE-GAM-002.md) — Game save-state / memory manipulation

---

## Offensive Recovery (CTF practitioner / solver)

Parse the save-file format (often a binary blob or JSON), locate the target field (score, item count, unlock flag), and overwrite it to the winning value — or use Cheat Engine to find and patch the live in-memory representation.

## Forensic / Blue-Team Perspective (DFIR analyst)

Save-file tampering demonstrates that any client-side state is untrusted; authoritative games must validate all game-state server-side or use cryptographically signed save files.

## Tools

- Cheat Engine
- python struct
- hex editors (HxD / 010 Editor)

## References

- Add challenge write-up link
