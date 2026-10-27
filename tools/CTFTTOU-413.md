# CTFTTOU-413 — LogFileParser

> **Tool ID:** `CTFTTOU-413`  
> **Related techniques/counters:** CTFTTE-FOR-022, CTFTCTE-FOR-022, CTFTTE-FOR-028, CTFTCTE-FOR-028

## Description

Parser for the NTFS `$LogFile`, the file system's transactional journal. LogFileParser (by Joakim Schicht, `jschicht`) decodes the journal's redo/undo records into the individual operations NTFS performed — file and directory create, delete, rename, data and `$STANDARD_INFORMATION`/`$FILE_NAME` timestamp changes, `$INDEX` updates — so a solver can reconstruct recent file-system activity and spot anti-forensic timestomping even after the files are gone. Output goes to CSV or a SQL schema for querying. Pairs naturally with MFT (`$MFT`) and USN journal (`$UsnJrnl:$J`) analysis to corroborate a Windows timeline.

## URL

- <https://github.com/jschicht/LogFileParser>

## Usage

```text
# GUI: point it at an extracted $LogFile (and optionally $MFT for name resolution),
# choose CSV or SQL output, then parse.
LogFileParser64.exe        # 64-bit build
LogFileParser.exe          # 32-bit build
# Extract the artifacts first with The Sleuth Kit / FTK Imager / KAPE:
#   icat image.raw <$LogFile-inode>  > LogFile
```

## Binaries

- LogFileParser64.exe — 64-bit (x64) build
- LogFileParser.exe — 32-bit (x86) build

## Skills

- [ctf-windows-artifact-timeline](../skills/CTFTSKL-005.md)

## Related Techniques

CTFTTE-FOR-022, CTFTCTE-FOR-022, CTFTTE-FOR-028, CTFTCTE-FOR-028

## References

- [LogFileParser (jschicht) — GitHub](https://github.com/jschicht/LogFileParser)
- [NTFS $LogFile forensics — overview](https://www.sans.org/blog/ntfs-log-tracker/)

## Notes

Used in Hackfest 2025 forensics (APT514 workshop, `02_Execution`) to recover file-system
operations from the NTFS `$LogFile`, alongside MFTECmd and LogParser.
