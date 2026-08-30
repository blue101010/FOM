# TODO — Suggested techniques & counter-techniques inferred


> Every suggestion below is a candidate **pair** (technique + counter-technique) following the
> same naming/ID rules as the existing corpus. Nothing here is added yet — this is the backlog.

## How to promote an entry (from CORRELATION.md)

1. Pick a category below — never `MSC`, never a new catch-all.
2. Create `techniques/CTFTTE-<CAT>-NNN.md` **and** `countertechniques/CTFTCTE-<CAT>-NNN.md`
   (same `NNN`), each with the `## Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).
3. Add the row to `tactics/CTFT-TA-<CAT>.md`.
4. Re-render and re-index:

```bash
python v2/render_taxonomy_docs.py --write
python v2/catalog_audit.py --write --write-index --write-catalog --check
```

## A. Populate `SDR` (Software-Defined Radio) — new family, next free: 002

| ID | Technique (hide/design) | Counter-technique (recover) | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| SDR-001 | RF/SDR signal embedding | Demodulate and decode RF captures (Gqrx, GnuRadio, Universal Radio Hacker) | `sdr_RF/`, `audio/rf_signal.wav` | T1001.002 |

## B. Populate `HWR` (Hardware) — reserved, empty, next free: 003

> Renumbered after the SDR split: former HWR-001 moved to SDR-001, former HWR-002/003 became HWR-001/002.

| ID | Technique (hide/design) | Counter-technique (recover) | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| HWR-001 | USB HID keystroke concealment | Reconstruct keystrokes from captured USB HID traffic | `usb/` (scan codes, HID tables) | T1056.001 |
| HWR-002 | Badge / embedded-device firmware concealment | Dump and reverse badge firmware | `badge/` | T1027 |

## C. New tactic `NET` (Network) — currently folded into FPN/WEB

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| NET-001 | Port/service discovery maze | Systematic port/service enumeration (nmap, rustscan, masscan) | `network/nmap/`, `network/rustscan/`, `network/masscan/`, `network/shadow1ng_fscan/` | T1046 |
| NET-002 | DNS covert channel / tunnel | Detect DNS tunneling and beaconing in PCAPs | `network/pcap-bloodhound/` (dns_tunnel, beaconing), `network/TTL.txt` | T1071.004 |
| NET-003 | SMB enumeration barrier | Enumerate SMB shares/versions | `smb/` | T1021.002 |
| NET-004 | Wi-Fi capture / handshake concealment | Crack WPA2 handshakes, decode Wi-Fi captures | `wifi/` | T1040 |
| NET-005 | Traffic tunnel / port-forwarding relay | Pivot via ssh -L/-R, chisel | `port_forwarding/`, `ssh/tunnel.md` | T1572 / T1090 |
| NET-006 | TTL / protocol-field covert channel | Decode TTL/ICMP/padding channels | `network/TTL.txt` | T1095 |
| NET-007 | Packet-capture forensics maze | Run beaconing/exfil/credential detectors over PCAPs | `network/pcap-bloodhound/`, `network/tshark/`, `network/sharker.md` | T1040 |

## D. Forensics (`FOR`, next free: 019)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| FOR-019 | JPEG marker / DCT coefficient corruption | Repair JPEG segments and decode DCT coefficients | `binary/JPEG/`, `to_categorize/to_categorize.md` (poorguy) | T1027 |
| FOR-020 | LUKS-encrypted volume concealment | Recover LUKS headers/keyslots, bruteforce passphrase | `luks/` | T1486 |
| FOR-021 | LVM fragment/concat volume labyrinth | Reassemble LVM logical volumes and mount | `lvm/LVM_Labyrinth.md` | T1564 |
| FOR-022 | Deleted-file / open-handle recovery | Recover deleted files via /proc handles, journal, carving | `misc/5_linux_Deleted_file.txt`, `network/8_hidden_deleted.txt` | T1070.004 |
| FOR-023 | SELinux context-based concealment | Analyze SELinux contexts blocking artifacts | `misc/4_Hidden in SELinux.txt` | T1562 |
| FOR-024 | Browser-profile artifact concealment | Parse Firefox/SQLite artifacts (places, logins, cookies) | `browers/`, `firefox/`, `forensics/analyze_firefox.py` | T1217 |
| FOR-025 | PDF object/stream hiding | Parse PDF xref, streams and filters | `PDF/pdf.md` | T1027 |
| FOR-026 | Memory-image OS-artifact recovery | Extract registry/services/process artifacts from memory images | `volatility/`, `autopsy/`, `binary/dump-all-memory-pid.sh` | T1003 |

## E. Reverse Engineering (`REV`, next free: 006)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| REV-006 | Java bytecode / JAR obfuscation | Decompile and deobfuscate JVM bytecode | `java/` (CTF.jar, Sudoku classes) | T1027 |
| REV-007 | Python bytecode (.pyc/.pyo) concealment | Decompile Python bytecode | `python_packages/`, `python_misc/` | T1027 |
| REV-008 | Functional-language binary concealment | Reverse Haskell/functional compiled artifacts | `haskell/` | T1027 |
| REV-009 | Assembly-level code-golf / shellcode RE | Disassemble and annotate asm snippets | `asm/` | T1027 |

## F. Binary Exploitation (`PWN`, next free: 006)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| PWN-006 | Stack canary / PIE / ASLR hardening puzzle | Leak canary/PIE base, ret2libc | `buffer_overflow/`, `gdb/` | T1068 |
| PWN-007 | Kernel/mseal-guarded memory puzzle | Exploit kernel-module or mseal protections | `kernel/kernel_hide.txt`, `memory_corruption/mseal.md` | T1068 |
| PWN-008 | Shellcode craft & encoding constraints | Generate/encode shellcode (alphanumeric, null-free) | `shellcode/`, `asm/exploit.asm` | T1055 |

## G. Cryptography (`CRY`, next free: 008)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| CRY-008 | Block-cipher mode / AES implementation weakness | Attack AES modes (padding oracle, IV flaws) | `crypto/AES/` | T1573.001 |
| CRY-009 | Stream-cipher keystream reuse (Salsa20) | Exploit keystream reuse to recover plaintext | `crypto/salsa20.py`, `crypto/stream_cipher_secret.md` | T1573.001 |
| CRY-010 | Certificate / PEM / ASN.1 field hiding | Parse certificates and extract hidden fields | `certifcates/` | T1552.001 |
| CRY-011 | Protocol implementation flaw (Heartbleed-style) | Reproduce protocol memory-leak vulnerabilities | `openssl/openssl_heartblead.txt` | T1190 |
| CRY-012 | Hash-cracking maze with constraints | Crack hashes under masks/rules | `crypto/MD5/`, `md5/` | T1110 |
| CRY-013 | Nonstandard-alphabet substitution (braille, cetacean) | Transcode nonstandard alphabets | `crypto/braille/`, `crypto/cetacean.py` | T1140 |

## H. Steganography (`STE`, next free: 010)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| STE-010 | Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV) | Detect and decode audio-domain stego | `audio/`, `stegano/7_checkaudiostegano.sh`, `stegano/8_audiostegano.md` | T1001.002 |
| STE-011 | Palette / bitplane LSB tricks | Analyze bitplanes and palette-based LSB | `binary/change_palette.py`, `stegano/extract_bitplanes.py` | T1001.002 |

## I. Web Exploitation (`WEB`, next free: 010)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| WEB-010 | LFI / log poisoning / php-filter chains | Exploit LFI to RCE or flag read | `web/LFI/` | T1190 |
| WEB-011 | Directory-traversal maze | Traverse filtered paths (PHP labyrinth) | `web/directory_traversal/` | T1190 |
| WEB-012 | XSS-driven flag exfiltration | Craft XSS payloads (stored/reflected/DOM) | `web/XSS/` | T1059.007 |
| WEB-013 | CSRF-gated state change | Forge cross-site requests | `web/CSRF/The_Illusion_of_Trust.md` | T1606 |
| WEB-014 | WebSocket message hiding | Intercept and decode WebSocket traffic | `websockets/` | T1071.001 |
| WEB-015 | CMS / WordPress plugin flaw | Enumerate and exploit WordPress (wpscan) | `wordpress/` | T1190 |
| WEB-016 | NoSQL injection | Inject Mongo/NoSQL queries | `database/mongo/` | T1190 |
| WEB-017 | Host-header / vhost fuzzing | Fuzz vhosts and host headers | `recon/vhosts.md`, `recon/bruteforcehostheader.png` | T1083 |

## J. OSINT (`OSI`, next free: 006)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| OSI-006 | Git-repository archaeology | Mine git history, objects and reflog | `git/3_Git_gone_wrong.txt` | T1596 |
| OSI-007 | Search-engine mining (dorking) | Run advanced dorks and search operators | `dorks/` | T1593.002 |
| OSI-008 | ASN / IP-range / subdomain recon | Map ASN, ranges, subdomains (bbot, assetfinder) | `recon/`, `TOOLS/assetfinder.md`, `recon/bbot.md` | T1596.001 |

## K. Cloud (`CLD`, next free: 006)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| CLD-006 | Cross-account role chaining / trust abuse | Chain sts:AssumeRole across accounts | `aws/` | T1078.004 |
| CLD-007 | Cloud NoSQL-store misconfiguration | Enumerate and query exposed cloud databases | `aws/dynamodb.md`, `database/` | T1213 |
| CLD-008 | Azure management-plane misconfiguration | Enumerate Azure AD/VM/storage from credentials | `azure/azure.md` | T1078.004 |

## L. AI / ML (`AIM`, next free: 006)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| AIM-006 | Self-hosted LLM platform misconfiguration | Audit ollama/oobabooga deployments for exposed endpoints | `ai/ollama/`, `ai/oobabooga_text-generation-webui.md`, `ai/anythingllm.md` | T1190 |
| AIM-007 | Agent / tool-calling guardrail bypass | Bypass agent tool policies | `ai/codex_runner.py` | — (emerging) |

## M. Full Pwn / Multi-Stage (`FPN`, next free: 008)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| FPN-008 | Linux local privesc chain (SUID, ACLs, sudo, capabilities) | Enumerate and chain Linux privesc vectors | `permissions_privesc/`, `network/7_suid_bin.txt` | T1068 / T1548 |
| FPN-009 | Redis/NoSQL service misconfiguration chain | Enumerate Redis/Mongo/MySQL, dump or RCE | `database/redis/`, `database/mongo/`, `database/mariadb/` | T1213 |
| FPN-010 | Reverse-shell delivery & listener operations | Catch, upgrade and persist reverse shells | `reverse_shell/` | T1059 |

## N. Game / Protocol (`GAM`, next free: 006) · Coding (`COD`, next free: 006) · Jail (`JAL`, next free: 006)

| ID | Technique | Counter-technique | Inferred from | ATT&CK anchor |
| --- | --- | --- | --- | --- |
| GAM-006 | Chatbot / choice-path bot puzzle | Script a bot interaction to reach the win branch | `puzzles/choochoobot.png` | T1071 |
| COD-006 | Combinatorial enumeration puzzle | Generate permutations/combinations efficiently | `LinuxMUP/` | — |
| COD-007 | Grid/logic-constraint puzzle (Sudoku) | Solve constraint grids programmatically | `java/Sudoku.java` | — |
| JAL-006 | WSL-interop sandbox escape | Escape WSL-interop boundaries | `sdr_RF/pulseaudio/pulseaudio_gqrx_wsl.md`, `kali/` | T1611 |

## O. Later / cross-cutting

- **`to_categorize/to_categorize.md`** still lists open items: base64-in-pcap (→ FOR/NET), VBA-macro
  strings in `.docm` (→ FOR-024-adjacent), rMQR (covered by FOR-012), corrupted-JPEG extra bytes
  before `0xd9` (→ FOR-019), strings-in-ELF (covered by FOR-017).
- Consider promoting tool notes (`network/pcap-bloodhound`, `stegano/*`, `database/enumredis.py`)
  into the v2 `tools.json` catalogue (TOOL-* entries) as the typed slice generalizes beyond Forensics.
- Wi-Fi (`wifi/`) can join `SDR` (RF domain) or stay in `NET` — decide before promoting NET-004;
  keep ATT&CK anchors per-entry, not per-tactic.
- `sdr_RF/` also documents Gqrx / pulseaudio-WSL tooling; fold it into `tools/` and `v2/tools.json`
  when SDR-001 is promoted.
