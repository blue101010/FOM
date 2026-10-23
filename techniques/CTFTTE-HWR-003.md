# CTFTTE-HWR-003 — PCB fabrication-layer concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-HWR`](../tactics/CTFT-TA-HWR.md) — Hardware  
> **Paired counter-technique:** [`CTFTCTE-HWR-003`](../countertechniques/CTFTCTE-HWR-003.md) — Render and diff every PCB fabrication layer

---

## How the challenge author hides

The flag is drawn as geometry inside a circuit board's fabrication data (Gerber, drill, or other manufacturing exports): copper text, artwork, or a pattern placed on a layer that is invisible or overlapped on the finished board, such as inner copper or areas under outer copper, or split across several layers. The files are plain coordinate streams, so the data surfaces only when each layer is plotted on its own.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1195.003 | Supply Chain Compromise: Compromise Hardware Supply Chain | Tampered fabrication data echoes design-stage hardware supply-chain compromise. |
| T1027 | Obfuscated Files or Information | Plot-only data hides in plain-text coordinate streams. |

## Tools

- [tracespace view](../tools/CTFTTOU-307.md)
- [gerbv](../tools/CTFTTOU-308.md)
- [KiCad GerbView](../tools/CTFTTOU-309.md)
- [gerber-layer-inspect.py](../tools/scripts/gerber-layer-inspect.py) ([CTFTTOU-310](../tools/CTFTTOU-310.md))
- [gerber-matplotlib-plot.py](../tools/scripts/gerber-matplotlib-plot.py) ([CTFTTOU-311](../tools/CTFTTOU-311.md))

## References

- <https://www.ucamco.com/en/gerber>
- <https://tracespace.io/view/>
- <https://ctfbase.com/writeup/20260128_htb_critical_flight>
- <https://cristi075.github.io/posts/htb-cyber-apocalypse-2023-critical-flight/>
- <https://github.com/pms67/HadesFCS>
