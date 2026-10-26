# CTFTTOU-340 — ook_decode.py

> **Tool ID:** `CTFTTOU-340`  
> **Related techniques/counters:** CTFTTE-SDR-002, CTFTCTE-SDR-002

## Description

Workspace-authored OOK/ASK pulse decoder (Python, NumPy/SciPy). It automates the
SDR-002 recovery end to end:

1. auto-tune to the carrier centroid, band-limit, take the envelope;
2. threshold into on/off runs, split frames on long gaps;
3. recover the symbol unit from the run lengths;
4. decode the line code: raw, Manchester (both pair phases × both conventions), PWM and PPM;
5. try all 8 byte alignments and score printable text plus a `--crib`.

It reports the preamble length, the sync word, flag-like strings anchored on the crib,
a pulse summary and an unverified `rtl_433 -X` flex suggestion. Inputs: `cu8`/`cs8`/`cs16`/`cf32`,
with sample rate and centre taken from a sidecar JSON or the filename when not given.

Validated on HTB "RFlag": with `--fs 2.048M --crib HTB{` it finds the carrier
at −226.1 kHz, 521 symbols of 439 µs, Manchester phase 0 (G.E. Thomas) and a
32-bit `0xAA` preamble, and prints `HTB{RF_H4ck1n6_1s_c00l!!!}` as candidate #1.
The toolkit self-test also covers synthetic Manchester-with-sync and PWM remotes.

## URL

Local (workspace): [.agents/ctf/ctf-sdr/scripts/ook_decode.py](../../.agents/ctf/ctf-sdr/scripts/ook_decode.py) — shared helpers in `sdrio.py` next to it.

## Usage

```bash
~/.venvs/ctfml/bin/python -I ook_decode.py signal.cf32 --fs 2.048M --crib 'HTB{'
~/.venvs/ctfml/bin/python -I ook_decode.py keyfob.cu8 --code pwm --top 3 --bits-out bits.txt
scripts\sdrpy.ps1 ook_decode.py C:\caps\remote.cf32 --fs 1M --json        # from Windows PowerShell
```

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — script toolkit index and self-test

## Skills

- [ctf-sdr-ook-line-code](../skills/CTFTSKL-002.md) — fine-grained FOM pair SDR-002

## Related Techniques

CTFTTE-SDR-002, CTFTCTE-SDR-002
