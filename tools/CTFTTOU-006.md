# CTFTTOU-006 — ExifTool

> **Tool ID:** `CTFTTOU-006`  
> **Related techniques/counters:** CTFTCTE-OSI-001, CTFTCTE-OSI-004, CTFTCTE-STE-004, CTFTCTE-STE-009, CTFTTE-OSI-001, CTFTTE-OSI-004

## Description

ExifTool reads metadata from supplied files and supports nested-container
inspection. CTFT records the tool as a reference; artifact access and any
execution remain outside the catalogue and require an authorized laboratory.

For imagery geolocation, `exiftool -a -u -g1 image.jpg` lists every group: GPS position
and altitude, capture timestamp (input to sun-position analysis when GPS is stripped)
and camera/phone model.

## URL

<https://exiftool.org/>