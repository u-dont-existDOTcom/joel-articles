# Handoff 1: Inner Child Therapy, humanizing by hand (Claude)

Written by Claude on 2026-09-29, 04:00 UTC, so Joel can open a fresh chat for this project.

## Where it lives

- **Repo:** `joel-articles`, branch `handoff/claude-dangerous-adult-20260924-1631`. Never touch `main`, never force-push, and merges need Joel's OK.
- **The article:** `articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md`.
  - Render it with `python3 tools/render_article_so_far.py <out.html>`, from `articles/inner-child-therapy/`. The render also runs the owner-edits check against `OWNER-EDITS.json`.
  - Send the rendered HTML to Joel at the end of every turn.
- **Rules and lessons:** all in `articles/inner-child-therapy/tools/`:
  - `HUMANIZATION-GATE.md`: the process, plus Joel's bans;
  - `JOEL-FIXES-CATALOGUE-20260928.md`: every one of Joel's fixes;
  - `PREDICTIONS.md`: every Pangram check, with the call made before it;
  - `tells_lint.py`: the linter;
  - `reviewer/`: the reviewer prompts, including `grounding.txt` (guide-grounding and logic review, 2026-09-29);
  - `calibration/`: texts with known Pangram results.
- **The current section's record:** `experiments/LOVE-DOESNT-WAIT-20260930.md` (the plan, each paragraph's rounds, lessons). The one before, Make the Protector Visible, is `experiments/MAKE-THE-PROTECTOR-VISIBLE-20260928.md`, with lessons P1–P14.

## Where the work stands

*Updated 2026-09-30, turn 7 (17:04 UTC onward). Turn 7 started "Love Doesn't Have to Wait for Trust": the h2 and P1–P6 are in, and together they're 100% Human (341 words). Turn 6 fixed P1's "sweet things" line and P4's "both sides" line in Not Every Hero, both at Joel's request, and the relationship paragraph's danger line.*

**Make the Protector Visible is done.** It's under `# Building Trust With Your Little One`, with Joel's h2 `## Not Every Hero Wears A Cape`. The earlier "Keep Your Word" was picked only because it was the one h2 of six that passed Pangram; never pick a heading by its Pangram result (`tools/HUMANIZATION-GATE.md`, "Headings").
- **P1 is Joel's** (the "What's a 'boundary'?" paragraph). Keep it exact. Its relationship lines moved to Also Look Outward on 2026-09-30.
- **P2 is Claude's**, with Joel's logic corrections.
- **P3 is Joel's.**
- **P4 is Claude's x1b** with Joel's ending.
- **P5 is Joel's final.**
- The section is 100% Human (539 words, with both headings).

**Also Look Outward** (under `# Before You Try to Go Deep`) now has, after "You may not know for certain…":
- Joel's Substack note as a bare URL. Keep it a bare URL on its own line: that's how Substack shows the preview.
- The relationship paragraph: Joel's meditation wording with two logic fixes, a danger line, and his romance guide linked on "a relationship". The section is 100% Human (436 words).

**Love Doesn't Have to Wait for Trust** (the guide's own h2, right after Not Every Hero): the h2 and P1–P6 are installed. The plan maps each guide paragraph to one article paragraph and cuts two repeats of Not Every Hero. It's in `articles/inner-child-therapy/experiments/LOVE-DOESNT-WAIT-20260930.md`, with each paragraph's rounds and results.
- P3–P4 are the bedtime story and what it did, in Joel's first person. They're pending his answer on whether it's his memory (E71). If it isn't, P3–P5 switch to a general voice.
- P6 is his "Big fuckity whoopty doo" exchange, word for word.

**Next:** P7 (G7: you don't have to accept every conclusion; listen for the concrete complaint), then P8 (the Fred Rogers scene, checked against a script breakdown; leave out "pauses"), through P14, then "Make a Simple Vow".
- Run the grounding reviewer on every draft (`tools/reviewer/reviewer.py grounding`), with Joel's rulings in the target. It flags MISFIRES: instructions that could hurt some reader, even when they carry the guide faithfully.
- It also lists the reader's open questions, sized by a push knob (`--push tight|default|wide`; the default is `default`: small changes only). Take ASK AUTHOR items to Joel, and put parked ones in `articles/inner-child-therapy/PARKED-READER-QUESTIONS.md`, not in the article.
- Give the cold read `"earlier": "section"` in the target, so it sees what a reader has already read.
- End every turn with both pages:
  - the article: `tools/render_article_so_far.py`;
  - the in-context page: `tools/render_in_context.py tools/in-context/<map>.json OUT --since <the commit Joel last saw>`.

**Open for Joel:**
- whether the bedtime story is his memory (asked 2026-09-30, about 18:55 UTC);
- the moved relationship paragraph (he hasn't said yet).

## How to check on Pangram

Use Joel's dashboard in the built-in browser pane, tab `seed`, at https://www.pangram.com/dashboard.
- `tools/pangram_batch_gen.py drafts.json out.json key1 key2 key3` builds a browser batch of up to 3 checks. Each check:
  - fills the textarea;
  - verifies its SHA-256;
  - clicks "Check for AI";
  - reads the result and the flagged spans (background `rgba(255, 86, 48, 0.1)`).
- Keep each batch to 3 checks, because the call has a 50-second deadline. If the last read times out, read the page separately.
- Log a prediction in `PREDICTIONS.md` before every check.

## Getting changes onto GitHub from the cloud container

The container can't push. Instead:
1. **Commit and make a patch.** Commit in `/root/work/joel-articles` with `git -c user.name=Claude -c user.email=noreply@anthropic.com commit`, ending the message with the Co-Authored-By and Claude-Session lines. Then run `git format-patch -1 HEAD --stdout > /mnt/user-data/outputs/xfer22/xferNN-0001.patch`.
2. **Copy it to Joel's laptop.** Gzip and base64 it, and split it into parts of 8,300 characters: `gzip -9 -c P.patch | base64 -w0 > xferNN.b64; split -b 8300 -d -a 1 xferNN.b64 xferNN.part`. Note each part's sha256 (`tr -d '\n' < part | sha256sum`). Read each part and write it with Desktop Commander `write_file` (deviceId `cf376439-4f04-4ddd-aeab-1a1c826fe34c`) to `/home/joel/ai-work/claude-dangerous-lane/inbox/`. Check every part's hash on the laptop before applying: on 2026-09-30 one mistyped character in a part was found this way.
3. **Apply and push there.** Use Desktop Commander `start_process` with the same deviceId. In one guarded command:
   - join the parts and check the base64 file's sha256;
   - decode it and check the patch's sha256;
   - in `/home/joel/ai-work/claude-dangerous-lane/joel-articles`, check that `origin/<branch>` and HEAD are the commit before (PREV), the tree is clean, and the branch is right;
   - run `git -c user.name=Claude -c user.email=noreply@anthropic.com am` (the laptop has no git identity, so a bare `git am` fails);
   - check that the new tree is the container's (TREE), then push.
4. **Resync the container:** `git fetch origin && git reset --hard origin/<branch>`, only when there's no diff.

Stay inside `/home/joel/ai-work/claude-dangerous-lane` on the laptop.

## Joel's standing rules for this project

- One paragraph at a time. Check each paragraph on Pangram alone and in its section, with its headings.
- Show every draft in context, next to the guide's original (`tools/render_in_context.py` makes the page; Joel, 2026-09-30: "make that durable").
- Report every cut and every move in the same message.
- Never use "the kid". Invent no facts about Joel's life. Don't polish Joel's words.
- Banned: "doesn't get to decide", "Fine," / "Good," / "Great," as a clause of their own, and wry humor. Don't overuse made-up scenes.
- Read the clock only at the start and end of a turn, and report both times.
- Learn from Joel's minimal fixes, and ask him for one when stuck, showing the flagged span.
- A paragraph has to hold up against the guide and the article as a whole, not only on its own: no dropped conditions, no evidence turned into proof, no "can" turned into "will", examples in the right job, and no repeats of earlier examples (Joel, 2026-09-29).
