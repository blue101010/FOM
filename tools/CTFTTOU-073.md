# CTFTTOU-073 — ghidra

> **Tool ID:** `CTFTTOU-073`  
> **Related techniques/counters:** CTFTTE-GAM-004, CTFTCTE-GAM-004, CTFTTE-HWR-002, CTFTCTE-HWR-002, CTFTTE-PWN-009, CTFTCTE-PWN-009, CTFTTE-PWN-010, CTFTCTE-PWN-010, CTFTTE-REV-001, CTFTCTE-REV-001, CTFTTE-REV-008, CTFTCTE-REV-008, CTFTTE-REV-009, CTFTCTE-REV-009, CTFTTE-REV-010, CTFTCTE-REV-010

## Description

NSA-developed open-source reverse-engineering suite (disassembler + decompiler). The
default static-analysis workbench across the RE-heavy domains: decompile win-condition
checks (GAM), badge firmware (HWR), anti-analysis-guarded flag logic (REV), and in
privilege-escalation work locate hard-coded constants such as a fixed output-folder name
a SUID helper writes to (PWN-009/010, REV-010). Go binaries decompiled here also expose
the package-path symbols that pivot to upstream source (CTFTCTE-REV-010).

## URL

<https://ghidra-sre.org/>

## Related Techniques

CTFTTE-GAM-004, CTFTCTE-GAM-004, CTFTTE-HWR-002, CTFTCTE-HWR-002, CTFTTE-PWN-009,
CTFTCTE-PWN-009, CTFTTE-PWN-010, CTFTCTE-PWN-010, CTFTTE-REV-001, CTFTCTE-REV-001,
CTFTTE-REV-008, CTFTCTE-REV-008, CTFTTE-REV-009, CTFTCTE-REV-009, CTFTTE-REV-010,
CTFTCTE-REV-010
