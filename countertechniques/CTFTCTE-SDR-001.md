# CTFTCTE-SDR-001 — Demodulate and decode RF captures

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-SDR`](../tactics/CTFT-TA-SDR.md) — Software-Defined Radio  
> **Counters technique:** [`CTFTTE-SDR-001`](../techniques/CTFTTE-SDR-001.md) — RF/SDR signal embedding

---

## Offensive Recovery (CTF practitioner / solver)

Load the IQ capture in Gqrx/GNU Radio, identify the modulation from the waterfall and constellation, demodulate, and decode the recovered bitstream into the flag.

## Forensic / Blue-Team Perspective (DFIR analyst)

RF captures are analyzed like any volatile signal artifact: center frequency, bandwidth and modulation are the recovery keys, and SDR snapshots can be replayed indefinitely.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | RF-domain data hiding echoes steganography; ATT&CK omits the demodulation craft. |

## Tools

- Gqrx
- GNU Radio Companion
- Universal Radio Hacker
- inspectrum
- multimon-ng

## References

- <https://github.com/jopohl/urh>

