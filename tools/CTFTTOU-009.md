# CTFTTOU-009 — ripgrep-all (rga)

> **Tool ID:** `CTFTTOU-009`  
> **Related techniques/counters:** CTFTCTE-WEB-019

## Description

ripgrep-all wraps ripgrep with per-file-type adapters so a single query covers plain text **and** encapsulated artefacts: PDF (poppler / `pdftotext`), Office and e-book documents (pandoc: `.docx`, `.epub`, `.odt`, `.ipynb`, `.fb2`), media metadata (ffmpeg: `.mp4`, `.mkv`, `.mp3`, `.flac`…), archives (zip, tar, gzip), SQLite databases and more. Every hit prints its file provenance and line. It is a discovery accelerator, not an extraction tool: it converts in memory, leaves artefacts untouched, and defers to dedicated tools for unpacking or stream-level parsing.

## Installation

- Prebuilt static binaries per release: `ripgrep_all-v*-x86_64-unknown-linux-musl.tar.gz`. Drop `rga` and `rga-preproc` into `~/.local/bin` — no root required.
- Requires `ripgrep` (`rg`) on the PATH.
- Adapters are optional capabilities detected at runtime: `pandoc` (docx/epub/odt/ipynb), `pdftotext` from poppler-utils (PDF), `ffmpeg` (media metadata), `unzip`, `sqlite3`.
- `rga --rga-list-adapters` shows every active adapter and the exact command it runs.

## Usage (CTF patterns)

- Whole-tree sweep including encapsulated files: `rga 'flag{' .`
- Minified single-line bundles: `rga --max-columns 300 'token|jwt|secret' assets/`
- Success-state vocabulary across every artefact at once: `rga -i 'access granted|reward|coupon|promo|redeem' .`
- Interactive preview of hits: pipe through `rga-fzf` / `rga-fzf-open` (shipped in the release archive).

## Limits

- Binary formats without a matching adapter are skipped silently — check `--rga-list-adapters` before trusting a negative result.
- PDF hits come from *visible* text extraction; objects hidden in unparsed streams or after EOF still require xref/stream parsing (`CTFTCTE-FOR-025`).
- Packed or encrypted containers are not unpacked; extraction belongs to dedicated tools (`CTFTCTE-FOR-015`).

## URL

<https://github.com/phiresky/ripgrep-all>

## Related Techniques

CTFTCTE-WEB-019
