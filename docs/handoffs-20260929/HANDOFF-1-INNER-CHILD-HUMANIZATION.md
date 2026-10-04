# Handoff 1: Inner Child Therapy, humanizing by hand (Claude)

Written by Claude on 2026-09-29, 04:00 UTC, so Joel can open a fresh chat for this project.

## Where it lives

- **Repo:** `joel-articles`, branch `handoff/claude-dangerous-adult-20260924-1631`. Never force-push, and merges into `main` need Joel's OK. He gave it for this branch on 2026-10-01, 02:40 UTC: "you can merge unless there's a reason not to then tell me". Since 15:59 that day, his "continue" is the OK: merge at the end of each turn he says it ("i guess it should be when i say "continue" right?").
- **The article:** `articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md`.
  - Render it from the repo root with `python3 tools/humanization/render_article_so_far.py <out.html> --article articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md --ledger articles/inner-child-therapy/OWNER-EDITS.json`. The render also runs the owner-edits check against `OWNER-EDITS.json`.
  - Send the rendered HTML to Joel at the end of every turn.
- **Rules and lessons:** in `articles/inner-child-therapy/tools/`:
  - `HUMANIZATION-GATE.md`: a pointer to the shared gate, `docs/HUMANIZATION-GATE.md` (the process, Joel's bans, and the lessons);
  - `PREDICTIONS.md`: every Pangram check, with the call made before it;
  - `targets/`: the reviewer targets, each with the article's and the guide's paths (`article`, `source`);
  - `in-context/`: the maps for the side-by-side page.
- **The shared tools,** in `tools/humanization/` from the repo root (`tools/humanization/README.md`):
  - `JOEL-FIXES-CATALOGUE-20260928.md`: every one of Joel's fixes;
  - `tells_lint.py`: the linter;
  - `reviewer/`: the reviewer prompts, including `grounding.txt` (guide-grounding and logic review, 2026-09-29);
  - `calibration/`: texts with known Pangram results.
- **The current section's record:** `experiments/LOVE-DOESNT-WAIT-20260930.md` (the plan, each paragraph's rounds, lessons). The one before, Make the Protector Visible, is `experiments/MAKE-THE-PROTECTOR-VISIBLE-20260928.md`, with lessons P1–P14.

## Where the work stands

*Updated 2026-10-04, turn 27 (01:33 UTC onward). The sequence is in as Hear the Protective Part First, four paragraphs: P1, Joel's P2, Joel's P3 (his one insertion, "(hopefully, right?)"), and one paragraph for the guide's last two, shortened. The h3, Start With Whatever Showed Up with both h3s, and the h1 are each 100% Human, high (413, 1,117, 1,690). The last paragraph took 25 checks: eight whole versions failed, then its halves split, and it was fixed window by window (E135: re-engage the reader inside the thought; stock casual moves read as AI). Not merged (no "continue"). Turn 26 (01:03 UTC onward). Joel fixed the sequence's P2 in four steps, each where the AI part began (E134; the catalogue has them), and kept the heading "Hear the Protective Part First". P3 to P5 didn't move in three rounds of changes at the start of the AI part (ten checks, all one AI window), so they wait on his read and on whether to cut what repeats. Not merged (no "continue"). Turn 25 (21:18 UTC onward). The marching-order check labels each sentence a step or a break now, with Joel's kinds of break; tested blind on 100 paragraphs, no break failed 23 of 30 and a break 27 of 70 (E133). It's `reviewer.py march`, run before Pangram. Two Common Protective Patterns is in, two paragraphs (the h1 with it 100% Human, 1,277). The guide's A Bottom-Up Sequence failed (P2 to P5 100% AI alone; the h1 with it 34% AI), so it waits. Merged after his "continue". Turn 24 (16:16 UTC onward). Joel's minimal fix of the altered-states paragraph is in, so When the Adult Voice Feels Fake is done through Start With Whatever Showed Up; the h1 with it is 100% Human (1,078). E131 is the marching order (a paragraph that only steps through a procedure reads as code put into English; break it, don't reword it), and E132 says a question the reader answers by looking back isn't open. Not merged (no "continue"). Turn 23 (04:31 UTC onward). Joel's P3–P5 are in (his P3 is mine without its last line), so Start With Whatever Showed Up is done; the h1 with them is 100% Human (974). E130 is why mine came out stiff: review flags answered by adding clauses. The guide update's altered-states paragraph failed alone three times (51%, 100% and 100% AI) though the h1 passed with each, so it waits for Joel. Merged after his "continue". Turn 22 (03:50 UTC onward). Pangram runs through Joel's new API key now (the gate's API line). Start With Whatever Showed Up P2 and P3 are in (the h1 with them 100% Human, 814); P4, P5a and P5b pass alone, but each one added after P3 tips the h1 (14–38% AI, E129). The guide was updated (`articles/inner-child-therapy/source/inner-child-guide-substack-20261003.txt`): its vow line is in Make a Simple Vow P3, the Borrowed Nurturer lines were already in the article, and the h1's new altered-states paragraph waits. Not merged (no "continue"). Turn 21 (01:06 UTC onward). Joel's list fixes are in (the h1's opening without "dinner", Love Doesn't Wait P12's questions 5 and 6), and they pass alone and in their sections; his rule is drop the item that matters least, split only when every item is needed (E126). Start With Whatever Showed Up P2, P3, P5a and P5b each passed alone (P5 is two paragraphs now, E128), but the account's Pangram credits ran out before the section check, so they aren't in. Merged after his "continue". Turn 20 (00:00 UTC onward). Joel's minimal fix of Start With Whatever Showed Up P1 is in (Human, medium on his check; the h1 with it 100% Human, 673): he split its two lists of three. The linter now fails two lists of three in one paragraph and flags one (E125), and the writer prompts take his bans from `owner_bans.txt` whole. No "continue", so not merged. Turn 19 (22:44 UTC onward). Joel picked adding the protective part to Start With Whatever Showed Up P1; with it the paragraph was 66% AI alone, so it waits. P4 is ready; P2, P3 and P5 had another round each (the record). Merged after his "continue". Turn 18 (18:56 UTC onward). Joel's P3, P4 and P6 are in, so The Parent You Inherited is done. Start With Whatever Showed Up has its heading, Joel's pl/ork paragraph and P1; P2–P5 have review notes (the record). The cold reader and the grounding review got four fixes (E119–E122). Merged after his "continue". Turn 17 (03:15 UTC onward). Joel's new P3 is in (who is feeling fake, E118), Scott's quote is confirmed, and the vow's P3 has his adopted proposal. The h2 The Parent You Inherited is in with P4 and P5; P6 isn't (six tries). Ask God for a Loan's food bank pointer still waits (E117). Merged after his "continue". Turn 16 (01:08 UTC onward). Joel's "Remind Yourself" is the Physical Reminder h3. The h1 When the Adult Voice Feels Fake has its opening (P1, Scott's quote, P3); its h2 The Parent You Inherited isn't in (P4 and P6 failed two tries each; P5 passes and waits). The far-back pointer sweep (E111, corrected: distance decides) cut two of mine; Ask God for a Loan's food bank pointer waits on its section (E117). Merged after his "continue". Turn 15 (00:16 UTC onward). Joel's fixes are in: his P1 rewrite, the "those grown-ups" pointer cut from the line after the vow (which now opens "Notice it"), the P4 examples cut, and his two Physical Reminder paragraphs in place of mine. The Physical Reminder section fails only under the guide's h3; that's his call. No "continue" this turn, so no merge. Turn 14 (20:51 UTC onward): Joel's P1 lines, P3 and P5 are in Make a Simple Vow with the vow and P4 proposals. Turn 13 (17:50 UTC onward): Make a Simple Vow is done (the h2 and P1–P5), and Joel adopted the Love Doesn't Wait P12 and P13 proposals. Turn 12 (15:59 UTC onward): Love Doesn't Have to Wait for Trust is done: Joel's P11, the P10 proposal adopted, P12–P14 installed. 😌 is back (E102), proposals are highlighted on the side-by-side page (E103), and his "continue" now means merge (see `docs/suggested-fixes-ledger.md`). Turn 11: his P9 and his emoji list (E100, E101).*

**Make the Protector Visible is done.** It's under `# Building Trust With Your Little One`, with Joel's h2 `## Not Every Hero Wears A Cape`. The earlier "Keep Your Word" was picked only because it was the one h2 of six that passed Pangram; never pick a heading by its Pangram result (`articles/inner-child-therapy/tools/HUMANIZATION-GATE.md`, "Headings").
- **P1 is Joel's** (the "What's a 'boundary'?" paragraph). Keep it exact. Its relationship lines moved to Also Look Outward on 2026-09-30.
- **P2 is Claude's**, with Joel's logic corrections.
- **P3 is Joel's.**
- **P4 is Claude's x1b** with Joel's ending.
- **P5 is Joel's final.**
- The section is 100% Human (539 words, with both headings).

**Also Look Outward** (under `# Before You Try to Go Deep`) now has, after "You may not know for certain…":
- Joel's Substack note as a bare URL. Keep it a bare URL on its own line: that's how Substack shows the preview.
- The relationship paragraph: Joel's meditation wording with two logic fixes, a danger line, and his romance guide linked on "a relationship". The section is 100% Human (436 words).

**Love Doesn't Have to Wait for Trust** (the guide's own h2, right after Not Every Hero) is done: the h2 and P1–P14, 100% Human together (1,236 words, with Joel's adopted P12 and P13 proposals). The plan maps each guide paragraph to one article paragraph and cuts two repeats of Not Every Hero. It's in `articles/inner-child-therapy/experiments/LOVE-DOESNT-WAIT-20260930.md`, with each paragraph's rounds and results.
- P3–P4 are the bedtime story and what it did, in Joel's first person: his own memory (confirmed 2026-10-01), and P4 is his own explanation of why fights don't usually go like that (adopted 02:40).
- P6 is his "Big fuckity whoopty doo" exchange, word for word. P9 and P11 are his own, word for word.

**Make a Simple Vow** (the guide's h2 after Love Doesn't Wait) is done: the h2 and P1–P5, 100% Human together (468 words, turn 15). P1's baby lines, P3 and P5 are Joel's; the line after the vow is his adopted proposal with his cut. The vow is a quote (a Markdown blockquote). The plan and each paragraph's rounds are in `articles/inner-child-therapy/experiments/MAKE-A-SIMPLE-VOW-20261001.md`.

**Remind Yourself** (Joel's h3 under the vow, 2026-10-02): his two paragraphs, Human on his check; with Make a Simple Vow above them, 100% Human (582).

**When the Adult Voice Feels Fake** (the guide's h1 after the vow): P1, Scott's quote (Joel confirmed it), Joel's P3 and his altered-states paragraph (turn 24); the h2 The Parent You Inherited (Joel's P4 and P6, my P5); and Start With Whatever Showed Up (Joel's pl/ork paragraph, his P1, my P2, his P3–P5) with its h3s Two Common Protective Patterns (turn 25) and Hear the Protective Part First (turn 27). 100% Human together (1,690, turn 27). The plan and the rounds are in `articles/inner-child-therapy/experiments/WHEN-THE-ADULT-VOICE-FEELS-FAKE-20261002.md`.

**Next:** Joel's new material from the map updates, merged in and deduped against the article as it is. Then When to Change the Strategy. Sections not written yet come from the updated guide. When a paragraph fails as one window, check its halves alone before rewriting it (E135).
- Every paragraph passes alone, and one under 50 words is checked with a neighbor that passes alone (Joel's shared rule, 2026-10-01, in `docs/HUMANIZATION-GATE.md` from the community lane). Turn 14 checked this lane's short ones that way: Love Doesn't Wait P14 (149), Make a Simple Vow P3 (138), the Physical Reminder opening (203), all 100% Human.
- A later paragraph can flip an earlier one on Pangram: on turn 13 three P3 drafts each flipped the vow section's opening, which had passed. Re-run the section check after every change.
- Run the grounding reviewer on every draft (`tools/humanization/reviewer/reviewer.py grounding`), with Joel's rulings in the target. It flags MISFIRES: instructions that could hurt some reader, even when they carry the guide faithfully.
- It also lists the reader's open questions, sized by a push knob (`--push tight|default|wide`; the default is `default`: small changes only). Take ASK AUTHOR items to Joel, and put parked ones in `articles/inner-child-therapy/PARKED-READER-QUESTIONS.md`, not in the article.
- Give the cold read `"earlier": "section"` in the target, so it sees what a reader has already read.
- End every turn with both pages (from the repo root, with `A=articles/inner-child-therapy`):
  - the article: `tools/humanization/render_article_so_far.py OUT --article $A/HUMANIZED-ARTICLE-SO-FAR.md --ledger $A/OWNER-EDITS.json`;
  - the in-context page: `tools/humanization/render_in_context.py $A/tools/in-context/<map>.json OUT --article $A/HUMANIZED-ARTICLE-SO-FAR.md --source $A/master.html --source-label "Guide original" --since <the commit Joel last saw>`.

**Open for Joel:**
- Hear the Protective Part First P4: the cold read's flag on its third sentence ("that" reads first as the step), open because the clarity fix put a 7% AI window into the h1 (turn 27); and the cut of the guide's "You don't need an age, a recovered memory, or a complete cast of parts".
- The P1 cut from turn 13: the guide's "skip the vow" for a present adult who still intends harm.
- The emoji placements, for his yes or no (he said he'd keep correcting them).
- The moved relationship paragraph (he hasn't said yet).

## How to check on Pangram

Since 2026-10-03 (turn 22), through Joel's API key, on the laptop with Desktop Commander, from the lane folder. Use `tools/humanization/pangram_api.py` (another lane's, merged as #134): it keeps each result keyed by the text's hash, so a text is never paid for twice, and saves the task id before polling, so a rerun resumes it. The turn-24 `pangram_api_check.py` does less and was only for this lane until #134 landed; with it, run `curl -fsSL https://raw.githubusercontent.com/u-dont-existDOTcom/joel-articles/COMMIT/tools/humanization/pangram_api_check.py | PANGRAM_KEY_FILE=<the key file Joel named> python3 - --sha COMMIT --run <pushed run file>` (the laptop has no checkout of the script) (ask him if this session doesn't have it). It keeps the lab's rules: one POST per text, model pangram-4, no repost after an ambiguous failure, version 4.0 checked, task ids printed. The dashboard route below is out of credits.

Use Joel's dashboard in the built-in browser pane, tab `seed`, at https://www.pangram.com/dashboard.
- `tools/humanization/pangram_batch_gen.py drafts.json out.json key1 key2 key3` builds a browser batch of up to 3 checks. Each check:
  - fills the textarea;
  - verifies its SHA-256;
  - clicks "Check for AI";
  - reads the result and the flagged spans (background `rgba(255, 86, 48, 0.1)`).
- Keep each batch to 3 checks: the call takes at most 25 actions and has a 50-second deadline. If the last read times out, read the page separately.
- Since 2026-10-01, push the texts first (in `articles/inner-child-therapy/tools/pangram-runs/`, with the predictions) and build the batch with `--url` and the raw.githubusercontent.com address of that commit: the page fetches the texts, so the batch stays small. A read that polls for "words scanned" returns as soon as the result is up (the turn-9 batches did).
- Log a prediction in `PREDICTIONS.md` before every check.

## Getting changes onto GitHub from the cloud container

Since 2026-10-01 a session can push directly once the repo is in its sources with push access (Joel, 02:40: "yes you can push from here"; the add-repo tool, with push access). A new session needs that again, with Joel's OK. Push from `/root/work/joel-articles`, the lane branch only, never force. If a session can't push, the laptop relay below is the fallback. On 2026-10-01 a safety check stopped it partway through pasting a base64 part, so prefer granting the lane's inbox folder and copying the files with the file-transfer tool, or sending Joel a git bundle.

The relay:
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
- Show every draft in context, next to the guide's original (`tools/humanization/render_in_context.py` makes the page; Joel, 2026-09-30: "make that durable").
- Report every cut and every move in the same message.
- Never use "the kid". Invent no facts about Joel's life. Don't polish Joel's words.
- Banned: "doesn't get to decide", "Fine," / "Good," / "Great," as a clause of their own, and wry humor. Don't overuse made-up scenes.
- Read the clock only at the start and end of a turn, and report both times.
- Learn from Joel's minimal fixes, and ask him for one when stuck, showing the flagged span.
- Every correction gets its "without me" lesson in the same turn: the signal that was already there, the check that should have acted, the change to it, a sweep of the article, and a line to Joel (2026-10-01, E94).
- Say which try every Pangram result came on (2026-10-01, E95).
- About one emoji per section on average, checked on Pangram like any other change (2026-10-01, E96), and only ones on the allowlist in `tools/humanization/EMOJI-LIST.md`: no pointers, no 😉, nothing that only labels a thing or an activity; ASCII like :) or "(hehe)" where it fits; "lol" is wry (2026-10-01, E97). A feeling's emoji can stay when it gives the line its beat (2026-10-01 15:59, E102).
- On the side-by-side page, a proposal's new words are highlighted (2026-10-01 15:59, E103).
- Love is felt, not faked: word a condition by what the reader can feel yet, never by whether they're sincere (2026-10-01 20:51, E107).
- The grown-up isn't only for when something's wrong: if the little one shows up for innocent fun, don't "put them in their place" (2026-10-01 20:51, E109).
- When the article retells a scene or a quote, carry the primary text's words, with a link (2026-10-01, E98).
- Emojis only from Joel's own list, darkest skin tone where there is one, and only where an emotion wants out, a heading wants one, a long stretch wants a break, or it says what the words can't (2026-10-01 13:57, E101).
- Finish the thought: a point the reader needs doesn't get cut because Pangram fights it; change its frame, and ask Joel with the flagged span (2026-10-01 13:57, E100).
- Joel's extreme examples explain his point; carry the reader's common case, and never poke readers to wonder whether they're the bad one (2026-10-01, E93).
- A paragraph has to hold up against the guide and the article as a whole, not only on its own: no dropped conditions, no evidence turned into proof, no "can" turned into "will", examples in the right job, and no repeats of earlier examples (Joel, 2026-09-29).
