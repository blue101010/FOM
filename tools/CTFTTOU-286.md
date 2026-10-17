# CTFTTOU-286 — diffutils / coreutils comparison set

> **Tool ID:** `CTFTTOU-286`  
> **Related techniques/counters:** CTFTTE-FOR-032, CTFTCTE-FOR-032, CTFTTE-FOR-033, CTFTCTE-FOR-033

## Description

The standard file-comparison and set-arithmetic toolset: `diff`/`cmp` for pairwise
difference, and `sha256sum | sort | uniq -c` (coreutils) to collapse a large directory of
near-identical files down to the single outlier by content hash. In a haystack challenge
the outlier is the file whose hash count is 1; the same `sort`/`uniq`/`comm` pipeline
reassembles fragments gathered from many files into a single ordered stream. Scales to
tens of thousands of inputs without loading them all into memory, which is why it replaces
a hand-written comparison loop.

## URL

<https://www.gnu.org/software/diffutils/> — coreutils: <https://www.gnu.org/software/coreutils/>

## Related Techniques

CTFTTE-FOR-032, CTFTCTE-FOR-032, CTFTTE-FOR-033, CTFTCTE-FOR-033
