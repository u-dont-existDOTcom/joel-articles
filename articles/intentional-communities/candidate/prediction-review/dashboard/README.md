# Prediction Scorecard

The page: https://claude.ai/artifact/Sjpy4EiZGUa21iiMstDLPv, a Dashboard-type artifact. Only the Claude account that published it can republish it.

- `index.html` is the page; `ds-calls.json` is its dataset `calls`, whose source is an uploaded JSON asset (`prediction-calls.json`); `meta.json` is the title.
- To rebuild after a turn with Pangram checks: `python3 prediction-review/scorecard.py OUT.json` (from the candidate folder), upload OUT.json to the artifact as an asset, point `ds-calls.json`'s `source.url` at the new asset's url, set `updated.at`, and republish the dataset.
- Joel, 2026-10-12 17:23 UTC: "regarding the prediction misses file i also don't know where that is, keep that updated i want to see you improving on that or if you need help lmk i can tell you why stuff sounds human or AI."
