# CTFTCTE-SDR-004 — Demodulate and run the protocol's reference decoder

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Counters technique:** [`CTFTTE-SDR-004`](../techniques/CTFTTE-SDR-004.md) — Flag carried by a standard digital radio protocol

---

## Offensive Recovery (CTF practitioner / solver)

1. Identify the protocol from the frequency and the sound or shape of the signal.
2. Demodulate to the decoder's expected input. Pager, APRS and DTMF need NFM audio at 22 050 Hz s16le, from `rtl_fm` live or an offline IQ demodulator from a capture. ADS-B needs the 2 MS/s 1090 MHz magnitude stream.
3. Feed the matching decoder: `multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a AFSK1200 -a DTMF`, `dump1090` or `rtl_adsb`.
4. Keep only frames whose checksum validates. Raw demodulator output includes noise frames.
5. Read the flag from the decoded fields (message text, callsign, comment).

## Forensic / Blue-Team Perspective (DFIR analyst)

Standard-protocol traffic is attributable: addresses, callsigns and ICAO identifiers tie frames to an emitter, and checksum-valid frames are the only admissible ones. Decoding is receive-only. Interfering with live aviation, maritime or paging systems is out of scope.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Recovery parses the standard protocol fields that carry the data. |

## Tools

- [multimon-ng](../tools/CTFTTOU-237.md)
- [dump1090](../tools/CTFTTOU-337.md)
- [adsb_crc.py](../../.agents/ctf/ctf-sdr/scripts/adsb_crc.py) ([CTFTTOU-345](../tools/CTFTTOU-345.md))
- [iq_demod.py](../../.agents/ctf/ctf-sdr/scripts/iq_demod.py) ([CTFTTOU-343](../tools/CTFTTOU-343.md))
- [rtl-sdr](../tools/CTFTTOU-335.md)
- [rtl_fm](../tools/CTFTTOU-348.md)
- [rtl_adsb](../tools/CTFTTOU-352.md)
- [rtl_tcp](../tools/CTFTTOU-350.md)

## References

- <https://github.com/EliasOenal/multimon-ng>
- <https://mode-s.org/decode/>
