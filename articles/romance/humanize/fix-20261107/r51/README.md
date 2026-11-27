# r51: the game live, and his post updated (2026-11-27 20:11 UTC)

His message: "signed in", "yes update the post", and his check of the r50 draft A:
[the result](https://www.pangram.com/feed/0795a354-3a4a-47b7-be7e-e6a6867ce8a1).

## His check of the r50 draft A

**Human Written, High: seven windows, every one Human High, one segment** ([RESULTS-whole-r50.json](RESULTS-whole-r50.json)).
The two one-sentence Medium windows of r49 are gone. Its text is the r50 draft A's rendered text exactly. Draft B stands
at its r49 check (six windows, all High), its text unchanged.

## The game, live

Coolify deployment `5l88fjtyxcisbrcpubmdybg5` of innerself `4f084198` (main, commit SHA `HEAD`), finished at 20:13 UTC
in 40 s, from the browser pane through the SSH tunnel once he had signed in. `https://innerself.love/love-honestly/`
is the build byte for byte (SHA-256 `343ee6e4...`); the homepage is unchanged. On the live page one card was played
for one person (step 1 aloud, "I have answered it", step 2 "What is this answer based on?", the follow-up, where it
leaves you) and for two on one phone (both safety checks, both private answers and labels, the spoken answers, the
follow-up, the private judgment). Recorded in innerself's `DEPLOYMENT.md` (its pull request 5) and the sites registry
(its pull request 4). The tunnel is closed.

## His post, updated (no email)

The plan: [make_update.py](make_update.py) → [UPDATE-PLAN.json](UPDATE-PLAN.json) (pushed at c6600abc): the 219
changed live paragraphs of the fixed version through r50 (49 removed), each with its links (24 in the new paragraphs,
366's to Esther Perel's post among them) and his five *word* emphases as italics; the reel after 149 and his opening's
video after 252; the typography swap everywhere; the title's date. Then [update.js](update.js) in the post's editor:
the editor's 457 paragraphs matched the index first, so nothing he changed since 23 November was overwritten; one
transaction (359 steps; 140 blocks swapped); its 441 paragraphs equal the plan's, with 18 pictures, 12 videos, 3
Instagram posts, 2 buttons and 12 rules; links 42 → 47, as the fixed version has; no curly quote or em dash left. Then
[dispatch.js](dispatch.js) and Update (`tools/humanization/substack_update.js`: the dialog had no email box and its one
box, "Schedule time to publish", unticked).

The live post now ([LIVE-CHECK-20261127.json](LIVE-CHECK-20261127.json)): its 441 paragraphs equal the plan, read
signed in and as a reader who isn't; the reel, the video and the link are in; the title says "Updated Nov 27, 2026";
no email went (`email_sent_at` is still the first publication's). Its social title (the browser tab's and share
previews' title, which the editor doesn't show) still said "Updated Aug 27, 2026": set to the post's title. Lesson
[romance-2026-11-27d](../../../../../docs/lessons/2026-11-27-2011-romance.md).

The reel's block is Substack's own: its address was pasted at the end of the temporary draft B (after his check) to get
the attributes Substack makes for it, its pictures rehosted; the post's two other Instagram posts and the reel read live
on Instagram (`instagram_alive.js`).

## What changes now

The live post is the fixed version. `whole/LIVE-INDEX.txt`, `live-check/LIVE-POST-BLOCKS-20261123.jsonl` and
`whole/REPLACEMENTS.json` describe the post before this update: any later change starts from a fresh copy of the live
post, never from these. The two temporary drafts are his to delete.
