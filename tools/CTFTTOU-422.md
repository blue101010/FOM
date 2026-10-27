# CTFTTOU-422 — Google Hacking Database (GHDB)

> **Tool ID:** `CTFTTOU-422`
> **Related techniques/counters:** CTFTTE-OSI-007, CTFTCTE-OSI-007

## Description

Exploit-DB's curated catalogue of **verified search dorks**, grouped by intent (footholds, sensitive
directories, files containing juicy info, vulnerable servers, error messages, camera/webcam
endpoints). It is the precise counterpart of "advanced dorks": instead of inventing operator
combinations, you take a category, read the operators it uses, and adapt the domain or keyword.

## URL

- <https://www.exploit-db.com/google-hacking-database>

## Usage

```text
# browse a category, then adapt a dork to the target
site:target.example filetype:pdf "flag"
site:target.example inurl:admin intitle:index
site:target.example ext:log "BEGIN RSA PRIVATE KEY"
"index of" "backup" site:target.example

# engines are not interchangeable: re-test operators on the engine you use
site: / filetype: / inurl: / intitle: / intext:  apply to Google and Bing with differences
DuckDuckGo supports site:, filetype: and quotes, but not inurl:/intitle:
```

## Notes

- Treat every GHDB entry as a **template**, not a payload: the operator set is the durable part, the
  literal (a vulnerable path, a product version) usually is not.
- Pair the manual reading with `googlesearch-python` (separate sheet) to iterate over a small list of
  dork templates programmatically; keep the volume low — search engines throttle aggressively and a
  CTF needs a handful of pages.
- For an indexed-but-unfindable flag, vary the *indexed artefact* rather than the dork: a paste, a
  repository file, a PDF, a log — each is a different `filetype:`/`site:` candidate.
- Record the exact dork that worked; a write-up that only says "found it via Google" is not
  reproducible.

## Related Techniques

CTFTTE-OSI-007, CTFTCTE-OSI-007
