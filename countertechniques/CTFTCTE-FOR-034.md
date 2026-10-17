# CTFTCTE-FOR-034 — Deobfuscate and trace client-side script to the payload

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-034`](../techniques/CTFTTE-FOR-034.md) — Obfuscated client-side script in a web artifact

---

## Offensive Recovery (CTF practitioner / solver)

1. Isolate the script from the artifact (the `<script>` block, the `.js` file, the HTML
   attachment) and work on it statically — do not open the page in a live browser.
2. Restore structure first: run it through [js-beautify](../tools/CTFTTOU-287.md) to expand
   the one-liner, then [de4js](../tools/CTFTTOU-263.md) to unpack `eval(p,a,c,k,e,d)` and
   `eval`/`Function` wrappers into plain source.
3. Decode the string literals: `String.fromCharCode`, `\xNN`/`\uNNNN`, base64 and URL layers
   go through [CyberChef](../tools/CTFTTOU-048.md). Follow the data flow to the sink — the
   `fetch`/`XMLHttpRequest` URL, the `document.location` redirect, or the variable printed/
   concatenated into the DOM — which is where the flag or exfil target resolves.
4. If the script self-decodes at run time, neutralise the sink and evaluate it safely:
   replace `eval`/network calls with `console.log` and run under Node in a throwaway
   sandbox to print the decoded value instead of executing it.

## Forensic / Blue-Team Perspective (DFIR analyst)

This is standard malicious-JavaScript triage for phishing and drive-by pages: beautify,
unpack, decode, and read the indicators (C2 URL, dropped filename, decoded command) without
detonating on the analysis host. Dynamic analysis, when required, uses an instrumented
JS sandbox (e.g. a `box-js`-style interpreter) rather than a real browser.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Recovery reverses packing/encoding to reveal the script's real behaviour. |
| T1059.007 | Command and Scripting Interpreter: JavaScript | The analysed payload is client-side JavaScript. |

## Tools

- [js-beautify](../tools/CTFTTOU-287.md)
- [de4js](../tools/CTFTTOU-263.md)
- [CyberChef](../tools/CTFTTOU-048.md)

## References

- <https://github.com/blue101010/writeups/blob/main/2024/cyber_apocalypse_2024_HTB/forensics/urgent/flag.md>
