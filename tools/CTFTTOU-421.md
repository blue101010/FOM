# CTFTTOU-421 — GitHub Code Search

> **Tool ID:** `CTFTTOU-421`
> **Related techniques/counters:** CTFTTE-OSI-005, CTFTCTE-OSI-005

## Description

GitHub's own code and commit search (`type=code`, `type=commits`, `type=repositories`), plus the same
queries through the REST API. It is the precise instrument behind "dorking" a repository host: it
searches file **contents** across public repositories, filters by repository, path and language, and —
with `type=commits` — reaches text that no longer exists in the default branch.

## URL

- <https://github.com/search?type=code>
- <https://docs.github.com/en/search-github/searching-on-github/searching-code>

## Usage

```text
# code search with qualifiers (web UI or the same q= string)
"flag{" repo:owner/name
"api_key" path:.env language:shell
"BEGIN RSA PRIVATE KEY" org:target-org

# commits: finds deleted secrets still present in history
https://github.com/search?q=repo%3Aowner%2Fname+%22api_key%22&type=commits

# API form (needs a token; code search requires authentication)
gh api -X GET search/code -f q='"flag{" repo:owner/name' --jq '.items[].html_url'

# clone-and-grep when the repo is small enough for full history
git clone --mirror https://github.com/owner/name.git && git -C name.git log -S 'flag{' --all
```

## Notes

- Code search needs an authenticated account; unauthenticated queries silently return a reduced view.
- Quote the literal, and prefer `repo:`/`org:` over a global search: a global `flag{` returns millions
  of hits from unrelated write-ups.
- `git log -S` (pickaxe) and `git log -p --all` on a mirror find secrets in history that code search
  indexes poorly; `trufflehog` and `gitleaks` (separate sheets) automate the same sweep with entropy
  and rule matching.
- A fork network triples the search noise but also keeps deleted commits alive — check forks when the
  upstream history was force-pushed.

## Related Techniques

CTFTTE-OSI-005, CTFTCTE-OSI-005
