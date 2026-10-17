# CTFTTOU-278 — usbmon

> **Tool ID:** `CTFTTOU-278`  
> **Related techniques/counters:** CTFTTE-HWR-001, CTFTCTE-HWR-001

## Description

Linux kernel USB capture facility (`modprobe usbmon`). Exposes raw USB traffic as
character devices under `/sys/kernel/debug/usb/usbmon/` (0u = all buses) that Wireshark
and tshark read directly as a capture source. Maintained as part of the kernel itself —
unlike legacy userspace dumpers, the capture path never goes stale. On Windows the
equivalent capture source is USBPcap, bundled with Wireshark.

## URL

<https://www.kernel.org/doc/html/latest/usb/usbmon.html>

## Related Techniques

CTFTTE-HWR-001, CTFTCTE-HWR-001
