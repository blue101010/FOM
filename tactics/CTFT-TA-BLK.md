# BLK — Blockchain

> **Domain ID:** `CTFT-TA-BLK`  
> **HTB mapping:** HTB: Blockchain  
> **Techniques:** 5

## Description

On-chain/contract concealment and EVM-level recovery.

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
| [CTFTTE-BLK-001](../techniques/CTFTTE-BLK-001.md) | Private storage-variable concealment | [CTFTCTE-BLK-001](../countertechniques/CTFTCTE-BLK-001.md) | Read contract storage slots directly | T1213 |
| [CTFTTE-BLK-002](../techniques/CTFTTE-BLK-002.md) | Reentrancy-gated flag | [CTFTCTE-BLK-002](../countertechniques/CTFTCTE-BLK-002.md) | Exploit reentrancy to set the flag | T1190 |
| [CTFTTE-BLK-003](../techniques/CTFTTE-BLK-003.md) | Unverified-bytecode logic hiding | [CTFTCTE-BLK-003](../countertechniques/CTFTCTE-BLK-003.md) | Decompile EVM bytecode | T1140 |
| [CTFTTE-BLK-004](../techniques/CTFTTE-BLK-004.md) | Hidden event-log / calldata concealment | [CTFTCTE-BLK-004](../countertechniques/CTFTCTE-BLK-004.md) | Parse transaction logs and calldata | T1213 |
| [CTFTTE-BLK-005](../techniques/CTFTTE-BLK-005.md) | Access-control flaw to set flag | [CTFTCTE-BLK-005](../countertechniques/CTFTCTE-BLK-005.md) | Craft a transaction abusing missing checks | T1548 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
