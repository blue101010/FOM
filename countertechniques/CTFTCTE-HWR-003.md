# CTFTCTE-HWR-003 — Render and diff every PCB fabrication layer

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-HWR`](../tactics/CTFT-TA-HWR.md) — Hardware  
> **Counters technique:** [`CTFTTE-HWR-003`](../techniques/CTFTTE-HWR-003.md) — PCB fabrication-layer concealment

---

## Offensive Recovery (CTF practitioner / solver)

Identify each file's layer, then render every layer on its own, not only the top/bottom composites. Flag geometry that does not belong to the circuit, such as strokes tied to no pad, via or copper fill. When the original design is available, diff layer by layer against it. Adjust orientation (rotation, mirroring) before reading recovered text.

## Forensic / Blue-Team Perspective (DFIR analyst)

Fabrication packages are hardware supply-chain evidence: they are hashed on receipt and diffed per layer against the released design. Unconnected geometry and inconsistent generator metadata are recorded as tampering indicators.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1195.003 | Supply Chain Compromise: Compromise Hardware Supply Chain | Diffing against the released design echoes hardware supply-chain tamper detection. |
| T1027 | Obfuscated Files or Information | Per-layer plotting reverses plot-only hiding. |

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
