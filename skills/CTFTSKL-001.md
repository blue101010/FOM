# CTFTSKL-001 — ctf-sdr

> **Skill ID:** `CTFTSKL-001`  
> **Kind:** Domain skill  
> **Related techniques/counters:** CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-003, CTFTCTE-SDR-003, CTFTTE-SDR-004, CTFTCTE-SDR-004, CTFTTE-SDR-005, CTFTCTE-SDR-005

## Description

Software-defined radio and RF signal techniques for CTF challenges. Load it when the artifact is:
- an IQ capture (`.cf32`, `.cu8`, `.cs16`, `.iq`, `.bin`);
- an RTL-SDR dongle or an `rtl_tcp` stream;
- an `rtl_power` survey;
- a transmission to decode: an OOK/ASK remote with a Manchester/PWM/PPM line code, an unknown modulation, pager/APRS/ADS-B frames, or a live RF fox hunt.

The skill walks the receive chain from capture metadata to the flag: identify the file,
locate the signal, classify the modulation, decode, validate. It also gives the toolkit
commands for each FOM SDR pair, verified pitfalls, and pivots to IoT, audio, misc and
forensics.

## Skill file

- [ctf-skills-main/ctf-sdr/SKILL.md](../../ctf-skills-main/ctf-sdr/SKILL.md) — canonical (Claude Code, Copilot and Codex read it through the `AGENTS.md` routing table)

## When to load

```yaml
artifact_type: iq-capture            # cf32 / cu8 / cs16, or live rtl_tcp
runtime: rtl-sdr | offline
evidence:
  - radio capture or dongle access in the challenge
  - carrier keyed fully on/off, runs of 1-2 symbol units      # -> SDR-002
  - no sample rate / centre given; cf32 with 256 levels       # -> SDR-003
  - decoder output with valid CRC (POCSAG/AX.25/Mode S)       # -> SDR-004
```

## FOM pairs

- [CTFTTE-SDR-001](../techniques/CTFTTE-SDR-001.md) / [CTFTCTE-SDR-001](../countertechniques/CTFTCTE-SDR-001.md) — unknown modulation
- [CTFTTE-SDR-002](../techniques/CTFTTE-SDR-002.md) / [CTFTCTE-SDR-002](../countertechniques/CTFTCTE-SDR-002.md) — line-coded OOK remote
- [CTFTTE-SDR-003](../techniques/CTFTTE-SDR-003.md) / [CTFTCTE-SDR-003](../countertechniques/CTFTCTE-SDR-003.md) — unlabelled IQ capture
- [CTFTTE-SDR-004](../techniques/CTFTTE-SDR-004.md) / [CTFTCTE-SDR-004](../countertechniques/CTFTCTE-SDR-004.md) — standard radio protocol
- [CTFTTE-SDR-005](../techniques/CTFTTE-SDR-005.md) / [CTFTCTE-SDR-005](../countertechniques/CTFTCTE-SDR-005.md) — transmitter in a live spectrum

## Tools

- [rtl-sdr](../tools/CTFTTOU-335.md)
- [rtl_test](../tools/CTFTTOU-346.md)
- [rtl_sdr](../tools/CTFTTOU-347.md)
- [rtl_fm](../tools/CTFTTOU-348.md)
- [rtl_power](../tools/CTFTTOU-349.md)
- [rtl_tcp](../tools/CTFTTOU-350.md)
- [rtl_eeprom](../tools/CTFTTOU-351.md)
- [rtl_adsb](../tools/CTFTTOU-352.md)
- [rtl_433](../tools/CTFTTOU-336.md)
- [dump1090](../tools/CTFTTOU-337.md)
- [SigDigger](../tools/CTFTTOU-338.md)
- [kalibrate-rtl](../tools/CTFTTOU-339.md)
- [ook_decode.py](../tools/CTFTTOU-340.md)
- [iq_check.py](../tools/CTFTTOU-341.md)
- [iq_segments.py](../tools/CTFTTOU-342.md)
- [iq_demod.py](../tools/CTFTTOU-343.md)
- [power_peaks.py](../tools/CTFTTOU-344.md)
- [adsb_crc.py](../tools/CTFTTOU-345.md)
- [inspectrum](../tools/CTFTTOU-236.md)
- [Universal Radio Hacker](../tools/CTFTTOU-235.md)
- [Gqrx](../tools/CTFTTOU-234.md)
- [GNU Radio Companion](../tools/CTFTTOU-233.md)
- [multimon-ng](../tools/CTFTTOU-237.md)

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md) — hardware profile, verified rtl-sdr options, script toolkit index, safety rules

## Related skills

- [ctf-sdr-ook-line-code](CTFTSKL-002.md) — fine-grained skill for SDR-002

## Notes

Worked example: HTB RFlag (`.agents/ctf/ctf-sdr/HTB_RF/`), evidence `EVID-SDR-002`.

## Related Techniques

CTFTTE-SDR-001, CTFTCTE-SDR-001, CTFTTE-SDR-002, CTFTCTE-SDR-002, CTFTTE-SDR-003, CTFTCTE-SDR-003, CTFTTE-SDR-004, CTFTCTE-SDR-004, CTFTTE-SDR-005, CTFTCTE-SDR-005
