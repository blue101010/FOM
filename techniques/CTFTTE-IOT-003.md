# CTFTTE-IOT-003 — Unauthenticated message-broker topic/queue concealment

> **Type:** Design / Hide Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Paired counter-technique:** [`CTFTCTE-IOT-003`](../countertechniques/CTFTCTE-IOT-003.md) — Enumerate broker topics/queues and capture service traffic

---

## How the challenge author hides

The ecosystem ships a publish/subscribe or message-queue service that accepts anonymous or
weakly-authenticated connections — any broker or bus technology (MQTT, CoAP resources, AMQP,
Redis pub/sub, a custom device bus). Data the player needs is stored or transits on
non-obvious channels: an unpublished topic, a retained message, a device-shadow update, a
dead-letter or administrative queue. The concealment is categorial: everyone treats the
broker as dumb infrastructure and nobody thinks to enumerate its namespace as an
information repository, the way one would enumerate a filesystem or an API.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Retained messages, shadows and admin queues routinely carry secrets nobody classified. |

## Tools

- [mosquitto clients](../tools/CTFTTOU-276.md) (MQTT family)
- [nmap](../tools/CTFTTOU-033.md)

## References

- <https://cwe.mitre.org/data/definitions/1188.html> (CWE-1188: Initialization of a Resource with an Insecure Configuration)
- Add challenge write-up link
