#!/usr/bin/env python3
"""Create technique + counter-technique pairs from the TODO backlog.

Each entry below is a curated pair (SCHEMA_V2 §3.5 per-entry ATT&CK table
included). The script:
  - writes techniques/CTFTTE-<CAT>-NNN.md and countertechniques/CTFTCTE-<CAT>-NNN.md,
  - creates tactics/CTFT-TA-NET.md (new NET family),
  - appends rows + refreshes the `Techniques:` count on each tactic page,
  - is idempotent: existing IDs are skipped.

Run:  python v2/create_todo_entries.py
Then: python v2/render_taxonomy_docs.py --write
      python v2/catalog_audit.py --write --write-index --write-catalog --check
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WU = "Add challenge write-up link"

TACTIC_NAMES = {
    "SDR": "Software-Defined Radio",
    "HWR": "Hardware",
    "NET": "Network",
    "FOR": "Forensics",
    "REV": "Reverse Engineering",
    "PWN": "Binary Exploitation",
    "CRY": "Cryptography",
    "STE": "Steganography",
    "WEB": "Web Exploitation",
    "OSI": "OSINT",
    "CLD": "Cloud",
    "AIM": "AI / ML",
    "FPN": "Full Pwn / Multi-Stage",
    "GAM": "Game / Protocol Automation",
    "COD": "Coding / Programming Puzzle",
    "JAL": "Jail / Sandbox Escape",
}

# entry: cat, num, technique name, counter name, hide, offensive, forensic,
#        tools, refs, attack rows [(id, name, note), ...], none-note
ENTRIES = [
    # ---------------- SDR ----------------
    ("SDR", "001", "RF/SDR signal embedding", "Demodulate and decode RF captures",
     "The flag is transmitted or stored as a modulated RF signal (AM/FM/FSK/PSK), an SDR IQ capture, or a hidden frequency in an audio/RF file; identifying the modulation is the first barrier.",
     "Load the IQ capture in Gqrx/GNU Radio, identify the modulation from the waterfall and constellation, demodulate, and decode the recovered bitstream into the flag.",
     "RF captures are analyzed like any volatile signal artifact: center frequency, bandwidth and modulation are the recovery keys, and SDR snapshots can be replayed indefinitely.",
     ["Gqrx", "GNU Radio Companion", "Universal Radio Hacker", "inspectrum", "multimon-ng"],
     ["https://github.com/jopohl/urh", WU],
     [("T1001.002", "Steganography", "RF-domain data hiding echoes steganography; ATT&CK omits the demodulation craft.")],
     "No direct ATT&CK equivalent."),
    # ---------------- HWR ----------------
    ("HWR", "001", "USB HID keystroke concealment", "Reconstruct keystrokes from captured USB HID traffic",
     "Flag text is typed by a (simulated) USB keyboard; only HID report bytes — scan codes, not characters — are captured, hiding the keystrokes behind the HID protocol.",
     "Decode the USB HID report descriptor and translate scan codes back into characters, including modifiers and non-US layouts.",
     "USB capture analysis treats keyboards as peripheral evidence; scan-code translation is deterministic and can be replayed against capture files.",
     ["usbmon", "Wireshark", "usbhid-dump", "tshark"],
     ["https://wiki.wireshark.org/CaptureSetup/USB", WU],
     [("T1056.001", "Keylogging", "Captured HID traffic echoes keylogging data sources; ATT&CK omits the scan-code recovery detail.")],
     "No direct ATT&CK equivalent."),
    ("HWR", "002", "Badge / embedded-device firmware concealment", "Dump and reverse badge firmware",
     "The flag lives in an electronic badge or embedded device: in firmware, EEPROM, or behind a hidden UART/JTAG/SPI interface.",
     "Identify the exposed interfaces (UART/JTAG/SPI), dump firmware or memory, and reverse it for strings and logic.",
     "Hardware triage records pinouts and interface activity; firmware dumps are hashed and preserved as evidence before analysis.",
     ["minicom", "flashrom", "binwalk", "ghidra"],
     ["https://github.com/ReFirmLabs/binwalk", WU],
     [("T1027", "Obfuscated Files or Information", "Firmware-level hiding echoes obfuscated payloads.")],
     "No direct ATT&CK equivalent."),
    # ---------------- NET ----------------
    ("NET", "001", "Port/service discovery maze", "Systematic port/service enumeration",
     "The flag sits behind a service on an unusual port, or the challenge hides which port is real among decoys; versions and banners mislead.",
     "Enumerate TCP/UDP ports with nmap/rustscan/masscan, fingerprint versions, then focus on the anomalous service.",
     "Scan discipline matters: logged scan footprints and scope limits are respected, and service banners are correlated with netflow.",
     ["nmap", "rustscan", "masscan", "netcat"],
     ["https://nmap.org/book/", WU],
     [("T1046", "Network Service Discovery", "CTFT adds the scan-tuning detail ATT&CK omits.")],
     "No direct ATT&CK equivalent."),
    ("NET", "002", "DNS covert channel / tunnel", "Detect DNS tunneling and beaconing in PCAPs",
     "Flag data is moved through DNS queries (labels encode chunks) or hidden in beacon intervals inside a capture.",
     "Parse DNS queries with tshark/zeek, decode label entropy, and reassemble the tunneled payload.",
     "DNS tunnel detection compares query entropy, label length and cadence against a baseline; C2-style beaconing leaves the same signature.",
     ["tshark", "zeek", "dnscat2", "pcap-bloodhound"],
     ["https://github.com/iagox86/dnscat2", WU],
     [("T1071.004", "DNS", "DNS tunneling; CTFT adds the decoding recipe.")],
     "No direct ATT&CK equivalent."),
    ("NET", "003", "SMB enumeration barrier", "Enumerate SMB shares/versions",
     "The flag is inside an SMB share whose name or permissions are part of the puzzle; protocol version mismatches hide content.",
     "Enumerate shares and dialect with smbclient/nmap scripts, list anonymously, and download the flag file.",
     "SMB session logs and share enumeration are standard IR steps; auditing records who listed what and when.",
     ["smbclient", "enum4linux", "crackmapexec", "nmap"],
     ["https://www.samba.org/", WU],
     [("T1021.002", "SMB/Windows Admin Shares", "Share enumeration mirrors admin-share access patterns.")],
     "No direct ATT&CK equivalent."),
    ("NET", "004", "Wi-Fi capture / handshake concealment", "Crack WPA2 handshakes, decode Wi-Fi captures",
     "The flag rides over Wi-Fi: the challenge ships a .cap with a WPA handshake or encrypted frames, and the passphrase is the gate.",
     "Extract the EAPOL 4-way handshake, run dictionary attacks (aircrack/hashcat mode 22000), then decrypt frames to read the flag.",
     "Wireless captures preserve association, handshake and traffic timing; cracking is governed by lab scope.",
     ["aircrack-ng", "hashcat", "hcxdumptool", "Wireshark"],
     ["https://www.aircrack-ng.org/", WU],
     [("T1040", "Network Sniffing", "Wi-Fi capture echoes network sniffing; ATT&CK omits the handshake-cracking craft.")],
     "No direct ATT&CK equivalent."),
    ("NET", "005", "Traffic tunnel / port-forwarding relay", "Pivot via ssh -L/-R, chisel",
     "The flag service is only reachable through a pivot host; direct connections fail.",
     "Relay traffic through the pivot (ssh -L/-R, chisel, socat) and reach the internal service.",
     "Tunnel artifacts appear as long-lived SSH/chisel sessions in logs; defenders track them as pivot-chain evidence.",
     ["ssh", "chisel", "socat", "proxychains"],
     ["https://github.com/jpillora/chisel", WU],
     [("T1572", "Protocol Tunneling", "Tunnel establishment mirrors protocol tunneling."),
      ("T1090", "Proxy", "Relay usage echoes proxy pivoting.")],
     "No direct ATT&CK equivalent."),
    ("NET", "006", "TTL / protocol-field covert channel", "Decode TTL/ICMP/padding channels",
     "Each packet's TTL (or ICMP type / payload padding) encodes one character; the flag is spread across a capture's protocol fields.",
     "Extract per-packet fields with tshark/scapy, map TTL deltas to characters, and reassemble the message.",
     "Covert-channel detection looks for unnatural field distributions; the same extraction logic serves both solver and analyst.",
     ["tshark", "scapy", "Wireshark"],
     ["https://scapy.net/", WU],
     [("T1095", "Non-Application Layer Protocol", "Field-level covert channels; ATT&CK omits the decoding detail.")],
     "No direct ATT&CK equivalent."),
    ("NET", "007", "Packet-capture forensics maze", "Run beaconing/exfil/credential detectors over PCAPs",
     "The flag is split among many packets or buried in protocol noise; the capture mixes decoys and real artifacts.",
     "Profile the capture (endpoints, protocols, timing), run detectors (beaconing, DNS tunnel, credentials, exfiltration) and pivot on the anomalies.",
     "PCAP analysis is core DFIR: detector output becomes an annotated timeline of what happened on the wire.",
     ["tshark", "Wireshark", "zeek", "pcap-bloodhound"],
     ["https://tshark.dev/", WU],
     [("T1040", "Network Sniffing", "Captured-traffic analysis echoes network-sniffing sources.")],
     "No direct ATT&CK equivalent."),
    # ---------------- FOR ----------------
    ("FOR", "019", "JPEG marker / DCT coefficient corruption", "Repair JPEG segments and decode DCT coefficients",
     "JPEG structure is tampered: extraneous bytes before the EOI marker, corrupted quantization tables, or DCT-coefficient tricks hide data.",
     "Parse JPEG segments (SOI..EOI), locate the real image data, repair markers and quantization tables, and decode DCT coefficients.",
     "JPEG repair is carving-adjacent: structural anomalies pinpoint the tampered region and often reveal embedded data.",
     ["xxd", "Python PIL", "jpegio", "binwalk"],
     ["https://github.com/corkami/pics", WU],
     [("T1027", "Obfuscated Files or Information", "Structural tampering echoes obfuscation; ATT&CK omits the JPEG repair craft.")],
     "No ATT&CK equivalent."),
    ("FOR", "020", "LUKS-encrypted volume concealment", "Recover LUKS headers/keyslots, bruteforce passphrase",
     "A partition is LUKS-encrypted and the passphrase (or a keyslot) is part of the puzzle; the flag is inside the decrypted filesystem.",
     "Identify LUKS headers/keyslots, attack the passphrase (dictionary/bruteforce via luks2john), unlock and mount the volume.",
     "Encrypted-media recovery must preserve header integrity; keyslot iteration counts and header backups decide feasibility.",
     ["cryptsetup", "luks2john", "hashcat", "dd"],
     ["https://gitlab.com/cryptsetup/cryptsetup", WU],
     [("T1486", "Data Encrypted for Impact", "Adversarial volume encryption; CTFT recovers it.")],
     "No ATT&CK equivalent."),
    ("FOR", "021", "LVM fragment/concat volume labyrinth", "Reassemble LVM logical volumes and mount",
     "The flag sits in an LVM volume assembled from scattered physical volumes or fragmented extents; naive mounting fails.",
     "Scan PVs/LVs, assemble the volume group, and mount the logical volume to read the flag.",
     "Volume reassembly mirrors RAID/LVM reconstruction: metadata blocks (PV headers) are the map.",
     ["pvscan", "vgscan", "lvdisplay", "mount"],
     ["https://man7.org/linux/man-pages/man8/lvm.8.html", WU],
     [("T1564", "Hide Artifacts", "Volume-level concealment; ATT&CK covers artifact hiding only generically.")],
     "No ATT&CK equivalent."),
    ("FOR", "022", "Deleted-file / open-handle recovery", "Recover deleted files via /proc handles, journal, carving",
     "The flag file is deleted but still open by a process, or recoverable from journal/extent remnants.",
     "Recover via /proc/<pid>/fd open handles, extundelete, journal replay, or raw carving.",
     "Deleted-file recovery is standard DFIR; open handles and journal remnants outlive directory entries.",
     ["ls -l /proc/*/fd", "extundelete", "debugfs", "foremost"],
     ["https://github.com/sleuthkit/sleuthkit", WU],
     [("T1070.004", "File Deletion", "Deletion-based hiding; CTFT reverses it.")],
     "No ATT&CK equivalent."),
    ("FOR", "023", "SELinux context-based concealment", "Analyze SELinux contexts blocking artifacts",
     "Files are labeled with SELinux contexts that deny access; the flag is present but context-blocked.",
     "Inspect contexts (ls -Z), identify the blocking policy, and read the file through allowed contexts or policy relaxation.",
     "Label forensics shows what a process could touch; context anomalies point at hidden artifacts.",
     ["ls -Z", "semanage", "audit2allow", "setenforce"],
     ["https://selinuxproject.org/", WU],
     [("T1562", "Impair Defenses", "Policy-based hiding echoes defense impairment.")],
     "No ATT&CK equivalent."),
    ("FOR", "024", "Browser-profile artifact concealment", "Parse Firefox/SQLite artifacts (places, logins, cookies)",
     "The flag is inside a browser profile: bookmarks, history, saved logins, cookies or localStorage.",
     "Open the profile's SQLite databases (places.sqlite, logins.json, cookies) and extract the flag.",
     "Browser artifacts are first-class DFIR evidence; parsing must preserve WAL/uncommitted rows.",
     ["sqlite3", "sqlitebrowser", "firefox_decrypt"],
     ["https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data", WU],
     [("T1217", "Browser Information Discovery", "Browser artifact mining; CTFT adds profile-parsing detail.")],
     "No direct ATT&CK technique."),
    ("FOR", "025", "PDF object/stream hiding", "Parse PDF xref, streams and filters",
     "The flag is inside PDF objects/streams (FlateDecode), hidden annotations, or appended after %%EOF.",
     "Parse the xref, decompress streams (qpdf/pdftk), and dump objects for strings.",
     "PDFs are compound artifacts; unparsed objects and post-EOF data are classic hiding spots.",
     ["qpdf", "pdftk", "pdf-parser.py", "strings"],
     ["https://blog.didierstevens.com/programs/pdf-tools/", WU],
     [("T1027", "Obfuscated Files or Information", "Container-level hiding echoes obfuscation.")],
     "No ATT&CK equivalent."),
    ("FOR", "026", "Memory-image OS-artifact recovery", "Extract registry/services/process artifacts from memory images",
     "The flag exists only in a Windows/Linux memory dump: registry hives, services, console history or process memory.",
     "Profile the image (volatility3), enumerate processes/registry, scan strings, and dump the owning structures.",
     "Memory forensics reconstructs transient OS state; plugin selection depends on the OS profile.",
     ["volatility3", "strings", "yara", "bulk_extractor"],
     ["https://github.com/volatilityfoundation/volatility3", WU],
     [("T1003", "OS Credential Dumping", "Memory extraction mirrors credential-dumping data sources.")],
     "No ATT&CK equivalent."),
    # ---------------- REV ----------------
    ("REV", "006", "Java bytecode / JAR obfuscation", "Decompile and deobfuscate JVM bytecode",
     "The flag check lives in obfuscated or compiled Java (JAR/class); strings and control flow are mangled.",
     "Decompile with CFR/JD-GUI, recover strings, trace the flag check, and reimplement the logic.",
     "Java artifacts preserve bytecode-level evidence; decompilers reconstruct behavior without the source.",
     ["CFR", "jd-gui", "javap", "procyon"],
     ["https://github.com/leibnitz27/cfr", WU],
     [("T1027", "Obfuscated Files or Information", "Bytecode obfuscation.")],
     "No ATT&CK equivalent."),
    ("REV", "007", "Python bytecode (.pyc/.pyo) concealment", "Decompile Python bytecode",
     "Only compiled .pyc/.pyo files ship; the flag logic is bytecode-only.",
     "Disassemble (dis/pycdc), decompile (uncompyle6/decompyle3), and recover the logic.",
     "Bytecode analysis works without running the interpreter; marshal headers reveal the Python version.",
     ["pycdc", "uncompyle6", "decompyle3", "dis"],
     ["https://github.com/zrax/pycdc", WU],
     [("T1027", "Obfuscated Files or Information", "Compiled-only distribution hides logic.")],
     "No ATT&CK equivalent."),
    ("REV", "008", "Functional-language binary concealment", "Reverse Haskell/functional compiled artifacts",
     "The binary is compiled Haskell (GHC runtime); closures and lazy evaluation obscure the flag logic.",
     "Locate GHC runtime entry points, identify CAFs and string literals, and reconstruct the evaluation.",
     "Functional binaries differ from C: symbol-heavy GHC RTS artifacts still expose strings and structure.",
     ["ghidra", "radare2", "strings"],
     ["https://github.com/radareorg/radare2", WU],
     [("T1027", "Obfuscated Files or Information", "Unusual-runtime binaries resist analysis.")],
     "No ATT&CK equivalent."),
    ("REV", "009", "Assembly-level code-golf / shellcode RE", "Disassemble and annotate asm snippets",
     "The flag check is a raw asm snippet or mini shellcode; brevity and tricks obscure intent.",
     "Disassemble (nasm/objdump/radare2), annotate registers and stack, and trace the check.",
     "Raw instruction sequences are analyzed the same way as extracted shellcode evidence.",
     ["nasm", "objdump", "radare2", "ghidra"],
     ["https://www.nasm.us/", WU],
     [("T1027", "Obfuscated Files or Information", "Code-golf obfuscation.")],
     "No ATT&CK equivalent."),
    # ---------------- PWN ----------------
    ("PWN", "006", "Stack canary / PIE / ASLR hardening puzzle", "Leak canary/PIE base, ret2libc",
     "The flag requires defeating canary, PIE and ASLR in a binary with a stack overflow.",
     "Leak the canary and PIE base via format/read leaks, then ret2libc to the win path.",
     "Exploit-development notes document the bypass chain; mitigations are the defensive counterpart.",
     ["pwntools", "gdb", "pwninit", "one_gadget"],
     ["https://github.com/Gallopsled/pwntools", WU],
     [("T1068", "Exploitation for Privilege Escalation", "Mitigation-bypass exploitation; ATT&CK omits the mechanics.")],
     "No ATT&CK equivalent."),
    ("PWN", "007", "Kernel/mseal-guarded memory puzzle", "Exploit kernel-module or mseal protections",
     "The flag requires a kernel-module exploit or bypassing new memory protections (mseal, KASLR).",
     "Analyze the module/interface, bypass mseal/KASLR, and escalate to read the flag.",
     "Kernel-layer artifacts (modules, memory protections) extend DFIR below userland.",
     ["gdb", "qemu", "pahole", "pwntools"],
     ["https://www.kernel.org/doc/", WU],
     [("T1068", "Exploitation for Privilege Escalation", "Kernel-layer escalation.")],
     "No ATT&CK equivalent."),
    ("PWN", "008", "Shellcode craft & encoding constraints", "Generate/encode shellcode (alphanumeric, null-free)",
     "The exploit must deliver shellcode under constraints: no nulls, alphanumeric only, or length limits.",
     "Generate or encode shellcode (msfvenom, custom encoders) and deliver it through the constrained path.",
     "Encoded shellcode shows the same encoder fingerprints in memory dumps as in exploit artifacts.",
     ["msfvenom", "pwntools shellcraft", "nasm"],
     ["https://github.com/Gallopsled/pwntools", WU],
     [("T1055", "Process Injection", "Shellcode delivery mirrors injection payloads.")],
     "No ATT&CK equivalent."),
    # ---------------- CRY ----------------
    ("CRY", "008", "Block-cipher mode / AES implementation weakness", "Attack AES modes (padding oracle, IV flaws)",
     "AES is used with a weak mode (ECB patterns, predictable IV, padding oracle); the flag ciphertext is given.",
     "Attack the mode: padding oracle, IV reuse, or ECB block analysis to recover plaintext.",
     "Weak-mode signatures (repeated blocks) identify misconfigured crypto in artifacts.",
     ["CyberChef", "pycryptodome", "padbuster"],
     ["https://github.com/AonCyberLabs/PadBuster", WU],
     [("T1573.001", "Symmetric Cryptography", "Misused symmetric crypto; ATT&CK omits the attack detail.")],
     "No ATT&CK equivalent."),
    ("CRY", "009", "Stream-cipher keystream reuse (Salsa20)", "Exploit keystream reuse to recover plaintext",
     "Two messages are encrypted under the same Salsa20 key/nonce; the XOR of ciphertexts leaks plaintext.",
     "XOR the ciphertexts, crib-drag the keystream, and recover both messages.",
     "Keystream reuse is detectable from ciphertext similarity; key-management flaws surface in logs.",
     ["CyberChef", "Python", "cribdrag"],
     ["https://github.com/SpiderLabs/cribdrag", WU],
     [("T1573.001", "Symmetric Cryptography", "Nonce-reuse cryptanalysis.")],
     "No ATT&CK equivalent."),
    ("CRY", "010", "Certificate / PEM / ASN.1 field hiding", "Parse certificates and extract hidden fields",
     "The flag is stashed in certificate fields (subject, extensions, serial) or in the ASN.1 structure.",
     "Parse with openssl x509 -text, decode DER/ASN.1, and inspect every field for the flag.",
     "Certificate inspection is routine; unusual extensions or serials are immediate artifacts.",
     ["openssl", "dumpasn1", "Python cryptography"],
     ["https://www.openssl.org/", WU],
     [("T1552.001", "Credentials in Files", "Certificates as secret carriers.")],
     "No ATT&CK equivalent."),
    ("CRY", "011", "Protocol implementation flaw (Heartbleed-style)", "Reproduce protocol memory-leak vulnerabilities",
     "The challenge emulates a protocol memory-leak flaw (Heartbleed-style); the flag leaks from server memory.",
     "Craft the malformed heartbeat/request, read the leaked buffer, and extract the flag.",
     "Protocol memory leaks are historical CVE evidence; reproduction is documented safely in labs.",
     ["openssl", "Python socket"],
     ["https://heartbleed.com/", WU],
     [("T1190", "Exploit Public-Facing Application", "Public-protocol memory-leak exploitation.")],
     "No ATT&CK equivalent."),
    ("CRY", "012", "Hash-cracking maze with constraints", "Crack hashes under masks/rules",
     "The flag is a hash whose preimage satisfies extra constraints (mask, salt, charset).",
     "Identify the hash type, build masks/rules, crack with hashcat/john, and verify.",
     "Hash recovery is standard evidence processing; salt and algorithm identification come first.",
     ["hashcat", "john", "hashid"],
     ["https://hashcat.net/hashcat/", WU],
     [("T1110", "Brute Force", "Credential-hash brute force; CTFT adds mask/rule craft.")],
     "No ATT&CK equivalent."),
    ("CRY", "013", "Nonstandard-alphabet substitution (braille, cetacean)", "Transcode nonstandard alphabets",
     "The flag is encoded in a nonstandard alphabet: Braille, cetacean/whale-speak, or a custom substitution.",
     "Identify the alphabet, transcode to plaintext, and decode.",
     "Unusual encodings are catalogued as data-obfuscation families; transcoding is deterministic.",
     ["CyberChef", "dcode.fr", "Python"],
     ["https://www.dcode.fr/", WU],
     [("T1140", "Deobfuscate/Decode Files or Information", "Encoding-layer deobfuscation.")],
     "No ATT&CK equivalent."),
    # ---------------- STE ----------------
    ("STE", "010", "Audio-domain stego beyond spectrograms (LSB/phase/DTMF/SSTV)", "Detect and decode audio-domain stego",
     "Data hides in audio beyond the spectrogram: LSB of samples, phase coding, DTMF tones, or SSTV frames.",
     "Analyze waveform/spectrum, decode DTMF/SSTV, or extract LSB/phase payloads.",
     "Audio analysis plots (waveform/spectrum/spectrogram) expose unnatural carriers; decoder selection follows the carrier type.",
     ["Audacity", "sox", "multimon-ng", "qsstv"],
     ["https://github.com/EliasOenal/multimon-ng", WU],
     [("T1001.002", "Steganography", "Audio-domain data hiding.")],
     "No ATT&CK equivalent."),
    ("STE", "011", "Palette / bitplane LSB tricks", "Analyze bitplanes and palette-based LSB",
     "The flag hides in bitplanes or palette indexes of an image (LSB across planes, palette reordering).",
     "Split bitplanes, analyze palette anomalies, and extract the hidden bits.",
     "Bitplane/palette analysis is standard steganalysis; visual inspection of planes reveals structure.",
     ["zsteg", "ImageMagick", "Stegsolve"],
     ["https://github.com/zed-0xff/zsteg", WU],
     [("T1001.002", "Steganography", "Image-domain data hiding.")],
     "No ATT&CK equivalent."),
    # ---------------- WEB ----------------
    ("WEB", "010", "LFI / log poisoning / php-filter chains", "Exploit LFI to RCE or flag read",
     "A local file include lets the solver read the flag or reach RCE through log poisoning or PHP filter chains.",
     "Use wrapper/filter chains (php://filter), poison logs with payloads, and include the flag or a shell.",
     "Web logs retain LFI probe fingerprints; filter-chain requests are distinctive.",
     ["Burp Suite", "curl", "php filter-chain generator"],
     ["https://github.com/synacktiv/php_filter_chain_generator", WU],
     [("T1190", "Exploit Public-Facing Application", "Public-app LFI exploitation.")],
     "No direct ATT&CK technique."),
    ("WEB", "011", "Directory-traversal maze", "Traverse filtered paths (PHP labyrinth)",
     "Path filters block traversal; the flag file is reachable only through filter quirks.",
     "Bypass the filters (encodings, absolute paths, null bytes) and traverse to the flag file.",
     "Traversal attempts appear as ../ patterns in access logs.",
     ["Burp Suite", "curl", "ffuf"],
     ["https://github.com/ffuf/ffuf", WU],
     [("T1190", "Exploit Public-Facing Application", "Path-traversal exploitation.")],
     "No direct ATT&CK technique."),
    ("WEB", "012", "XSS-driven flag exfiltration", "Craft XSS payloads (stored/reflected/DOM)",
     "The flag is delivered to an admin/bot that visits attacker-controlled content; XSS triggers the read.",
     "Craft stored/reflected/DOM payloads that read the flag and exfiltrate it.",
     "XSS artifacts live in page source, logs and browser history; CSP reports corroborate.",
     ["Burp Suite", "browser devtools"],
     ["https://portswigger.net/web-security/cross-site-scripting", WU],
     [("T1059.007", "JavaScript", "Browser-executed script craft; ATT&CK omits XSS mechanics.")],
     "No direct ATT&CK technique."),
    ("WEB", "013", "CSRF-gated state change", "Forge cross-site requests",
     "The flag is released only after a state change that requires a forged cross-site request from the victim session.",
     "Forge the cross-site request (form auto-submit) to trigger the state change and capture the flag.",
     "CSRF attempts are visible as cross-origin referer mismatches and suspicious requests in logs.",
     ["Burp Suite", "browser"],
     ["https://owasp.org/www-community/attacks/csrf", WU],
     [("T1606", "Forge Web Credentials", "Cross-site forgery of web interactions.")],
     "No direct ATT&CK technique."),
    ("WEB", "014", "WebSocket message hiding", "Intercept and decode WebSocket traffic",
     "The flag travels over a WebSocket channel; plain HTTP tools miss it.",
     "Intercept the WS upgrade and frames (Burp/Chrome), replay and decode the messages.",
     "WebSocket sessions are full-duplex artifacts; frame capture requires the upgrade context.",
     ["Burp Suite", "Chrome devtools", "websocat"],
     ["https://github.com/vi/websocat", WU],
     [("T1071.001", "Web Protocols", "Hidden channels over web protocols.")],
     "No direct ATT&CK technique."),
    ("WEB", "015", "CMS / WordPress plugin flaw", "Enumerate and exploit WordPress (wpscan)",
     "The flag hides behind a vulnerable WordPress plugin/theme or weak admin credentials.",
     "Enumerate plugins/users with wpscan, exploit the flaw or crack the login, and read the flag.",
     "CMS logs record plugin-abuse patterns; version banners pin the vulnerable surface.",
     ["wpscan", "curl", "hydra"],
     ["https://wpscan.com/wordpress-security-scanner", WU],
     [("T1190", "Exploit Public-Facing Application", "CMS exploitation.")],
     "No direct ATT&CK technique."),
    ("WEB", "016", "NoSQL injection", "Inject Mongo/NoSQL queries",
     "The flag query is gated by a NoSQL (Mongo) filter; operator injection bypasses it.",
     "Inject NoSQL operators ($gt/$ne/$where) to bypass auth/filters and dump the flag.",
     "NoSQL payloads ($ operators) appear in application logs; unusual query shapes are the tell.",
     ["Burp Suite", "mongosh", "NoSQLMap"],
     ["https://github.com/codingo/NoSQLMap", WU],
     [("T1190", "Exploit Public-Facing Application", "Injection on public apps.")],
     "No direct ATT&CK technique."),
    ("WEB", "017", "Host-header / vhost fuzzing", "Fuzz vhosts and host headers",
     "The flag app is served only under a specific Host header or virtual host.",
     "Fuzz Host headers and vhost names (ffuf/gobuster) and reach the hidden vhost.",
     "Vhost discovery correlates TLS SNI and Host headers in proxy logs.",
     ["ffuf", "gobuster", "Burp Intruder"],
     ["https://github.com/ffuf/ffuf", WU],
     [("T1083", "File and Directory Discovery", "Vhost / host-header discovery.")],
     "No direct ATT&CK technique."),
    # ---------------- OSI ----------------
    ("OSI", "006", "Git-repository archaeology", "Mine git history, objects and reflog",
     "The flag (or a credential) is in git history: old commits, dangling objects, or reflog entries.",
     "Mine the repository: git log, reflog, dangling objects, and search every blob.",
     "Git archaeology recovers deleted content deterministically from object storage.",
     ["git", "gitgrabber", "trufflehog"],
     ["https://github.com/trufflesecurity/trufflehog", WU],
     [("T1596", "Search Open Technical Databases", "Repository mining for secrets.")],
     "No direct ATT&CK technique."),
    ("OSI", "007", "Search-engine mining (dorking)", "Run advanced dorks and search operators",
     "The flag content is indexed but only findable through precise search operators.",
     "Run advanced dorks (site:, inurl:, filetype:) to surface the indexed flag material.",
     "Dorking is documented OSINT methodology; queries are logged and reproducible.",
     ["Google/Bing dorks", "googlesearch-python"],
     ["https://www.exploit-db.com/google-hacking-database", WU],
     [("T1593.002", "Search Engines", "Search-engine OSINT; CTFT adds operator craft.")],
     "No direct ATT&CK technique."),
    ("OSI", "008", "ASN / IP-range / subdomain recon", "Map ASN, ranges, subdomains (bbot, assetfinder)",
     "The flag lives on infrastructure hidden among an ASN/IP range or a forgotten subdomain.",
     "Map ASN/ranges, enumerate subdomains (bbot, assetfinder), resolve and scan the attack surface.",
     "Infrastructure mapping is standard attribution work; asset inventories are rebuilt the same way.",
     ["bbot", "assetfinder", "amass", "dnsx"],
     ["https://github.com/blacklanternsecurity/bbot", WU],
     [("T1596.001", "DNS/Passive DNS", "DNS/asset enumeration.")],
     "No direct ATT&CK technique."),
    # ---------------- CLD ----------------
    ("CLD", "006", "Cross-account role chaining / trust abuse", "Chain sts:AssumeRole across accounts",
     "The flag is in a second AWS account reachable only by chaining role assumptions through trust relationships.",
     "Enumerate roles, chain sts:AssumeRole across accounts, and reach the target resources.",
     "CloudTrail records every AssumeRole hop; the chain is reconstructible from role ARNs.",
     ["awscli", "enumerate-iam", "pacu"],
     ["https://github.com/RhinoSecurityLabs/pacu", WU],
     [("T1078.004", "Cloud Accounts", "Role-based cloud account access.")],
     "No direct ATT&CK technique."),
    ("CLD", "007", "Cloud NoSQL-store misconfiguration", "Enumerate and query exposed cloud databases",
     "A cloud NoSQL store (DynamoDB or similar) is exposed or over-permissioned and holds the flag.",
     "Enumerate the table/index, query it with the available permissions, and read the flag.",
     "Cloud database exposure is logged via CloudTrail; scan results document the misconfiguration.",
     ["awscli dynamodb", "NoSQLMap", "boto3"],
     ["https://boto3.amazonaws.com/v1/documentation/api/latest/index.html", WU],
     [("T1213", "Data from Information Repositories", "Cloud data-store enumeration.")],
     "No direct ATT&CK technique."),
    ("CLD", "008", "Azure management-plane misconfiguration", "Enumerate Azure AD/VM/storage from credentials",
     "Leaked Azure credentials unlock management-plane access where the flag sits (AD users, VMs, storage).",
     "Use the credentials against the management plane: enumerate AD, VMs and storage accounts, and extract the flag.",
     "Azure AD sign-in logs and activity logs document every management-plane call.",
     ["azure-cli", "Az PowerShell", "AADInternals"],
     ["https://learn.microsoft.com/en-us/cli/azure/", WU],
     [("T1078.004", "Cloud Accounts", "Management-plane access from valid cloud credentials.")],
     "No direct ATT&CK technique."),
    # ---------------- AIM ----------------
    ("AIM", "006", "Self-hosted LLM platform misconfiguration", "Audit ollama/oobabooga deployments for exposed endpoints",
     "A self-hosted LLM (ollama/oobabooga) is exposed or misconfigured; the flag hides in model outputs, endpoints, or host files.",
     "Enumerate the exposed endpoints/APIs, query the model, and pivot to the host if the deployment is over-permissive.",
     "LLM deployment logs record queries and endpoints; exposure scanning is the same as any service audit.",
     ["ollama CLI", "curl", "nmap"],
     ["https://github.com/ollama/ollama", WU],
     [("T1190", "Exploit Public-Facing Application", "Exposed LLM endpoints.")],
     "No ATT&CK equivalent."),
    ("AIM", "007", "Agent / tool-calling guardrail bypass", "Bypass agent tool policies",
     "An agent is constrained by guardrails over its tools; the flag requires coaxing it past the policy.",
     "Craft prompts/tool-call sequences that bypass the guardrails and retrieve the flag.",
     "Agent logs replay the tool-call trace; guardrail violations are auditable events.",
     ["Python", "agent CLIs"],
     ["https://github.com/microsoft/autogen", WU],
     [],
     "No ATT&CK equivalent; emerging LLM-security craft."),
    # ---------------- FPN ----------------
    ("FPN", "008", "Linux local privesc chain (SUID, ACLs, sudo, capabilities)", "Enumerate and chain Linux privesc vectors",
     "The flag is root-only; escalation requires chaining SUID binaries, ACLs, sudo rules or capabilities.",
     "Enumerate privesc vectors (linpeas), exploit one or chain several, and read the flag.",
     "Privilege-boundary audits list SUID/capability drift; escalation paths leave execve logs.",
     ["linpeas", "pspy", "GTFOBins"],
     ["https://gtfobins.github.io/", WU],
     [("T1068", "Exploitation for Privilege Escalation", "Escalation exploitation."),
      ("T1548", "Abuse Elevation Control Mechanism", "SUID/sudo/capability abuse.")],
     "No direct ATT&CK technique."),
    ("FPN", "009", "Redis/NoSQL service misconfiguration chain", "Enumerate Redis/Mongo/MySQL, dump or RCE",
     "An internal DB service is misconfigured (no auth, weak credentials); the flag is in the data or reachable via RCE.",
     "Enumerate the service, dump data or achieve code execution, and pivot to the flag.",
     "DB access logs and audit trails record the enumeration and exfiltration.",
     ["redis-cli", "mongosh", "mysql", "crackmapexec"],
     ["https://redis.io/docs/latest/commands/", WU],
     [("T1213", "Data from Information Repositories", "Database data extraction.")],
     "No direct ATT&CK technique."),
    ("FPN", "010", "Reverse-shell delivery & listener operations", "Catch, upgrade and persist reverse shells",
     "The flag requires a stable reverse shell through restricted channels (firewalls, encodings).",
     "Deliver a reverse shell (bash/python/php), catch it with a listener, upgrade to a PTY, and persist.",
     "Reverse shells leave outbound connection signatures; listener-side artifacts document the callback.",
     ["netcat", "pwncat", "socat"],
     ["https://github.com/calebstewart/pwncat", WU],
     [("T1059", "Command and Scripting Interpreter", "Command-shell channel establishment.")],
     "No direct ATT&CK technique."),
    # ---------------- GAM / COD / JAL ----------------
    ("GAM", "006", "Chatbot / choice-path bot puzzle", "Script a bot interaction to reach the win branch",
     "A chatbot or choice-path bot hides the flag behind a specific interaction branch.",
     "Script the interaction (automate the choices) to reach the win branch and capture the flag.",
     "Bot transcripts are replayable evidence; choice sequences reproduce the path.",
     ["pwntools", "Python requests"],
     ["https://github.com/Gallopsled/pwntools", WU],
     [("T1071", "Application Layer Protocol", "Scripted application-layer interaction.")],
     "No ATT&CK equivalent."),
    ("COD", "006", "Combinatorial enumeration puzzle", "Generate permutations/combinations efficiently",
     "The flag key is a permutation/combination of inputs; naive search is too slow.",
     "Generate permutations/combinations efficiently (itertools, backtracking) to find the satisfying one.",
     "Combinatorial solutions are deterministic; the program is the evidence of the method.",
     ["Python itertools", "C++"],
     ["https://docs.python.org/3/library/itertools.html", WU],
     [],
     "No ATT&CK equivalent; competitive-programming puzzle craft."),
    ("COD", "007", "Grid/logic-constraint puzzle (Sudoku)", "Solve constraint grids programmatically",
     "The flag requires solving a Sudoku or constraint grid programmatically.",
     "Model the constraints (backtracking/SAT) and solve the grid to extract the flag.",
     "Constraint puzzles are pure computation; solvers double as verifiers.",
     ["Python", "z3"],
     ["https://github.com/Z3Prover/z3", WU],
     [],
     "No ATT&CK equivalent; constraint-satisfaction craft."),
    ("JAL", "006", "WSL-interop sandbox escape", "Escape WSL-interop boundaries",
     "The flag is on the Windows host or on the other side of a WSL interop boundary; the WSL shell is confined.",
     "Abuse WSL interop (interop binaries, mounts) to cross the boundary and read the host flag.",
     "WSL interop activity maps to process and mount artifacts on both OS sides.",
     ["wsl.exe", "bash", "interop binaries"],
     ["https://learn.microsoft.com/en-us/windows/wsl/", WU],
     [("T1611", "Escape to Host", "WSL-to-host boundary escape.")],
     "No ATT&CK equivalent."),
]

TACTIC_BOILERPLATE = """## Relation to MITRE ATT&CK

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


---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
"""

TECHNIQUE_HEADER = """# {tech_id} — {tname}

> **Type:** Design / Hide Technique  
> **Tactic:** [`{tactic_id}`](../tactics/{tactic_id}.md) — {tactic_name}  
> **Paired counter-technique:** [`{counter_id}`](../countertechniques/{counter_id}.md) — {cname}

---

## How the challenge author hides

{hide}

"""

COUNTER_HEADER = """# {counter_id} — {cname}

> **Type:** Counter-Technique  
> **Tactic:** [`{tactic_id}`](../tactics/{tactic_id}.md) — {tactic_name}  
> **Counters technique:** [`{tech_id}`](../techniques/{tech_id}.md) — {tname}

---

## Offensive Recovery (CTF practitioner / solver)

{off}

## Forensic / Blue-Team Perspective (DFIR analyst)

{forensic}

"""


def attack_table(rows: list[tuple[str, str, str]], none_note: str) -> str:
    lines = ["## Related MITRE ATT&CK", "",
             "| ATT&CK ID | ATT&CK technique | Relation note |",
             "| --- | --- | --- |"]
    if rows:
        for att_id, name, note in rows:
            lines.append(f"| {att_id} | {name} | {note} |")
    else:
        lines.append(f"| \u2014 | \u2014 | {none_note} |")
    return "\n".join(lines)


def tool_refs(tools: list[str], refs: list[str]) -> str:
    out = ["## Tools", ""]
    out += [f"- {t}" for t in tools]
    out += ["", "## References", ""]
    out += [f"- {r}" for r in refs]
    return "\n".join(out)


def excerpt(rows: list[tuple[str, str, str]], none_note: str) -> str:
    return " / ".join(att_id for att_id, _n, _r in rows) if rows else none_note


def make_tactic_page(cat: str) -> str:
    return (
        f"# {cat} — {TACTIC_NAMES[cat]}\n\n"
        f"> **Tactic ID:** `CTFT-TA-{cat}`  \n"
        f"> **HTB mapping:** HTB: Misc (Network)  \n"
        f"> **Techniques:** 0\n\n"
        "## Description\n\n"
        "Hiding flags behind network discovery, sniffing, tunneling and protocol-barrier puzzles.\n\n"
        f"{TACTIC_BOILERPLATE}"
    )


def main() -> None:
    technique_dir = ROOT / "techniques"
    counter_dir = ROOT / "countertechniques"
    tactic_dir = ROOT / "tactics"

    net_tactic = tactic_dir / "CTFT-TA-NET.md"
    if not net_tactic.exists():
        net_tactic.write_text(make_tactic_page("NET"), encoding="utf-8")
        print(f"created {net_tactic.relative_to(ROOT)}")

    rows_by_cat: dict[str, list[str]] = defaultdict(list)
    created = 0
    for cat, num, tname, cname, hide, off, forensic, tools, refs, attack, none_note in ENTRY_LIST:
        tech_id = f"CTFTTE-{cat}-{num}"
        counter_id = f"CTFTCTE-{cat}-{num}"
        tactic_id = f"CTFT-TA-{cat}"
        tactic_name = TACTIC_NAMES[cat]

        tech_path = technique_dir / f"{tech_id}.md"
        counter_path = counter_dir / f"{counter_id}.md"

        tech_text = TECHNIQUE_HEADER.format(
            tech_id=tech_id, tname=tname, tactic_id=tactic_id, tactic_name=tactic_name,
            counter_id=counter_id, cname=cname, hide=hide,
        ) + attack_table(attack, none_note) + "\n\n" + tool_refs(tools, refs) + "\n"

        counter_text = COUNTER_HEADER.format(
            counter_id=counter_id, cname=cname, tactic_id=tactic_id, tactic_name=tactic_name,
            tech_id=tech_id, tname=tname, off=off, forensic=forensic,
        ) + attack_table(attack, none_note) + "\n\n" + tool_refs(tools, refs) + "\n"

        if tech_path.exists():
            print(f"skip (exists): {tech_id}")
        else:
            tech_path.write_text(tech_text, encoding="utf-8")
            created += 1
        if counter_path.exists():
            print(f"skip (exists): {counter_id}")
        else:
            counter_path.write_text(counter_text, encoding="utf-8")
            created += 1

        row = (f"| [{tech_id}](../techniques/{tech_id}.md) | {tname} |"
               f" [{counter_id}](../countertechniques/{counter_id}.md) | {cname} |"
               f" {excerpt(attack, none_note)} |")
        rows_by_cat[cat].append(row)

    # Append rows + refresh counts on tactic pages.
    for cat, rows in rows_by_cat.items():
        path = tactic_dir / f"CTFT-TA-{cat}.md"
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        new_rows = [r for r in rows if r.split("](", 1)[0][2:] not in text]
        header_idx = next(i for i, line in enumerate(lines) if line.startswith("| --- |"))
        last_row_idx = max(
            (i for i, line in enumerate(lines) if line.startswith("| [CTFTTE-")),
            default=header_idx,
        )
        inserted = lines[: last_row_idx + 1] + new_rows + lines[last_row_idx + 1:]
        count = sum(1 for line in inserted if line.startswith("| [CTFTTE-"))
        merged = "\n".join(inserted) + "\n"
        merged = re.sub(r"\*\*Techniques:\*\* \d+", f"**Techniques:** {count}", merged, count=1)
        path.write_text(merged, encoding="utf-8")
        print(f"tactic {cat}: +{len(new_rows)} rows, Techniques: {count}")

    print(f"created {created} files")


ENTRY_LIST = ENTRIES

if __name__ == "__main__":
    main()
