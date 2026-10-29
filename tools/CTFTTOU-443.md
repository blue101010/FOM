# CTFTTOU-443 — dtc

> **Tool ID:** `CTFTTOU-443`  
> **Related techniques/counters:** CTFTTE-IOT-008, CTFTCTE-IOT-008

## Description

The Device Tree Compiler suite (`device-tree-compiler` package): `dtc` converts between
human-readable DTS source and compiled DTB blobs, `fdtdump`/`fdtdisasm` pretty-print a
compiled blob with its structure block and strings, and `fdtget`/`fdtput` read and write
individual properties without a full decompile.

A `.dtb` is a Flattened Device Tree (magic `0xd00dfeed`) — a hardware-description table,
not an executable. Disassemblers and binary-analysis loaders reject it outright ("No load
spec found"), so `dtc` is the only route to readable content. In an emulation workflow the
decompiled tree settles two questions: which UART the console is attached to, and which
disk/SD aliases the kernel's `root=` argument must name.

## URL

- <https://git.kernel.org/pub/scm/utils/dtc/dtc.git>
- <https://www.devicetree.org/specifications/>

## Usage

```bash
sudo apt install -y device-tree-compiler

# decompile a blob to readable source
dtc -I dtb -O dts board.dtb > board.dts

# structure + strings dump without converting
fdtdump -s board.dtb

# read one property (console alias, partition alias)
fdtget board.dtb /aliases serial0
```

## Notes

- `file` identifies the blob ("Device Tree Blob version 17, boot CPU 0, …") — the version
  and block sizes it prints are the quickest sanity check before decompiling.
- A DTB supplied with a challenge is usually the emulator's board description, not the
  device's own: decompiling it tells you which machine type the boot expects.
- `dtc` round-trips with warnings about phandle references; they are informational, not
  failures.

## Related Techniques

CTFTTE-IOT-008, CTFTCTE-IOT-008
