# CTFTTOU-444 — qemu-img

> **Tool ID:** `CTFTTOU-444`  
> **Part of:** [`CTFTTOU-262`](CTFTTOU-262.md) — qemu  
> **Related techniques/counters:** CTFTTE-FOR-035, CTFTCTE-FOR-035, CTFTTE-IOT-008, CTFTCTE-IOT-008, CTFTTE-IOT-009, CTFTCTE-IOT-009

## Description

The disk-image utility of the qemu suite: converts between every virtualization container
(raw, qcow2, vmdk, vdi, vhdx, and appliance-archive members), resizes images, and reports
format, virtual size and encryption via `info`. Its sibling `qemu-nbd` exposes an image as a
network block device so partition tools can map it without a full conversion.

Two behaviours matter for CTF work:

- **container friction** — an emulator that refuses an image (wrong format, non-power-of-two
  size) is answered by `convert`/`resize`, never by touching the original;
- **legacy qcow2 AES** — `info`/`file` report "AES-encrypted (v2/v3)". The format has no
  separate key file: converting to another format prompts for the image password and
  decrypts in passing.

## URL

- <https://www.qemu.org/docs/master/interop/qemu-img.html>

## Usage

```bash
# identify a container before choosing a tool
qemu-img info image.qcow2

# convert between containers (vmdk member of an appliance archive -> qcow2)
qemu-img convert -f vmdk -O qcow2 disk001.vmdk disk.qcow2

# decrypt legacy qcow2 AES: convert prompts for the image password
qemu-img convert -O raw encrypted.qcow2 decrypted.img

# resize when the emulator demands a power-of-two size
qemu-img resize sdcard.qcow2 128M

# expose an image as a block device for partition mapping
sudo qemu-nbd --connect=/dev/nbd0 disk.qcow2
```

## Notes

- `convert` writes a new file and never modifies the source — it doubles as the
  work-on-a-copy step.
- Resizing up is safe; resizing down loses data.
- The qcow2 AES format is deprecated upstream; a decrypted copy is a derived artifact and
  should be labelled as such.

## Related Techniques

CTFTTE-FOR-035, CTFTCTE-FOR-035, CTFTTE-IOT-008, CTFTCTE-IOT-008, CTFTTE-IOT-009, CTFTCTE-IOT-009
