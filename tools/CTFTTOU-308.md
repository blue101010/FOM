# CTFTTOU-308 — gerbv

> **Tool ID:** `CTFTTOU-308`  
> **Related techniques/counters:** CTFTTE-HWR-003, CTFTCTE-HWR-003

## Description

Open-source Gerber (RS-274X) and Excellon drill viewer (gEDA project). It opens
any number of layers, with per-layer visibility, colour and alpha, a measure tool
and coordinate readout. It also exports to PNG, SVG and PDF from the command line
(`gerbv -x png -D 1200 -o out.png layer.gbr`), which makes it scriptable for
batch layer rendering. Available in Kali/Debian: `sudo apt install gerbv`.

## URL

<https://gerbv.github.io/>

## Related Techniques

CTFTTE-HWR-003, CTFTCTE-HWR-003
