# CTFTTOU-418 — Nominatim

> **Tool ID:** `CTFTTOU-418`
> **Related techniques/counters:** CTFTTE-OSI-001, CTFTCTE-OSI-001

## Description

OpenStreetMap's geocoding service: **reverse geocoding** (coordinates → street address, place names,
administrative units) and forward search (name → coordinates). Free, no API key, JSON output, and it
returns the structured fields a geo-guessing challenge needs — house number, road, suburb, city,
`display_name`, bounding box, plus OSM identifiers.

In an OSINT geolocation workflow it is the step that turns "I think this photo was taken here" into
"this is 4 Rue X, in the Y quarter of Z", which is what usually has to be typed into the answer box.

## URL

- <https://nominatim.org/>
- <https://nominatim.openstreetmap.org/ui/search.html> (web UI)

## Usage

```bash
# reverse geocoding: coordinates -> address (format=jsonv2 keeps the fields flat)
curl -s -A 'ctf-osint/1.0' \
  'https://nominatim.openstreetmap.org/reverse?lat=48.8584&lon=2.2945&format=jsonv2' | jq .

# extra detail: OSM tags and alternate names, where landmark clues hide
curl -s -A 'ctf-osint/1.0' \
  'https://nominatim.openstreetmap.org/reverse?lat=48.8584&lon=2.2945&format=jsonv2&extratags=1&namedetails=1' | jq .

# forward search when the photo gives a name, not a position
curl -s -A 'ctf-osint/1.0' \
  'https://nominatim.openstreetmap.org/search?q=water tower+krakow&format=jsonv2&limit=5' | jq .
```

## Notes

- **Set a User-Agent and stay under one request per second.** The public instance blocks anonymous
  bulk traffic; a challenge never needs more than a handful of calls.
- `format=jsonv2` is the flat, readable one; `polygon_geojson=1` returns the boundary geometry when a
  challenge asks for a shape rather than a point.
- Prefer coordinates in **decimal degrees**; the service also accepts `lat=..&lon=..` inside a bounding
  query, useful to check which of two candidate spots resolves to a plausible address.
- The address granularity is uneven by country: a rural coordinate may return only a municipality,
  which is often the intended answer level.

## Related Techniques

CTFTTE-OSI-001, CTFTCTE-OSI-001
