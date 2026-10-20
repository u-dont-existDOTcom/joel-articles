# Review Interface Browser Test

- **Result:** fail
- **Tested UTC:** 2026-10-20T12:56:02+00:00
- **Browser:** Chromium via Playwright
- **Review:** `Owner-to-Candidate-r03.html` — `7a4f5467b70fe142c43f9ce48cdd608a1d6818a240b8f17619d5487afa1c86af`
- **Article:** not supplied
- **Review load:** 0.694 seconds
- **Navigation:** file://
- **Network policy:** external HTTP(S) requests blocked; loopback allowed only when file:// was unavailable
- **Clipboard path:** deterministic injected writeText sink; browser permission path remains destination-specific

## Tests

| Test | Status | Detail |
|---|---|---|
| local-file navigation | pass | file:// |
| open exact review file | pass | file://; loaded in 0.694s |
| offline review | pass | external requests blocked: 0 |
| fixed interface controls | pass |  |
| review format | pass | joel-commentable-diff-review-v4 |
| view mode | pass | comparison |
| sliders on second line with clear technical label | pass | {"headline_bottom": 630.9375, "tuners_top": 637.9375, "technical_label": "Technical detail"} |
| whole-cell comment create/reopen/edit/delete and Enter/Shift+Enter/Escape | pass |  |
| selected-text comment survives toolbar focus | pass | at got to yo |
| Keep/Remove/Brainstorm and supersession | pass |  |
| four sliders | pass | {".humor-slider": 4, ".tech-slider": 0, ".length-slider": 3, ".blunt-slider": 1} |
| reasoning panel | pass |  |
| moved/consolidated destination jump | pass | r0377 |
| changed-only filtering | pass | equal rows: 50 |
| search | pass | that |
| Copy JSON | pass |  |
| Copy Markdown | pass |  |
| JSON/Markdown export and parse | fail | items: 2 |
| reload and local persistence | pass |  |
| no console errors | pass |  |
| no page errors | pass |  |
| review links: empty and internal fragments | pass | {"link_count": 1, "empty_targets": [], "unresolved_internal_fragments": [], "attachment_to_intended_text": "manual editorial audit required"} |

## Limitations

- Link attachment to the intended phrase requires editorial comparison with the authoritative source.
- When navigation_mode is page.set_content-fallback, controls and persistence use an exact-HTML injection plus deterministic Storage shim; this does not prove local-file navigation. This run never proves Opera-specific behavior or publication-platform reconstruction.
- A modest-laptop claim requires testing on that class of machine; this report records only the current environment.
