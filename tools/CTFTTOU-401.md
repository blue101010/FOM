# CTFTTOU-401 — EVTX / python-evtx

> **Tool ID:** `CTFTTOU-401`
> **Related techniques/counters:** CTFTTE-FOR-028, CTFTCTE-FOR-028

## Description

Two complementary Windows Event Log (`.evtx`) parsers for reconstructing
timelines and recovering concealed event-log evidence:

- **EVTX (Rust)** — omerbenamram/EVTX: fast cross-platform parser. Builds the
  `evtx_dump` CLI (xml/json/jsonl output, WEVT template extraction,
  chunk-slack-safe reads).
- **python-evtx** — williballenthin's pure-Python parser (Debian/Kali package
  `python3-evtx`, PyPI `python-evtx`). Provides `evtx_dump.py`,
  `evtx_dump_json.py`, `evtx_filter_records.py`, `evtx_templates.py`,
  `evtx_record_structure.py`, …

## URL

- <https://github.com/omerbenamram/EVTX>
- <https://pkg.kali.org/pkg/python-evtx>

## Install locations (this machine — Kali WSL)

| Artifact | Path |
| --- | --- |
| Source clone | `~/TOOLS/EVTX` (built with cargo: `target/release/evtx_dump`) |
| Rust CLI on PATH | `~/.local/bin/evtx_dump-rs` (symlink) |
| Python venv | `~/.venvs/evtx` — `pip install 'python-evtx==0.7.4'` |
| Kali package (alt.) | `python3-evtx` via apt, provides `/usr/bin/evtx_dump.py` |

## Usage

```bash
# Rust parser — fast, xml by default; -o json / jsonl for machine output
~/.local/bin/evtx_dump-rs -o json input.evtx | head
~/.local/bin/evtx_dump-rs -t 4 input.evtx            # limit threads
~/.local/bin/evtx_dump-rs extract-wevt-templates -h  # template cache helper

# Python parser — extra utilities
~/.venvs/evtx/bin/evtx_dump.py input.evtx
~/.venvs/evtx/bin/evtx_dump_chunk_slack.py -h   # dirty/VSS evtx recovery
~/.venvs/evtx/bin/evtx_filter_records.py -h
```

## Notes

- `python-evtx` 0.8.1 ships broken console scripts
  (`ModuleNotFoundError: No module named 'scripts'`); pin **0.7.4** in the venv.
- Use `evtx_dump_chunk_slack.py` for truncated or dirty files (the repo's
  `samples/` contains `2-system-Security-dirty.evtx` as a test case).

## Skills

- [ctf-evtx](../skills/CTFTSKL-003.md) — EVTX parsing and Windows timeline reconstruction (FOR-028)
