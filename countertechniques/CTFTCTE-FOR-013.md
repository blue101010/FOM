# CTFTCTE-FOR-013 — Retrieve information from diagram encodings

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-013`](../techniques/CTFTTE-FOR-013.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Treat the diagram as a positional code rather than a picture: establish the alphabet (how many
distinct states a cell can take), the reading order, and the grouping that maps cells to
symbols. Clock-like and lamp-row diagrams encode digits per row; colour or fill state usually
carries the value. For the Mengenlehreuhr family see
[`CTFTCTE-FOR-014`](CTFTCTE-FOR-014.md).

## Forensic / Blue-Team Perspective (DFIR analyst)

Diagram encodings leave no file-format trace — the carrier is an ordinary image. Only the
surrounding challenge context, or a recognisable diagram layout, identifies them.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Diagram encodings are CTF-specific obfuscation ATT&CK omits. |

## Tools

_See references._

## References

**Sources**

- (1) [Mengenlehreuhr Wikipedia](https://en.wikipedia.org/wiki/Mengenlehreuhr)

[Mengenlehreuhr dodona.be](https://dodona.be/en/courses/1/series/279/activities/527398301/)

[2024 - NSEC -  Dorsolateral Challenge](https://github.com/blue101010/writeups/blob/main/2024/NSEC/Dorsolateral/dorsolateral.md)


