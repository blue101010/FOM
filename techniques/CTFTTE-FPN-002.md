# CTFTTE-FPN-002 — Windows Active Directory fullpwn

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-FPN`](../tactics/CTFT-TA-FPN.md) — Full Pwn / Multi-Stage  
> **Paired counter-technique:** [`CTFTCTE-FPN-002`](../countertechniques/CTFTCTE-FPN-002.md) — Enumerate AD, abuse delegation or ACL paths to the DC

---

## How the challenge author hides

The flag resides on a Domain Controller; reaching it requires a chain of AD-specific attacks (Kerberoasting, AS-REP Roasting, delegation abuse, or ACL exploitation) rather than a single CVE.

## ATT\&CK Complementarity

Complements TA0006 (Credential Access) and T1558 (Steal or Forge Kerberos Tickets) with CTF-specific AD attack-chain sequencing detail.

## Tools

- bloodhound / sharphound
- impacket
- kerbrute
- evil-winrm

## References

- https://github.com/BloodHoundAD/BloodHound
- https://github.com/fortra/impacket
- Add challenge write-up link
