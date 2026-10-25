# Reviewer brief: two proposed sentence changes in one article

You are one of three independent reviewers. You have no other context, and that is intended. Your verdict decides whether each change may be shown to the author as a proposed revision. Be critical: a PASS you don't believe in is worse than a FAIL.

The articles are Joel's (his byline, his casual voice): a long self-hypnosis guide, and a long essay on intentional communities with a How-To Manual. Parts of both were rewritten by a humanizing tool, Emulate, which sometimes dropped or changed his points. Each proposed change is a small edit by an AI writer that puts one of his points back, or mends a sentence, in the article's own words. For each NAME, its folder (the `folder` field in GATE-INPUTS.json) holds:

- `DRAFT.txt`: the exact new words (a sentence, two, or the changed part of a long sentence).
- `CONTEXT.txt`: its section as it would read with the change, which holds the draft once.
- `SOURCE.txt`: the sentence it replaces, and his own line it comes from (his published post, or his answer).

`/home/claude/ja-community/articles/inner-signal/humanize/fix-20261025/emulate-check/gate/GATE-INPUTS.json` gives, for each NAME: its `folder`, the change in words (`the_change`), the three SHA-256 hashes your report must carry, and the mechanical linter's findings on the draft (`lint_findings`, each a label and examples). The tell rows are defined in `/home/claude/ja-community/docs/HUMANIZATION-TELL-INVENTORY.md` (T01 to T29, C01 to C04); read its general rules first. Each folder's `ADMISSION.json` has the writer's own judgment on every row and a reason for each linter finding, if you want to see what the writer claims.

The NAMEs: C-E2, C-E3a (the community essay).

## Your role

You are cold reader 1. Read each CONTEXT.txt the way a first-time reader of the article would, then look hard at the draft inside it: does it read naturally there, does every pronoun point where it should, does it follow from the sentence before it, and does it carry any tell from the inventory? Then make the tell and linter judgments below.

## For each NAME

Do one NAME at a time: read its three files, judge it, and write its review file before you open the next NAME's files.

1. Read DRAFT.txt, CONTEXT.txt and SOURCE.txt (and `the_change`).
2. Judge the draft in its context against every tell row. Note any row you find actually happening (PRESENT), and whether it is justified there.
3. Judge each linter finding: is the flag a real problem here, or does the context answer it? A finding you accept goes in `resolved_lint_labels` with its exact label string; one you don't accept makes the verdict FAIL.
4. Verdict PASS only if the change does what `the_change` says, keeps his meaning (SOURCE.txt), adds no claim or fact his line doesn't have, has no unjustified tell, and reads right in its context. Otherwise FAIL, and put each problem in `unresolved` (a short string each).

Write one JSON file per NAME, with the Write tool, at `<folder>/REVIEW-cold_read_1.json`, in exactly this shape:

```json
{
  "schema": "JOEL_COLD_REVIEW_V1",
  "role": "cold_read_1",
  "candidate_sha256": "<from GATE-INPUTS.json>",
  "context_sha256": "<from GATE-INPUTS.json>",
  "source_sha256": "<from GATE-INPUTS.json>",
  "verdict": "PASS or FAIL",
  "unresolved": [],
  "reviewer": {
    "name": "Claude Sonnet, fresh subagent (cold reader 1)",
    "context_id": "emulate-gate-cold_read_1-subagent-r2c",
    "origin": "Claude Agent tool subagent, model sonnet, a fresh context with only this brief and its files, launched 2026-10-25 by session_01Mxpoi6tFT3FgKmBvtGjRtS (the writer's session), round 2"
  },
  "evidence": "Your specific evaluation of this draft against its source and context: quote the words you judged, say what you checked and what you found, including each linter finding and any PRESENT row.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

Copy the hashes exactly; don't compute them. Use only the Read and Write tools, no web, and write only these review files. When both files are written, reply with one line per NAME: its verdict and, for a FAIL, why.
