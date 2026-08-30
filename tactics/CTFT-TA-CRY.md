# CRY — Cryptography

> **Tactic ID:** `CTFT-TA-CRY`  
> **HTB mapping:** HTB: Crypto  
> **Techniques:** 13

## Description

Deliberately weakened or layered crypto and its cryptanalysis.

## Relation to MITRE ATT&CK

CTFT tactics are a CTF-specific layer that *complements* MITRE ATT&CK. ATT&CK
models real adversary behaviour at the campaign level; CTFT models the
challenge-craft (forensic, cryptographic, steganographic and puzzle) detail
that ATT&CK intentionally leaves out, and that CTF solvers and DFIR analysts
rely on. CTFT never re-labels an existing ATT&CK technique.

> Per-entry related ATT&CK IDs are rendered on every technique and
> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).


## Techniques ↔ Counter-techniques

| Technique | Hide / Design name | Counter-technique | Counter name | ATT&CK note (excerpt) |
| --- | --- | --- | --- | --- |
| [CTFTTE-CRY-001](../techniques/CTFTTE-CRY-001.md) | Weak RSA parameter design | [CTFTCTE-CRY-001](../countertechniques/CTFTCTE-CRY-001.md) | Recover the RSA private key from weak parameters | No ATT&CK equivalent |
| [CTFTTE-CRY-002](../techniques/CTFTTE-CRY-002.md) | Classical cipher layering | [CTFTCTE-CRY-002](../countertechniques/CTFTCTE-CRY-002.md) | Break layered classical ciphers | No ATT&CK equivalent. |
| [CTFTTE-CRY-003](../techniques/CTFTTE-CRY-003.md) | Repeating-key XOR / ECB pattern | [CTFTCTE-CRY-003](../countertechniques/CTFTCTE-CRY-003.md) | Exploit key reuse and block-mode patterns | No ATT&CK equivalent. |
| [CTFTTE-CRY-004](../techniques/CTFTTE-CRY-004.md) | Nonce reuse in cryptographic operations | [CTFTCTE-CRY-004](../countertechniques/CTFTCTE-CRY-004.md) | Assess nonce reuse and its cryptographic consequence | No ATT&CK equivalent. |
| [CTFTTE-CRY-005](../techniques/CTFTTE-CRY-005.md) | Hash length-extension exposure | [CTFTCTE-CRY-005](../countertechniques/CTFTCTE-CRY-005.md) | Forge data via length extension | No ATT&CK equivalent. |
| [CTFTTE-CRY-006](../techniques/CTFTTE-CRY-006.md) | Nested encoding obfuscation | [CTFTCTE-CRY-006](../countertechniques/CTFTCTE-CRY-006.md) | Unwrap chained encodings | No ATT&CK equivalent. |
| [CTFTTE-CRY-007](../techniques/CTFTTE-CRY-007.md) | Deliberately predictable stateful pseudo-random generator | [CTFTCTE-CRY-007](../countertechniques/CTFTCTE-CRY-007.md) | Assess and predict recoverable PRNG state | No ATT&CK equivalent. |
| [CTFTTE-CRY-008](../techniques/CTFTTE-CRY-008.md) | Block-cipher mode / AES implementation weakness | [CTFTCTE-CRY-008](../countertechniques/CTFTCTE-CRY-008.md) | Attack AES modes (padding oracle, IV flaws) | T1573.001 |
| [CTFTTE-CRY-009](../techniques/CTFTTE-CRY-009.md) | Stream-cipher keystream reuse (Salsa20) | [CTFTCTE-CRY-009](../countertechniques/CTFTCTE-CRY-009.md) | Exploit keystream reuse to recover plaintext | T1573.001 |
| [CTFTTE-CRY-010](../techniques/CTFTTE-CRY-010.md) | Certificate / PEM / ASN.1 field hiding | [CTFTCTE-CRY-010](../countertechniques/CTFTCTE-CRY-010.md) | Parse certificates and extract hidden fields | T1552.001 |
| [CTFTTE-CRY-011](../techniques/CTFTTE-CRY-011.md) | Protocol implementation flaw (Heartbleed-style) | [CTFTCTE-CRY-011](../countertechniques/CTFTCTE-CRY-011.md) | Reproduce protocol memory-leak vulnerabilities | T1190 |
| [CTFTTE-CRY-012](../techniques/CTFTTE-CRY-012.md) | Hash-cracking maze with constraints | [CTFTCTE-CRY-012](../countertechniques/CTFTCTE-CRY-012.md) | Crack hashes under masks/rules | T1110 |
| [CTFTTE-CRY-013](../techniques/CTFTTE-CRY-013.md) | Nonstandard-alphabet substitution (braille, cetacean) | [CTFTCTE-CRY-013](../countertechniques/CTFTCTE-CRY-013.md) | Transcode nonstandard alphabets | T1140 |


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
