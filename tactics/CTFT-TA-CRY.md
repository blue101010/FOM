# CRY — Cryptography

> **Tactic ID:** `CTFT-TA-CRY`  
> **HTB mapping:** HTB: Crypto  
> **Techniques:** 6

## Description

Deliberately weakened or layered crypto and its cryptanalysis.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-CRY-001](../techniques/CTFTTE-CRY-001.md) | Weak RSA parameter design | [CTFTCTE-CRY-001](../countertechniques/CTFTCTE-CRY-001.md) | Recover the RSA private key from weak parameters | No ATT&CK equivalent |
| [CTFTTE-CRY-002](../techniques/CTFTTE-CRY-002.md) | Classical cipher layering | [CTFTCTE-CRY-002](../countertechniques/CTFTCTE-CRY-002.md) | Break layered classical ciphers | No ATT&CK equivalent. |
| [CTFTTE-CRY-003](../techniques/CTFTTE-CRY-003.md) | Repeating-key XOR / ECB pattern | [CTFTCTE-CRY-003](../countertechniques/CTFTCTE-CRY-003.md) | Exploit key reuse and block-mode patterns | No ATT&CK equivalent. |
| [CTFTTE-CRY-004](../techniques/CTFTTE-CRY-004.md) | Predictable PRNG / nonce reuse | [CTFTCTE-CRY-004](../countertechniques/CTFTCTE-CRY-004.md) | Reconstruct keys from broken randomness | No ATT&CK equivalent. |
| [CTFTTE-CRY-005](../techniques/CTFTTE-CRY-005.md) | Hash length-extension exposure | [CTFTCTE-CRY-005](../countertechniques/CTFTCTE-CRY-005.md) | Forge data via length extension | No ATT&CK equivalent. |
| [CTFTTE-CRY-006](../techniques/CTFTTE-CRY-006.md) | Nested encoding obfuscation | [CTFTCTE-CRY-006](../countertechniques/CTFTCTE-CRY-006.md) | Unwrap chained encodings | No ATT&CK equivalent. |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
