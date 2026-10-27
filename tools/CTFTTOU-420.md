# CTFTTOU-420 — archive.today

> **Tool ID:** `CTFTTOU-420`
> **Related techniques/counters:** CTFTTE-OSI-003, CTFTCTE-OSI-003

## Description

On-demand web archive with a searchable index of snapshots, complementary to the Wayback Machine:
archive.today keeps **page-state captures** (including comments and JS-rendered content) and exposes
them under several mirrors (`archive.ph`, `archive.today`, `archive.is`, `archive.li`). In a
"the flag was edited out" challenge it is the second place to look, because a page can be archived
here even when the CDX index has no capture.

## URL

- <https://archive.ph/>

## Usage

```text
# capture/search by URL: paste the target URL in the search box
https://archive.ph/https://target.example/page

# newest snapshot of a URL
https://archive.ph/newest/https://target.example/page

# from the target page itself, deployments often expose "archive" links;
# the mirrors are interchangeable when one is rate-limited
```

## Notes

- Compare **timestamps against the edit window**: a snapshot older than the edit is the one that still
  carries the removed text.
- Archives store the rendered DOM, so a value that was client-side (a flag in an inline script) can
  survive here even though the origin never served it again.
- The Wayback Machine has the broader crawl but a thinner index for low-traffic CTF domains; the CDX
  API (`web.archive.org/cdx/search/cdx?url=…&output=json`) is the precise way to list what exists
  before fetching anything.
- Both services honour removal requests, so an empty result is not proof that the content never
  existed — record the attempt and move to repository history instead.

## Related Techniques

CTFTTE-OSI-003, CTFTCTE-OSI-003
