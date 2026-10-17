# CTFTTOU-285 — oletools (olevba / oledump)

> **Tool ID:** `CTFTTOU-285`  
> **Related techniques/counters:** CTFTTE-FOR-031, CTFTCTE-FOR-031

## Description

Python toolkit for analysing Microsoft OLE2 / Office Open XML documents. `olevba`
extracts and deobfuscates VBA macro source from `.doc`/`.docm`/`.xlsm` files and flags
suspicious constructs (auto-exec, `Chr()`/`StrReverse` string building, shell-out);
`oledump.py` lists the OLE streams and dumps the raw macro bytes for manual decoding.
The direct way to pull the hidden string out of a macro-bearing Office document without
opening it in Office.

## URL

<https://github.com/decalage2/oletools>

## Related Techniques

CTFTTE-FOR-031, CTFTCTE-FOR-031
