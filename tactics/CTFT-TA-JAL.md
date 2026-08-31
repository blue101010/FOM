# JAL — Jail / Sandbox Escape

> **Domain ID:** `CTFT-TA-JAL`  
> **HTB mapping:** HTB: Misc (Jail)  
> **Techniques:** 6

## Description

Challenges where the author constructs a restricted execution environment — a language-level sandbox, a limited shell, or an OS/kernel isolation boundary — to prevent direct flag access. Solvers must find a path out of the confinement.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-JAL-001](../techniques/CTFTTE-JAL-001.md) | Python jail (pyjail) confinement | [CTFTCTE-JAL-001](../countertechniques/CTFTCTE-JAL-001.md) | Escape the Python sandbox | T1059.006 |
| [CTFTTE-JAL-002](../techniques/CTFTTE-JAL-002.md) | Restricted-shell confinement | [CTFTCTE-JAL-002](../countertechniques/CTFTCTE-JAL-002.md) | Escape the restricted shell | T1059 |
| [CTFTTE-JAL-003](../techniques/CTFTTE-JAL-003.md) | Docker / container escape | [CTFTCTE-JAL-003](../countertechniques/CTFTCTE-JAL-003.md) | Break out of the container to the host | T1611 |
| [CTFTTE-JAL-004](../techniques/CTFTTE-JAL-004.md) | JavaScript browser-sandbox jail | [CTFTCTE-JAL-004](../countertechniques/CTFTCTE-JAL-004.md) | Traverse the prototype chain to escape | T1059.007 |
| [CTFTTE-JAL-005](../techniques/CTFTTE-JAL-005.md) | Seccomp / AppArmor policy confinement | [CTFTCTE-JAL-005](../countertechniques/CTFTCTE-JAL-005.md) | Identify allowed syscalls and pivot around the filter | T1055 |
| [CTFTTE-JAL-006](../techniques/CTFTTE-JAL-006.md) | WSL-interop sandbox escape | [CTFTCTE-JAL-006](../countertechniques/CTFTCTE-JAL-006.md) | Escape WSL-interop boundaries | T1611 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
