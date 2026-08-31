# CTFTCTE-STE-006 — Detect and decode linguistic steganography

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-STE`](../tactics/CTFT-TA-STE.md) — Steganography  
> **Counters technique:** [`CTFTTE-STE-006`](../techniques/CTFTTE-STE-006.md)  

---

## Offensive Recovery (CTF practitioner / solver)

Linguistic steganography hides the payload in the *choice* of words, not in the bytes that
carry them. Work on the text as a sequence of decisions: first letters of each line, sentence
or paragraph (acrostic), every n-th word, synonym substitution against a plausible baseline,
or deliberate misspellings. Reconstruct the candidate string for each rule and test it against
the expected flag format before trying the next.

## Forensic / Blue-Team Perspective (DFIR analyst)

The carrier is valid, readable prose, so no file-format check will flag it. Detection is
statistical: unusual synonym distribution, an improbable rate of typos, or word choices that
diverge from the author's other texts.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1001.002 | Steganography | Linguistic steganography. |

## Tools

- CyberChef
- manual analysis

## References

**Sources**

- (1) [Steganography — Wikipedia](https://en.wikipedia.org/wiki/Steganography)

**Writeups**

- Add challenge write-up link
