# CTFTTOU-288 — ROPgadget

> **Tool ID:** `CTFTTOU-288`  
> **Related techniques/counters:** CTFTTE-PWN-004, CTFTCTE-PWN-004, CTFTTE-PWN-011, CTFTCTE-PWN-011

## Description

Scans ELF/PE/Mach-o binaries for ROP gadgets (`pop rdi; ret`, stack pivots, syscall
sequences) and full ROP/JOP chain search. Companion of pwntools for building
register-setup chains — the standard first move when a win function gates on
argument registers. Also distributed as a Python package (install into the shared
pwn venv, never system pip on Kali/PEP 668):

```sh
~/.venvs/ctfpwn/bin/pip install 'ROPgadget==7.7'
~/.venvs/ctfpwn/bin/ROPgadget --binary ./target --only "pop|ret"
```

## URL

<https://github.com/JonathanSalwan/ROPgadget>

## Related Techniques

CTFTTE-PWN-004, CTFTCTE-PWN-004, CTFTTE-PWN-011, CTFTCTE-PWN-011
