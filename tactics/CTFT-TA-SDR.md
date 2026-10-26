# SDR — Software-Defined Radio

> **Domain ID:** `CTFT-TA-SDR`  
> **HTB mapping:** HTB: Hardware  
> **Techniques:** 5

## Description

Hiding data in RF captures and modulated signals, and recovering it through
SDR demodulation and decoding. Split from HWR (Hardware), which keeps
embedded-device and physical-interface concealment. The barrier can sit at
any layer of the receive chain:

- finding the signal in a live spectrum;
- reading an unlabelled IQ file (format, sample rate, centre);
- identifying the modulation;
- slicing on-off-keyed symbols and undoing a line code (Manchester, PWM, PPM);
- running a standard protocol decoder (pager, packet, ADS-B).

IoT protocol stacks with pairing keys (Zigbee/BLE) stay in IOT; tones already
in an audio file stay in STE. Recovery is receive-only.

## Positioning and external anchors

A domain is a **subject** axis: it answers *what kind of challenge is this*, not
*what is the player trying to achieve*. The player-objective axis is tracked
separately and is deliberately still underived (SCHEMA_V3 §3.9).

CTFT relates to external catalogues — MITRE ATT&CK, CAPEC, CWE, OWASP WSTG —
without deriving from any of them. External identifiers are **anchors carried
per entry**, never the definition of an entry.

> Each technique and resolution-technique page carries its own
> `Related MITRE ATT&CK` table (SCHEMA_V3 §3.5). The `ATT&CK` column below is an
> orientation excerpt of those tables, nothing more.

## Techniques ↔ Resolution-techniques

| Technique | Hide / Design name | Resolution-technique | Recovery action | ATT&CK |
| --- | --- | --- | --- | --- |
| [CTFTTE-SDR-001](../techniques/CTFTTE-SDR-001.md) | RF/SDR signal embedding | [CTFTCTE-SDR-001](../countertechniques/CTFTCTE-SDR-001.md) | Demodulate and decode RF captures | T1001.002 |
| [CTFTTE-SDR-002](../techniques/CTFTTE-SDR-002.md) | Line-coded on-off-keyed remote transmission | [CTFTCTE-SDR-002](../countertechniques/CTFTCTE-SDR-002.md) | Slice the envelope into symbols and decode the line code | T1132, T1001.002 |
| [CTFTTE-SDR-003](../techniques/CTFTTE-SDR-003.md) | Unlabelled IQ capture (format, sample rate and centre withheld) | [CTFTCTE-SDR-003](../countertechniques/CTFTCTE-SDR-003.md) | Fingerprint the IQ format and recover rate and centre | T1027 |
| [CTFTTE-SDR-004](../techniques/CTFTTE-SDR-004.md) | Flag carried by a standard digital radio protocol | [CTFTCTE-SDR-004](../countertechniques/CTFTCTE-SDR-004.md) | Demodulate and run the protocol's reference decoder | T1071 |
| [CTFTTE-SDR-005](../techniques/CTFTTE-SDR-005.md) | Flag transmitter hidden in a live spectrum | [CTFTCTE-SDR-005](../countertechniques/CTFTCTE-SDR-005.md) | Baseline the band and diff live sweeps | T1001 |

---
*See [CORRELATION.md](../CORRELATION.md) for the full cross-reference matrix.*
