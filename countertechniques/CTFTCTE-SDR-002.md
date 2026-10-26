# CTFTCTE-SDR-002 — Slice the envelope into symbols and decode the line code

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Counters technique:** [`CTFTTE-SDR-002`](../techniques/CTFTTE-SDR-002.md) — Line-coded on-off-keyed remote transmission

---

## Offensive Recovery (CTF practitioner / solver)

1. Find the burst carrier in the spectrum. Mix it to 0 Hz and band-limit it to a few times its occupied width.
2. Take the amplitude envelope and threshold it midway between the noise level and the on level to get on/off runs.
3. Split transmissions on long gaps. Recover the symbol unit as the largest length that fits every run as an integer multiple. The symbol rate is 1/unit; the Manchester bit rate is half of that.
4. Choose the line code from the run widths:
   - only 1–2-unit runs → Manchester; try both pair phases and both conventions (`10`=1 G.E. Thomas, `01`=1 IEEE 802.3);
   - two pulse widths with a constant period → PWM;
   - two gap widths → PPM.
5. Byte-align on the end of the 1010… preamble or on the sync word, convert to bytes and search for the flag format.
6. In inspectrum, the equivalent manual route is: cursors over the burst, an amplitude plot, a threshold plot, then extract the symbols and keep every other bit for Manchester.
7. `rtl_433 -A` prints a pulse analysis and a flex decoder (`-X`) to replay the decode.

## Forensic / Blue-Team Perspective (DFIR analyst)

A fixed-code OOK remote is replayable: once the payload is recovered from one capture, the same burst opens the door again. The finding is recorded with carrier frequency, symbol timing, line code and frame layout. Several captures are compared to tell fixed codes from rolling codes before any security claim is made. Analysis is receive-only; retransmission needs a licensed, isolated test setup.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1132 | Data Encoding | Recovery reverses the line code (Manchester/PWM/PPM) and the framing before reading the payload. |
| T1001.002 | Steganography | The payload is extracted from a radio burst disguised as an ordinary remote-control signal. |

## Tools

- [inspectrum](../tools/CTFTTOU-236.md)
- [Universal Radio Hacker](../tools/CTFTTOU-235.md)
- [rtl_433](../tools/CTFTTOU-336.md)
- [ook_decode.py](../../.agents/ctf/ctf-sdr/scripts/ook_decode.py) ([CTFTTOU-340](../tools/CTFTTOU-340.md))
- [iq_segments.py](../../.agents/ctf/ctf-sdr/scripts/iq_segments.py) ([CTFTTOU-342](../tools/CTFTTOU-342.md))
- [iq_check.py](../../.agents/ctf/ctf-sdr/scripts/iq_check.py) ([CTFTTOU-341](../tools/CTFTTOU-341.md))
- [rtl_sdr](../tools/CTFTTOU-347.md)
- [rtl_tcp](../tools/CTFTTOU-350.md)

## References

- <https://github.com/miek/inspectrum>
- <https://github.com/merbanan/rtl_433/blob/master/docs/ANALYZE.md>
- <https://github.com/jopohl/urh>
