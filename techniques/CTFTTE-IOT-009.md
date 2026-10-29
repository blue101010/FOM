# CTFTTE-IOT-009 — Offline credential reset on a mounted rootfs

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-009`](../countertechniques/CTFTCTE-IOT-009.md) — Mount the rootfs offline and reset or crack the credential

---

## How the challenge author hides

The device's only interactive surface is a login prompt, and the objective sits behind it:
a boot banner, a login-time script, or a shell session the player must reach. No credentials
are given. The image itself is handed over unencrypted, so the rootfs can be mounted offline
— the concealment is the assumption that the player will treat the login as a wall to crack
rather than a file to edit. The author often raises the stakes by pairing the account with a
strong password hash that resists wordlist and rule attacks (see CTFTTE-CRY-012), pushing the
solver toward offline cracking while the mount-and-edit path stays open. Distinct from
CTFTTE-IOT-002, where the credential gate is a device web application with a backdoor, and
from CTFTTE-FOR-020, where the volume itself is encrypted.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1003 | OS Credential Dumping | Reading the offline credential store of a mounted image is credential dumping without ever running the device. |
| T1078 | Valid Accounts | Blanking or replacing the stored hash is the preparation half of valid-account use; the login is the use. |

## Tools

- [losetup / kpartx](../tools/CTFTTOU-445.md)
- [qemu-img](../tools/CTFTTOU-444.md)
- [hashcat](../tools/CTFTTOU-011.md)

## Indicators

- a login prompt on the emulated or physical console with no credentials provided anywhere in the challenge text
- a rootfs partition that mounts read-write offline, with a standard credential store (`/etc/shadow` or equivalent)
- a password hash that survives wordlist and rule attacks, hinting the intended path is not cracking
- an objective phrased as what the system *shows* or *does* once logged in, rather than a stored secret

## References

- <https://man7.org/linux/man-pages/man5/shadow.5.html>
- <https://hashcat.net/hashcat/>
