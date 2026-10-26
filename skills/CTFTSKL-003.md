# CTFTSKL-003 — ctf-evtx

> **Skill ID:** `CTFTSKL-003`  
> **Kind:** Tool manual  
> **Related techniques/counters:** CTFTTE-FOR-028, CTFTCTE-FOR-028

## Description

Parses Windows EVTX event logs in Kali WSL with the fast Rust parser from
omerbenamram/EVTX (`evtx_dump-rs`), the pure-Python `python-evtx` utilities, and
the Rust-backed `evtx` Python bindings. Covers XML/JSON/JSONL dumps, WEVT
template caches, chunk-slack recovery for dirty logs, batch processing with
`fd`, and the FOR-028 playbook for reconstructing a Windows timeline.

## Skill file

- [ctf-skills-main/ctf-evtx/SKILL.md](../../ctf-skills-main/ctf-evtx/SKILL.md) — canonical

## When to load

```yaml
artifact_type: evtx-log          # .evtx file, or Windows image / folder with event logs
evidence:
  - task: reconstruct what happened / Windows timeline
  - concealed or wiped events suspected; dirty/truncated log files
  - Provider/EventID/timestamp correlation required across System/Security logs
```

## FOM pairs

- [CTFTTE-FOR-028](../techniques/CTFTTE-FOR-028.md) / [CTFTCTE-FOR-028](../countertechniques/CTFTCTE-FOR-028.md) — Windows event-log evidence concealment / reconstruct the timeline from Windows event logs

## Tools

- [EVTX / python-evtx](../tools/CTFTTOU-401.md)

## Notes

Installed in Kali WSL: Rust CLI `~/.local/bin/evtx_dump-rs` (source
`~/TOOLS/EVTX`), Python venv `~/.venvs/evtx` (`python-evtx==0.7.4` + `evtx`
bindings). Tested against `~/TOOLS/EVTX/samples/` including the dirty/VSS file.

## Related Techniques

CTFTTE-FOR-028, CTFTCTE-FOR-028
