# CTFTTOU-304 — coreutils

> **Tool ID:** `CTFTTOU-304`  
> **Related techniques/counters:** CTFTTE-FOR-032, CTFTCTE-FOR-032, CTFTTE-FOR-033, CTFTCTE-FOR-033

## Description

GNU core utilities used as a comparison set: `sha256sum | sort | uniq -c` collapses many near-identical files to the single outlier by content hash; `sort` / `uniq` / `comm` reassemble fragments into one ordered stream.

## URL

<https://www.gnu.org/software/coreutils/>

## Related Techniques

CTFTTE-FOR-032, CTFTCTE-FOR-032, CTFTTE-FOR-033, CTFTCTE-FOR-033
