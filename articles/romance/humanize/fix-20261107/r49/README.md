# r49: getting the game and the article ready to publish

His message, 2026-11-27 17:14 UTC, after v0.9.3 and the lessons for the universal rules:

> ok good so are we ready to publish the game and article now

## The game

- His "ok good" answered the request for his OK on v0.9.3, and I took it as that OK (said so in chat). The game's
  [pull request](https://github.com/u-dont-existDOTcom/love-honestly/pull/2) was marked ready and merged at its checked
  head (d1fac49); merging there deploys nothing.
- The site that serves the game, `innerself`, got a branch and a
  [pull request](https://github.com/u-dont-existDOTcom/innerself/pull/4) that vendors v0.9.3 beside v0.5.4 (kept for
  rollback) and points the build, the checks, the route inventory and the notes at it; the transform and its two inserted
  blocks are unchanged. `npm ci && npm test` passed (180 route contracts, the built page minus the two blocks is the file
  byte for byte), and a browser played one card for one person in the built `/love-honestly/` page. Its lane item
  (2026-10-31-mailbox-every-turn) is adopted. Not merged and not deployed: that waits for his go.

## The article: ready for his whole-article check

Since his last whole-article check (the r39 drafts, 2026-11-24), his new opening of "Primal attraction", Senegal, J-B54,
the corrected pointer and his ninth-page answers went in: 30 live paragraphs changed or added (218 replacements, from
198). Every section check already read Human High in every window except his one-word "Woops...".

- **The word-for-sense read** of those 30 paragraphs ([sense/CHANGED-SINCE-R39.md](sense/CHANGED-SINCE-R39.md), 1,993
  words): two fresh readers (Sonnet) on seed 1127 each found two of its three planted errors; both read the planted
  "pacific" (for "specific") as meaning "calm" in its sentence about confidence that comes from deep relaxation, so that
  canary fits its place. A third reader on new planted errors (seed 1128, [sense-seed1128/](sense-seed1128/)) found all
  three and nothing else. The one other finding, from readers 1 and 2 ("likely"), and its fate are in
  [sense/TRACE.md](sense/TRACE.md): nothing to fix. The non-word net found nine words, all his.
- **The drafts**: A and B cleared and pasted again from commit b0c80524 (218 replacements) in the built-in browser
  ([DRAFTS.json](../whole/DRAFTS.json), entry "r49"). A's secret link rendered the built text exactly (203 lines); B's
  (174 lines) with the two editor effects r40 recorded: his one double space made single, and the opening quote before
  "for safety and legal reasons" curled the wrong way. The two secret links went to him in chat, not into Git.

## A slip of mine, fixed

The lesson of the turn before, romance-2026-11-27a, didn't reach main with r48: `lane_push.py` stages the article's
folder and the lane's state, and a new file under `docs/lessons/` needs `--add`. It goes in with this turn's push. A
check that refuses a push leaving the lane's own new lesson file behind is a follow-up for `lane_push.py`.

## Next

1. His whole-article check: his extension on the two secret links.
2. Then the live update of his post with his OK, no email: the changed paragraphs merged into the editor HTML
   (`tools/humanization/substack_merge.py`), 366's link to Esther Perel's post, the reel embedded after 149, his new
   opening's video and links, the typography swap and the "Updated" date. He deletes the two drafts.
3. The game, on his go: merge the innerself pull request, deploy it through Coolify, compare the live page with the
   build (minus the two blocks, byte for byte), and play a card there.
