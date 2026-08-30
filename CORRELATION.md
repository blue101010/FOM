# CTFT Correlation Matrix

Every **Design / Hide Technique** (`CTFTTE-<CAT>-NNN`) and the
**Counter-Technique** (`CTFTCTE-<CAT>-NNN`) that recovers it, grouped by tactic.
IDs pair one-to-one: `CTFTTE-FOR-004` is always answered by `CTFTCTE-FOR-004`.

> Generated from the files in `techniques/` and `countertechniques/` on 2026-08-30T21:58:15+00:00
> by `v2/render_taxonomy_docs.py`. **161 complete pairs** across **19 active tactics**. Do not hand-edit: rename the entry, then re-render.

---

## Tactics at a glance

Order follows the challenge-category picker.

| # | Code | Picker label | Tactic | Pairs |
| --- | --- | --- | --- | --- |
| 1 | [`FOR`](#ctft-ta-for) | Forensics | Forensics | 26 |
| 2 | [`WEB`](#ctft-ta-web) | Web | Web Exploitation | 17 |
| 3 | [`CRY`](#ctft-ta-cry) | Crypto | Cryptography | 13 |
| 4 | [`PWN`](#ctft-ta-pwn) | Binary | Binary Exploitation | 8 |
| 5 | [`REV`](#ctft-ta-rev) | Reverse | Reverse Engineering | 9 |
| 6 | [`STE`](#ctft-ta-ste) | Stego | Steganography | 11 |
| 7 | [`OSI`](#ctft-ta-osi) | OSINT | OSINT | 8 |
| 8 | [`CLD`](#ctft-ta-cld) | Cloud | Cloud | 8 |
| 9 | [`BLK`](#ctft-ta-blk) | Blockchain | Blockchain | 5 |
| 10 | [`AIM`](#ctft-ta-aim) | AI/ML | AI / ML | 7 |
| 11 | [`ICS`](#ctft-ta-ics) | ICS/SCADA | ICS / SCADA | 5 |
| 12 | [`MOB`](#ctft-ta-mob) | Mobile | Mobile | 5 |
| 13 | [`JAL`](#ctft-ta-jal) | Jail escape | Jail / Sandbox Escape | 6 |
| 14 | [`GAM`](#ctft-ta-gam) | Game/Proto | Game / Protocol Automation (GamePwn) | 6 |
| 15 | [`COD`](#ctft-ta-cod) | Coding | Coding / Programming Puzzle | 7 |
| 16 | [`NET`](#ctft-ta-net) | Network | Network | 7 |
| 17 | [`FPN`](#ctft-ta-fpn) | Full Pwn | Full Pwn / Multi-Stage | 10 |
| 18 | [`HWR`](#ctft-ta-hwr) | Hardware | Hardware | 2 |
| 19 | [`SDR`](#ctft-ta-sdr) | SDR / RF | Software-Defined Radio | 1 |
| | | | **Total** | **161** |

**Retired — do not use.** `MSC` (Misc) was a catch-all whose entries all
duplicated a precise tactic; file those challenges under `JAL`, `COD`, `GAM`
or `FPN` instead. See the [supersession map](#retired-categories) below.

---

## <a id="ctft-ta-for"></a>`CTFT-TA-FOR` — Forensics

> [tactic page](tactics/CTFT-TA-FOR.md) · 26 pairs · HTB: Forensics

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-FOR-001](techniques/CTFTTE-FOR-001.md) | Magic-byte / file-signature tampering | [CTFTCTE-FOR-001](countertechniques/CTFTCTE-FOR-001.md) | Recover the legitimate file signature |
| 2 | [CTFTTE-FOR-002](techniques/CTFTTE-FOR-002.md) | Slack-space and unallocated-area concealment | [CTFTCTE-FOR-002](countertechniques/CTFTCTE-FOR-002.md) | Carve hidden files from slack/unallocated space |
| 3 | [CTFTTE-FOR-003](techniques/CTFTTE-FOR-003.md) | Timestomping (MACB manipulation) | [CTFTCTE-FOR-003](countertechniques/CTFTCTE-FOR-003.md) | Detect and reconstruct true timestamps |
| 4 | [CTFTTE-FOR-004](techniques/CTFTTE-FOR-004.md) | NTFS Alternate Data Stream hiding | [CTFTCTE-FOR-004](countertechniques/CTFTCTE-FOR-004.md) | Enumerate and extract Alternate Data Streams |
| 5 | [CTFTTE-FOR-005](techniques/CTFTTE-FOR-005.md) | Memory-resident artifact concealment | [CTFTCTE-FOR-005](countertechniques/CTFTCTE-FOR-005.md) | Recover secrets from a memory image |
| 6 | [CTFTTE-FOR-006](techniques/CTFTTE-FOR-006.md) | PCAP payload obfuscation | [CTFTCTE-FOR-006](countertechniques/CTFTCTE-FOR-006.md) | Reassemble and decode hidden network payloads |
| 7 | [CTFTTE-FOR-007](techniques/CTFTTE-FOR-007.md) | Modify legitimate header signature of a file | [CTFTCTE-FOR-007](countertechniques/CTFTCTE-FOR-007.md) | Recover legitimate signature of a file |
| 8 | [CTFTTE-FOR-008](techniques/CTFTTE-FOR-008.md) | Modify legitimate header signature of a file via python script | [CTFTCTE-FOR-008](countertechniques/CTFTCTE-FOR-008.md) | Recover legitimate header signature of an OpenEXR image file |
| 9 | [CTFTTE-FOR-009](techniques/CTFTTE-FOR-009.md) | Corrupt Image file magic signature | [CTFTCTE-FOR-009](countertechniques/CTFTCTE-FOR-009.md) | Counter — Corrupt Image file magic signature |
| 10 | [CTFTTE-FOR-010](techniques/CTFTTE-FOR-010.md) | Use special encoding system to hide data with visual, machine-readable form. | [CTFTCTE-FOR-010](countertechniques/CTFTCTE-FOR-010.md) | Retrieve information from QR codes ⚠ |
| 11 | [CTFTTE-FOR-011](techniques/CTFTTE-FOR-011.md) | Use special encoding system to hide data with QR codes | [CTFTCTE-FOR-011](countertechniques/CTFTCTE-FOR-011.md) | Retrieve information from rMQR codes ⚠ |
| 12 | [CTFTTE-FOR-012](techniques/CTFTTE-FOR-012.md) | Use special encoding system to hide data with RMQR codes | [CTFTCTE-FOR-012](countertechniques/CTFTCTE-FOR-012.md) | Retrieve information from JAB QR codes (2D color bar code) ⚠ |
| 13 | [CTFTTE-FOR-013](techniques/CTFTTE-FOR-013.md) | Conceal information with diagrams encoding | [CTFTCTE-FOR-013](countertechniques/CTFTCTE-FOR-013.md) | Retrieve information from Mengenlehreuhr diagrams encoding ⚠ |
| 14 | [CTFTTE-FOR-014](techniques/CTFTTE-FOR-014.md) | Conceal information with Mengenlehreuhr diagrams encoding | [CTFTCTE-FOR-014](countertechniques/CTFTCTE-FOR-014.md) | Counter — Conceal information with Mengenlehreuhr diagrams encoding |
| 15 | [CTFTTE-FOR-015](techniques/CTFTTE-FOR-015.md) | Conceal information with packagers | [CTFTCTE-FOR-015](countertechniques/CTFTCTE-FOR-015.md) | Recover from packager obfuscations |
| 16 | [CTFTTE-FOR-016](techniques/CTFTTE-FOR-016.md) | Conceal information with date and time representations | [CTFTCTE-FOR-016](countertechniques/CTFTCTE-FOR-016.md) | Recover information with date and time representations |
| 17 | [CTFTTE-FOR-017](techniques/CTFTTE-FOR-017.md) | Conceal text data strings in ELF binary | [CTFTCTE-FOR-017](countertechniques/CTFTCTE-FOR-017.md) | Recover text data strings from ELF binary |
| 18 | [CTFTTE-FOR-018](techniques/CTFTTE-FOR-018.md) | MFT record and attribute tampering | [CTFTCTE-FOR-018](countertechniques/CTFTCTE-FOR-018.md) | Analyze orphaned MFT records and raw attributes |
| 19 | [CTFTTE-FOR-019](techniques/CTFTTE-FOR-019.md) | JPEG marker / DCT coefficient corruption | [CTFTCTE-FOR-019](countertechniques/CTFTCTE-FOR-019.md) | Repair JPEG segments and decode DCT coefficients |
| 20 | [CTFTTE-FOR-020](techniques/CTFTTE-FOR-020.md) | LUKS-encrypted volume concealment | [CTFTCTE-FOR-020](countertechniques/CTFTCTE-FOR-020.md) | Recover LUKS headers/keyslots, bruteforce passphrase |
| 21 | [CTFTTE-FOR-021](techniques/CTFTTE-FOR-021.md) | LVM fragment/concat volume labyrinth | [CTFTCTE-FOR-021](countertechniques/CTFTCTE-FOR-021.md) | Reassemble LVM logical volumes and mount |
| 22 | [CTFTTE-FOR-022](techniques/CTFTTE-FOR-022.md) | Deleted-file / open-handle recovery | [CTFTCTE-FOR-022](countertechniques/CTFTCTE-FOR-022.md) | Recover deleted files via /proc handles, journal, carving |
| 23 | [CTFTTE-FOR-023](techniques/CTFTTE-FOR-023.md) | SELinux context-based concealment | [CTFTCTE-FOR-023](countertechniques/CTFTCTE-FOR-023.md) | Analyze SELinux contexts blocking artifacts |
| 24 | [CTFTTE-FOR-024](techniques/CTFTTE-FOR-024.md) | Browser-profile artifact concealment | [CTFTCTE-FOR-024](countertechniques/CTFTCTE-FOR-024.md) | Parse Firefox/SQLite artifacts (places, logins, cookies) |
| 25 | [CTFTTE-FOR-025](techniques/CTFTTE-FOR-025.md) | PDF object/stream hiding | [CTFTCTE-FOR-025](countertechniques/CTFTCTE-FOR-025.md) | Parse PDF xref, streams and filters |
| 26 | [CTFTTE-FOR-026](techniques/CTFTTE-FOR-026.md) | Memory-image OS-artifact recovery | [CTFTCTE-FOR-026](countertechniques/CTFTCTE-FOR-026.md) | Extract registry/services/process artifacts from memory images |


## <a id="ctft-ta-web"></a>`CTFT-TA-WEB` — Web Exploitation

> [tactic page](tactics/CTFT-TA-WEB.md) · 17 pairs · HTB: Web

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-WEB-001](techniques/CTFTTE-WEB-001.md) | Obscured endpoint / source-comment hiding | [CTFTCTE-WEB-001](countertechniques/CTFTCTE-WEB-001.md) | Content discovery and source review |
| 2 | [CTFTTE-WEB-002](techniques/CTFTTE-WEB-002.md) | IDOR / predictable object obscurity | [CTFTCTE-WEB-002](countertechniques/CTFTCTE-WEB-002.md) | Enumerate insecure direct object references |
| 3 | [CTFTTE-WEB-003](techniques/CTFTTE-WEB-003.md) | JWT misconfiguration | [CTFTCTE-WEB-003](countertechniques/CTFTCTE-WEB-003.md) | Forge or downgrade a JSON Web Token |
| 4 | [CTFTTE-WEB-004](techniques/CTFTTE-WEB-004.md) | Blind / WAF-evaded SQL injection | [CTFTCTE-WEB-004](countertechniques/CTFTCTE-WEB-004.md) | Extract data via blind injection |
| 5 | [CTFTTE-WEB-005](techniques/CTFTTE-WEB-005.md) | Server-side template injection | [CTFTCTE-WEB-005](countertechniques/CTFTCTE-WEB-005.md) | Exploit template evaluation |
| 6 | [CTFTTE-WEB-006](techniques/CTFTTE-WEB-006.md) | Client-side obfuscated logic | [CTFTCTE-WEB-006](countertechniques/CTFTCTE-WEB-006.md) | Deobfuscate and dynamically analyze JS |
| 7 | [CTFTTE-WEB-007](techniques/CTFTTE-WEB-007.md) | Deployment metadata index disclosure | [CTFTCTE-WEB-007](countertechniques/CTFTCTE-WEB-007.md) | Analyze a disclosed deployment metadata index |
| 8 | [CTFTTE-WEB-008](techniques/CTFTTE-WEB-008.md) | Legacy short-name namespace disclosure | [CTFTCTE-WEB-008](countertechniques/CTFTCTE-WEB-008.md) | Reconcile a disclosed short-name namespace |
| 9 | [CTFTTE-WEB-009](techniques/CTFTTE-WEB-009.md) | Web configuration secret exposure | [CTFTCTE-WEB-009](countertechniques/CTFTCTE-WEB-009.md) | Classify a configuration secret exposure |
| 10 | [CTFTTE-WEB-010](techniques/CTFTTE-WEB-010.md) | LFI / log poisoning / php-filter chains | [CTFTCTE-WEB-010](countertechniques/CTFTCTE-WEB-010.md) | Exploit LFI to RCE or flag read |
| 11 | [CTFTTE-WEB-011](techniques/CTFTTE-WEB-011.md) | Directory-traversal maze | [CTFTCTE-WEB-011](countertechniques/CTFTCTE-WEB-011.md) | Traverse filtered paths (PHP labyrinth) |
| 12 | [CTFTTE-WEB-012](techniques/CTFTTE-WEB-012.md) | XSS-driven flag exfiltration | [CTFTCTE-WEB-012](countertechniques/CTFTCTE-WEB-012.md) | Craft XSS payloads (stored/reflected/DOM) |
| 13 | [CTFTTE-WEB-013](techniques/CTFTTE-WEB-013.md) | CSRF-gated state change | [CTFTCTE-WEB-013](countertechniques/CTFTCTE-WEB-013.md) | Forge cross-site requests |
| 14 | [CTFTTE-WEB-014](techniques/CTFTTE-WEB-014.md) | WebSocket message hiding | [CTFTCTE-WEB-014](countertechniques/CTFTCTE-WEB-014.md) | Intercept and decode WebSocket traffic |
| 15 | [CTFTTE-WEB-015](techniques/CTFTTE-WEB-015.md) | CMS / WordPress plugin flaw | [CTFTCTE-WEB-015](countertechniques/CTFTCTE-WEB-015.md) | Enumerate and exploit WordPress (wpscan) |
| 16 | [CTFTTE-WEB-016](techniques/CTFTTE-WEB-016.md) | NoSQL injection | [CTFTCTE-WEB-016](countertechniques/CTFTCTE-WEB-016.md) | Inject Mongo/NoSQL queries |
| 17 | [CTFTTE-WEB-017](techniques/CTFTTE-WEB-017.md) | Host-header / vhost fuzzing | [CTFTCTE-WEB-017](countertechniques/CTFTCTE-WEB-017.md) | Fuzz vhosts and host headers |


## <a id="ctft-ta-cry"></a>`CTFT-TA-CRY` — Cryptography

> [tactic page](tactics/CTFT-TA-CRY.md) · 13 pairs · HTB: Crypto

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-CRY-001](techniques/CTFTTE-CRY-001.md) | Weak RSA parameter design | [CTFTCTE-CRY-001](countertechniques/CTFTCTE-CRY-001.md) | Recover the RSA private key from weak parameters |
| 2 | [CTFTTE-CRY-002](techniques/CTFTTE-CRY-002.md) | Classical cipher layering | [CTFTCTE-CRY-002](countertechniques/CTFTCTE-CRY-002.md) | Break layered classical ciphers |
| 3 | [CTFTTE-CRY-003](techniques/CTFTTE-CRY-003.md) | Repeating-key XOR / ECB pattern | [CTFTCTE-CRY-003](countertechniques/CTFTCTE-CRY-003.md) | Exploit key reuse and block-mode patterns |
| 4 | [CTFTTE-CRY-004](techniques/CTFTTE-CRY-004.md) | Nonce reuse in cryptographic operations | [CTFTCTE-CRY-004](countertechniques/CTFTCTE-CRY-004.md) | Assess nonce reuse and its cryptographic consequence |
| 5 | [CTFTTE-CRY-005](techniques/CTFTTE-CRY-005.md) | Hash length-extension exposure | [CTFTCTE-CRY-005](countertechniques/CTFTCTE-CRY-005.md) | Forge data via length extension |
| 6 | [CTFTTE-CRY-006](techniques/CTFTTE-CRY-006.md) | Nested encoding obfuscation | [CTFTCTE-CRY-006](countertechniques/CTFTCTE-CRY-006.md) | Unwrap chained encodings |
| 7 | [CTFTTE-CRY-007](techniques/CTFTTE-CRY-007.md) | Deliberately predictable stateful pseudo-random generator | [CTFTCTE-CRY-007](countertechniques/CTFTCTE-CRY-007.md) | Assess and predict recoverable PRNG state |
| 8 | [CTFTTE-CRY-008](techniques/CTFTTE-CRY-008.md) | Block-cipher mode / AES implementation weakness | [CTFTCTE-CRY-008](countertechniques/CTFTCTE-CRY-008.md) | Attack AES modes (padding oracle, IV flaws) |
| 9 | [CTFTTE-CRY-009](techniques/CTFTTE-CRY-009.md) | Stream-cipher keystream reuse (Salsa20) | [CTFTCTE-CRY-009](countertechniques/CTFTCTE-CRY-009.md) | Exploit keystream reuse to recover plaintext |
| 10 | [CTFTTE-CRY-010](techniques/CTFTTE-CRY-010.md) | Certificate / PEM / ASN.1 field hiding | [CTFTCTE-CRY-010](countertechniques/CTFTCTE-CRY-010.md) | Parse certificates and extract hidden fields |
| 11 | [CTFTTE-CRY-011](techniques/CTFTTE-CRY-011.md) | Protocol implementation flaw (Heartbleed-style) | [CTFTCTE-CRY-011](countertechniques/CTFTCTE-CRY-011.md) | Reproduce protocol memory-leak vulnerabilities |
| 12 | [CTFTTE-CRY-012](techniques/CTFTTE-CRY-012.md) | Hash-cracking maze with constraints | [CTFTCTE-CRY-012](countertechniques/CTFTCTE-CRY-012.md) | Crack hashes under masks/rules |
| 13 | [CTFTTE-CRY-013](techniques/CTFTTE-CRY-013.md) | Nonstandard-alphabet substitution (braille, cetacean) | [CTFTCTE-CRY-013](countertechniques/CTFTCTE-CRY-013.md) | Transcode nonstandard alphabets |


## <a id="ctft-ta-pwn"></a>`CTFT-TA-PWN` — Binary Exploitation

> [tactic page](tactics/CTFT-TA-PWN.md) · 8 pairs · HTB: Pwn

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-PWN-001](techniques/CTFTTE-PWN-001.md) | Hidden win-function backdoor | [CTFTCTE-PWN-001](countertechniques/CTFTCTE-PWN-001.md) | Redirect execution to the win function |
| 2 | [CTFTTE-PWN-002](techniques/CTFTTE-PWN-002.md) | Format-string information hiding | [CTFTCTE-PWN-002](countertechniques/CTFTCTE-PWN-002.md) | Leak and overwrite via format string |
| 3 | [CTFTTE-PWN-003](techniques/CTFTTE-PWN-003.md) | Heap-grooming puzzle | [CTFTCTE-PWN-003](countertechniques/CTFTCTE-PWN-003.md) | Groom the heap to corrupt allocator metadata |
| 4 | [CTFTTE-PWN-004](techniques/CTFTTE-PWN-004.md) | Stripped/static gadget search | [CTFTCTE-PWN-004](countertechniques/CTFTCTE-PWN-004.md) | Build a ROP chain from available gadgets |
| 5 | [CTFTTE-PWN-005](techniques/CTFTTE-PWN-005.md) | seccomp-restricted shell puzzle | [CTFTCTE-PWN-005](countertechniques/CTFTCTE-PWN-005.md) | Open-Read-Write the flag under seccomp |
| 6 | [CTFTTE-PWN-006](techniques/CTFTTE-PWN-006.md) | Stack canary / PIE / ASLR hardening puzzle | [CTFTCTE-PWN-006](countertechniques/CTFTCTE-PWN-006.md) | Leak canary/PIE base, ret2libc |
| 7 | [CTFTTE-PWN-007](techniques/CTFTTE-PWN-007.md) | Kernel/mseal-guarded memory puzzle | [CTFTCTE-PWN-007](countertechniques/CTFTCTE-PWN-007.md) | Exploit kernel-module or mseal protections |
| 8 | [CTFTTE-PWN-008](techniques/CTFTTE-PWN-008.md) | Shellcode craft & encoding constraints | [CTFTCTE-PWN-008](countertechniques/CTFTCTE-PWN-008.md) | Generate/encode shellcode (alphanumeric, null-free) |


## <a id="ctft-ta-rev"></a>`CTFT-TA-REV` — Reverse Engineering

> [tactic page](tactics/CTFT-TA-REV.md) · 9 pairs · HTB: Reversing

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-REV-001](techniques/CTFTTE-REV-001.md) | Anti-debugging / anti-analysis guards | [CTFTCTE-REV-001](countertechniques/CTFTCTE-REV-001.md) | Bypass anti-analysis to reach the check |
| 2 | [CTFTTE-REV-002](techniques/CTFTTE-REV-002.md) | Packing / runtime self-modification | [CTFTCTE-REV-002](countertechniques/CTFTCTE-REV-002.md) | Unpack and dump the real code |
| 3 | [CTFTTE-REV-003](techniques/CTFTTE-REV-003.md) | Control-flow obfuscation / opaque predicates | [CTFTCTE-REV-003](countertechniques/CTFTCTE-REV-003.md) | Deobfuscate flattened control flow |
| 4 | [CTFTTE-REV-004](techniques/CTFTTE-REV-004.md) | Custom VM / bytecode interpreter | [CTFTCTE-REV-004](countertechniques/CTFTCTE-REV-004.md) | Reconstruct the VM and lift its bytecode |
| 5 | [CTFTTE-REV-005](techniques/CTFTTE-REV-005.md) | Constraint-gated flag check | [CTFTCTE-REV-005](countertechniques/CTFTCTE-REV-005.md) | Solve the check with an SMT/symbolic engine |
| 6 | [CTFTTE-REV-006](techniques/CTFTTE-REV-006.md) | Java bytecode / JAR obfuscation | [CTFTCTE-REV-006](countertechniques/CTFTCTE-REV-006.md) | Decompile and deobfuscate JVM bytecode |
| 7 | [CTFTTE-REV-007](techniques/CTFTTE-REV-007.md) | Python bytecode (.pyc/.pyo) concealment | [CTFTCTE-REV-007](countertechniques/CTFTCTE-REV-007.md) | Decompile Python bytecode |
| 8 | [CTFTTE-REV-008](techniques/CTFTTE-REV-008.md) | Functional-language binary concealment | [CTFTCTE-REV-008](countertechniques/CTFTCTE-REV-008.md) | Reverse Haskell/functional compiled artifacts |
| 9 | [CTFTTE-REV-009](techniques/CTFTTE-REV-009.md) | Assembly-level code-golf / shellcode RE | [CTFTCTE-REV-009](countertechniques/CTFTCTE-REV-009.md) | Disassemble and annotate asm snippets |


## <a id="ctft-ta-ste"></a>`CTFT-TA-STE` — Steganography

> [tactic page](tactics/CTFT-TA-STE.md) · 11 pairs · HTB: Forensics/Misc (Stego)

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-STE-001](techniques/CTFTTE-STE-001.md) | LSB image steganography | [CTFTCTE-STE-001](countertechniques/CTFTCTE-STE-001.md) | Extract least-significant-bit payloads |
| 2 | [CTFTTE-STE-002](techniques/CTFTTE-STE-002.md) | Appended data / polyglot after EOF | [CTFTCTE-STE-002](countertechniques/CTFTCTE-STE-002.md) | Detect and split appended/embedded files |
| 3 | [CTFTTE-STE-003](techniques/CTFTTE-STE-003.md) | Audio spectrogram hiding | [CTFTCTE-STE-003](countertechniques/CTFTCTE-STE-003.md) | Reveal data in the audio spectrogram |
| 4 | [CTFTTE-STE-004](techniques/CTFTTE-STE-004.md) | Metadata / EXIF embedding | [CTFTCTE-STE-004](countertechniques/CTFTCTE-STE-004.md) | Extract concealed metadata fields |
| 5 | [CTFTTE-STE-005](techniques/CTFTTE-STE-005.md) | Zero-width / whitespace text steganography | [CTFTCTE-STE-005](countertechniques/CTFTCTE-STE-005.md) | Decode invisible-character payloads |
| 6 | [CTFTTE-STE-006](techniques/CTFTTE-STE-006.md) | Conceal information within digital media with **linguistic** steganography | [CTFTCTE-STE-006](countertechniques/CTFTCTE-STE-006.md) | Counter — Conceal information within digital media with **linguistic** steganography |
| 7 | [CTFTTE-STE-007](techniques/CTFTTE-STE-007.md) | Conceal information within digital media with **technical** steganography | [CTFTCTE-STE-007](countertechniques/CTFTCTE-STE-007.md) | Counter — Conceal information within digital media with **technical** steganography |
| 8 | [CTFTTE-STE-008](techniques/CTFTTE-STE-008.md) | Conceal via **technical text** steganography | [CTFTCTE-STE-008](countertechniques/CTFTCTE-STE-008.md) | Counter — Conceal via **technical text** steganography |
| 9 | [CTFTTE-STE-009](techniques/CTFTTE-STE-009.md) | Nested metadata-container embedding | [CTFTCTE-STE-009](countertechniques/CTFTCTE-STE-009.md) | Recursively inspect nested metadata containers |
| 10 | [CTFTTE-STE-010](techniques/CTFTTE-STE-010.md) | Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV) | [CTFTCTE-STE-010](countertechniques/CTFTCTE-STE-010.md) | Detect and decode audio-domain stego |
| 11 | [CTFTTE-STE-011](techniques/CTFTTE-STE-011.md) | Palette / bitplane LSB tricks | [CTFTCTE-STE-011](countertechniques/CTFTCTE-STE-011.md) | Analyze bitplanes and palette-based LSB |


## <a id="ctft-ta-osi"></a>`CTFT-TA-OSI` — OSINT

> [tactic page](tactics/CTFT-TA-OSI.md) · 8 pairs · HTB: OSINT

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-OSI-001](techniques/CTFTTE-OSI-001.md) | Metadata-dispersed identity/location | [CTFTCTE-OSI-001](countertechniques/CTFTCTE-OSI-001.md) | Correlate leaked metadata |
| 2 | [CTFTTE-OSI-002](techniques/CTFTTE-OSI-002.md) | Cross-platform username pivot | [CTFTCTE-OSI-002](countertechniques/CTFTCTE-OSI-002.md) | Enumerate accounts across platforms |
| 3 | [CTFTTE-OSI-003](techniques/CTFTTE-OSI-003.md) | Historical / cached content concealment | [CTFTCTE-OSI-003](countertechniques/CTFTCTE-OSI-003.md) | Recover deleted or changed content |
| 4 | [CTFTTE-OSI-004](techniques/CTFTTE-OSI-004.md) | Geolocation from imagery | [CTFTCTE-OSI-004](countertechniques/CTFTCTE-OSI-004.md) | Geolocate using visual cues |
| 5 | [CTFTTE-OSI-005](techniques/CTFTTE-OSI-005.md) | Public-record / repo leak pivot | [CTFTCTE-OSI-005](countertechniques/CTFTCTE-OSI-005.md) | Mine public repositories and records |
| 6 | [CTFTTE-OSI-006](techniques/CTFTTE-OSI-006.md) | Git-repository archaeology | [CTFTCTE-OSI-006](countertechniques/CTFTCTE-OSI-006.md) | Mine git history, objects and reflog |
| 7 | [CTFTTE-OSI-007](techniques/CTFTTE-OSI-007.md) | Search-engine mining (dorking) | [CTFTCTE-OSI-007](countertechniques/CTFTCTE-OSI-007.md) | Run advanced dorks and search operators |
| 8 | [CTFTTE-OSI-008](techniques/CTFTTE-OSI-008.md) | ASN / IP-range / subdomain recon | [CTFTCTE-OSI-008](countertechniques/CTFTCTE-OSI-008.md) | Map ASN, ranges, subdomains (bbot, assetfinder) |


## <a id="ctft-ta-cld"></a>`CTFT-TA-CLD` — Cloud

> [tactic page](tactics/CTFT-TA-CLD.md) · 8 pairs · HTB: Cloud

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-CLD-001](techniques/CTFTTE-CLD-001.md) | Misconfigured object-storage exposure | [CTFTCTE-CLD-001](countertechniques/CTFTCTE-CLD-001.md) | Enumerate and list public buckets |
| 2 | [CTFTTE-CLD-002](techniques/CTFTTE-CLD-002.md) | Over-permissive IAM role | [CTFTCTE-CLD-002](countertechniques/CTFTCTE-CLD-002.md) | Enumerate and assume reachable roles |
| 3 | [CTFTTE-CLD-003](techniques/CTFTTE-CLD-003.md) | Instance metadata service exposure | [CTFTCTE-CLD-003](countertechniques/CTFTCTE-CLD-003.md) | Retrieve credentials via SSRF to IMDS |
| 4 | [CTFTTE-CLD-004](techniques/CTFTTE-CLD-004.md) | Secrets in function config / layers | [CTFTCTE-CLD-004](countertechniques/CTFTCTE-CLD-004.md) | Dump serverless configuration and layers |
| 5 | [CTFTTE-CLD-005](techniques/CTFTTE-CLD-005.md) | Container image / registry leak | [CTFTCTE-CLD-005](countertechniques/CTFTCTE-CLD-005.md) | Pull and inspect image layers |
| 6 | [CTFTTE-CLD-006](techniques/CTFTTE-CLD-006.md) | Cross-account role chaining / trust abuse | [CTFTCTE-CLD-006](countertechniques/CTFTCTE-CLD-006.md) | Chain sts:AssumeRole across accounts |
| 7 | [CTFTTE-CLD-007](techniques/CTFTTE-CLD-007.md) | Cloud NoSQL-store misconfiguration | [CTFTCTE-CLD-007](countertechniques/CTFTCTE-CLD-007.md) | Enumerate and query exposed cloud databases |
| 8 | [CTFTTE-CLD-008](techniques/CTFTTE-CLD-008.md) | Azure management-plane misconfiguration | [CTFTCTE-CLD-008](countertechniques/CTFTCTE-CLD-008.md) | Enumerate Azure AD/VM/storage from credentials |


## <a id="ctft-ta-blk"></a>`CTFT-TA-BLK` — Blockchain

> [tactic page](tactics/CTFT-TA-BLK.md) · 5 pairs · HTB: Blockchain

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-BLK-001](techniques/CTFTTE-BLK-001.md) | Private storage-variable concealment | [CTFTCTE-BLK-001](countertechniques/CTFTCTE-BLK-001.md) | Read contract storage slots directly |
| 2 | [CTFTTE-BLK-002](techniques/CTFTTE-BLK-002.md) | Reentrancy-gated flag | [CTFTCTE-BLK-002](countertechniques/CTFTCTE-BLK-002.md) | Exploit reentrancy to set the flag |
| 3 | [CTFTTE-BLK-003](techniques/CTFTTE-BLK-003.md) | Unverified-bytecode logic hiding | [CTFTCTE-BLK-003](countertechniques/CTFTCTE-BLK-003.md) | Decompile EVM bytecode |
| 4 | [CTFTTE-BLK-004](techniques/CTFTTE-BLK-004.md) | Hidden event-log / calldata concealment | [CTFTCTE-BLK-004](countertechniques/CTFTCTE-BLK-004.md) | Parse transaction logs and calldata |
| 5 | [CTFTTE-BLK-005](techniques/CTFTTE-BLK-005.md) | Access-control flaw to set flag | [CTFTCTE-BLK-005](countertechniques/CTFTCTE-BLK-005.md) | Craft a transaction abusing missing checks |


## <a id="ctft-ta-aim"></a>`CTFT-TA-AIM` — AI / ML

> [tactic page](tactics/CTFT-TA-AIM.md) · 7 pairs · HTB: AI-ML

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-AIM-001](techniques/CTFTTE-AIM-001.md) | Secret embedded in model weights | [CTFTCTE-AIM-001](countertechniques/CTFTCTE-AIM-001.md) | Extract tensors and inspect weights |
| 2 | [CTFTTE-AIM-002](techniques/CTFTTE-AIM-002.md) | Prompt-injection-gated flag | [CTFTCTE-AIM-002](countertechniques/CTFTCTE-AIM-002.md) | Extract the flag via crafted prompts |
| 3 | [CTFTTE-AIM-003](techniques/CTFTTE-AIM-003.md) | Adversarial-input requirement | [CTFTCTE-AIM-003](countertechniques/CTFTCTE-AIM-003.md) | Generate an adversarial example |
| 4 | [CTFTTE-AIM-004](techniques/CTFTTE-AIM-004.md) | Malicious / opaque serialized model | [CTFTCTE-AIM-004](countertechniques/CTFTCTE-AIM-004.md) | Safely inspect serialized model files |
| 5 | [CTFTTE-AIM-005](techniques/CTFTTE-AIM-005.md) | Training-data leakage via queries | [CTFTCTE-AIM-005](countertechniques/CTFTCTE-AIM-005.md) | Recover secrets through model inversion |
| 6 | [CTFTTE-AIM-006](techniques/CTFTTE-AIM-006.md) | Self-hosted LLM platform misconfiguration | [CTFTCTE-AIM-006](countertechniques/CTFTCTE-AIM-006.md) | Audit ollama/oobabooga deployments for exposed endpoints |
| 7 | [CTFTTE-AIM-007](techniques/CTFTTE-AIM-007.md) | Agent / tool-calling guardrail bypass | [CTFTCTE-AIM-007](countertechniques/CTFTCTE-AIM-007.md) | Bypass agent tool policies |


## <a id="ctft-ta-ics"></a>`CTFT-TA-ICS` — ICS / SCADA

> [tactic page](tactics/CTFT-TA-ICS.md) · 5 pairs · HTB: ICS

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-ICS-001](techniques/CTFTTE-ICS-001.md) | Modbus holding-register concealment | [CTFTCTE-ICS-001](countertechniques/CTFTCTE-ICS-001.md) | Read Modbus registers |
| 2 | [CTFTTE-ICS-002](techniques/CTFTTE-ICS-002.md) | S7comm PLC memory hiding | [CTFTCTE-ICS-002](countertechniques/CTFTCTE-ICS-002.md) | Read S7 data blocks |
| 3 | [CTFTTE-ICS-003](techniques/CTFTTE-ICS-003.md) | Proprietary-protocol capture concealment | [CTFTCTE-ICS-003](countertechniques/CTFTCTE-ICS-003.md) | Dissect industrial protocol captures |
| 4 | [CTFTTE-ICS-004](techniques/CTFTTE-ICS-004.md) | HMI project-file secrets | [CTFTCTE-ICS-004](countertechniques/CTFTCTE-ICS-004.md) | Parse HMI/SCADA project files |
| 5 | [CTFTTE-ICS-005](techniques/CTFTTE-ICS-005.md) | DNP3 / BACnet object enumeration | [CTFTCTE-ICS-005](countertechniques/CTFTCTE-ICS-005.md) | Enumerate protocol objects |


## <a id="ctft-ta-mob"></a>`CTFT-TA-MOB` — Mobile

> [tactic page](tactics/CTFT-TA-MOB.md) · 5 pairs · HTB: Mobile

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-MOB-001](techniques/CTFTTE-MOB-001.md) | Hardcoded secrets in app resources | [CTFTCTE-MOB-001](countertechniques/CTFTCTE-MOB-001.md) | Decompile the APK and extract secrets |
| 2 | [CTFTTE-MOB-002](techniques/CTFTTE-MOB-002.md) | Native-library logic hiding | [CTFTCTE-MOB-002](countertechniques/CTFTCTE-MOB-002.md) | Reverse the native .so |
| 3 | [CTFTTE-MOB-003](techniques/CTFTTE-MOB-003.md) | Certificate pinning as capture barrier | [CTFTCTE-MOB-003](countertechniques/CTFTCTE-MOB-003.md) | Bypass pinning to observe traffic |
| 4 | [CTFTTE-MOB-004](techniques/CTFTTE-MOB-004.md) | DEX obfuscation | [CTFTCTE-MOB-004](countertechniques/CTFTCTE-MOB-004.md) | Deobfuscate renamed/obfuscated bytecode |
| 5 | [CTFTTE-MOB-005](techniques/CTFTTE-MOB-005.md) | Runtime/device-conditioned flag | [CTFTCTE-MOB-005](countertechniques/CTFTCTE-MOB-005.md) | Hook the app to satisfy runtime checks |


## <a id="ctft-ta-jal"></a>`CTFT-TA-JAL` — Jail / Sandbox Escape

> [tactic page](tactics/CTFT-TA-JAL.md) · 6 pairs · HTB: Misc (Jail)

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-JAL-001](techniques/CTFTTE-JAL-001.md) | Python jail (pyjail) confinement | [CTFTCTE-JAL-001](countertechniques/CTFTCTE-JAL-001.md) | Escape the Python sandbox |
| 2 | [CTFTTE-JAL-002](techniques/CTFTTE-JAL-002.md) | Restricted-shell confinement | [CTFTCTE-JAL-002](countertechniques/CTFTCTE-JAL-002.md) | Escape the restricted shell |
| 3 | [CTFTTE-JAL-003](techniques/CTFTTE-JAL-003.md) | Docker / container escape | [CTFTCTE-JAL-003](countertechniques/CTFTCTE-JAL-003.md) | Break out of the container to the host |
| 4 | [CTFTTE-JAL-004](techniques/CTFTTE-JAL-004.md) | JavaScript browser-sandbox jail | [CTFTCTE-JAL-004](countertechniques/CTFTCTE-JAL-004.md) | Traverse the prototype chain to escape |
| 5 | [CTFTTE-JAL-005](techniques/CTFTTE-JAL-005.md) | Seccomp / AppArmor policy confinement | [CTFTCTE-JAL-005](countertechniques/CTFTCTE-JAL-005.md) | Identify allowed syscalls and pivot around the filter |
| 6 | [CTFTTE-JAL-006](techniques/CTFTTE-JAL-006.md) | WSL-interop sandbox escape | [CTFTCTE-JAL-006](countertechniques/CTFTCTE-JAL-006.md) | Escape WSL-interop boundaries |


## <a id="ctft-ta-gam"></a>`CTFT-TA-GAM` — Game / Protocol Automation (GamePwn)

> [tactic page](tactics/CTFT-TA-GAM.md) · 6 pairs · HTB: GamePwn

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-GAM-001](techniques/CTFTTE-GAM-001.md) | Networked game / protocol automation | [CTFTCTE-GAM-001](countertechniques/CTFTCTE-GAM-001.md) | Script a client to beat the protocol |
| 2 | [CTFTTE-GAM-002](techniques/CTFTTE-GAM-002.md) | Game save-state / memory manipulation | [CTFTCTE-GAM-002](countertechniques/CTFTCTE-GAM-002.md) | Hex-edit the save file or patch in-memory values |
| 3 | [CTFTTE-GAM-003](techniques/CTFTTE-GAM-003.md) | Bot-vs-AI / ML-opponent challenge | [CTFTCTE-GAM-003](countertechniques/CTFTCTE-GAM-003.md) | Exploit AI weaknesses or craft adversarial inputs |
| 4 | [CTFTTE-GAM-004](techniques/CTFTTE-GAM-004.md) | Game binary win-condition bypass | [CTFTCTE-GAM-004](countertechniques/CTFTCTE-GAM-004.md) | Patch the jump / comparison to force a win state |
| 5 | [CTFTTE-GAM-005](techniques/CTFTTE-GAM-005.md) | Protocol sequence replay / race | [CTFTCTE-GAM-005](countertechniques/CTFTCTE-GAM-005.md) | Record, replay, or race the server sequence precisely |
| 6 | [CTFTTE-GAM-006](techniques/CTFTTE-GAM-006.md) | Chatbot / choice-path bot puzzle | [CTFTCTE-GAM-006](countertechniques/CTFTCTE-GAM-006.md) | Script a bot interaction to reach the win branch |


## <a id="ctft-ta-cod"></a>`CTFT-TA-COD` — Coding / Programming Puzzle

> [tactic page](tactics/CTFT-TA-COD.md) · 7 pairs · HTB: Coding

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-COD-001](techniques/CTFTTE-COD-001.md) | Esolang / unusual-encoding puzzle | [CTFTCTE-COD-001](countertechniques/CTFTCTE-COD-001.md) | Interpret or transpile the encoding |
| 2 | [CTFTTE-COD-002](techniques/CTFTTE-COD-002.md) | Algorithm optimisation challenge | [CTFTCTE-COD-002](countertechniques/CTFTCTE-COD-002.md) | Implement an efficient algorithm to satisfy the server |
| 3 | [CTFTTE-COD-003](techniques/CTFTTE-COD-003.md) | Scripted protocol / automation marathon | [CTFTCTE-COD-003](countertechniques/CTFTCTE-COD-003.md) | Write a pwntools script to complete all rounds |
| 4 | [CTFTTE-COD-004](techniques/CTFTTE-COD-004.md) | Code-golf / polyglot code puzzle | [CTFTCTE-COD-004](countertechniques/CTFTCTE-COD-004.md) | Craft a minimal polyglot that satisfies every parser |
| 5 | [CTFTTE-COD-005](techniques/CTFTTE-COD-005.md) | Symbolic-execution / SMT-solver puzzle | [CTFTCTE-COD-005](countertechniques/CTFTCTE-COD-005.md) | Extract constraints and solve with Z3 / angr |
| 6 | [CTFTTE-COD-006](techniques/CTFTTE-COD-006.md) | Combinatorial enumeration puzzle | [CTFTCTE-COD-006](countertechniques/CTFTCTE-COD-006.md) | Generate permutations/combinations efficiently |
| 7 | [CTFTTE-COD-007](techniques/CTFTTE-COD-007.md) | Grid/logic-constraint puzzle (Sudoku) | [CTFTCTE-COD-007](countertechniques/CTFTCTE-COD-007.md) | Solve constraint grids programmatically |


## <a id="ctft-ta-net"></a>`CTFT-TA-NET` — Network

> [tactic page](tactics/CTFT-TA-NET.md) · 7 pairs · HTB: Misc (Network)

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-NET-001](techniques/CTFTTE-NET-001.md) | Port/service discovery maze | [CTFTCTE-NET-001](countertechniques/CTFTCTE-NET-001.md) | Systematic port/service enumeration |
| 2 | [CTFTTE-NET-002](techniques/CTFTTE-NET-002.md) | DNS covert channel / tunnel | [CTFTCTE-NET-002](countertechniques/CTFTCTE-NET-002.md) | Detect DNS tunneling and beaconing in PCAPs |
| 3 | [CTFTTE-NET-003](techniques/CTFTTE-NET-003.md) | SMB enumeration barrier | [CTFTCTE-NET-003](countertechniques/CTFTCTE-NET-003.md) | Enumerate SMB shares/versions |
| 4 | [CTFTTE-NET-004](techniques/CTFTTE-NET-004.md) | Wi-Fi capture / handshake concealment | [CTFTCTE-NET-004](countertechniques/CTFTCTE-NET-004.md) | Crack WPA2 handshakes, decode Wi-Fi captures |
| 5 | [CTFTTE-NET-005](techniques/CTFTTE-NET-005.md) | Traffic tunnel / port-forwarding relay | [CTFTCTE-NET-005](countertechniques/CTFTCTE-NET-005.md) | Pivot via ssh -L/-R, chisel |
| 6 | [CTFTTE-NET-006](techniques/CTFTTE-NET-006.md) | TTL / protocol-field covert channel | [CTFTCTE-NET-006](countertechniques/CTFTCTE-NET-006.md) | Decode TTL/ICMP/padding channels |
| 7 | [CTFTTE-NET-007](techniques/CTFTTE-NET-007.md) | Packet-capture forensics maze | [CTFTCTE-NET-007](countertechniques/CTFTCTE-NET-007.md) | Run beaconing/exfil/credential detectors over PCAPs |


## <a id="ctft-ta-fpn"></a>`CTFT-TA-FPN` — Full Pwn / Multi-Stage

> [tactic page](tactics/CTFT-TA-FPN.md) · 10 pairs · HTB: Fullpwn

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-FPN-001](techniques/CTFTTE-FPN-001.md) | Multi-stage chained challenge | [CTFTCTE-FPN-001](countertechniques/CTFTCTE-FPN-001.md) | Chain enumeration, foothold and privilege escalation |
| 2 | [CTFTTE-FPN-002](techniques/CTFTTE-FPN-002.md) | Windows Active Directory fullpwn | [CTFTCTE-FPN-002](countertechniques/CTFTCTE-FPN-002.md) | Enumerate AD, abuse delegation or ACL paths to the DC |
| 3 | [CTFTTE-FPN-003](techniques/CTFTTE-FPN-003.md) | Multi-hop network pivot | [CTFTCTE-FPN-003](countertechniques/CTFTCTE-FPN-003.md) | Tunnel through compromised hosts to reach the flag |
| 4 | [CTFTTE-FPN-004](techniques/CTFTTE-FPN-004.md) | Container / service misconfiguration chain | [CTFTCTE-FPN-004](countertechniques/CTFTCTE-FPN-004.md) | Chain service misconfig and container escape to host |
| 5 | [CTFTTE-FPN-005](techniques/CTFTTE-FPN-005.md) | Cloud-integrated fullpwn | [CTFTCTE-FPN-005](countertechniques/CTFTCTE-FPN-005.md) | Pivot from on-prem to cloud IAM to retrieve the secret |
| 6 | [CTFTTE-FPN-006](techniques/CTFTTE-FPN-006.md) | Chained database trust-context escalation | [CTFTCTE-FPN-006](countertechniques/CTFTCTE-FPN-006.md) | Map database trust contexts and privilege boundaries |
| 7 | [CTFTTE-FPN-007](techniques/CTFTTE-FPN-007.md) | Uninventoried dual-stack management path | [CTFTCTE-FPN-007](countertechniques/CTFTCTE-FPN-007.md) | Reconcile dual-stack management exposure |
| 8 | [CTFTTE-FPN-008](techniques/CTFTTE-FPN-008.md) | Linux local privesc chain (SUID, ACLs, sudo, capabilities) | [CTFTCTE-FPN-008](countertechniques/CTFTCTE-FPN-008.md) | Enumerate and chain Linux privesc vectors |
| 9 | [CTFTTE-FPN-009](techniques/CTFTTE-FPN-009.md) | Redis/NoSQL service misconfiguration chain | [CTFTCTE-FPN-009](countertechniques/CTFTCTE-FPN-009.md) | Enumerate Redis/Mongo/MySQL, dump or RCE |
| 10 | [CTFTTE-FPN-010](techniques/CTFTTE-FPN-010.md) | Reverse-shell delivery & listener operations | [CTFTCTE-FPN-010](countertechniques/CTFTCTE-FPN-010.md) | Catch, upgrade and persist reverse shells |


## <a id="ctft-ta-hwr"></a>`CTFT-TA-HWR` — Hardware

> [tactic page](tactics/CTFT-TA-HWR.md) · 2 pairs · HTB: Hardware

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-HWR-001](techniques/CTFTTE-HWR-001.md) | USB HID keystroke concealment | [CTFTCTE-HWR-001](countertechniques/CTFTCTE-HWR-001.md) | Reconstruct keystrokes from captured USB HID traffic |
| 2 | [CTFTTE-HWR-002](techniques/CTFTTE-HWR-002.md) | Badge / embedded-device firmware concealment | [CTFTCTE-HWR-002](countertechniques/CTFTCTE-HWR-002.md) | Dump and reverse badge firmware |


## <a id="ctft-ta-sdr"></a>`CTFT-TA-SDR` — Software-Defined Radio

> [tactic page](tactics/CTFT-TA-SDR.md) · 1 pairs · HTB: Hardware

| # | Technique ID | Hide / Design name | Counter-technique ID | Counter name |
| --- | --- | --- | --- | --- |
| 1 | [CTFTTE-SDR-001](techniques/CTFTTE-SDR-001.md) | RF/SDR signal embedding | [CTFTCTE-SDR-001](countertechniques/CTFTCTE-SDR-001.md) | Demodulate and decode RF captures |


---

<a id="retired-categories"></a>
## Retired categories

### `CTFT-TA-MSC` — retired

Removed from the corpus; the originals are kept out-of-tree under `backup/deprecated-msc/`. Never reuse these IDs.

Retired IDs are written bare (`MSC-001`) so that the integrity audit,
which scans this file for `CTFTTE-*` / `CTFTCTE-*` pairs, does not read
them back as live entries.

| Retired pair | Superseded by | Name |
| --- | --- | --- |
| `MSC-001` | [`CTFTTE-JAL-001`](techniques/CTFTTE-JAL-001.md) / [`CTFTCTE-JAL-001`](countertechniques/CTFTCTE-JAL-001.md) | Python jail (pyjail) confinement |
| `MSC-002` | [`CTFTTE-JAL-002`](techniques/CTFTTE-JAL-002.md) / [`CTFTCTE-JAL-002`](countertechniques/CTFTCTE-JAL-002.md) | Restricted-shell confinement |
| `MSC-003` | [`CTFTTE-COD-001`](techniques/CTFTTE-COD-001.md) / [`CTFTCTE-COD-001`](countertechniques/CTFTCTE-COD-001.md) | Esolang / unusual-encoding puzzle |
| `MSC-004` | [`CTFTTE-GAM-001`](techniques/CTFTTE-GAM-001.md) / [`CTFTCTE-GAM-001`](countertechniques/CTFTCTE-GAM-001.md) | Networked game / protocol automation |
| `MSC-005` | [`CTFTTE-FPN-001`](techniques/CTFTTE-FPN-001.md) / [`CTFTCTE-FPN-001`](countertechniques/CTFTCTE-FPN-001.md) | Multi-stage chained challenge |

---

## Pairs flagged for review

⚠ **Subject mismatch** — the counter-technique does not answer the technique it is paired with. Fixing this is an editorial change to the entry content, not to this matrix.

| Pair | Issue |
| --- | --- |
| `CTFTTE-FOR-010` / `CTFTCTE-FOR-010` | technique is the generic parent (visual machine-readable encoding); counter answers QR only |
| `CTFTTE-FOR-011` / `CTFTCTE-FOR-011` | technique covers QR codes; counter answers rMQR codes |
| `CTFTTE-FOR-012` / `CTFTCTE-FOR-012` | technique covers rMQR codes; counter answers JAB (colour) codes |
| `CTFTTE-FOR-013` / `CTFTCTE-FOR-013` | technique is the generic parent (diagram encoding); counter answers Mengenlehreuhr only |

**Placeholder counter names** — titled `Counter — <technique name>` instead of naming the recovery action:

- `CTFTCTE-FOR-009`
- `CTFTCTE-FOR-014`
- `CTFTCTE-STE-006`
- `CTFTCTE-STE-007`
- `CTFTCTE-STE-008`

---

## Adding an entry

1. Pick a category from the table above — never `MSC`, never a new catch-all.
2. Create `techniques/CTFTTE-<CAT>-NNN.md` **and** `countertechniques/CTFTCTE-<CAT>-NNN.md` with the same `NNN`.
3. Add the row to `tactics/CTFT-TA-<CAT>.md`.
4. Re-render and re-index:

```bash
python v2/render_taxonomy_docs.py --write
python v2/catalog_audit.py --write --write-index --write-catalog --check
```

See [README.md](README.md) for the model, and `HIERARCHY.md` (rendered locally by the same script) for the flat listing.
