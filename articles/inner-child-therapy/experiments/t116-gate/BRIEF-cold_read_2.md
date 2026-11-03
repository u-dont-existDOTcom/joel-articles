# Reviewer brief: six few-word changes in a self-help guide

You are one of three independent reviewers. You have no other context, and that is intended. Your verdict decides whether each item may go to the author as a ready suggestion. Be critical: a PASS you don't believe in is worse than a FAIL.

The guide is Joel's inner child reparenting guide: his byline, his casual voice (jokes, emoji, slang, French-style spacing before ! ? : and « » quote marks are all his and are NOT part of what you review). He has just reorganized the whole guide himself. In six places his moves or cuts left a pointer or a "that X" pointing the wrong way or at nothing, and an AI editor (the writer) proposes a few words for each. Only the writer's words are under review; everything else in each sentence is Joel's.

**The six items, G1 to G6.** For each, the folder `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t116-gate/<ID>/` holds:

- `DRAFT.txt`: the writer's words only, exactly as they would read (two to eight words).
- `CHANGE.txt`: the change ("X" becomes "Y"), the whole sentence as it would read, and why.
- `CONTEXT.txt`: the section as it would read (the heading above, with its Markdown #s, and the section's paragraphs); it holds the draft once.
- `SOURCE.txt`: the paragraph as it is now, and what the change must keep.

`/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t116-gate/GATE-INPUTS.json` gives each item's three SHA-256 hashes (candidate_sha256, context_sha256, source_sha256), which your report must carry exactly, and the mechanical linter's findings (none for these six). The AI-writing tell rows are defined in `/home/claude/joel-articles-ro/docs/HUMANIZATION-TELL-INVENTORY.md` (T01 to T29, C01 to C04); read its general rules and rows first, once. The whole guide, if you need to check where a section is, is `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t116-joel/JOEL-GUIDE-20261103.md` (search it; don't read it all).

**Work one item at a time:** read G1's files, write G1's report file, then open G2's files, and so on. Write each report before you open the next item's files.

Each report is a JSON file, `/home/claude/joel-articles-ro/articles/inner-child-therapy/experiments/t116-gate/<ID>/REVIEW-cold_read_2.json`, exactly in this shape:

```json
{
  "schema": "JOEL_COLD_REVIEW_V1",
  "role": "cold_read_2",
  "candidate_sha256": "<from GATE-INPUTS.json for this item>",
  "context_sha256": "<from GATE-INPUTS.json for this item>",
  "source_sha256": "<from GATE-INPUTS.json for this item>",
  "verdict": "PASS or FAIL",
  "unresolved": [],
  "reviewer": {"name": "Claude Sonnet, fresh subagent (the second cold reader)", "context_id": "t116-gate-cold-read-2-subagent", "origin": "Agent tool, a fresh context with only this brief and its files, launched by the Inner Child lane session (https://claude.ai/code/session_01NbUfhcTaRT8sbjyYV1wEFq), turn 116, 2026-11-03"},
  "evidence": "Specific, critical evaluation of the literal words in their sentence and section: quote them.",
  "resolved_tell_ids": [],
  "resolved_lint_labels": []
}
```

On a FAIL, put what is wrong in "unresolved" (one string per problem) and say in "evidence" what would fix it. When all six files are written, reply with one line per item: its ID and your verdict.

## Your role

You are the second cold reader, independent of the first. Read each CONTEXT.txt as a reader of the published guide would, then look at the writer's words in their sentence. Ask: would a reader stumble here, in either the old wording (SOURCE.txt) or the new? Does the new wording sound like the same author as the rest of the section, or like an editor's insertion? Is it the smallest change that fixes the problem? PASS only if it reads right, in his voice, and fixes the problem without any tell row from the inventory. Do not judge Joel's own words, spacing or punctuation.
