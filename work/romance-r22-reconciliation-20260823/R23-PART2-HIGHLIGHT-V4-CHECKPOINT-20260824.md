# Romance r23 Part 2 highlight-recovery checkpoint

Updated: 2026-08-24

## Exact detector state

- r23 Part 2 SHA-256: `a0dce58d2958e8467c1ba66cbed20b7c7ae075b8eddc7e1365eb8728485ff7f3`
- 9,917 words
- Pangram 4.0 Human `0.9965084195`
- AI `0.0034915956`
- AI-assisted `0.0`
- stored report summary: `A single AI-generated segment`
- no repeat detector submission is authorized merely to localize this result.

## What read-only recovery established

1. Structured History localization and direct-report structured binding both failed closed at `bind_exact_history_record`; neither submitted text to the detector.
2. DOM inspector v1 falsely treated Pangram orange navigation styling as a highlight.
3. DOM inspector v2 inspected only the first report page and found no anomalous article-text style there.
4. Report-page inspector v3 paginated all seven stored report pages. Every page-level Details classification is Human. The residual is therefore smaller than a report page and cannot be localized from page-level labels.
5. The three r23 Part-2 authorized edits land on different stored report pages:
   - R23-03 `Can making love be a spiritual practice?`: page 1;
   - R23-04 owner-final mutual-friend sentence: end of page 3;
   - R23-05 `I can hear a whole future...`: page 4.
   All three pages are Human at page level.

## Root-cause correction to the recovery tooling

The v2 DOM evidence shows the report contains an actual button labeled `AI Highlight` (`button#radix-_r_15_`). Pangram's July 2026 knowledge-hub documentation states that AI segments are displayed inline in the report body (AI red, AI-assisted yellow, Human green). The v1-v3 recovery scripts never activated that stored-report highlight view before trying to identify the marked prose.

Therefore the earlier localization failures are tooling limitations, not evidence against any Romance sentence.

Private executor main now contains a read-only v4 inspector which:
- validates the exact already-paid stored result;
- activates the existing report's `AI Highlight` control;
- records only bounded marked/style-run snippets and compact style/ancestor metadata inside `.mp-block`;
- paginates the stored report;
- persists `detector_submission_attempted: false`;
- has no Pangram detector-submit or API-key path.

A v4 read-only request was added for evidence branch:
`evidence/pangram-report-dom/romance-r23-part2-v4-highlight-20260824-a`.

## Editorial preflight while localization is pending

No Part-2 prose is changed at this checkpoint.

Cold review of the three r23 Part-2 edits found no credible reason to alter R23-04 or R23-05 independent of detector evidence. R23-04 is owner-final and performs a necessary community function; R23-05 is a compressed concrete future-image and performs the section's live contrast.

R23-03 has one possible realization-only improvement if page 1 is implicated: replace `She has also collected a ton of stories from students who say...` with `She also has a ton of stories from students who say...`. This would restore the more natural r22 thought movement while preserving the r23 student-report attribution correction and leaving the jade-egg preliminary-training claim unchanged. It is only a fallback candidate, not an accepted edit or detector attribution.

Reduced D2 preservation assessment for that fallback:
- proposition: unchanged;
- certainty/scope: unchanged;
- attribution: unchanged (`students who say` remains explicit);
- actor/action/object: unchanged;
- chronology/causality: unchanged;
- links/headings/placement: unchanged;
- unexplained substantive deltas: 0.

Do not materialize or certify that fallback solely because it seems detector-friendly. First use the stored-report highlight evidence if it becomes available.

## Next action

1. Read the v4 evidence branch if/when it appears.
2. Map any marked bounded snippet exactly to the authorized Part-2 source.
3. Inspect the complete natural section and determine whether a real editorial repair is justified.
4. If a repair is accepted, re-run the required preservation/architecture gates and certify only the changed exact Part-2 boundary through GUI.
5. Never resubmit exact r23 Part 1; do not merge/promote/publish r23 before the Part-2 gate is resolved or Joel explicitly accepts the residual.
