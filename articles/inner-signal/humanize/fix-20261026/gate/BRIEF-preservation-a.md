# Reviewer brief: three proposed sentence changes in one article

You are one of three independent reviewers. You have no other context, and that is intended. Your verdict decides whether each change may be shown to the author as a proposed revision. Be critical: a PASS you don't believe in is worse than a FAIL.

The article is Joel's (his byline, his casual voice): a long self-hypnosis guide, with inner child and parts work and many safety cautions. A Pangram check read a few of its sentences as AI-written. Each proposed change replaces those sentences with the same passage as a humanizing tool, Emulate, rewrote it (only the flagged sentences are swapped in), sometimes with a small fix by an AI writer that puts back a point Emulate shifted; `the_change` says which. For each NAME, its folder (the `folder` field in GATE-INPUTS.json) holds:

- `DRAFT.txt`: the exact new words (a sentence, two, or the changed part of a long sentence).
- `CONTEXT.txt`: its section as it would read with the change, which holds the draft once.
- `SOURCE.txt`: the words it replaces, and the meaning to keep with where it comes from (his published guide, his inner child guide, or a card he approved).

`/home/claude/ja-community/articles/inner-signal/humanize/fix-20261026/gate/GATE-INPUTS.json` gives, for each NAME: its `folder`, the change in words (`the_change`), the three SHA-256 hashes your report must carry, and the mechanical linter's findings on the draft (`lint_findings`, each a label and examples). The tell rows are defined in `/home/claude/ja-community/docs/HUMANIZATION-TELL-INVENTORY.md` (T01 to T29, C01 to C04); read its general rules first. Each folder's `ADMISSION.json` has the writer's own judgment on every row and a reason for each linter finding, if you want to see what the writer claims.

The NAMEs: G-S2, G-S3a, G-S3b.

## Your role

You are the preservation reviewer. For each NAME, compare the draft with SOURCE.txt word by word: does it say what his own line says, no more and no less? Flag anything added (a claim, a condition, a person, a number), anything of his it still leaves out that the change says it puts back, and any change in strength or in who does what. Then make the tell and linter judgments below.

## For each NAME

Do one NAME at a time: read its three files, judge it, and write its review file before you open the next NAME's files.

1. Read DRAFT.txt, CONTEXT.txt and SOURCE.txt (and `the_change`).
2. Judge the draft in its context against every tell row. Note any row you find actually happening (PRESENT), and whether it is justified there.
3. Judge each linter finding: is the flag a real problem here, or does the context answer it? A finding you accept goes in `resolved_lint_labels` with its exact label string; one you don't accept makes the verdict FAIL.
4. Verdict PASS only if the change does what `the_change` says, keeps the meaning in SOURCE.txt, adds no claim or fact it doesn't have, has no unjustified tell, and reads right in its context. Otherwise FAIL, and put each problem in `unresolved` (a short string each).

Write one JSON file per NAME, with the Write tool, at `<folder>/REVIEW-preservation.json`, in exactly this shape:

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
    "name": "Claude Sonnet, fresh subagent (preservation reviewer)",
    "context_id": "b479-gate-preservation-subagent-a",
    "origin": "Claude Agent tool subagent, model sonnet, a fresh context with only this brief and its files, launched 2026-10-26 by session_01Mxpoi6tFT3FgKmBvtGjRtS (the writer's session)"
  },
  "evidence": "Your specific evaluation of this draft against its source and context: quote the words you judged, say what you checked and what you found, including each linter finding and any PRESENT row.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

Copy the hashes exactly; don't compute them. Use only the Read and Write tools, no web, and write only these review files. When all three files are written, reply with one line per NAME: its verdict and, for a FAIL, why.
