# CTFTCTE-MOB-001 — Decompile the APK and extract secrets

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Counters technique:** [`CTFTTE-MOB-001`](../techniques/CTFTTE-MOB-001.md) — Hardcoded secrets in app resources

---

## Offensive Recovery (CTF practitioner / solver)

Decompile to Java/smali and grep resources/strings for the secret.

## Forensic / Blue-Team Perspective (DFIR analyst)

Static review of the package documents secrets shipped inside the artifact.

## Tools

- jadx
- apktool
- strings

## References

- https://github.com/skylot/jadx
- Add challenge write-up link