# CTFTTE-FOR-034 — Obfuscated client-side script in a web artifact

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-034`](../countertechniques/CTFTCTE-FOR-034.md) — Deobfuscate and trace client-side script to the payload

---

## How the challenge author hides

A captured web artifact — a phishing page, a saved HTML file, an email attachment — carries
a block of deliberately obfuscated JavaScript. The script is minified to one line, packed
(`eval(function(p,a,c,k,e,d)...)`), and its strings are hex/base64/`String.fromCharCode`
encoded, so the real behaviour (the exfiltration URL, the decoded flag, the dropped payload
name) is not visible in the page source. Rendering the page runs the script but hides the
mechanism; reading the source shows only noise. The analyst is meant to statically
deobfuscate and follow the data flow to the hidden value rather than detonate the page.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The script's logic and strings are packed/encoded to resist source review. |
| T1059.007 | Command and Scripting Interpreter: JavaScript | The concealed payload is carried in client-side JavaScript inside a web artifact. |

## Tools

- [js-beautify](../tools/CTFTTOU-287.md)
- [de4js](../tools/CTFTTOU-263.md)
- [CyberChef](../tools/CTFTTOU-048.md)

## References

- <https://github.com/blue101010/writeups/blob/main/2024/cyber_apocalypse_2024_HTB/forensics/urgent/flag.md> (HTB Cyber Apocalypse 2024 "urgent")
