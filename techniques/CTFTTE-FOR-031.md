# CTFTTE-FOR-031 — Office VBA macro string concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-031`](../countertechniques/CTFTCTE-FOR-031.md) — Extract and decode strings from Office VBA macros

---

## How the challenge author hides

The flag is placed inside a VBA macro embedded in a macro-enabled Office document
(`.docm`, `.xlsm`, `.doc`). It is never present as plaintext: the macro rebuilds it at run
time from obfuscated pieces — character-code arrays (`Chr(72) & Chr(84) & ...`),
`StrReverse`, split-and-concatenate, base64 or XOR routines — so opening the document and
reading the visible text yields nothing, and the string does not survive a plain `strings`
pass over the ZIP container. The concealment leans on the analyst either trusting the
rendered document or lacking Office to "run" the macro.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The payload string is assembled at run time from obfuscated fragments rather than stored literally. |
| T1059.005 | Command and Scripting Interpreter: Visual Basic | The hidden data lives in VBA macro code inside an Office document. |

## Tools

- [oletools](../tools/CTFTTOU-301.md)
- [oledump.py](../tools/CTFTTOU-302.md)
- [CyberChef](../tools/CTFTTOU-048.md)
- [strings](../tools/CTFTTOU-200.md)

## References

- <https://github.com/jselliott/HTBCyberSanta2021/tree/main/forensics/giveaway> (HTB Cyber Santa 2021 "giveaway")
- <https://github.com/decalage2/oletools>
