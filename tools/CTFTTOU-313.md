# CTFTTOU-313 — DirBuster

> **Tool ID:** `CTFTTOU-313`  
> **Related techniques/counters:** CTFTCTE-WEB-001, CTFTTE-WEB-001

## Description

OWASP Java GUI directory and file brute-forcer (legacy). Its multi-threaded engine and the
`directory-list-2.3-*.txt` wordlists (shipped in Kali under `/usr/share/wordlists/dirbuster`)
remain widely used. The project is no longer maintained, and OWASP folded the feature into ZAP
(Forced Browse). For new work prefer [ffuf](CTFTTOU-013.md), [gobuster](CTFTTOU-079.md) or
[feroxbuster](CTFTTOU-078.md) with the same wordlists.

## URL

<https://sourceforge.net/projects/dirbuster/>

## Related Techniques

CTFTCTE-WEB-001, CTFTTE-WEB-001
