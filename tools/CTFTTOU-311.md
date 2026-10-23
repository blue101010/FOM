# CTFTTOU-311 — gerber-matplotlib-plot.py

> **Tool ID:** `CTFTTOU-311`  
> **Related techniques/counters:** CTFTTE-HWR-003, CTFTCTE-HWR-003

## Description

CTFT copy of the classic write-up approach to Gerber files: regex-parse
`X<n>Y<n>D0<n>` operations and plot D01 strokes as lines and D03 flashes as dots
with matplotlib, one PNG per layer, with an optional `--window` zoom in file units.
Generalised from the CTFBase "Critical Flight" script (local solve
`2026/HB/TRY/Critical_Flight/solve_visualize.py`, with hard-coded layers and
windows replaced by CLI arguments). Requires matplotlib (`~/.venvs/ctfml` or
`sudo apt install python3-matplotlib`).

It is a baseline. It skips modal coordinates and ignores aperture widths, arcs,
regions and clear polarity. For faithful rendering, reference-free hunting and
diffing use [gerber-layer-inspect.py](CTFTTOU-310.md).

## URL

<https://github.com/blue101010/FOM/blob/main/tools/scripts/gerber-matplotlib-plot.py>

Local copy: [scripts/gerber-matplotlib-plot.py](scripts/gerber-matplotlib-plot.py)

## Related Techniques

CTFTTE-HWR-003, CTFTCTE-HWR-003
