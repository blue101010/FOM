# BLK — Blockchain

> **Tactic ID:** `CTFT-TA-BLK`  
> **HTB mapping:** HTB: Blockchain  
> **Techniques:** 5

## Description

On-chain/contract concealment and EVM-level recovery.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-BLK-001](../techniques/CTFTTE-BLK-001.md) | Private storage-variable concealment | [CTFTCTE-BLK-001](../countertechniques/CTFTCTE-BLK-001.md) | Read contract storage slots directly | No ATT&CK equivalent |
| [CTFTTE-BLK-002](../techniques/CTFTTE-BLK-002.md) | Reentrancy-gated flag | [CTFTCTE-BLK-002](../countertechniques/CTFTCTE-BLK-002.md) | Exploit reentrancy to set the flag | No ATT&CK equivalent. |
| [CTFTTE-BLK-003](../techniques/CTFTTE-BLK-003.md) | Unverified-bytecode logic hiding | [CTFTCTE-BLK-003](../countertechniques/CTFTCTE-BLK-003.md) | Decompile EVM bytecode | No ATT&CK equivalent. |
| [CTFTTE-BLK-004](../techniques/CTFTTE-BLK-004.md) | Hidden event-log / calldata concealment | [CTFTCTE-BLK-004](../countertechniques/CTFTCTE-BLK-004.md) | Parse transaction logs and calldata | No ATT&CK equivalent. |
| [CTFTTE-BLK-005](../techniques/CTFTTE-BLK-005.md) | Access-control flaw to set flag | [CTFTCTE-BLK-005](../countertechniques/CTFTCTE-BLK-005.md) | Craft a transaction abusing missing checks | No ATT&CK equivalent. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
