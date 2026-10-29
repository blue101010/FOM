# CTFTTOU-446 — what3words

> **Tool ID:** `CTFTTOU-446`  
> **Related techniques/counters:** CTFTTE-OSI-010, CTFTCTE-OSI-010

## Description

Word-address geocoding service: the globe is divided into 3 m squares and each square is
addressed by three dictionary words (`word.word.word`). The words resolve to coordinates
through the web UI or the developer API, and the API also reverse-geocodes coordinates
back to words.

In an OSINT workflow it is the step that turns a recovered three-word string — which
looks like a passphrase or a cracked secret — into a physical location, which then feeds
a reverse-geocoder (Nominatim) and a public-records pivot. The wordlist is versioned and
language-specific: the same square has different words per language, and the list is
revised over time, so a resolution should record its date.

## URL

- <https://what3words.com/>
- <https://developer.what3words.com/>

## Usage

```bash
# resolve words to coordinates (API key from the developer portal)
curl -s "https://api.what3words.com/v3/convert-to-coordinates?words=word.one.two&key=API_KEY"

# reverse: coordinates to words
curl -s "https://api.what3words.com/v3/convert-to-3wa?coordinates=51.1,0.1&key=API_KEY"
```

## Notes

- No key needed for one-off lookups in the web UI; the API requires a free developer key.
- A rejected word triple is usually a language mismatch — try the other supported
  languages before concluding the words are not an address.
- The resolved square is a few metres: it identifies a location precisely, which is what
  makes the subsequent address/attribution pivot strong.

## Related Techniques

CTFTTE-OSI-010, CTFTCTE-OSI-010
