# CTFTTOU-029 — UPX

> **Tool ID:** `CTFTTOU-029`  
> **Related techniques/counters:** CTFTTE-FPN-016, CTFTCTE-FPN-016

## Description

Executable packer. In the writeup a single `upx` pass over a potato-class binary was enough to clear Microsoft Defender static detection, allowing the impersonation exploit to execute on the victim. The packer signature is equally a detection clue for the defensive side.

## URL

<https://upx.github.io/>

## Related Techniques

CTFTTE-FPN-016, CTFTCTE-FPN-016
