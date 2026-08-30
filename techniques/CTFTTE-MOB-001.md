# CTFTTE-MOB-001 — Hardcoded secrets in app resources

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-MOB`](../tactics/CTFT-TA-MOB.md) — Mobile  
> **Paired counter-technique:** [`CTFTCTE-MOB-001`](../countertechniques/CTFTCTE-MOB-001.md) — Decompile the APK and extract secrets

---

## How the challenge author hides

Keys/flags are embedded in resources, strings, or smali rather than fetched at runtime.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552.001 | Credentials in Files | APK resource secrets. |

## Tools

- jadx
- apktool
- strings

## References

- https://github.com/skylot/jadx
- Add challenge write-up link