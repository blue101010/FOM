#!/usr/bin/env python3
"""Attach the per-entry `## Related MITRE ATT&CK` table to every technique and
counter-technique page (SCHEMA_V2 §3.5).

The tactic pages used to be the only per-entry ATT&CK surface (an excerpt
column); this script promotes a curated ID -> ATT&CK mapping onto each entry
page so potentially related MITRE ATT&CK techniques are displayed where the
reader lands, and adds a pointer sentence on each tactic page.

Usage:
    python v2/attach_attack_related.py            # dry run (default)
    python v2/attach_attack_related.py --write    # apply to the corpus
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Curated mapping: "<CAT>-NNN" -> ([ (att&ck id, name, note), ... ], none-note)
# The none-note renders as a single explicit empty row when no ATT&CK technique
# is potentially related. Counter-techniques reuse their paired entry's list.
# ---------------------------------------------------------------------------
ATTACK: dict[str, tuple[list[tuple[str, str, str]], str]] = {
    # --- FOR — Forensics ---------------------------------------------------
    "FOR-001": ([("T1027", "Obfuscated Files or Information",
                  "ATT&CK omits the byte-level magic-header recovery detail.")], "No ATT&CK equivalent."),
    "FOR-002": ([("T1564", "Hide Artifacts",
                  "Slack/unallocated-space carving is media-forensics craft; ATT&CK covers artifact hiding only generically.")], "No ATT&CK equivalent."),
    "FOR-003": ([("T1070.006", "Timestomp",
                  "CTFT details MACB timestomping mechanics ATT&CK describes only at technique level.")], "No ATT&CK equivalent."),
    "FOR-004": ([("T1564.004", "NTFS File Attributes",
                  "ATT&CK covers ADS hiding; CTFT details enumeration and extraction.")], "No ATT&CK equivalent."),
    "FOR-005": ([("T1014", "Rootkit",
                  "Volatile-memory DFIR; ATT&CK models rootkit-style memory concealment only generically.")], "No ATT&CK equivalent."),
    "FOR-006": ([("T1573", "Encrypted Channel",
                  "PCAP payload obfuscation echoes encrypted-channel traffic; ATT&CK omits reassembly craft.")], "No ATT&CK equivalent."),
    "FOR-007": ([("T1027", "Obfuscated Files or Information",
                  "ATT&CK omits the byte-level header-recovery detail.")], "No ATT&CK equivalent."),
    "FOR-008": ([("T1027", "Obfuscated Files or Information",
                  "ATT&CK omits the byte-level header-recovery detail.")], "No ATT&CK equivalent."),
    "FOR-009": ([("T1027", "Obfuscated Files or Information",
                  "ATT&CK omits the byte-level magic-header repair detail.")], "No ATT&CK equivalent."),
    "FOR-010": ([("T1027", "Obfuscated Files or Information",
                  "Visual machine-readable encodings (QR) are CTF-specific obfuscation ATT&CK omits.")], "No ATT&CK equivalent."),
    "FOR-011": ([("T1027", "Obfuscated Files or Information",
                  "QR-code encodings are CTF-specific obfuscation ATT&CK omits.")], "No ATT&CK equivalent."),
    "FOR-012": ([("T1027", "Obfuscated Files or Information",
                  "rMQR encodings are CTF-specific obfuscation ATT&CK omits.")], "No ATT&CK equivalent."),
    "FOR-013": ([("T1027", "Obfuscated Files or Information",
                  "Diagram encodings are CTF-specific obfuscation ATT&CK omits.")], "No ATT&CK equivalent."),
    "FOR-014": ([("T1027", "Obfuscated Files or Information",
                  "Diagram encodings are CTF-specific obfuscation ATT&CK omits.")], "No ATT&CK equivalent."),
    "FOR-015": ([("T1027.002", "Software Packing",
                  "Packager obfuscation echoes software packing.")], "No ATT&CK equivalent."),
    "FOR-016": ([("T1027", "Obfuscated Files or Information",
                  "Date/time encodings are CTF-specific obfuscation ATT&CK omits.")], "No ATT&CK equivalent."),
    "FOR-017": ([("T1027", "Obfuscated Files or Information",
                  "Strings concealed in ELF binaries echo obfuscated payloads.")], "No ATT&CK equivalent."),
    "FOR-018": ([("T1564.001", "Hidden Files and Directories",
                  "MFT-level tampering extends hidden-file craft below ATT&CK granularity.")], "No ATT&CK equivalent."),
    # --- WEB — Web Exploitation ---------------------------------------------
    "WEB-001": ([("T1552.001", "Credentials in Files",
                  "Source-comment/endpoint hiding is CTF craft; credential discovery is the closest ATT&CK echo.")], "No direct ATT&CK technique."),
    "WEB-002": ([("T1213", "Data from Information Repositories",
                  "IDOR abuse echoes unauthorized data access from repositories.")], "No direct ATT&CK technique."),
    "WEB-003": ([("T1606", "Forge Web Credentials",
                  "JWT misconfiguration echoes web credential forgery.")], "No direct ATT&CK technique."),
    "WEB-004": ([("T1190", "Exploit Public-Facing Application",
                  "ATT&CK has no SQLi technique; public-application exploitation is the closest echo.")], "No direct ATT&CK technique."),
    "WEB-005": ([("T1190", "Exploit Public-Facing Application",
                  "SSTI echoes public-application exploitation.")], "No direct ATT&CK technique."),
    "WEB-006": ([("T1027", "Obfuscated Files or Information",
                  "Client-side JavaScript obfuscation.")], "No direct ATT&CK technique."),
    "WEB-007": ([("T1083", "File and Directory Discovery",
                  "Deployment-metadata disclosure echoes file/directory discovery.")], "No direct ATT&CK technique."),
    "WEB-008": ([("T1083", "File and Directory Discovery",
                  "8.3 short-name disclosure echoes filesystem discovery.")], "No direct ATT&CK technique."),
    "WEB-009": ([("T1552", "Unsecured Credentials",
                  "Configuration secret exposure echoes unsecured credentials.")], "No direct ATT&CK technique."),
    # --- CRY — Cryptography --------------------------------------------------
    "CRY-001": ([("T1573", "Encrypted Channel",
                  "Weak RSA parameter design; ATT&CK omits cryptanalytic key recovery.")], "No ATT&CK equivalent."),
    "CRY-002": ([("T1027", "Obfuscated Files or Information",
                  "Layered classical ciphers echo obfuscation rather than adversary crypto.")], "No ATT&CK equivalent."),
    "CRY-003": ([("T1573.001", "Symmetric Cryptography",
                  "ECB/repeating-XOR structural leakage; ATT&CK omits the cryptanalysis detail.")], "No ATT&CK equivalent."),
    "CRY-004": ([("T1573.001", "Symmetric Cryptography",
                  "Nonce-reuse consequences are cryptanalytic craft ATT&CK omits.")], "No ATT&CK equivalent."),
    "CRY-005": ([], "No ATT&CK equivalent; hash length-extension forgery craft."),
    "CRY-006": ([("T1140", "Deobfuscate/Decode Files or Information",
                  "Chained encodings echo deobfuscation/decoding.")], "No ATT&CK equivalent."),
    "CRY-007": ([("T1573.001", "Symmetric Cryptography",
                  "Predictable PRNG state undermines stream cryptography; recovery is CTF-specific.")], "No ATT&CK equivalent."),
    # --- PWN — Binary Exploitation -------------------------------------------
    "PWN-001": ([("T1068", "Exploitation for Privilege Escalation",
                  "Win-function backdoors echo privilege-escalation exploitation.")], "No ATT&CK equivalent."),
    "PWN-002": ([("T1068", "Exploitation for Privilege Escalation",
                  "Format-string leak/write mechanics are omitted by ATT&CK.")], "No ATT&CK equivalent."),
    "PWN-003": ([("T1068", "Exploitation for Privilege Escalation",
                  "Heap-grooming mechanics are omitted by ATT&CK.")], "No ATT&CK equivalent."),
    "PWN-004": ([("T1211", "Exploitation for Defense Evasion",
                  "ROP-chain construction bypasses mitigations ATT&CK does not model.")], "No ATT&CK equivalent."),
    "PWN-005": ([("T1059", "Command and Scripting Interpreter",
                  "seccomp-restricted ORW shellcraft is CTF-specific.")], "No ATT&CK equivalent."),
    # --- REV — Reverse Engineering -------------------------------------------
    "REV-001": ([("T1622", "Debugger Evasion", "Anti-debugging guards.")], "No ATT&CK equivalent."),
    "REV-002": ([("T1027.002", "Software Packing", "Packing / runtime self-modification.")], "No ATT&CK equivalent."),
    "REV-003": ([("T1027", "Obfuscated Files or Information",
                  "Control-flow flattening and opaque predicates.")], "No ATT&CK equivalent."),
    "REV-004": ([("T1027", "Obfuscated Files or Information",
                  "Custom VM bytecode interpretation.")], "No ATT&CK equivalent."),
    "REV-005": ([("T1480", "Execution Guardrails",
                  "Constraint-gated flag checks echo execution guardrails.")], "No ATT&CK equivalent."),
    # --- STE — Steganography --------------------------------------------------
    "STE-001": ([("T1001.002", "Steganography",
                  "CTFT details LSB extraction mechanics ATT&CK omits.")], "No ATT&CK equivalent."),
    "STE-002": ([("T1001.002", "Steganography",
                  "Polyglot / appended-data concealment.")], "No ATT&CK equivalent."),
    "STE-003": ([("T1001.002", "Steganography",
                  "Spectrogram embedding.")], "No ATT&CK equivalent."),
    "STE-004": ([("T1001.002", "Steganography",
                  "Metadata / EXIF embedding.")], "No ATT&CK equivalent."),
    "STE-005": ([("T1001.002", "Steganography",
                  "Zero-width / whitespace text steganography.")], "No ATT&CK equivalent."),
    "STE-006": ([("T1001.002", "Steganography",
                  "Linguistic steganography.")], "No ATT&CK equivalent."),
    "STE-007": ([("T1001.002", "Steganography",
                  "Technical steganography.")], "No ATT&CK equivalent."),
    "STE-008": ([("T1001.002", "Steganography",
                  "Technical text steganography.")], "No ATT&CK equivalent."),
    "STE-009": ([("T1001.002", "Steganography",
                  "Nested metadata containers.")], "No ATT&CK equivalent."),
    # --- OSI — OSINT ----------------------------------------------------------
    "OSI-001": ([("T1589", "Gather Victim Identity Information",
                  "Metadata correlation echoes identity gathering.")], "No direct ATT&CK technique."),
    "OSI-002": ([("T1593", "Search Open Websites/Domains",
                  "Username pivoting echoes open-web searching.")], "No direct ATT&CK technique."),
    "OSI-003": ([("T1593.002", "Search Engines",
                  "Cached-content recovery echoes search-engine mining.")], "No direct ATT&CK technique."),
    "OSI-004": ([("T1589", "Gather Victim Identity Information",
                  "Imagery geolocation is OSINT craft ATT&CK omits.")], "No direct ATT&CK technique."),
    "OSI-005": ([("T1596", "Search Open Technical Databases",
                  "Public-repo mining echoes open-technical-database searching.")], "No direct ATT&CK technique."),
    # --- CLD — Cloud -----------------------------------------------------------
    "CLD-001": ([("T1530", "Data from Cloud Storage Object",
                  "Misconfigured object storage.")], "No direct ATT&CK technique."),
    "CLD-002": ([("T1078.004", "Cloud Accounts",
                  "Over-permissive IAM roles.")], "No direct ATT&CK technique."),
    "CLD-003": ([("T1552.005", "Cloud Instance Metadata API",
                  "IMDS credential retrieval.")], "No direct ATT&CK technique."),
    "CLD-004": ([("T1552", "Unsecured Credentials",
                  "Secrets in serverless configuration.")], "No direct ATT&CK technique."),
    "CLD-005": ([("T1613", "Container and Resource Discovery",
                  "Container image / registry inspection.")], "No direct ATT&CK technique."),
    # --- BLK — Blockchain -------------------------------------------------------
    "BLK-001": ([("T1213", "Data from Information Repositories",
                  "Storage-slot reading echoes data-from-repositories.")], "No ATT&CK equivalent."),
    "BLK-002": ([("T1190", "Exploit Public-Facing Application",
                  "Reentrancy exploitation of a public contract.")], "No ATT&CK equivalent."),
    "BLK-003": ([("T1140", "Deobfuscate/Decode Files or Information",
                  "EVM decompilation echoes deobfuscation.")], "No ATT&CK equivalent."),
    "BLK-004": ([("T1213", "Data from Information Repositories",
                  "Transaction-log / calldata mining.")], "No ATT&CK equivalent."),
    "BLK-005": ([("T1548", "Abuse Elevation Control Mechanism",
                  "Missing access checks echo elevation-control abuse.")], "No ATT&CK equivalent."),
    # --- AIM — AI / ML ------------------------------------------------------------
    "AIM-001": ([("T1552", "Unsecured Credentials",
                  "Secrets embedded in model artifacts.")], "No ATT&CK equivalent."),
    "AIM-002": ([("T1190", "Exploit Public-Facing Application",
                  "Prompt-injection is emerging LLM-security craft ATT&CK does not model.")], "No ATT&CK equivalent."),
    "AIM-003": ([], "No ATT&CK equivalent; adversarial-example craft."),
    "AIM-004": ([("T1190", "Exploit Public-Facing Application",
                  "Malicious serialized models echo public-app exploitation on ML serving endpoints.")], "No ATT&CK equivalent."),
    "AIM-005": ([("T1213", "Data from Information Repositories",
                  "Model inversion echoes data extraction from repositories.")], "No ATT&CK equivalent."),
    # --- ICS — ICS / SCADA (ATT&CK for ICS) -----------------------------------------
    "ICS-001": ([("T0861", "Point & Tag Identification",
                  "ICS ATT&CK: Modbus register reads.")], "No direct ATT&CK technique."),
    "ICS-002": ([("T0861", "Point & Tag Identification",
                  "ICS ATT&CK: S7 data-block reads.")], "No direct ATT&CK technique."),
    "ICS-003": ([("T0842", "Network Sniffing",
                  "ICS ATT&CK: industrial protocol captures.")], "No direct ATT&CK technique."),
    "ICS-004": ([("T0843", "Program Download",
                  "ICS ATT&CK: HMI project-file secrets.")], "No direct ATT&CK technique."),
    "ICS-005": ([("T0861", "Point & Tag Identification",
                  "ICS ATT&CK: DNP3/BACnet object enumeration.")], "No direct ATT&CK technique."),
    # --- MOB — Mobile ----------------------------------------------------------------
    "MOB-001": ([("T1552.001", "Credentials in Files",
                  "APK resource secrets.")], "No direct ATT&CK technique."),
    "MOB-002": ([("T1406", "Obfuscated Files or Information (Mobile)",
                  "Native-library logic hiding.")], "No direct ATT&CK technique."),
    "MOB-003": ([("T1557", "Man-in-the-Middle",
                  "Certificate pinning as a MITM barrier.")], "No direct ATT&CK technique."),
    "MOB-004": ([("T1406", "Obfuscated Files or Information (Mobile)",
                  "DEX obfuscation.")], "No direct ATT&CK technique."),
    "MOB-005": ([("T1497", "Virtualization/Sandbox Evasion",
                  "Runtime/device-conditioned checks echo sandbox evasion.")], "No direct ATT&CK technique."),
    # --- JAL — Jail / Sandbox Escape ------------------------------------------------
    "JAL-001": ([("T1059.006", "Python",
                  "Python sandbox escape; ATT&CK models Python scripting for other purposes.")], "No ATT&CK equivalent."),
    "JAL-002": ([("T1059", "Command and Scripting Interpreter",
                  "Restricted-shell escape details ATT&CK omits.")], "No ATT&CK equivalent."),
    "JAL-003": ([("T1611", "Escape to Host",
                  "Container escape paths ATT&CK describes generically.")], "No ATT&CK equivalent."),
    "JAL-004": ([("T1059.007", "JavaScript",
                  "JS sandbox-escape craft.")], "No ATT&CK equivalent."),
    "JAL-005": ([("T1055", "Process Injection",
                  "Seccomp/AppArmor filter-bypass detail ATT&CK omits.")], "No ATT&CK equivalent."),
    # --- GAM — Game / Protocol Automation ---------------------------------------------
    "GAM-001": ([("T1071", "Application Layer Protocol",
                  "Game-protocol automation.")], "No ATT&CK equivalent."),
    "GAM-002": ([("T1213", "Data from Information Repositories",
                  "Save-state manipulation.")], "No ATT&CK equivalent."),
    "GAM-003": ([], "No ATT&CK equivalent; adversarial gameplay craft."),
    "GAM-004": ([("T1055", "Process Injection",
                  "Memory patching to force a win state.")], "No ATT&CK equivalent."),
    "GAM-005": ([("T1071", "Application Layer Protocol",
                  "Protocol replay / race.")], "No ATT&CK equivalent."),
    # --- COD — Coding / Programming Puzzle ---------------------------------------------
    "COD-001": ([("T1140", "Deobfuscate/Decode Files or Information",
                  "Esolang decoding echoes deobfuscation.")], "No ATT&CK equivalent."),
    "COD-002": ([], "No ATT&CK equivalent; competitive-programming puzzle craft."),
    "COD-003": ([("T1071", "Application Layer Protocol",
                  "Protocol-automation marathon.")], "No ATT&CK equivalent."),
    "COD-004": ([("T1027", "Obfuscated Files or Information",
                  "Polyglot craft.")], "No ATT&CK equivalent."),
    "COD-005": ([], "No ATT&CK equivalent; constraint-satisfaction craft."),
    # --- FPN — Full Pwn / Multi-Stage ---------------------------------------------------
    "FPN-001": ([("T1190", "Exploit Public-Facing Application", "Initial access."),
                 ("T1078", "Valid Accounts", "Foothold and movement.")],
                "Multi-stage chains link most directly to full ATT&CK kill chains."),
    "FPN-002": ([("T1558", "Steal or Forge Kerberos Tickets", "AD ticket abuse."),
                 ("T1482", "Domain Trust Discovery", "Domain mapping.")],
                "AD fullpwn links most directly to ATT&CK."),
    "FPN-003": ([("T1572", "Protocol Tunneling", "Pivot tunnels."),
                 ("T1090", "Proxy", "Pivot relays.")],
                "Pivot-chain detail ATT&CK describes at a higher level."),
    "FPN-004": ([("T1611", "Escape to Host", "Container escape."),
                 ("T1190", "Exploit Public-Facing Application", "Service exploitation.")],
                "Service misconfig to container escape."),
    "FPN-005": ([("T1078.004", "Cloud Accounts", "Cloud IAM pivot."),
                 ("T1552.005", "Cloud Instance Metadata API", "IMDS credential theft.")],
                "On-prem to cloud pivot."),
    "FPN-006": ([("T1213", "Data from Information Repositories",
                  "Database trust-context escalation.")], "No direct ATT&CK technique."),
    "FPN-007": ([("T1083", "File and Directory Discovery",
                  "Dual-stack management exposure.")], "No direct ATT&CK technique."),
}

DEFAULT_NONE = "No direct ATT&CK equivalent."

# ---------------------------------------------------------------------------

COMPLEMENT_RE = re.compile(r"(?m)^## ATT\\&?CK Complementarity\b.*?(?=^## |\Z)", re.DOTALL)
TOOLS_RE = re.compile(r"(?m)^## Tools\b")
REFERENCES_RE = re.compile(r"(?m)^## References\b")
TACTIC_SENTENCE_RE = re.compile(r"(CTFT never re-labels an existing ATT\&?CK technique\.)")


def render_table(rows: list[tuple[str, str, str]], none_note: str) -> str:
    lines = ["## Related MITRE ATT&CK", "",
             "| ATT&CK ID | ATT&CK technique | Relation note |",
             "| --- | --- | --- |"]
    if rows:
        for att_id, name, note in rows:
            lines.append(f"| {att_id} | {name} | {note} |")
    else:
        lines.append(f"| \u2014 | \u2014 | {none_note} |")
    return "\n".join(lines)


def mapping(key: str) -> tuple[list[tuple[str, str, str]], str]:
    rows, none_note = ATTACK.get(key, ([], DEFAULT_NONE))
    return rows, none_note


def update_technique(path: Path) -> tuple[str, str]:
    key = path.stem[len("CTFTTE-"):]
    section = render_table(*mapping(key)) + "\n\n"
    text = path.read_text(encoding="utf-8", errors="replace")
    if "## Related MITRE ATT&CK" in text:
        # Second pass: the new table already exists; just drop the legacy section.
        new = COMPLEMENT_RE.sub("", text, count=1)
    elif COMPLEMENT_RE.search(text):
        new = COMPLEMENT_RE.sub(lambda m: section, text, count=1)
    else:
        anchor = TOOLS_RE.search(text) or REFERENCES_RE.search(text)
        if anchor:
            new = text[: anchor.start()] + section + text[anchor.start():]
        else:
            new = text.rstrip() + "\n\n" + section
    return text, new


def update_counter(path: Path) -> tuple[str, str]:
    key = path.stem[len("CTFTCTE-"):]
    text = path.read_text(encoding="utf-8", errors="replace")
    if "## Related MITRE ATT&CK" in text:
        return text, text
    section = render_table(*mapping(key)) + "\n\n"
    anchor = TOOLS_RE.search(text) or REFERENCES_RE.search(text)
    if anchor:
        new = text[: anchor.start()] + section + text[anchor.start():]
    else:
        new = text.rstrip() + "\n\n" + section
    return text, new


POINTER = ("\n\n> Per-entry related ATT&CK IDs are rendered on every technique and\n"
           "> counter-technique page as a `Related MITRE ATT&CK` table (SCHEMA_V2 §3.5).\n")


def update_tactic(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    if "Related MITRE ATT&CK` table" in text:
        return text, text
    new = TACTIC_SENTENCE_RE.sub(lambda m: m.group(1) + POINTER, text, count=1)
    return text, new


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="apply changes (default: dry run)")
    args = parser.parse_args()

    techniques = sorted((ROOT / "techniques").glob("CTFTTE-*.md"))
    counters = sorted((ROOT / "countertechniques").glob("CTFTCTE-*.md"))
    tactics = sorted((ROOT / "tactics").glob("CTFT-TA-*.md"))

    missing_map = sorted(
        path.stem[len("CTFTTE-"):] for path in techniques
        if path.stem[len("CTFTTE-"):] not in ATTACK
    )

    jobs: list[tuple[Path, tuple[str, str]]] = []
    for path in techniques:
        jobs.append((path, update_technique(path)))
    for path in counters:
        jobs.append((path, update_counter(path)))
    for path in tactics:
        jobs.append((path, update_tactic(path)))

    changed = [(path, old, new) for path, (old, new) in jobs if new != old]
    mode = "WRITE" if args.write else "DRY"
    print(f"{mode}   techniques={len(techniques)} counters={len(counters)} "
          f"tactics={len(tactics)} changed={len(changed)}")
    for path, _old, _new in changed:
        print(f"  {'would change' if not args.write else 'updated'}: {path.relative_to(ROOT)}")
    if missing_map:
        print("MISSING from ATTACK map (rendered with default none-note):", ", ".join(missing_map))

    if args.write:
        for path, _old, new in changed:
            path.write_text(new, encoding="utf-8")
        print(f"Applied {len(changed)} updates.")


if __name__ == "__main__":
    main()
