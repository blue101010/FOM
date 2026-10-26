# CTFTTE-SDR-002 — Line-coded on-off-keyed remote transmission

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Paired counter-technique:** [`CTFTCTE-SDR-002`](../countertechniques/CTFTCTE-SDR-002.md) — Slice the envelope into symbols and decode the line code

---

## How the challenge author hides

The flag is the payload of a short on-off-keyed (OOK/ASK) burst such as a garage-door remote, key fob or 433/868 MHz sensor. The carrier is only switched on and off, so demodulated audio sounds like clicks and carries no readable content. The bits are line-coded, typically Manchester (each bit is a transition pair), PWM (short/long pulse) or PPM (short/long gap), and framed by a 1010… preamble and a sync word. That doubles the symbol count and hides the byte alignment. The capture usually arrives as raw IQ (`.cf32`, `.cu8`) with the carrier off-centre. Distinct from CTFTTE-IOT-005, where the subject is an IoT protocol stack and its pairing keys, and from CTFTTE-SDR-001, where the modulation itself (AM/FM/FSK/PSK/QAM) is the barrier.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1132 | Data Encoding | Line coding (Manchester/PWM/PPM) is a reversible encoding layered under the payload; ATT&CK omits the RF physical layer. |
| T1001.002 | Steganography | The payload rides inside a radio burst that looks like an ordinary remote-control signal. |

## Tools

- [inspectrum](../tools/CTFTTOU-236.md)
- [Universal Radio Hacker](../tools/CTFTTOU-235.md)
- [rtl_433](../tools/CTFTTOU-336.md)
- [ook_decode.py](../../.agents/ctf/ctf-sdr/scripts/ook_decode.py) ([CTFTTOU-340](../tools/CTFTTOU-340.md))
- [iq_segments.py](../../.agents/ctf/ctf-sdr/scripts/iq_segments.py) ([CTFTTOU-342](../tools/CTFTTOU-342.md))
- [iq_check.py](../../.agents/ctf/ctf-sdr/scripts/iq_check.py) ([CTFTTOU-341](../tools/CTFTTOU-341.md))
- [rtl_sdr](../tools/CTFTTOU-347.md)
- [rtl_tcp](../tools/CTFTTOU-350.md)

## Indicators

- IQ capture holding a single narrow carrier (about 10–20 kHz occupied) that is fully on or off, with no FM/PSK structure
- inside a burst, no run longer than two symbol units (Manchester), or two pulse widths with a constant period (PWM/PPM)
- leading `0xAA`/`0x55` bytes once decoded (preamble) followed by a fixed word (sync)
- challenge story about a remote, key fob, garage, gate, doorbell or wireless sensor in the 315/433/868/915 MHz ISM bands

## References

- <https://github.com/miek/inspectrum>
- <https://github.com/merbanan/rtl_433>
- <https://en.wikipedia.org/wiki/Manchester_code>
