# Review Interface Browser Test

- **Result:** fail
- **Tested UTC:** 2026-09-11T17:06:33+00:00
- **Browser:** Chromium via Playwright
- **Review:** `CHANGES-REVIEW.html` — `f16da31d028a2276b3572816019db38f8094195ee740dc9badcd1437acb95e28`
- **Article:** `master.html` — `842bead8f862873e6b5391cfa06bacb4ddfa3910568876112f45bef8fd3b24ab`
- **Review load:** 1.002 seconds
- **Navigation:** page.set_content-fallback
- **Network policy:** external HTTP(S) requests blocked; loopback allowed only when file:// was unavailable
- **Clipboard path:** deterministic injected writeText sink; browser permission path remains destination-specific

## Tests

| Test | Status | Detail |
|---|---|---|
| local-file navigation | not-applicable | file:// and loopback navigation blocked; exact HTML tested with page.set_content. file error: Page.goto: net::ERR_BLOCKED_BY_ADMINISTRATOR at file:///mnt/data/sync-work/joel-articles/articles/inner-signal/sync-r03/CHANGES-REVIEW.html Call log:   - navigating to "file:///mnt/data/sync-work/joel-articles/articles/inner-signal/sync-r03/CHANGES-REVIEW.html", waiting until "load" ; loopback error: Page.goto: net::ERR_BLOCKED_BY_ADMINISTRATOR at http://127.0.0.1:33727/sync-r03/CHANGES-REVIEW.html Call log:   - navigating to "http://127.0.0.1:33727/sync-r03/CHANGES-REVIEW.html", waiting until "load"  |
| open exact review file | pass | page.set_content-fallback; loaded in 1.002s |
| offline review | pass | external requests blocked: 0 |
| fixed interface controls | pass |  |
| review format | pass | joel-commentable-diff-review-v4 |
| view mode | pass | comparison |
| sliders on second line with clear technical label | pass | {"headline_bottom": 285.859375, "tuners_top": 292.859375, "technical_label": "Technical detail"} |
| whole-cell comment create/reopen/edit/delete and Enter/Shift+Enter/Escape | pass |  |
| selected-text comment survives toolbar focus | pass | gin with Qui |
| Keep/Remove/Brainstorm and supersession | pass |  |
| four sliders | pass | {".humor-slider": 4, ".tech-slider": 0, ".length-slider": 3, ".blunt-slider": 1} |
| reasoning panel | pass |  |
| moved/consolidated destination jump | not-applicable | no moved/consolidated row in this review |
| changed-only filtering | pass | equal rows: 0 |
| search | pass | Begin |
| Copy JSON | pass |  |
| Copy Markdown | pass |  |
| JSON/Markdown export and parse | pass | items: 2 |
| reload and local persistence | pass |  |
| open packaged article as local file | fail | console errors: 6 |
| no console errors | pass |  |
| no page errors | pass |  |
| review links: empty and internal fragments | pass | {"link_count": 1, "empty_targets": [], "unresolved_internal_fragments": [], "attachment_to_intended_text": "manual editorial audit required"} |
| article links: empty and internal fragments | pass | {"link_count": 48, "empty_targets": [], "unresolved_internal_fragments": [], "attachment_to_intended_text": "manual editorial audit required"} |

## Limitations

- Link attachment to the intended phrase requires editorial comparison with the authoritative source.
- When navigation_mode is page.set_content-fallback, controls and persistence use an exact-HTML injection plus deterministic Storage shim; this does not prove local-file navigation. This run never proves Opera-specific behavior or publication-platform reconstruction.
- A modest-laptop claim requires testing on that class of machine; this report records only the current environment.
