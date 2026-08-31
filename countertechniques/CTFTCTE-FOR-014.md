# CTFTCTE-FOR-014 — Retrieve information from Mengenlehreuhr diagram encodings

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-014`](../techniques/CTFTTE-FOR-014.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Retrieve information with [Mengenlehreuhr](https://en.wikipedia.org/wiki/Mengenlehreuhr) diagram
encoding. The clock has five rows: seconds (blinking), 5-hour, 1-hour, 5-minute and 1-minute
blocks. Count the lit cells per row and recombine to the encoded value.

Example: see [2024 - NSEC - Dorsolateral Challenge](https://github.com/blue101010/writeups/blob/main/2024/NSEC/Dorsolateral/dorsolateral.md)

## Forensic / Blue-Team Perspective (DFIR analyst)

The encoding is time-shaped but carries arbitrary values; do not assume a decoded row group is
an actual timestamp before checking the range.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Mengenlehreuhr diagram encoding is CTF-specific obfuscation ATT&CK omits. |

## Tools

_See references._

## References

**Sources**

- (1) [Mengenlehreuhr dodona.be](https://dodona.be/en/courses/1/series/279/activities/527398301/)
- (2) [Mengenlehreuhr Wikipedia](https://en.wikipedia.org/wiki/Mengenlehreuhr)

**Writeups**

- (1) [2024 - NSEC - Dorsolateral Challenge](https://github.com/blue101010/writeups/blob/main/2024/NSEC/Dorsolateral/dorsolateral.md)
