# CTFTTOU-094 — waybackurls

> **Tool ID:** `CTFTTOU-094`  
> **Related techniques/counters:** CTFTCTE-OSI-003, CTFTTE-OSI-003

## Description

Pulls every URL the Wayback Machine knows for a host out of the CDX index and prints one per line. It
is the bulk form of a single-URL CDX query: pipe one or more hostnames in, get the archived URL
surface out — the raw material for removed pages, forgotten paths, old parameters and files that still
exist in the archive.

## URL

<https://github.com/tomnomnom/waybackurls>

## Install (Kali WSL)

```bash
go install github.com/tomnomnom/waybackurls@latest     # binary lands in $(go env GOPATH)/bin
# PATH must contain ~/go/bin — otherwise call ~/go/bin/waybackurls
```

## Usage

The real interface is **stdin, one host per line**, and every flag is single-dash:

```bash
printf 'example.com\n' | waybackurls              # every archived URL for the host
printf 'example.com\n' | waybackurls -dates       # prefix each line with its fetch date
printf 'example.com\n' | waybackurls -no-subs     # exclude subdomains
cat hosts.txt | waybackurls | sort -u > urls.txt
waybackurls -get-versions <host>                  # crawled versions of the input URL
```

Output is a plain URL list — filter it downstream:

```bash
# artefacts worth opening first
grep -Ei '\.(bak|old|orig|zip|tar|gz|sql|env|log|json|txt)$' urls.txt
# distinct query keys across the archive, which reveal parameters that once existed
awk -F'?' 'NF>1 {print $2}' urls.txt | tr '&' '\n' | cut -d= -f1 | sort -u
```

## Notes

- **No long options.** `waybackurls --version` fails with `flag provided but not defined: -version`;
  the flag list is `-dates`, `-get-versions`, `-no-subs`.
- **It reads stdin, so a bare `waybackurls` looks hung.** Always pipe a host (or use the
  `-get-versions` form above); `Ctrl-C` is the expected way out of an accidental empty invocation.
- An empty result means *not archived*, not *never existed*: cross-check `archive.today` and the live
  host. The CDX API remains the precise instrument when you need `statuscode`/`mimetype` columns for a
  single pattern.
- Unauthenticated public Archive.org endpoint: no key, but it throttles. One challenge host is one
  host — do not feed a wordlist of thousands.
- `-dates` is what turns the URL list into a timeline; correlate first appearance with the challenge
  story before assuming a path is relevant.

## Related Techniques

CTFTCTE-OSI-003, CTFTTE-OSI-003
