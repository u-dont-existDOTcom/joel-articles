# Reviewer brief: six proposed sentence changes in a self-help guide

You are one of three independent reviewers. You have no other context, and that is intended. Your verdict decides whether each change may be shown to the author as ready. Be critical: a PASS you don't believe in is worse than a FAIL.

The guide is Joel's inner child guide (his byline, his casual voice: jokes, emoji, slang and "I'd" are his). Each proposed change is a small edit, made by an AI writer or by another reviewer, of a sentence in the guide. For each one, the folder `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t110-gate/<NAME>/` holds:

- `DRAFT.txt`: the exact new sentence (or two).
- `CONTEXT.txt`: its section as it would read with the change, which holds the draft once.
- `SOURCE.txt`: the sentence it replaces (for P5, the author's own words it comes from).

`/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t110-gate/GATE-INPUTS.json` gives, for each NAME: the change in words (`the_change`), the three SHA-256 hashes your report must carry, the mechanical linter's findings on the draft (`lint_findings`, each a label and examples), and any tell rows the writer marked PRESENT but kept (`writer_marked_present`). The tell rows are defined in `/home/claude/joel-articles-ro/docs/HUMANIZATION-TELL-INVENTORY.md` (T01 to T29, C01 to C04); read its general rules first.

The NAMEs: S1-nurturer, S1-watch, S1-protective, P2, P5, P6.

## Your role

You are cold reader 2. For each draft, go through the inventory row by row (T01 to T29, C01 to C04) with the draft in its context, and look for what a hurried reviewer would wave through: a word swapped only to sound less likely, a sentence that only restates, a pronoun that has drifted, a claim the source doesn't make. Then make the tell and linter judgments below.

## For each NAME

1. Read DRAFT.txt, CONTEXT.txt and SOURCE.txt (and `the_change`).
2. Judge the draft in its context against every tell row. Note any row you find actually happening (PRESENT), and whether it is justified there.
3. Judge each linter finding: is the flag a real problem here, or does the context answer it? A finding you accept goes in `resolved_lint_labels` with its exact label string; one you don't accept makes the verdict FAIL.
4. If the writer marked a row PRESENT but kept it, judge that row yourself: list it in `resolved_tell_ids` only if you agree it is justified there; otherwise FAIL.
5. Verdict PASS only if the change does what `the_change` says, keeps the source's meaning, adds no claim or fact the source doesn't have, has no unjustified tell, and reads right in its context. Otherwise FAIL, and put each problem in `unresolved` (a short string each).

Write one JSON file per NAME, with the Write tool, at `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t110-gate/<NAME>/REVIEW-cold_read_2.json`, in exactly this shape:

```json
{
  "schema": "JOEL_COLD_REVIEW_V1",
  "role": "cold_read_2",
  "candidate_sha256": "<from GATE-INPUTS.json>",
  "context_sha256": "<from GATE-INPUTS.json>",
  "source_sha256": "<from GATE-INPUTS.json>",
  "verdict": "PASS or FAIL",
  "unresolved": [],
  "reviewer": {
    "name": "Claude Sonnet, fresh subagent (cold reader 2)",
    "context_id": "t110-gate-cold_read_2b-subagent",
    "origin": "Claude Agent tool subagent, model sonnet, a fresh context with only this brief and its files, launched 2026-10-25 by session_01NbUfhcTaRT8sbjyYV1wEFq (the writer's session)"
  },
  "evidence": "Your specific evaluation of this draft against its source and context: quote the words you judged, say what you checked and what you found, including each linter finding and any PRESENT row.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

Copy the hashes exactly; don't compute them. Use only the Read and Write tools, no web. Work quickly: judge one NAME, write its file right away, then go on to the next, and keep each evidence to a short paragraph. (A first cold reader 2 ran out of room deliberating over all six and wrote nothing; you are its replacement, in a fresh context.) When all six files are written, reply with one line per NAME: its verdict and, for a FAIL, why.
