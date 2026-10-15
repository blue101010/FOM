# CTFTTOU-276 — mosquitto clients

> **Tool ID:** `CTFTTOU-276`  
> **Related techniques/counters:** CTFTTE-IOT-003, CTFTCTE-IOT-003

## Description

Eclipse Mosquitto is the open-source reference implementation of an MQTT broker; the
`mosquitto-clients` package ships its command-line clients `mosquitto_sub` and
`mosquitto_pub`. On Kali: `sudo apt install mosquitto-clients` (the broker itself is the
separate `mosquitto` package). Typical triage: `mosquitto_sub -h <host> -t '#' -v`
subscribes to every topic (wildcard `#`), so retained messages and the whole topic
namespace appear at once; `-u`/`-P` pass credentials when the broker ACL requires them.

## URL

<https://mosquitto.org/>

## Related Techniques

CTFTTE-IOT-003, CTFTCTE-IOT-003
