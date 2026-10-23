# CTFTTOU-307 — tracespace view

> **Tool ID:** `CTFTTOU-307`  
> **Related techniques/counters:** CTFTTE-HWR-003, CTFTCTE-HWR-003

## Description

Online Gerber and Excellon drill viewer that runs in the browser (open-source
tracespace project). Drop a folder or zip of fabrication files: it identifies each
layer, renders top and bottom board composites, and lets each layer be toggled and
viewed on its own, including inner copper, which the composites hide. It is the
fastest first look at an unknown PCB package, with no install. For confidential
boards, or for exact coordinates and crops, use gerbv / KiCad GerbView or
[gerber-layer-inspect.py](CTFTTOU-310.md) offline.

## URL

<https://tracespace.io/view/>

## Related Techniques

CTFTTE-HWR-003, CTFTCTE-HWR-003
