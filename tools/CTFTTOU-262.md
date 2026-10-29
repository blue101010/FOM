# CTFTTOU-262 — qemu

> **Tool ID:** `CTFTTOU-262`  
> **Related techniques/counters:** CTFTCTE-PWN-007, CTFTTE-PWN-007, CTFTTE-IOT-008, CTFTCTE-IOT-008, CTFTTE-IOT-009, CTFTCTE-IOT-009

## Description

Machine emulator/virtualizer used to run and debug foreign-architecture binaries. Two
modes matter: user-mode emulation runs a single binary against its own libraries, and
full-system emulation boots a complete disk image on an emulated board — the latter needs
a machine type, optionally a kernel and device tree, and a `root=` boot argument that
names the emulated disk device.

## Binaries

- [qemu-img](CTFTTOU-444.md) — disk-image conversion, resizing, inspection, legacy qcow2 AES decryption
- `qemu-nbd` — expose an image as a network block device for partition mapping
- `qemu-system-arm` — full-system ARM emulation (`-M <board>`, `-kernel`, `-dtb`, `-drive`, `-append`)
- `qemu-system-x86_64` — full-system x86-64 emulation (`-hda`, `-boot c`, `-enable-kvm`)
- `qemu-<arch>-static` — user-mode emulation of a single binary (see CTFTTE-PWN-007)

## URL

<https://www.qemu.org/>

## Related Techniques

CTFTCTE-PWN-007, CTFTTE-PWN-007, CTFTTE-IOT-008, CTFTCTE-IOT-008, CTFTTE-IOT-009, CTFTCTE-IOT-009
