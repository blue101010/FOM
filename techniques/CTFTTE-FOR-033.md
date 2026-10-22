# CTFTTE-FOR-033 — Flag fragments disseminated across filesystem artifacts

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FOR`](../tactics/CTFT-TA-FOR.md) — Forensics  
> **Paired counter-technique:** [`CTFTCTE-FOR-033`](../countertechniques/CTFTCTE-FOR-033.md) — Aggregate disseminated flag fragments across files

---

## How the challenge author hides

No single file holds the flag. It is broken into pieces and scattered across many locations —
individual characters embedded in shell-persistence files (`.bashrc`, cron entries, systemd
units, `/etc/*`), one letter per file in a tree, or fragments appended to otherwise innocuous
logs. Each fragment on its own is meaningless, and the flag only appears once every piece is
collected in the correct order. The concealment defeats a single-file search: the analyst has
to recognise the dissemination pattern (which files, which position marks ordering) and
reassemble, not just locate.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1027 | Obfuscated Files or Information | The secret is split into fragments distributed across unrelated artifacts so no single file reveals it. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | Shell-startup and persistence files are a common carrier for the disseminated fragments. |

## Tools

- [grep](../tools/CTFTTOU-036.md)
- [strings](../tools/CTFTTOU-200.md)
- [diffutils](../tools/CTFTTOU-303.md)
- [coreutils](../tools/CTFTTOU-304.md)

## References

- <https://github.com/blue101010/writeups/blob/main/2024/cyber_apocalypse_2024_HTB/forensics/it_has_begun/flag.md> (HTB Cyber Apocalypse 2024 "it has begun")
- <https://github.com/blue101010/writeups/blob/main/2023/LinuxMeetup_Montreal/init2_recherche.md> (Linux Meetup Montréal 2023, disseminated-letters pattern)
