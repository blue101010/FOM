# CTFTCTE-IOT-003 — Enumerate broker topics/queues and capture service traffic

> **Type:** Counter-Technique  
> **Tactic:** [`CTFT-TA-IOT`](../tactics/CTFT-TA-IOT.md) — IoT / Embedded  
> **Counters technique:** [`CTFTTE-IOT-003`](../techniques/CTFTTE-IOT-003.md) — Unauthenticated message-broker topic/queue concealment

---

## Offensive Recovery (CTF practitioner / solver)

1. Identify the service and its protocol from the port and banner (nmap service scan;
   brokers also answer protocol-native PING/INFO probes).
2. Enumerate the namespace the way the protocol allows: wildcard or catch-all
   subscriptions where supported (MQTT `#`), resource discovery endpoints (CoAP
   `.well-known/core`), queue/channel listing in management interfaces, or brute-force
   of channel names from challenge vocabulary.
3. Mine the surrounding artifacts for credentials when auth is required: the firmware
   image (IOT-001), the device story, vendor defaults — read ACLs are often anonymous
   even where write is gated.
4. Capture long enough for periodic traffic; retained or scheduled messages usually
   reveal the channel map without any guesswork.
5. Validate: the data found on the channel satisfies the challenge's flag format.

## Forensic / Blue-Team Perspective (DFIR analyst)

Anonymous broker namespaces are an inventory problem: map every topic/queue namespace,
classify payloads for secrets (tokens, credentials, personal data), and alert on anonymous
subscriptions and listings. An open broker is the IoT equivalent of an open storage bucket.

## Related MITRE ATT&CK

| ATT&CK ID | ATT&CK technique | Relation note |
| --- | --- | --- |
| T1552 | Unsecured Credentials | Retained messages, shadows and admin queues routinely carry secrets nobody classified. |

## Tools

- [mosquitto clients](../tools/CTFTTOU-276.md) (MQTT family)
- [nmap](../tools/CTFTTOU-033.md)
- [mitmproxy](../tools/CTFTTOU-083.md) (plain-protocol interception)

## References

- <https://cwe.mitre.org/data/definitions/1188.html>
- Add challenge write-up link
