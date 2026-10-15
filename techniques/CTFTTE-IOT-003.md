# CTFTTE-IOT-003 — Unauthenticated MQTT/CoAP broker topic concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-003`](../countertechniques/CTFTCTE-IOT-003.md) — Enumerate broker topics and capture device traffic

---

## How the challenge author hides

The device ecosystem publishes telemetry (and the flag) over an MQTT broker or CoAP server
with no authentication, or with credentials only implied by the challenge story. The flag
transits on a non-obvious topic name (`home/garage/secret`, a device shadow update, a
retained message) or a CoAP resource path; the concealment is that nobody thinks to treat the
broker as an information repository and enumerate its topic namespace.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Retained broker messages and device shadows routinely carry secrets no one classified. |

## Tools

- mosquitto clients ([CTFTTOU-276](../tools/CTFTTOU-276.md))
- [nmap](../tools/CTFTTOU-033.md)

## References

- <https://mqtt.org/> — protocol semantics (retained messages, wildcards)
- Add challenge write-up link
