# CTFTTE-WEB-019 — Decoy obfuscated asset / empty-safe lure

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-WEB`](../tactics/CTFT-TA-WEB.md) — Web Exploitation  
> **Paired counter-technique:** [`CTFTCTE-WEB-019`](../countertechniques/CTFTCTE-WEB-019.md) — Timeboxed deobfuscation triage

---

## How the challenge author hides

A prominent asset is deliberately obfuscated (string-array rotation, control-flow flattening, console neutralization — the typical `javascript-obfuscator` signature) so it looks like the payload, while containing no host, no secret and no network side effect. Decorative "hint" commands on the page reinforce the lure. The asset is an empty safe: the obfuscation is the decoy, not the protection.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Here obfuscation serves distraction, not payload concealment — a CTF-specific inversion. |

## Tools

- webcrack
- ripgrep
- browser devtools

## References

- <https://github.com/j4k0xb/webcrack>
- Add challenge write-up link
