# CTFTSKL-002 — ctf-sdr-ook-line-code

> **Skill ID:** `CTFTSKL-002`  
> **Kind:** Fine-grained skill (one FOM pair)  
> **Related techniques/counters:** CTFTTE-SDR-002, CTFTCTE-SDR-002

## Description

Solves radio challenges where the flag is the payload of an on-off-keyed (OOK/ASK)
burst: a garage remote, key fob, doorbell or 315/433/868 MHz sensor, given as an IQ
capture or captured live. The steps are:
1. recover the symbol clock from the pulse widths;
2. decode the line code: Manchester in both conventions and both phases, PWM or PPM;
3. align bytes on the preamble and sync word, then read the flag.

It includes a triage table (wrong alignment, inverted convention, PWM versus Manchester),
a 15-line NumPy decode that needs no toolkit, and `ook_decode.py` / `rtl_433` / inspectrum
routes. All of them are verified on HTB RFlag.

## Skill file

- [ctf-skills-main/ctf-sdr-ook-line-code/SKILL.md](../../ctf-skills-main/ctf-sdr-ook-line-code/SKILL.md) — canonical

## When to load

```yaml
artifact_type: iq-capture           # signal.cf32 / capture.cu8, or a live 315/433/868/915 MHz burst
evidence:
  - single narrow carrier (~10-20 kHz occupied) switched fully on/off
  - story: garage, gate, remote key, key fob, doorbell, wireless sensor
  - envelope runs of 1-2 symbol units only (Manchester) or two pulse widths with a constant period (PWM/PPM)
```

## FOM pairs

- [CTFTTE-SDR-002](../techniques/CTFTTE-SDR-002.md) / [CTFTCTE-SDR-002](../countertechniques/CTFTCTE-SDR-002.md) — line-coded OOK remote

## Tools

- [ook_decode.py](../tools/CTFTTOU-340.md)
- [iq_segments.py](../tools/CTFTTOU-342.md)
- [iq_check.py](../tools/CTFTTOU-341.md)
- [rtl_433](../tools/CTFTTOU-336.md)
- [inspectrum](../tools/CTFTTOU-236.md)
- [rtl_sdr](../tools/CTFTTOU-347.md)

## Agents

- [ctf-sdr agent](../../.agents/ctf/ctf-sdr/AGENT.md)

## Related skills

- [ctf-sdr](CTFTSKL-001.md) — parent domain skill

## Notes

Evidence `EVID-SDR-002` (HTB RFlag): `ook_decode.py signal.cf32 --fs 2.048M --crib HTB{`
recovers `HTB{RF_H4ck1n6_1s_c00l!!!}` as candidate #1 (Manchester phase 0, G.E. Thomas,
32-bit `0xAA` preamble).

## Related Techniques

CTFTTE-SDR-002, CTFTCTE-SDR-002
