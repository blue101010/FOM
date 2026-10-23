# CTFTTOU-309 — KiCad GerbView

> **Tool ID:** `CTFTTOU-309`  
> **Related techniques/counters:** CTFTTE-HWR-003, CTFTCTE-HWR-003

## Description

Gerber/drill viewer shipped with the KiCad EDA suite. It loads a whole fabrication
package as layers, reads X2 attributes (`TF.FileFunction`, aperture functions,
net names), and can export the Gerbers back into a `.kicad_pcb` for inspection in
Pcbnew. It is the reference renderer for KiCad-generated packages, the usual
source of CTF board files.

## URL

<https://www.kicad.org/>

## Related Techniques

CTFTTE-HWR-003, CTFTCTE-HWR-003
