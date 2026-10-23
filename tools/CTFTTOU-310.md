# CTFTTOU-310 — gerber-layer-inspect.py

> **Tool ID:** `CTFTTOU-310`  
> **Related techniques/counters:** CTFTTE-HWR-003, CTFTCTE-HWR-003

## Description

CTFT-authored Gerber RS-274X analyser (Python, standard library only — no pip
install, safe on Kali under PEP 668). Four subcommands:

- `info` — layer inventory from `TF.FileFunction` (KiCad comment form included);
  flags inner copper layers.
- `render` — PNG (built-in rasterizer, readable by vision-capable agents) or SVG,
  with `--window X1,Y1,X2,Y2`, `--ppmm`, `--mirror`, `--rotate 90|180|270`.
- `hunt` — reference-free detector. It reports copper stroke components that touch
  no pad/via flash and no pour region, i.e. drawn text or artwork, clusters them,
  and writes zoomed crops (both 90° and 270° for vertical runs).
- `diff` — suspect vs reference layer, keyed on geometry plus aperture definition
  (not per-file D-code numbers). ADDED and REMOVED clusters are filtered by
  `--min-segments` to absorb cross-CAD-version re-export noise.

It supersedes the matplotlib baseline [gerber-matplotlib-plot.py](CTFTTOU-311.md), which matches only `X..Y..D0n` lines. It handles modal
coordinates, the `%FS` format and `%MO` units, arcs (G02/G03, G74/G75), regions
(G36/G37), clear polarity (`%LPC%`), and KiCad `RoundRect` macro pads.
`--selftest` covers parsing, hunt, diff, arcs and PNG output.

Validated on HTB "Critical Flight": `hunt` returns exactly the two payload
clusters (B_Cu and In1_Cu) in under a second, and `diff` against the upstream
pms67/HadesFCS Gerbers confirms them as the only additions.

## URL

<https://github.com/blue101010/FOM/blob/main/tools/scripts/gerber-layer-inspect.py>

Local copy: [scripts/gerber-layer-inspect.py](scripts/gerber-layer-inspect.py)

## Related Techniques

CTFTTE-HWR-003, CTFTCTE-HWR-003
