# CTFTTOU-419 — Google Maps

> **Tool ID:** `CTFTTOU-419`
> **Related techniques/counters:** CTFTTE-OSI-001, CTFTCTE-OSI-001

## Description

Google's map product, used here for the two things OSM-derived tooling does not give: **Street View**
coverage of the exact spot, and **historical Street View** (the clock icon in the imagery date menu),
which is what a time-scoped geolocation challenge usually hinges on. It also carries satellite
imagery, 3D buildings, "What's here" reverse lookup and the distance-measuring tool for scale checks
(road width, shadow-to-object ratios, building footprint).

## URL

- <https://www.google.com/maps>

## Usage

```text
# put the coordinates straight in the search box, zoom with @lat,lng,<zoom>z
48.8584, 2.2945                     -> drops a pin at that exact point
https://www.google.com/maps/@48.8584,2.2945,17z

# Street View: open the pegman / click the blue line, then compare
#   - imagery date is shown bottom-right; older captures are behind the clock icon
#   - the compass and the camera height matter when matching a photo's horizon

# measure: right-click -> "Measure distance" (scale check for lanes, buildings, containers)
```

## Notes

- The imagery date menu is the discriminator for "this photo was taken in year N" challenges: the
  visible state of the scene must match that year, and a building added later rules a candidate out.
- Street View is `© Google` manual-use only; scripted scraping breaks the terms and is not needed —
  a geolocation solve is a handful of interactive looks.
- Coverage is uneven: if Street View is missing, cross-check with the sibling sheets
  (Yandex Images, Wikimapia, Mapillary-style user imagery) before discarding the hypothesis.
- Satellite and Street View can disagree on dates; state which layer you used when the answer depends
  on it.

## Related Techniques

CTFTTE-OSI-001, CTFTCTE-OSI-001
