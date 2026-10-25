# CTFTTOU-331 — Arjun

> **Tool ID:** `CTFTTOU-331`  
> **Related techniques/counters:** CTFTCTE-WEB-001, CTFTCTE-WEB-017, CTFTCTE-WEB-020, CTFTTE-WEB-001, CTFTTE-WEB-017, CTFTTE-WEB-020

## Description

HTTP parameter discovery tool for GET and POST endpoints. Detects hidden parameters that may be vulnerable to injection attacks or information disclosure. Uses **time-based analysis** to identify parameters that are not visible in HTML, JavaScript, or API documentation but exist in backend logic.

## URL

<https://github.com/s0md3v/Arjun>

## Installation

**Already installed in this workspace:**
```bash
# Verify installation
arjun --version  # Output: v2.2.7

# Location
which arjun  # Output: /home/fhp/.local/bin/arjun
```

**Installation methods:**
```bash
# pipx (recommended)
pipx install arjun

# pip (user)
python3 -m pip install --user arjun

# From source
git clone https://github.com/s0md3v/Arjun.git
cd Arjun
python3 -m pip install -r requirements.txt
python3 arjun.py
```

## Usage

**Quick start:**
```bash
# Basic GET parameter discovery
arjun -u "https://target.com/api"

# POST parameter discovery
arjun -u "https://target.com/login" --post

# JSON API parameter discovery
arjun -u "https://target.com/api" --post --json '{}'

# With custom wordlist
arjun -u "https://target.com/api" -w params.txt
```

## Related Techniques

CTFTCTE-WEB-001, CTFTCTE-WEB-017, CTFTCTE-WEB-020, CTFTTE-WEB-001, CTFTTE-WEB-017, CTFTTE-WEB-020

## Skills

A dedicated skill for Arjun usage in CTFs is available:

**Skill:** `ctf-arjun`  
**Location:** `/mnt/c/DATA/CTF/ctf-skills-main/ctf-arjun/SKILL.md`  
**Purpose:** Comprehensive guide for HTTP parameter discovery in CTF challenges

### Skill Features:
- Complete option reference
- Practical CTF examples and walkthroughs
- 10+ real-world use cases
- Troubleshooting guide
- Custom wordlist creation
- Performance optimization tips
- Integration with other tools (ffuf, SQLmap, Burp Suite)
- Comparison with similar tools

### When to Load This Skill:
- Hidden parameters suspected in web endpoints
- API endpoints with undocumented functionality
- Debug/admin mode discovery
- Injection point identification
- Parameter casing variations needed
- Rate-limited or unstable targets requiring careful scanning

### Quick Access:
```
Load skill: /ctf-arjun
```

## References

- [ctf-arjun/SKILL.md](/mnt/c/DATA/CTF/ctf-skills-main/ctf-arjun/SKILL.md) - Dedicated Arjun skill
- [ctf-web-enumeration/SKILL.md](/mnt/c/DATA/CTF/ctf-skills-main/ctf-web-enumeration/SKILL.md) - Web enumeration skill (includes Arjun reference card)
- [GitHub Repository](https://github.com/s0md3v/Arjun) - Official repository
- [PyPI Package](https://pypi.org/project/arjun/) - Python package
