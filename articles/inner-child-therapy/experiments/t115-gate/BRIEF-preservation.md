# Reviewer brief: five reworded paragraphs and seven cuts in a self-help guide

You are one of three independent reviewers. You have no other context, and that is intended. Your verdict decides whether each item may go to the author as ready. Be critical: a PASS you don't believe in is worse than a FAIL.

The guide is Joel's inner child guide (his byline, his casual voice: jokes, emoji, slang and "I'd" are his). A whole-guide check in the AI detector Pangram read some sentences below "Human, high confidence", and Joel asked for one more pass on them. The method he set: the AI writer finds the AI-writing tells in its own paragraphs and takes them out, adding nothing: a cut where a sentence restates, sums up or reassures, or where another line already says it; otherwise the point said once, plainly. Joel's own words are not touched.

**Five reworded paragraphs (NAMEs F02, F04, F05, F06, F10).** For each NAME, the folder `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t115-gate/<NAME>/` holds:

- `DRAFT.txt`: the changed sentences as they would read, exactly.
- `CONTEXT.txt`: their block as it would read (the heading above, with its Markdown #s, and the block's paragraphs); it holds the draft once.
- `SOURCE.txt`: the paragraph as it is now, what the change must keep, and for F04 (a safety paragraph) the grounding's MUSTs and the guide's own lines.
- `CHANGE.txt`: what the detector read there, the tell named, and the change.

`/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t115-gate/GATE-INPUTS.json` gives, for each NAME: `the_change`, the three SHA-256 hashes your report must carry, the mechanical linter's findings on the draft (`lint_findings`, each a label, examples and the writer's reason), and any tell rows the writer marked PRESENT but kept (`writer_marked_present`). The tell rows are defined in `/home/claude/joel-articles-ro/docs/HUMANIZATION-TELL-INVENTORY.md` (T01 to T29, C01 to C04); read its general rules first.

**Seven cuts (F01, F03, F07, F08, F09, F11, F12)** are in `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t115-gate/CUTS.json`: for each, the paragraph `before` and `after`, the block as it would read (`block_after`), the tell named, and what the cut `keeps` and `drops`. A cut adds no words.

## Your role

You are the preservation reviewer. Your main question for each NAME and each cut: is it true to its SOURCE? Does the new wording keep every point the paragraph as it is now makes (`SOURCE.txt` says what it must keep; for F04, a safety paragraph, every safety instruction, its conditions and order, and the grounding's MUSTs quoted there), without adding a claim, a tone or a promise? For a cut: is what it drops really said elsewhere, or not important? A lost safety point, a changed claim or an added one is a FAIL.

## For each NAME

1. Read DRAFT.txt, CONTEXT.txt, SOURCE.txt and CHANGE.txt.
2. Judge the draft in its context against every tell row. Note any row you find actually happening (PRESENT), and whether it is justified there.
3. Judge each linter finding: is the flag a real problem here, or does the context answer it? A finding you accept goes in `resolved_lint_labels` with its exact label string, copied from GATE-INPUTS.json; one you don't accept makes the verdict FAIL.
4. If the writer marked a row PRESENT but kept it, judge that row yourself: list it in `resolved_tell_ids` only if you agree it is justified there; otherwise FAIL.
5. Verdict PASS only if the change does what `the_change` says, is true to its source, adds no claim, has no unjustified tell, and reads right in its context. Otherwise FAIL, and put each problem in `unresolved` (a short string each), with a better wording if you have one.

Write one JSON file per NAME, with the Write tool, at `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t115-gate/<NAME>/REVIEW-preservation.json`, in exactly this shape:

```json
{
  "schema": "JOEL_COLD_REVIEW_V1",
  "role": "preservation",
  "candidate_sha256": "<from GATE-INPUTS.json>",
  "context_sha256": "<from GATE-INPUTS.json>",
  "source_sha256": "<from GATE-INPUTS.json>",
  "verdict": "PASS or FAIL",
  "unresolved": [],
  "reviewer": {
    "name": "Claude Sonnet, fresh subagent (the preservation reviewer)",
    "context_id": "t115-gate-preservation-subagent",
    "origin": "Agent tool, a fresh context with only this brief and its files, launched by the Inner Child lane session (https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq), turn 115, 2026-10-26"
  },
  "evidence": "Two to four sentences: quote the words you judged, say what you checked and found, including each linter finding and any PRESENT row.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

Copy the hashes exactly; don't compute them.

## The cuts

For each cut in CUTS.json, judge it in your role and write one file, `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t115-gate/CUTS-REVIEW-preservation.json`:

```json
{
  "schema": "JOEL_CUT_REVIEW_V1",
  "role": "preservation",
  "reviewer": {"name": "Claude Sonnet, fresh subagent (the preservation reviewer)", "context_id": "t115-gate-preservation-cuts-subagent"},
  "cuts": {
    "F01": {"verdict": "PASS or FAIL", "note": "One or two sentences: what you checked, and for a FAIL what is lost or wrong."}
  }
}
```

with all seven cuts in `cuts`.

Use only the Read and Write tools, no web. Keep each evidence and note short, judge each item in a few lines, and write each file as soon as you have judged it; a long deliberation can run you out of output room before you write anything. When all six files are written, reply with one line per NAME and per cut: its verdict and, for a FAIL, why.
