# Artifact Family Dependency Ledger Template

Use one ledger for an article and every related destination: archival HTML, transfer-ready payload, helper, original-vs-current review, correction-only review, changed-passages diff, comment-resolution ledger, continuation handover, self-hosted page, Ghost card, manual, app, worksheet, or sibling guide.

## Family metadata

- **Family ID:**
- **Project-state file:**
- **Current revision ID/status:** `rNN-candidate` / `rNN-approved`
- **Canonical source article/draft:**
- **Original raw editor HTML:**
- **Last user-approved article + SHA-256:**
- **Exact current diff baseline + SHA-256:**
- **Current revision/date:**
- **Current archival source SHA-256:**
- **Current editor-body SHA-256:**
- **Active source packet:**
- **Immutable source-comments file + SHA-256/count:**
- **Open comment count accepted by owner:**
- **Review interface format/row scope:**
- **Authoritative package + SHA-256:**
- **Confirmed publishing browser/path:**
- **Owner-approved omissions:**
- **Section-provenance ledger:**
- **Cumulative omission audit:**
- **Assistant-produced recheck queue:**

## Source-to-destination dependencies

| ID | Updated source passage/object | Meaning and rhetorical function | Required context/anchor | Attribution status | Destinations that may require update | Updated destinations | Intentionally omitted destination + reason | Status |
|---|---|---|---|---|---|---|---|---|
| AF-001 |  |  |  |  |  |  |  | open |

## Native-object placement inventory

| Order | Object type | Exact source hash | Canonical URL/node ID | Preceding anchor | Following anchor | Editorial function | Approved destination | Transfer conversion | Destination result |
|---|---|---|---|---|---|---|---|---|---|

## Destination inventory

| Destination | Mode | Canonical file/URL | Depends on | Transfer/adapter | Validation plane | Destination test | Last verified |
|---|---|---|---|---|---|---|---|
| Substack archive | archival editor-body HTML |  |  | exact raw islands | source fidelity |  |  |
| Transfer payload | one rich-HTML payload unless native uploaded video is present; otherwise ordered rich-HTML parts plus manual native-video insertion |  | exact final archival HTML | confirmed wrapper/object conversions; native-video exclusion/split; video-post canonical URL without split | transfer conversion |  |  |
| Substack helper | local Opera helper |  | transfer payload part(s) + recorded native-video manual steps | immediate ClipboardItem + silent fallback; ordered Copy Part controls only for native uploaded-video boundaries | compatibility regression | real Substack paste plus manual native-video reinsertion |  |
| Original review | original-vs-current side-by-side |  | original + current article | review interface | semantic comparison | local browser QA |  |
| Correction review | previous-delivery-vs-corrected side-by-side |  | previous delivery + corrected article | review interface | repair comparison | local browser QA |  |
| Full-draft review | complete current article, one-column commentable | current article | interactive review full-draft mode | full-article review | local browser QA |  |
| Review diff | changed-passages diff |  | original/previous + current HTML | html_diff.py | source comparison | local file only |  |
| Raw source comments | immutable JSON |  | user export | none | provenance | JSON parse/hash |  |
| Comment ledger | issue-resolution Markdown/JSON |  | raw comments + review rows + chronology | reconciliation | resolution | zero-open audit or accepted exceptions |  |
| Project state | canonical Markdown |  | last approved artifact + current family | PROJECT-STATE-TEMPLATE.md | portability/authority | file/hash audit |  |
| Changelog/README | project records |  | project state + delivery | package templates | portability | file audit |  |
| Browser-test report | exact-file interaction report |  | packaged review/article | review_interface_browser_test.py | interface behavior | local/offline browser QA |  |
| Package manifest/checksums | manifest + SHA256SUMS |  | staged family | review_package.py | integrity | clean-unzip verification |  |
| Continuation handover | compact project state |  | entire family | handover fields in PROJECT_STATE.md | portability | file/hash audit |  |
| Section provenance | owner/assistant origin and approval states |  | current article | provenance ledger | authority/recheck | zero unqueued assistant sections |  |
| Omission audit | cumulative moved/omitted/restored/owner-deleted items |  | source packet + revision history | omission ledger | preservation | unresolved assistant omissions resolved or accepted |  |
| Assistant recheck queue | assistant-produced/owner-accepted sections |  | provenance ledger | full-context recheck | publication readiness | queue resolved before publication |  |
| Family ZIP | current authoritative delivery |  | all declared current artifacts | review_package.py | completeness | unzip/integrity test |  |
| Self-hosted page | standalone HTML |  | approved article content/assets | self-host adapter | source + destination | hosted-page test |  |
| Ghost card | embedded fragment |  | self-hosted/article artifact | Ghost adapter | source + destination | real Ghost upload |  |

### Substack video object distinction

- **Native Substack-uploaded video:** preserve the exact source island and identity in archival HTML; exclude it from every clipboard payload; split the helper at its exact position; record ordered manual reinsertion with preceding/following anchors.
- **Substack video-post embed:** preserve the exact source island in the archive; use its canonical post URL alone at the same source position in the current payload part; do not split solely for it.
- **YouTube:** keep as an independent object type under its own tested transfer status.

## Canonical URL equivalence

Compare URLs by canonical value rather than descriptive label. Record redirects, pointer domains, tracking variants, and the one canonical destination used by the family.

| Descriptive label | Supplied URL | Canonical URL | Equivalent? | Notes |
|---|---|---|---|---|

## Completion rule

A revision is not complete until every affected destination is updated, explicitly deferred, or intentionally omitted with a reason. For substantial annotated review, the last approved baseline and candidate are named and hashed; every raw comment has a ledger status; unresolved count is zero or explicitly accepted; and the current family is packaged in one authoritative ZIP with project state, immutable source comments, changelog, README, manifest, and checksums. Include a continuation handover only when an actual worker transfer is requested or planned. Every full handoff also includes section provenance, the cumulative omission audit, and the assistant-produced recheck queue. Unavailable authoritative artifacts are listed rather than reconstructed. Rebuild the transfer-ready payload and helper from the exact approved archival HTML after every change that alters prose, headings, links, source order, or native-object placement. Source fidelity, transfer conversion, interface behavior, package integrity, and destination success remain separate findings. This multi-file delivery rule does not force a fresh conversation or repeated ZIP after every intermediate pass.
