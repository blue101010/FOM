# CTFTTOU-417 — hermes-dec

> **Tool ID:** `CTFTTOU-417`
> **Related techniques/counters:** CTFTTE-MOB-009, CTFTCTE-MOB-009

## Description

Decompiler, disassembler and file parser for Hermes bytecode — the engine format cross-platform
mobile frameworks ship in production builds. Three entry points, each usable without executing the
target:

- **`hbc-file-parser`** — header and metadata: bytecode version, string table, function count. Use it
  first: the version decides whether a decompiler will produce code or noise.
- **`hbc-disassembler`** — instruction listing, enough to confirm control flow and to grep constants.
- **`hbc-decompiler`** — reconstructs modules and functions as JavaScript, keeping the compiler's
  original function names as annotations (`// Original name: …`), which is what turns a flat listing
  into a readable call graph.

Pure Python, installs into a venv, works fully offline on an extracted bundle.

## URL

- <https://github.com/P1sec/hermes-dec>

## Install (Kali WSL)

`pipx` keeps the tool isolated from the system interpreter and puts the three entry points on
`PATH`; no venv prefix is needed in the commands below.

```bash
pipx install hermes-dec
pipx list --short | grep hermes        # hermes-dec 0.1.8
which hbc-file-parser hbc-decompiler   # ~/.local/bin/...
```

`pipx` environments are tied to the distribution Python: after an interpreter bump they die with the
classic *bad interpreter* error, and `pipx reinstall hermes-dec` rebuilds them.

## Usage

```bash
# 1. header first: the engine version gates the decompiler
hbc-file-parser assets/index.android.bundle | head -20

# 2. constants and structure when a full decompile is not needed
hbc-disassembler assets/index.android.bundle > out.hasm

# 3. readable reconstruction
hbc-decompiler assets/index.android.bundle out.js
```

## Notes

- Version pair used for validation: `hermes-dec 0.1.8` installed with `pipx`, on **bytecode version 96**
  (magic `0x1f1903c103bc1fc6`); a 1.9 MB bundle decompiled to ~342 000 lines in about 15 seconds.
- Both platforms ship the same format: an Android `assets/*.bundle` and an iOS
  `Payload/*.app/main.jsbundle` of the same app carry the same version, so one decompilation answers
  for both.
- `file` already reports `Hermes JavaScript bytecode, version N` — a one-second triage before
  installing anything.
- A bytecode version outside the tool's supported range does not fail loudly; it emits
  plausible-looking nonsense. Cross-check the version from `hbc-file-parser` before trusting output.
- One `grep` pass over the raw bundle is still worth it: URL and endpoint literals survive
  compilation and often expose the network surface before any decompilation.

## Related Techniques

CTFTTE-MOB-009, CTFTCTE-MOB-009
