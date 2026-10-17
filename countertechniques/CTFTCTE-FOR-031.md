# CTFTCTE-FOR-031 — Extract and decode strings from Office VBA macros

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Counters technique:** [`CTFTTE-FOR-031`](../techniques/CTFTTE-FOR-031.md) — Office VBA macro string concealment

---

## Offensive Recovery (CTF practitioner / solver)

1. Confirm the container: a `.docm`/`.xlsm` is a ZIP — `unzip -l` lists the parts and
   `word/vbaProject.bin` (or `xl/vbaProject.bin`) is the OLE stream holding the macros.
2. Dump the macro source without Office: `olevba <file>` extracts the VBA and highlights
   auto-exec entry points and string-building constructs; `oledump.py` dumps the raw stream
   bytes when `olevba` can't parse a mangled project.
3. Read the deobfuscation `olevba` already performed; for anything it leaves, reproduce the
   macro's own transform by hand — evaluate the `Chr()`/`StrReverse`/concat chain, or feed
   the base64/XOR argument to [CyberChef](../tools/CTFTTOU-048.md).
4. If the macro only reconstructs the string at run time, port the VBA expression to Python
   (or run it in a sandboxed VBA host) and print the result instead of executing the rest.

## Forensic / Blue-Team Perspective (DFIR analyst)

Macro malware is triaged the same way: `olevba`/`oledump` over the document, never
double-clicking it. Analysts record the auto-exec triggers (`AutoOpen`, `Document_Open`),
the deobfuscated indicators (URLs, dropped filenames), and whether the macro is signed.
Detonation, if needed, happens in an isolated VM with Office instrumented, not on the
analysis host.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | Recovery reverses the run-time string assembly to reveal the literal payload. |
| T1059.005 | Command and Scripting Interpreter: Visual Basic | The analysed logic is VBA macro code inside an Office document. |

## Tools

- [oletools (olevba / oledump)](../tools/CTFTTOU-285.md)
- [CyberChef](../tools/CTFTTOU-048.md)
- [strings](../tools/CTFTTOU-200.md)

## References

- <https://github.com/jselliott/HTBCyberSanta2021/tree/main/forensics/giveaway>
- <https://github.com/decalage2/oletools>
