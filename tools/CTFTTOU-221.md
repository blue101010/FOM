# CTFTTOU-221 — cloudfox

> **Tool ID:** `CTFTTOU-221`  
> **Related techniques/counters:** CTFTCTE-FPN-005, CTFTTE-FPN-005

## Description

Finds exploitable attack paths in cloud infrastructure (AWS/Azure/GCP). **Go binary —
NOT on PyPI**: `pipx install cloudfox` fails with "not found in the package registry"
on this box (pipx 1.15/uv). Install the prebuilt release instead (verified 2026-11,
Kali WSL → `cloudfox version 2.0.5`):

```sh
curl -sL -o /tmp/cloudfox.zip https://github.com/BishopFox/cloudfox/releases/latest/download/cloudfox-linux-amd64.zip
unzip -o -q /tmp/cloudfox.zip -d /tmp/cloudfox-bin
cp /tmp/cloudfox-bin/cloudfox/cloudfox ~/.local/bin/cloudfox && chmod +x ~/.local/bin/cloudfox
cloudfox aws --profile <profile>            # module list: cloudfox aws --help
# e.g. cloudfox aws enum-perms / secrets / buckets — fast (Go) vs pure-Python scoutsuite (CTFTTOU-226)
```

Prefer cloudfox over scoutsuite under CTF time pressure; scoutsuite stays the optional
slow broad posture dump (`~/.venvs/ctfcloud/bin/pip install scoutsuite`).

## URL

<https://github.com/BishopFox/cloudfox>

## Related Techniques

CTFTCTE-FPN-005, CTFTTE-FPN-005

## Skills

- [CTFTSKL-019 ctf-cloud-aws](../skills/CTFTSKL-019.md) — attack-path enumeration across services
