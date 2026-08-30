# CTFT Correlation Matrix

Quick cross-reference of every **Design / Hide Technique** and its paired **Counter-Technique**, grouped by tactic.


---


## `CTFT-TA-AIM` — AI / ML

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-AIM-001](techniques/CTFTTE-AIM-001.md) | Secret embedded in model weights | [CTFTCTE-AIM-001](countertechniques/CTFTCTE-AIM-001.md) | Extract tensors and inspect weights |
| 2 | [CTFTTE-AIM-002](techniques/CTFTTE-AIM-002.md) | Prompt-injection-gated flag | [CTFTCTE-AIM-002](countertechniques/CTFTCTE-AIM-002.md) | Extract the flag via crafted prompts |
| 3 | [CTFTTE-AIM-003](techniques/CTFTTE-AIM-003.md) | Adversarial-input requirement | [CTFTCTE-AIM-003](countertechniques/CTFTCTE-AIM-003.md) | Generate an adversarial example |
| 4 | [CTFTTE-AIM-004](techniques/CTFTTE-AIM-004.md) | Malicious / opaque serialized model | [CTFTCTE-AIM-004](countertechniques/CTFTCTE-AIM-004.md) | Safely inspect serialized model files |
| 5 | [CTFTTE-AIM-005](techniques/CTFTTE-AIM-005.md) | Training-data leakage via queries | [CTFTCTE-AIM-005](countertechniques/CTFTCTE-AIM-005.md) | Recover secrets through model inversion |


## `CTFT-TA-BLK` — Blockchain

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-BLK-001](techniques/CTFTTE-BLK-001.md) | Private storage-variable concealment | [CTFTCTE-BLK-001](countertechniques/CTFTCTE-BLK-001.md) | Read contract storage slots directly |
| 2 | [CTFTTE-BLK-002](techniques/CTFTTE-BLK-002.md) | Reentrancy-gated flag | [CTFTCTE-BLK-002](countertechniques/CTFTCTE-BLK-002.md) | Exploit reentrancy to set the flag |
| 3 | [CTFTTE-BLK-003](techniques/CTFTTE-BLK-003.md) | Unverified-bytecode logic hiding | [CTFTCTE-BLK-003](countertechniques/CTFTCTE-BLK-003.md) | Decompile EVM bytecode |
| 4 | [CTFTTE-BLK-004](techniques/CTFTTE-BLK-004.md) | Hidden event-log / calldata concealment | [CTFTCTE-BLK-004](countertechniques/CTFTCTE-BLK-004.md) | Parse transaction logs and calldata |
| 5 | [CTFTTE-BLK-005](techniques/CTFTTE-BLK-005.md) | Access-control flaw to set flag | [CTFTCTE-BLK-005](countertechniques/CTFTCTE-BLK-005.md) | Craft a transaction abusing missing checks |


## `CTFT-TA-CLD` — Cloud

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-CLD-001](techniques/CTFTTE-CLD-001.md) | Misconfigured object-storage exposure | [CTFTCTE-CLD-001](countertechniques/CTFTCTE-CLD-001.md) | Enumerate and list public buckets |
| 2 | [CTFTTE-CLD-002](techniques/CTFTTE-CLD-002.md) | Over-permissive IAM role | [CTFTCTE-CLD-002](countertechniques/CTFTCTE-CLD-002.md) | Enumerate and assume reachable roles |
| 3 | [CTFTTE-CLD-003](techniques/CTFTTE-CLD-003.md) | Instance metadata service exposure | [CTFTCTE-CLD-003](countertechniques/CTFTCTE-CLD-003.md) | Retrieve credentials via SSRF to IMDS |
| 4 | [CTFTTE-CLD-004](techniques/CTFTTE-CLD-004.md) | Secrets in function config / layers | [CTFTCTE-CLD-004](countertechniques/CTFTCTE-CLD-004.md) | Dump serverless configuration and layers |
| 5 | [CTFTTE-CLD-005](techniques/CTFTTE-CLD-005.md) | Container image / registry leak | [CTFTCTE-CLD-005](countertechniques/CTFTCTE-CLD-005.md) | Pull and inspect image layers |


## `CTFT-TA-COD` — Coding / Programming Puzzle

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-COD-001](techniques/CTFTTE-COD-001.md) | Esolang / unusual-encoding puzzle | [CTFTCTE-COD-001](countertechniques/CTFTCTE-COD-001.md) | Interpret or transpile the encoding |
| 2 | [CTFTTE-COD-002](techniques/CTFTTE-COD-002.md) | Algorithm optimisation challenge | [CTFTCTE-COD-002](countertechniques/CTFTCTE-COD-002.md) | Implement an efficient algorithm to satisfy the server |
| 3 | [CTFTTE-COD-003](techniques/CTFTTE-COD-003.md) | Scripted protocol / automation marathon | [CTFTCTE-COD-003](countertechniques/CTFTCTE-COD-003.md) | Write a pwntools script to complete all rounds |
| 4 | [CTFTTE-COD-004](techniques/CTFTTE-COD-004.md) | Code-golf / polyglot code puzzle | [CTFTCTE-COD-004](countertechniques/CTFTCTE-COD-004.md) | Craft a minimal polyglot that satisfies every parser |
| 5 | [CTFTTE-COD-005](techniques/CTFTTE-COD-005.md) | Symbolic-execution / SMT-solver puzzle | [CTFTCTE-COD-005](countertechniques/CTFTCTE-COD-005.md) | Extract constraints and solve with Z3 / angr |


## `CTFT-TA-CRY` — Cryptography 

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-CRY-001](techniques/CTFTTE-CRY-001.md) | Weak RSA parameter design | [CTFTCTE-CRY-001](countertechniques/CTFTCTE-CRY-001.md) | Recover the RSA private key from weak parameters |
| 2 | [CTFTTE-CRY-002](techniques/CTFTTE-CRY-002.md) | Classical cipher layering | [CTFTCTE-CRY-002](countertechniques/CTFTCTE-CRY-002.md) | Break layered classical ciphers |
| 3 | [CTFTTE-CRY-003](techniques/CTFTTE-CRY-003.md) | Repeating-key XOR / ECB pattern | [CTFTCTE-CRY-003](countertechniques/CTFTCTE-CRY-003.md) | Exploit key reuse and block-mode patterns |
| 4 | [CTFTTE-CRY-004](techniques/CTFTTE-CRY-004.md) | Predictable PRNG / nonce reuse | [CTFTCTE-CRY-004](countertechniques/CTFTCTE-CRY-004.md) | Reconstruct keys from broken randomness |
| 5 | [CTFTTE-CRY-005](techniques/CTFTTE-CRY-005.md) | Hash length-extension exposure | [CTFTCTE-CRY-005](countertechniques/CTFTCTE-CRY-005.md) | Forge data via length extension |
| 6 | [CTFTTE-CRY-006](techniques/CTFTTE-CRY-006.md) | Nested encoding obfuscation | [CTFTCTE-CRY-006](countertechniques/CTFTCTE-CRY-006.md) | Unwrap chained encodings |


## `CTFT-TA-FOR` — Forensics

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-FOR-001](techniques/CTFTTE-FOR-001.md) | Magic-byte / file-signature tampering | [CTFTCTE-FOR-001](countertechniques/CTFTCTE-FOR-001.md) | Recover the legitimate file signature |
| 2 | [CTFTTE-FOR-002](techniques/CTFTTE-FOR-002.md) | Slack-space and unallocated-area concealment | [CTFTCTE-FOR-002](countertechniques/CTFTCTE-FOR-002.md) | Carve hidden files from slack/unallocated space |
| 3 | [CTFTTE-FOR-003](techniques/CTFTTE-FOR-003.md) | Timestomping (MACB manipulation) | [CTFTCTE-FOR-003](countertechniques/CTFTCTE-FOR-003.md) | Detect and reconstruct true timestamps |
| 4 | [CTFTTE-FOR-004](techniques/CTFTTE-FOR-004.md) | NTFS Alternate Data Stream hiding | [CTFTCTE-FOR-004](countertechniques/CTFTCTE-FOR-004.md) | Enumerate and extract Alternate Data Streams |
| 5 | [CTFTTE-FOR-005](techniques/CTFTTE-FOR-005.md) | Memory-resident artifact concealment | [CTFTCTE-FOR-005](countertechniques/CTFTCTE-FOR-005.md) | Recover secrets from a memory image |
| 6 | [CTFTTE-FOR-006](techniques/CTFTTE-FOR-006.md) | PCAP payload obfuscation | [CTFTCTE-FOR-006](countertechniques/CTFTCTE-FOR-006.md) | Reassemble and decode hidden network payloads |
| 7 | [CTFTTE-FOR-007](techniques/CTFTTE-FOR-007.md) | Modify legitimate header signature of a file | [CTFTCTE-FOR-007](countertechniques/CTFTCTE-FOR-007.md) | Recover legitimate signature of a file |
| 8 | [CTFTTE-FOR-008](techniques/CTFTTE-FOR-008.md) | Modify legitimate header signature of a file via python scri | [CTFTCTE-FOR-008](countertechniques/CTFTCTE-FOR-008.md) | Recover legitimate header signature of an OpenEXR image file |
| 9 | [CTFTTE-FOR-009](techniques/CTFTTE-FOR-009.md) | Corrupt Image file magic signature | [CTFTCTE-FOR-009](countertechniques/CTFTCTE-FOR-009.md) | Counter — Corrupt Image file magic signature |
| 10 | [CTFTTE-FOR-010](techniques/CTFTTE-FOR-010.md) | Use special encoding system to hide data with visual, machin | [CTFTCTE-FOR-010](countertechniques/CTFTCTE-FOR-010.md) | Retrieve information from QR codes |
| 11 | [CTFTTE-FOR-011](techniques/CTFTTE-FOR-011.md) | Use special encoding system to hide data with QR codes | [CTFTCTE-FOR-011](countertechniques/CTFTCTE-FOR-011.md) | Retrieve information from rMQR codes |
| 12 | [CTFTTE-FOR-012](techniques/CTFTTE-FOR-012.md) | Use special encoding system to hide data with RMQR codes | [CTFTCTE-FOR-012](countertechniques/CTFTCTE-FOR-012.md) | Retrieve information from JAB QR codes (2D color bar code) |
| 13 | [CTFTTE-FOR-013](techniques/CTFTTE-FOR-013.md) | Conceal information with diagrams encoding | [CTFTCTE-FOR-013](countertechniques/CTFTCTE-FOR-013.md) | Retrieve information from Mengenlehreuhr diagrams encoding |
| 14 | [CTFTTE-FOR-014](techniques/CTFTTE-FOR-014.md) | Conceal information with Mengenlehreuhr diagrams encoding | [CTFTCTE-FOR-014](countertechniques/CTFTCTE-FOR-014.md) | Counter — Conceal information with Mengenlehreuhr diagrams e |
| 15 | [CTFTTE-FOR-015](techniques/CTFTTE-FOR-015.md) | Conceal information with packagers | [CTFTCTE-FOR-015](countertechniques/CTFTCTE-FOR-015.md) | Recover from packager obfuscations |
| 16 | [CTFTTE-FOR-016](techniques/CTFTTE-FOR-016.md) | Conceal information with date and time representations | [CTFTCTE-FOR-016](countertechniques/CTFTCTE-FOR-016.md) | Recover information with date and time representations |
| 17 | [CTFTTE-FOR-017](techniques/CTFTTE-FOR-017.md) | Conceal text data strings in ELF binary | [CTFTCTE-FOR-017](countertechniques/CTFTCTE-FOR-017.md) | Recover text data strings from ELF binary |


## `CTFT-TA-FPN` — Full Pwn / Multi-Stage

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-FPN-001](techniques/CTFTTE-FPN-001.md) | Multi-stage chained challenge | [CTFTCTE-FPN-001](countertechniques/CTFTCTE-FPN-001.md) | Chain enumeration, foothold and privilege escalation |
| 2 | [CTFTTE-FPN-002](techniques/CTFTTE-FPN-002.md) | Windows Active Directory fullpwn | [CTFTCTE-FPN-002](countertechniques/CTFTCTE-FPN-002.md) | Enumerate AD, abuse delegation or ACL paths to the DC |
| 3 | [CTFTTE-FPN-003](techniques/CTFTTE-FPN-003.md) | Multi-hop network pivot | [CTFTCTE-FPN-003](countertechniques/CTFTCTE-FPN-003.md) | Tunnel through compromised hosts to reach the flag |
| 4 | [CTFTTE-FPN-004](techniques/CTFTTE-FPN-004.md) | Container / service misconfiguration chain | [CTFTCTE-FPN-004](countertechniques/CTFTCTE-FPN-004.md) | Chain service misconfig and container escape to host |
| 5 | [CTFTTE-FPN-005](techniques/CTFTTE-FPN-005.md) | Cloud-integrated fullpwn | [CTFTCTE-FPN-005](countertechniques/CTFTCTE-FPN-005.md) | Pivot from on-prem to cloud IAM to retrieve the secret |


## `CTFT-TA-GAM` — Game / Protocol Automation (GamePwn)

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-GAM-001](techniques/CTFTTE-GAM-001.md) | Networked game / protocol automation | [CTFTCTE-GAM-001](countertechniques/CTFTCTE-GAM-001.md) | Script a client to beat the protocol |
| 2 | [CTFTTE-GAM-002](techniques/CTFTTE-GAM-002.md) | Game save-state / memory manipulation | [CTFTCTE-GAM-002](countertechniques/CTFTCTE-GAM-002.md) | Hex-edit the save file or patch in-memory values |
| 3 | [CTFTTE-GAM-003](techniques/CTFTTE-GAM-003.md) | Bot-vs-AI / ML-opponent challenge | [CTFTCTE-GAM-003](countertechniques/CTFTCTE-GAM-003.md) | Exploit AI weaknesses or craft adversarial inputs |
| 4 | [CTFTTE-GAM-004](techniques/CTFTTE-GAM-004.md) | Game binary win-condition bypass | [CTFTCTE-GAM-004](countertechniques/CTFTCTE-GAM-004.md) | Patch the jump / comparison to force a win state |
| 5 | [CTFTTE-GAM-005](techniques/CTFTTE-GAM-005.md) | Protocol sequence replay / race | [CTFTCTE-GAM-005](countertechniques/CTFTCTE-GAM-005.md) | Record, replay, or race the server sequence precisely |


## `CTFT-TA-ICS` — ICS / SCADA

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-ICS-001](techniques/CTFTTE-ICS-001.md) | Modbus holding-register concealment | [CTFTCTE-ICS-001](countertechniques/CTFTCTE-ICS-001.md) | Read Modbus registers |
| 2 | [CTFTTE-ICS-002](techniques/CTFTTE-ICS-002.md) | S7comm PLC memory hiding | [CTFTCTE-ICS-002](countertechniques/CTFTCTE-ICS-002.md) | Read S7 data blocks |
| 3 | [CTFTTE-ICS-003](techniques/CTFTTE-ICS-003.md) | Proprietary-protocol capture concealment | [CTFTCTE-ICS-003](countertechniques/CTFTCTE-ICS-003.md) | Dissect industrial protocol captures |
| 4 | [CTFTTE-ICS-004](techniques/CTFTTE-ICS-004.md) | HMI project-file secrets | [CTFTCTE-ICS-004](countertechniques/CTFTCTE-ICS-004.md) | Parse HMI/SCADA project files |
| 5 | [CTFTTE-ICS-005](techniques/CTFTTE-ICS-005.md) | DNP3 / BACnet object enumeration | [CTFTCTE-ICS-005](countertechniques/CTFTCTE-ICS-005.md) | Enumerate protocol objects |


## `CTFT-TA-JAL` — Jail / Sandbox Escape

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-JAL-001](techniques/CTFTTE-JAL-001.md) | Python jail (pyjail) confinement | [CTFTCTE-JAL-001](countertechniques/CTFTCTE-JAL-001.md) | Escape the Python sandbox |
| 2 | [CTFTTE-JAL-002](techniques/CTFTTE-JAL-002.md) | Restricted-shell confinement | [CTFTCTE-JAL-002](countertechniques/CTFTCTE-JAL-002.md) | Escape the restricted shell |
| 3 | [CTFTTE-JAL-003](techniques/CTFTTE-JAL-003.md) | Docker / container escape | [CTFTCTE-JAL-003](countertechniques/CTFTCTE-JAL-003.md) | Break out of the container to the host |
| 4 | [CTFTTE-JAL-004](techniques/CTFTTE-JAL-004.md) | JavaScript browser-sandbox jail | [CTFTCTE-JAL-004](countertechniques/CTFTCTE-JAL-004.md) | Traverse the prototype chain to escape |
| 5 | [CTFTTE-JAL-005](techniques/CTFTTE-JAL-005.md) | Seccomp / AppArmor policy confinement | [CTFTCTE-JAL-005](countertechniques/CTFTCTE-JAL-005.md) | Identify allowed syscalls and pivot around the filter |


## `CTFT-TA-MOB` — Mobile

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-MOB-001](techniques/CTFTTE-MOB-001.md) | Hardcoded secrets in app resources | [CTFTCTE-MOB-001](countertechniques/CTFTCTE-MOB-001.md) | Decompile the APK and extract secrets |
| 2 | [CTFTTE-MOB-002](techniques/CTFTTE-MOB-002.md) | Native-library logic hiding | [CTFTCTE-MOB-002](countertechniques/CTFTCTE-MOB-002.md) | Reverse the native .so |
| 3 | [CTFTTE-MOB-003](techniques/CTFTTE-MOB-003.md) | Certificate pinning as capture barrier | [CTFTCTE-MOB-003](countertechniques/CTFTCTE-MOB-003.md) | Bypass pinning to observe traffic |
| 4 | [CTFTTE-MOB-004](techniques/CTFTTE-MOB-004.md) | DEX obfuscation | [CTFTCTE-MOB-004](countertechniques/CTFTCTE-MOB-004.md) | Deobfuscate renamed/obfuscated bytecode |
| 5 | [CTFTTE-MOB-005](techniques/CTFTTE-MOB-005.md) | Runtime/device-conditioned flag | [CTFTCTE-MOB-005](countertechniques/CTFTCTE-MOB-005.md) | Hook the app to satisfy runtime checks |


## `CTFT-TA-OSI` — OSINT 

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-OSI-001](techniques/CTFTTE-OSI-001.md) | Metadata-dispersed identity/location | [CTFTCTE-OSI-001](countertechniques/CTFTCTE-OSI-001.md) | Correlate leaked metadata |
| 2 | [CTFTTE-OSI-002](techniques/CTFTTE-OSI-002.md) | Cross-platform username pivot | [CTFTCTE-OSI-002](countertechniques/CTFTCTE-OSI-002.md) | Enumerate accounts across platforms |
| 3 | [CTFTTE-OSI-003](techniques/CTFTTE-OSI-003.md) | Historical / cached content concealment | [CTFTCTE-OSI-003](countertechniques/CTFTCTE-OSI-003.md) | Recover deleted or changed content |
| 4 | [CTFTTE-OSI-004](techniques/CTFTTE-OSI-004.md) | Geolocation from imagery | [CTFTCTE-OSI-004](countertechniques/CTFTCTE-OSI-004.md) | Geolocate using visual cues |
| 5 | [CTFTTE-OSI-005](techniques/CTFTTE-OSI-005.md) | Public-record / repo leak pivot | [CTFTCTE-OSI-005](countertechniques/CTFTCTE-OSI-005.md) | Mine public repositories and records |


## `CTFT-TA-PWN` — Binary Exploitation  

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-PWN-001](techniques/CTFTTE-PWN-001.md) | Hidden win-function backdoor | [CTFTCTE-PWN-001](countertechniques/CTFTCTE-PWN-001.md) | Redirect execution to the win function |
| 2 | [CTFTTE-PWN-002](techniques/CTFTTE-PWN-002.md) | Format-string information hiding | [CTFTCTE-PWN-002](countertechniques/CTFTCTE-PWN-002.md) | Leak and overwrite via format string |
| 3 | [CTFTTE-PWN-003](techniques/CTFTTE-PWN-003.md) | Heap-grooming puzzle | [CTFTCTE-PWN-003](countertechniques/CTFTCTE-PWN-003.md) | Groom the heap to corrupt allocator metadata |
| 4 | [CTFTTE-PWN-004](techniques/CTFTTE-PWN-004.md) | Stripped/static gadget search | [CTFTCTE-PWN-004](countertechniques/CTFTCTE-PWN-004.md) | Build a ROP chain from available gadgets |
| 5 | [CTFTTE-PWN-005](techniques/CTFTTE-PWN-005.md) | seccomp-restricted shell puzzle | [CTFTCTE-PWN-005](countertechniques/CTFTCTE-PWN-005.md) | Open-Read-Write the flag under seccomp |


## `CTFT-TA-REV` — Reverse Engineering 

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-REV-001](techniques/CTFTTE-REV-001.md) | Anti-debugging / anti-analysis guards | [CTFTCTE-REV-001](countertechniques/CTFTCTE-REV-001.md) | Bypass anti-analysis to reach the check |
| 2 | [CTFTTE-REV-002](techniques/CTFTTE-REV-002.md) | Packing / runtime self-modification | [CTFTCTE-REV-002](countertechniques/CTFTCTE-REV-002.md) | Unpack and dump the real code |
| 3 | [CTFTTE-REV-003](techniques/CTFTTE-REV-003.md) | Control-flow obfuscation / opaque predicates | [CTFTCTE-REV-003](countertechniques/CTFTCTE-REV-003.md) | Deobfuscate flattened control flow |
| 4 | [CTFTTE-REV-004](techniques/CTFTTE-REV-004.md) | Custom VM / bytecode interpreter | [CTFTCTE-REV-004](countertechniques/CTFTCTE-REV-004.md) | Reconstruct the VM and lift its bytecode |
| 5 | [CTFTTE-REV-005](techniques/CTFTTE-REV-005.md) | Constraint-gated flag check | [CTFTCTE-REV-005](countertechniques/CTFTCTE-REV-005.md) | Solve the check with an SMT/symbolic engine |


## `CTFT-TA-STE` — Steganography 

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-STE-001](techniques/CTFTTE-STE-001.md) | LSB image steganography | [CTFTCTE-STE-001](countertechniques/CTFTCTE-STE-001.md) | Extract least-significant-bit payloads |
| 2 | [CTFTTE-STE-002](techniques/CTFTTE-STE-002.md) | Appended data / polyglot after EOF | [CTFTCTE-STE-002](countertechniques/CTFTCTE-STE-002.md) | Detect and split appended/embedded files |
| 3 | [CTFTTE-STE-003](techniques/CTFTTE-STE-003.md) | Audio spectrogram hiding | [CTFTCTE-STE-003](countertechniques/CTFTCTE-STE-003.md) | Reveal data in the audio spectrogram |
| 4 | [CTFTTE-STE-004](techniques/CTFTTE-STE-004.md) | Metadata / EXIF embedding | [CTFTCTE-STE-004](countertechniques/CTFTCTE-STE-004.md) | Extract concealed metadata fields |
| 5 | [CTFTTE-STE-005](techniques/CTFTTE-STE-005.md) | Zero-width / whitespace text steganography | [CTFTCTE-STE-005](countertechniques/CTFTCTE-STE-005.md) | Decode invisible-character payloads |
| 6 | [CTFTTE-STE-006](techniques/CTFTTE-STE-006.md) | Conceal information within digital media with **linguistic** | [CTFTCTE-STE-006](countertechniques/CTFTCTE-STE-006.md) | Counter — Conceal information within digital media with **li |
| 7 | [CTFTTE-STE-007](techniques/CTFTTE-STE-007.md) | Conceal information within digital media with **technical**  | [CTFTCTE-STE-007](countertechniques/CTFTCTE-STE-007.md) | Counter — Conceal information within digital media with **te |
| 8 | [CTFTTE-STE-008](techniques/CTFTTE-STE-008.md) | Conceal via **technical text** steganography | [CTFTCTE-STE-008](countertechniques/CTFTCTE-STE-008.md) | Counter — Conceal via **technical text** steganography |


## `CTFT-TA-WEB` — Web Exploitation

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-WEB-001](techniques/CTFTTE-WEB-001.md) | Obscured endpoint / source-comment hiding | [CTFTCTE-WEB-001](countertechniques/CTFTCTE-WEB-001.md) | Content discovery and source review |
| 2 | [CTFTTE-WEB-002](techniques/CTFTTE-WEB-002.md) | IDOR / predictable object obscurity | [CTFTCTE-WEB-002](countertechniques/CTFTCTE-WEB-002.md) | Enumerate insecure direct object references |
| 3 | [CTFTTE-WEB-003](techniques/CTFTTE-WEB-003.md) | JWT misconfiguration | [CTFTCTE-WEB-003](countertechniques/CTFTCTE-WEB-003.md) | Forge or downgrade a JSON Web Token |
| 4 | [CTFTTE-WEB-004](techniques/CTFTTE-WEB-004.md) | Blind / WAF-evaded SQL injection | [CTFTCTE-WEB-004](countertechniques/CTFTCTE-WEB-004.md) | Extract data via blind injection |
| 5 | [CTFTTE-WEB-005](techniques/CTFTTE-WEB-005.md) | Server-side template injection | [CTFTCTE-WEB-005](countertechniques/CTFTCTE-WEB-005.md) | Exploit template evaluation |
| 6 | [CTFTTE-WEB-006](techniques/CTFTTE-WEB-006.md) | Client-side obfuscated logic | [CTFTCTE-WEB-006](countertechniques/CTFTCTE-WEB-006.md) | Deobfuscate and dynamically analyze JS |

## `CTFT-TA-MSC` — Misc / Jail / Coding / Fullpwn

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-MSC-001](techniques/CTFTTE-MSC-001.md) | Python jail (pyjail) confinement | [CTFTCTE-MSC-001](countertechniques/CTFTCTE-MSC-001.md) | Escape the Python sandbox |
| 2 | [CTFTTE-MSC-002](techniques/CTFTTE-MSC-002.md) | Restricted-shell confinement | [CTFTCTE-MSC-002](countertechniques/CTFTCTE-MSC-002.md) | Escape the restricted shell |
| 3 | [CTFTTE-MSC-003](techniques/CTFTTE-MSC-003.md) | Esolang / unusual-encoding puzzle | [CTFTCTE-MSC-003](countertechniques/CTFTCTE-MSC-003.md) | Interpret or transpile the encoding |
| 4 | [CTFTTE-MSC-004](techniques/CTFTTE-MSC-004.md) | Networked game / protocol automation (GamePwn) | [CTFTCTE-MSC-004](countertechniques/CTFTCTE-MSC-004.md) | Script a client to beat the protocol |
| 5 | [CTFTTE-MSC-005](techniques/CTFTTE-MSC-005.md) | Multi-stage chained challenge (Fullpwn) | [CTFTCTE-MSC-005](countertechniques/CTFTCTE-MSC-005.md) | Chain enumeration, foothold and privilege escalation |


---

