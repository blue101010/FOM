# CTFTTE-SDR-004 — Flag carried by a standard digital radio protocol

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Paired counter-technique:** [`CTFTCTE-SDR-004`](../countertechniques/CTFTCTE-SDR-004.md) — Demodulate and run the protocol's reference decoder

---

## How the challenge author hides

The flag is sent in the fields of a documented over-the-air protocol:

- a pager message (POCSAG/FLEX);
- an AFSK1200 AX.25/APRS packet;
- DTMF or Morse keyed on a carrier;
- an ADS-B/Mode S frame (callsign, squawk);
- an AIS message;
- RDS radiotext on broadcast FM.

The concealment is the stack. The signal must first be demodulated (usually NFM or WBFM, or 1090 MHz pulse position) and then parsed by a decoder for that protocol, whose checksum separates real frames from noise. Distinct from CTFTTE-STE-010, where the tones already sit in an audio file, and from CTFTTE-SDR-002, where the framing is custom.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1071 | Application Layer Protocol | Data hides in the fields of a legitimate, standard protocol; here the protocol is a radio one. |

## Tools

- [multimon-ng](../tools/CTFTTOU-237.md)
- [dump1090](../tools/CTFTTOU-337.md)
- [adsb_crc.py](../../.agents/ctf/ctf-sdr/scripts/adsb_crc.py) ([CTFTTOU-345](../tools/CTFTTOU-345.md))
- [iq_demod.py](../../.agents/ctf/ctf-sdr/scripts/iq_demod.py) ([CTFTTOU-343](../tools/CTFTTOU-343.md))
- [rtl-sdr](../tools/CTFTTOU-335.md)
- [rtl_fm](../tools/CTFTTOU-348.md)
- [rtl_adsb](../tools/CTFTTOU-352.md)
- [rtl_tcp](../tools/CTFTTOU-350.md)

## Indicators

- known protocol frequencies: 1090 MHz (ADS-B), 144.39/144.80 MHz (APRS), 161.975/162.025 MHz (AIS), VHF/UHF pager channels, 87.5–108 MHz (RDS)
- audio after FM demodulation that sounds like a modem (AFSK), pager bursts or DTMF tones
- decoders that output frames with a valid checksum (CRC-24 for Mode S, BCH for POCSAG, FCS for AX.25)

## References

- <https://github.com/EliasOenal/multimon-ng>
- <https://mode-s.org/decode/>
- <https://github.com/antirez/dump1090>
