# CTFTTOU-126 — binwalk v3 (Rust)

> **Tool ID:** `CTFTTOU-126`  
> **Related techniques/counters:** CTFTCTE-FOR-001, CTFTCTE-FOR-002, CTFTCTE-FOR-009, CTFTCTE-FOR-019, CTFTCTE-HWR-002, CTFTCTE-STE-002, CTFTCTE-STE-007, CTFTTE-FOR-001, CTFTTE-FOR-002, CTFTTE-FOR-019, CTFTTE-HWR-002, CTFTTE-STE-002

## Description

Firmware/image analysis tool that finds and extracts embedded files. **v3 is a Rust
rewrite** of the Python v2: multi-threaded signature scanning, so MB-sized blobs scan
in milliseconds instead of seconds, and results can be logged as JSON.

Kali ships v3 as the **`binwalk3`** apt package. The legacy v2 (`binwalk` /
`python3-binwalk`) stays installed because the `kali-linux-large` metapackage depends
on it — **never `apt remove binwalk`**; shadow it instead (`~/.local/bin` is first in
PATH):

```sh
sudo apt install -y binwalk3
ln -sf /usr/bin/binwalk3 ~/.local/bin/binwalk   # `binwalk` = v3
binwalk --version                                # binwalk 3.1.0
```

### v3 CLI (flat on the Kali build — no `scan` subcommand)

| Command | Effect |
|---|---|
| `binwalk file.bin` | Signature scan: table of decimal/hex offset + description |
| `binwalk -e file.bin` | Extract known types → `extractions/<file>.extracted/<HEXOFFSET>/` |
| `binwalk -eM file.bin` | Matryoshka: recursively scan extracted files |
| `binwalk -a -l hits.json file.bin` | ALL signatures at ALL offsets + JSON log — replaces v2 `--dd='.*'` carve-all (read offsets from the JSON, `dd` manually) |
| `binwalk -E file.bin` | Entropy plot saved to `<file>.png` (v2 printed ASCII to stdout); flat high entropy = encrypted/compressed |
| `binwalk -C dir -t N file.bin` | Custom extraction dir (default `extractions/`), thread count |
| `binwalk -y zip -x gzip file.bin` | Include/exclude signatures — put FILE first or use `--`, multi-value options swallow trailing args |
| `binwalk -L` | List all signatures and their extractors |

**Dropped in v3:** `--dd` (→ `-a -l` + `dd`), `-A` opcode scan (→ `rasm2 -D` / `r2 -A`),
`-W/--hexdump` (→ `xxd`). Extraction base dir changed: v2 `_<file>.extracted` → v3
`extractions/`.

Verified 2026-11 on Kali WSL (binwalk3 3.1.0-0kali4): scan+extract of an ELF with an
appended ZIP completed in ~30 ms; extraction landed at
`extractions/fw.bin.extracted/28B88/...`.

## URL

<https://github.com/ReFirmLabs/binwalk>

## AGENT & SKILLS

- [ctf-iot](../../ctf-skills-main/ctf-iot/SKILL.md) + [firmware.md](../../ctf-skills-main/ctf-iot/firmware.md) — firmware unpacking workflow (CTFTTE-IOT-001)
- [ctf-reverse](../../ctf-skills-main/ctf-reverse/SKILL.md) — embedded/IoT firmware RE (`platforms.md`)
- [ctf-forensics](../../ctf-skills-main/ctf-forensics/SKILL.md) — disk/stego carving (`disk-recovery.md`)
- [ctf-misc](../../ctf-skills-main/ctf-misc/SKILL.md) — polyglot triage (`encodings-advanced.md`)

## Related Techniques

CTFTCTE-FOR-001, CTFTCTE-FOR-002, CTFTCTE-FOR-009, CTFTCTE-FOR-019, CTFTCTE-HWR-002, CTFTCTE-STE-002, CTFTCTE-STE-007, CTFTTE-FOR-001, CTFTTE-FOR-002, CTFTTE-FOR-019, CTFTTE-HWR-002, CTFTTE-STE-002
