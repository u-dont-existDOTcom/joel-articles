# Reviewer brief: proposed headings and one sentence in a self-help guide

You are one of three independent reviewers. You have no other context, and that is intended. Your verdict decides whether each item may be shown to the author as ready. Be critical: a PASS you don't believe in is worse than a FAIL.

The guide is Joel's inner child guide (his byline, his casual voice: jokes, emoji, slang and "I'd" are his). Joel asked for a clear little heading over each paragraph that is its own case, so readers can skip the parts that don't apply to them ("assuming the headings are very clear"). An AI writer proposed the headings; each NAME below is one heading whose words are new (headings made of the paragraph's own words are outside this review), except NAME solomon, which is one of Joel's sentences with a few words changed at his request. For each NAME, the folder `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t113-gate/<NAME>/` holds:

- `DRAFT.txt`: the exact new words (the heading's text, or the sentence).
- `CONTEXT.txt`: its section as it would read, plain text, headings marked with their Markdown #s; it holds the draft once.
- `SOURCE.txt`: what the words must be true to (for a heading, the paragraphs it stands over, as they are now; for solomon, Joel's sentence and the study it links).

`/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t113-gate/GATE-INPUTS-R2.json` gives, for each NAME: the change in words (`the_change`), the three SHA-256 hashes your report must carry, the mechanical linter's findings on the draft (`lint_findings`, each a label, examples and the writer's reason), and any tell rows the writer marked PRESENT but kept (`writer_marked_present`). The tell rows are defined in `/home/claude/joel-articles-ro/docs/HUMANIZATION-TELL-INVENTORY.md` (T01 to T29, C01 to C04); read its general rules first. Many rows are written for sentences and paragraphs; for a heading, judge whether the row's operation is actually happening in that heading in its place.

Your NAMEs: escape-trips, escape-prone, therapist-ifs, borrow-guiding.

## Your role

You are the second cold reader, independent of the first. Read each CONTEXT.txt top to bottom, then judge each NAME. Your main questions: is anything about it wrong, misleading or unclear in its place (a heading that promises something its paragraph doesn't deliver, a pronoun with no clear antecedent, a heading that splits a line from the line it answers)? Taken together with the section's other headings, does the set read as a natural set of cases for this guide, or as a tidy taxonomy built for coverage? Be specific and quote the words you judge. Then make the tell and linter judgments below.

## For each NAME

1. Read DRAFT.txt, CONTEXT.txt and SOURCE.txt (and `the_change`).
2. Judge the draft in its context against every tell row. Note any row you find actually happening (PRESENT), and whether it is justified there.
3. Judge each linter finding: is the flag a real problem here, or does the context answer it? A finding you accept goes in `resolved_lint_labels` with its exact label string, copied from GATE-INPUTS-R2.json; one you don't accept makes the verdict FAIL.
4. If the writer marked a row PRESENT but kept it, judge that row yourself: list it in `resolved_tell_ids` only if you agree it is justified there; otherwise FAIL.
5. Verdict PASS only if the item does what `the_change` says, is true to its source, adds no claim the source doesn't have, has no unjustified tell, and reads right in its context. Otherwise FAIL, and put each problem in `unresolved` (a short string each), with a better heading if you have one.

Write one JSON file per NAME, with the Write tool, at `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t113-gate/<NAME>/REVIEW-cold_read_2.json`, in exactly this shape:

```json
{
  "schema": "JOEL_COLD_REVIEW_V1",
  "role": "cold_read_2",
  "candidate_sha256": "<from GATE-INPUTS-R2.json>",
  "context_sha256": "<from GATE-INPUTS-R2.json>",
  "source_sha256": "<from GATE-INPUTS-R2.json>",
  "verdict": "PASS or FAIL",
  "unresolved": [],
  "reviewer": {
    "name": "Claude Sonnet, fresh subagent (cold read 2 reviewer, r2c)",
    "context_id": "t113-gate-cold-read-2-r2c-subagent",
    "origin": "Agent tool, a fresh context with only this brief and its files, launched by the Inner Child lane session (https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq), turn 113, 2026-10-25"
  },
  "evidence": "Two to four sentences: quote the words you judged, say what you checked and found, including each linter finding and any PRESENT row.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

Copy the hashes exactly; don't compute them. Keep each evidence to two to four sentences. Use only the Read and Write tools, no web. When all your files are written, reply with one line per NAME: its verdict and, for a FAIL, why.

This is the second round: some headings changed after the first reviewers' notes, and some sections changed around unchanged headings, so each folder holds the section as it reads now. Work efficiently: keep your thinking short, judge each NAME in a few lines, and write each file as soon as you have judged it. A long deliberation will run you out of output room before you write anything.
