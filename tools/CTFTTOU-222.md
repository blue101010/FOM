# CTFTTOU-222 — enumerate-iam

> **Tool ID:** `CTFTTOU-222`  
> **Related techniques/counters:** CTFTCTE-CLD-002, CTFTCTE-CLD-006, CTFTTE-CLD-002, CTFTTE-CLD-006

## Description

Enumerates permissions of a set of AWS credentials (brute-forces the IAM permission
surface). **Plain Python script — no setup.py, NOT pipx-installable** (`pipx install
enumerate-iam` fails on this box). Install by clone + venv deps + shim (verified
2026-11, Kali WSL; PEP 668 — never system pip):

```sh
git clone --depth 1 https://github.com/andresriancho/enumerate-iam.git ~/TOOLS/enumerate-iam
~/.venvs/ctfcloud/bin/pip install -r ~/TOOLS/enumerate-iam/requirements.txt
printf '#!/bin/sh\nexec %s/bin/python %s/enumerate-iam.py "$@"\n' "$HOME/.venvs/ctfcloud" "$HOME/TOOLS/enumerate-iam" > ~/.local/bin/enumerate-iam
chmod +x ~/.local/bin/enumerate-iam
enumerate-iam --access-key AKIA... --secret-key ... [--session-token ...] --region eu-west-1
```

## URL

<https://github.com/andresriancho/enumerate-iam>

## Related Techniques

CTFTCTE-CLD-002, CTFTCTE-CLD-006, CTFTTE-CLD-002, CTFTTE-CLD-006

## Skills

- [CTFTSKL-019 ctf-cloud-aws](../skills/CTFTSKL-019.md) — permission-surface discovery from a key
