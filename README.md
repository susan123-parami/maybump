# The Four Mes

> Reading my own GPS like a diary.

A personal data-storytelling dashboard built from my own iPhone Bump location export. Made for DATA 201, May 2026.

**Live dashboard**: deployed on Streamlit Cloud (link in this repo's settings).

## What it is

A self-contained 3D interactive map of every place my phone logged a GPS presence over the months I've used Bump, framed through four personas (Home Me, Adventure Me, Traveler Me, Student Me). Plus a light Story page with stats, charts, an honest ethics section, and a "Predicting Me" behavioural decision tree.

## Stack

- **deck.gl 9** for 3D hex extrusion on top of...
- **MapLibre GL JS 5** for the basemap and globe projection (basemap by CARTO + OpenStreetMap)
- **h3-js 4** for Uber's H3 hexagonal indexing
- **D3.js 7** for the analytical charts on the Story screen
- **Streamlit** wrapper for hosting only

All visual libraries load from CDN. The dashboard (`bump_3d.html`) is one self-contained file.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Streamlit wrapper, just embeds the HTML |
| `requirements.txt` | Python deps (just streamlit) |
| `bump_3d.html` | The dashboard, single self-contained file |
| `scratch_map_3221_hexes.csv` | Raw H3 hex log data (3,221 rows) |
| `places_87.csv` | 87 places I tagged in Bump |
| `report.pdf` | Project report (4 pages) |
| `README.md` | This file |

## Running locally

```
pip install -r requirements.txt
streamlit run app.py
```

Or just open `bump_3d.html` directly in a browser. Both work.

## Note

This dashboard knowingly publishes my real home and workplace. I am the data subject and the publisher; consent is mine to give. Do not replicate this pattern with someone else's data without explicit consent.
