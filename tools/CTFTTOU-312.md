# CTFTTOU-312 — dirb

> **Tool ID:** `CTFTTOU-312`  
> **Related techniques/counters:** CTFTCTE-WEB-001, CTFTCTE-WEB-007, CTFTTE-WEB-001, CTFTTE-WEB-007

## Description

Classic wordlist-based web content scanner: requests each word as a path (optionally with
extensions via `-X`) and recurses into found directories. Ships the `common.txt` / `big.txt`
wordlists in `/usr/share/dirb/wordlists`, which other fuzzers commonly reuse. Single-threaded and
slow compared with [ffuf](CTFTTOU-013.md), [gobuster](CTFTTOU-079.md) or
[feroxbuster](CTFTTOU-078.md), but still a zero-configuration first pass on Kali.

## URL

<https://dirb.sourceforge.net/>

## Related Techniques

CTFTCTE-WEB-001, CTFTCTE-WEB-007, CTFTTE-WEB-001, CTFTTE-WEB-007
