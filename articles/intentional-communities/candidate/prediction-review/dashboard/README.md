# Prediction Scorecard

The page: https://claude.ai/artifact/Sjpy4EiZGUa21iiMstDLPv, a Dashboard-type artifact. Only the Claude account that published it can republish it.

Its content lives in the artifact's own store (the ArtifactData tool), not in published files: `dash/meta` (`{title}`),
`datasets/calls` (`{title, description, source: {kind: "file", url, name, format}, updated: {at, by}}`) and `files/index.html`
(`{text}`, the page; `index.html` here is a copy). Publishing files to the artifact changes nothing on the page. Until
2026-10-17 the lane did that, so the page never showed anything (Joel, 23:10 UTC: "your scorecard is always empty"): the
uploaded file was a summary, not the one row per check that the page counts, and the store's `datasets/calls` kept pointing at an
upload that had since been deleted (its `data/users/me/runs` document said "Couldn't load the file (404).").

- To rebuild after a turn with Pangram checks: `python3 prediction-review/scorecard.py prediction-review/prediction-calls.json`
  (from the candidate folder). It also writes `prediction-calls-rows.json`, one row per check (batch, the check's id as `text`,
  section, my call, Pangram's result, why, an excerpt, `right` and `passed` as 1 or 0; since 2026-10-18 also `said_human`, the check's
  `kind` from its batch's GATE.json, and `chance` when the PREDICTIONS table has a chance column), the shape the page counts.
- Upload that file to the artifact as an asset (the Artifact tool's publish with `asset: true`), then an ArtifactData `update` of
  `datasets/calls`, pinned to its version: `source.url` the new asset's url as it came, `source.name`, and `updated` (`at`: the
  last check's Pangram time, `by`: who, through which batch). `ds-calls.json` here mirrors that document.
- Only then delete the old asset. The page reads whatever `datasets/calls` points at, so deleting an asset it still points at
  empties the page.
- After Joel opens it, `data/users/me/runs` (ArtifactData `get`) says whether the dataset loaded.
- Joel, 2026-10-12 17:23 UTC: "regarding the prediction misses file i also don't know where that is, keep that updated i want to see you improving on that or if you need help lmk i can tell you why stuff sounds human or AI."

- The page (`files/index.html` in the store; `index.html` here): since 2026-10-18 it also shows the always-Human bar, how often I said
  Human, and a panel of my rewrites' first-check pass rate and sections' pass rate per ten batches. To change it, edit `index.html`
  here, test its calculations with the rows in Node (`node test_calcs.js` here mocks `dash` and runs every `dash.calc` on the rows), then an
  ArtifactData `update` of `files/index.html` (`{text}`), pinned to its version.

- 2026-10-18 (hypnosis guide lane, after 440g): the rows now hold both lanes (`lane`), the page has a panel of my chances
  (the Brier score by lane, a calibration table by bins of my chance) and of the hypnosis guide's Emulate screens per batch
  (`files/index.html` version 3, `datasets/calls` version 12, asset `/_blob/350ec5e0c68e2f108918e2eb5cee830a`). The
  asset it replaced, `/_blob/44b7cc69fd5868d86493664675de4327`, is no longer referenced and can be deleted (deleting
  asks the person to confirm, so it was left for a session with Joel there).

- 2026-10-18 (after 445g): `datasets/calls` version 13 points at asset `/_blob/bbc181a3ac210712a8ed29ec0a891941`; the one before it,
  `/_blob/350ec5e0c68e2f108918e2eb5cee830a`, and the older `/_blob/44b7cc69fd5868d86493664675de4327` are no longer referenced (deleting
  asks the person to confirm, so they were left).
