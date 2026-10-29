# CTFTTOU-445 — losetup / kpartx

> **Tool ID:** `CTFTTOU-445`  
> **Related techniques/counters:** CTFTTE-IOT-009, CTFTCTE-IOT-009, CTFTTE-FOR-035, CTFTCTE-FOR-035, CTFTTE-IOT-001, CTFTCTE-IOT-001

## Description

Partition mapping for disk images, the step between "I have an image file" and "I can
mount a filesystem from it":

- `losetup -fP image` attaches a raw image to the next free loop device **and** scans
  partitions, creating `/dev/loopXpN` nodes for each entry in the table;
- `kpartx -av` builds the same device-mapper nodes for images sitting on top of another
  block layer (a qcow2 exposed via `qemu-nbd`, an LVM volume), where a plain loop attach
  cannot see the partitions;
- `kpartx -d` / `losetup -D` tear the mapping down cleanly before the image is used
  elsewhere.

Combined with `file -s` on each mapper node, it identifies every filesystem in an image
without booting it — the entry point for offline rootfs inspection, credential-store
access and evidence carving.

## URL

- <https://man7.org/linux/man-pages/man8/losetup.8.html>
- <https://man7.org/linux/man-pages/man8/kpartx.8.html>

## Usage

```bash
# raw image: loop attach with partition scan
sudo losetup -fP image.raw
file -s /dev/loop0p*          # identify each partition
sudo mount /dev/loop0p2 /mnt/rootfs

# qcow2 (via nbd) or image on another block layer
sudo qemu-nbd --connect=/dev/nbd0 image.qcow2
sudo kpartx -av /dev/nbd0
sudo mount /dev/mapper/nbd0p2 /mnt/rootfs

# teardown
sudo umount /mnt/rootfs
sudo kpartx -d /dev/nbd0 && sudo qemu-nbd --disconnect /dev/nbd0
sudo losetup -D
```

## Notes

- Always operate on a copy when the mount is read-write — the mapping writes through to
  the image file.
- Partition-table CHS values can be garbage while the start-sector offsets are valid:
  trust the offsets, not the geometry.
- `mount -o loop` on the image file is the one-partition shortcut; `losetup -fP`/`kpartx`
  are needed the moment there is more than one partition or a block layer in between.

## Related Techniques

CTFTTE-IOT-009, CTFTCTE-IOT-009, CTFTTE-FOR-035, CTFTCTE-FOR-035, CTFTTE-IOT-001, CTFTCTE-IOT-001
