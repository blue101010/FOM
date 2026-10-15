# CTFTCTE-IOT-003 — Enumerate broker topics and capture device traffic

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-003`](../techniques/CTFTTE-IOT-003.md) — Unauthenticated MQTT/CoAP broker topic concealment

---

## Offensive Recovery (CTF practitioner / solver)

1. Find the broker: nmap service scan for 1883/8883 (MQTT), 5683/5684 (CoAP/DTLS).
2. Subscribe with wildcards (`mosquitto_sub -t '#' -v`) — retained messages and the full
   topic namespace usually reveal the device tree immediately.
3. If credentials are required, mine the firmware (IOT-001) and the device story for
   defaults; many brokers ship with anonymous read ACLs even when write is gated.
4. For CoAP, enumerate resource paths (`.well-known/core` when enabled) and GET/observe.
5. Validate: capture long enough for periodic telemetry; the flag transits or is retained.

## Forensic / Blue-Team Perspective (DFIR analyst)

Unauthenticated brokers are an inventory problem: map every topic namespace, classify
payloads for secrets (tokens, coordinates, credentials), and alert on anonymous
subscriptions. Broker ACL misconfiguration is the IoT equivalent of an open S3 bucket.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Retained broker messages and device shadows routinely carry secrets no one classified. |

## Tools

- mosquitto clients ([CTFTTOU-276](../tools/CTFTTOU-276.md))
- [nmap](../tools/CTFTTOU-033.md)
- [mitmproxy](../tools/CTFTTOU-083.md) (plain MQTT interception)

## References

- <https://mqtt.org/>
- Add challenge write-up link
