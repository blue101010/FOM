# CTFTTOU-318 — wget

> **Tool ID:** `CTFTTOU-318`  
> **Related techniques/counters:** CTFTCTE-WEB-007, CTFTCTE-WEB-022, CTFTTE-WEB-007, CTFTTE-WEB-022

## Description

GNU non-interactive downloader. Its recursive mirroring (`-r -np -nH`, `--mirror`) pulls
whole exposed trees such as directory listings, an exposed `.git/` or bundled assets with
their source maps, for offline analysis. Complements [curl](CTFTTOU-038.md), which is better
for single crafted requests.

## URL

<https://www.gnu.org/software/wget/>

## Related Techniques

CTFTCTE-WEB-007, CTFTCTE-WEB-022, CTFTTE-WEB-007, CTFTTE-WEB-022
