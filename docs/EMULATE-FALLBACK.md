# Emulate as a fallback, and how to learn from it

**Status: ACTIVE for every article, 2026-09-30.** Joel set its place in the order: "emulate would come after the rewrite loop because the purpose of emulate is as a fallback if my system can't pass pangram." Claude wrote the rest from the Emulate run. The Inner Child chat reviewed it on 2026-10-01 and changed four things: who decides whether a published article's paragraph is Joel's own words (section 2), where the tool runs (section 3), what Joel's review of the system's first six paragraphs found (section 1), and how to collect the reviewer's 50 calls (section 6). The reasons are next to each change.

**Which order, by kind of text (Joel, 2026-09-30, 20:31 UTC):**
- **A published article being humanized:** Emulate goes first on its Pangram-flagged paragraphs. The text is already Joel's, so the job is to change its shape without changing its meaning. Everything after the Emulate call (sections 3 to 5) still applies, above all the blind trace and his side-by-side review.
- **New writing (the Inner Child article and anything drafted from a guide or notes):** Emulate comes only after the reviewer-writer loop has failed. That's where the system learns. Where it clashes with `HUMANIZATION-GATE.md`, the gate wins, and Joel hears about the clash.

Joel's aim: "ultimately i'm hoping we don't need pangram or emulate at all, but we're still using them as fallbacks until we're sure about that." So the order is:
1. **The system:** `HUMANIZATION-GATE.md`. That's sense, preservation, fresh writers, the linter and tell ledger, and the reviewer-writer loop.
2. **Pangram:** the outside check, alone and in the section.
3. **Emulate:** only once the reviewer-writer loop has failed on a paragraph. A published article's flagged paragraphs are the exception: they go to Emulate first (above).

Each use of Emulate stores a lesson, so it's needed less over time.

The evidence is on branch `claude/emulate-lessons-20260930`, in `articles/inner-child-therapy/experiments/emulate-20260929/analysis/`:
- `CLAUDE-LESSONS.md`: the rules, by check id;
- `CLAUDE-SLOP-COMPARISON.md`: Emulate compared with Joel's own fixes;
- `CLAUDE-REVIEW-20260930.md`: GPT's run of 336 versions from three published articles;
- `CLAUDE-PILOT-20260930.md`: the first section assembled from Emulate's versions;
- `REVIEWER-ON-EMULATE-20260930.md`: the reviewer's verdicts on Emulate's output.

## 1. What the Emulate run showed

### What Emulate does

- **It passes Pangram almost every time.** 56 of 57 whole outputs came back 100% Human. So did every rewritten paragraph of the community article's first section, alone and in the section, once fixed.
- **It retells rather than paraphrases.** Only 9% of its words sit in runs of four or more words from the draft; in Joel's fixes it's 47%. It keeps the draft's points in the draft's order, one new sentence for each old one.
- **It shifts meaning everywhere, a little at a time.** A fresh agent that hadn't seen Claude's notes traced community section 1 both ways against the original. It found 61 changes of meaning or strength (`runs/articles/intentional-communities/candidate/ic01-blind-trace.md` on the evidence branch).
  - Most are small: "roughly eighty" became "maybe eighty".
  - About ten matter. A dropped "I'm proposing" left "these healing communities" with nothing to refer to. "Learn autonomy by living it" became "learn how the Zapatistas practice autonomy". Joel's own remembered thought, "I'd rather be sleeping", became "you generally felt like you'd rather be sleeping".
  - Claude's own review had logged 12 changes and asked Joel about 4. A careful read by whoever chose the version isn't enough; the blind trace is.
- **It makes the same big mistakes again and again:**
  - it invents people and facts: "my kids", "Brooke" and "$500 boots", "your toddler" and "McDonald's", memories in the community article, a factory "mostly around electricity";
  - it changes who did what: the woman who ran the factory "started" it;
  - it drops conditions and safety lines: the below-90-BPM threshold and a stop instruction in neuro de-armoring, and the final safety paragraph of the hypnosis guide;
  - it reverses a point: "most of the time you can just tick them off";
  - it changes person: Scott's data told in the first person, "tell them" for "tell yourself", a gender for the little one;
  - it swaps AI phrasing for stock self-help phrasing: "It's important to remember", "warm fuzzy feelings", "embark on this journey";
  - it lengthens lists: A01's six feelings became ten;
  - it adds noise: "do n't", odd quote marks, British spellings, typos.
- **It runs longer:** about 22% on inputs under 300 words.
- **Use the API, not the website.** Several website versions stopped mid-sentence or picked up page text ("Continue reading…"). The four API outputs so far ended cleanly.
- **Its versions survive small fixes.** 13 of 13 small corrections to passing versions stayed 100% Human on Pangram. Community section 1 took 12 logged changes, one of them a splice, and still passed. Nothing yet says how many fixes one paragraph can take, or whether the reviewer still passes them.

### What the system says about Emulate's output

The reviewer from the reviewer-writer loop is the part of the system that's stricter than Pangram: when it says HUMAN, Pangram has agreed every time so far. On 2026-09-30 it was run blind, by its validated route: Opus, the shared rubric and the labeled examples, as in `tools/humanization/reviewer/README.md`.
- **What it judged:** ten of Claude's inner child drafts that Pangram calls AI, and Emulate's versions of the same ten, which Pangram calls Human.
- **How:** two reviewers, each seeing only one version of each pair, plus four known controls each.
- **The drafts:** all ten called AI.
- **Emulate's versions:** all ten called HUMAN, at confidence 55 to 85. So Emulate's output passes the reviewer as well as Pangram.
- **The controls:**
  - All four Pangram-AI paragraphs were called AI.
  - Of four Claude paragraphs that Pangram passed, the reviewer called three AI, at 60, 78 and 80. That's where the system is stricter than Pangram: on our own writing near the line.
- **What it named as human in Emulate's versions** was mostly roughness: comma splices, a missing article, garbled phrases, clumsy repetition, "etc." lists, and endings that don't sum up. Our fixes remove some of that roughness, so the reviewer runs again on the fixed version. The gate requires that anyway.
- **The linter doesn't separate them.**
  - All ten drafts came out REVIEW.
  - Of the Emulate versions, seven were REVIEW, two CLEAR and one FAIL. The FAIL was A18, on coach phrases at 2.03 per 100 words, just over the limit.

### What Pangram catches

Where a finding matches a rule the gate already has, it's named in brackets.
- **Sentences get caught together.** One of Claude's sentences put back into a passing Emulate version left the text 100% Human 32 times out of 36. So a paragraph can keep most of its sentences once the loud ones change. [Chicken-and-Egg P2: Joel's paragraph with one sentence of Claude's passed.]
- **The loudest sentence is a run of vivid examples in one breath.** Three of the four put-backs that flipped a passing text were that kind of sentence. A five-part list of reasons didn't flip one. Joel keeps one or two examples, each in its own sentence. [B4/E15, and his list style in Borrow One Competency.]
- **A summing-up "what X ends up doing is Y" sentence** turned a 75-word passing text 100% AI. It's one case. [Close to T29/E74, the concluding last sentence.]
- **Reshape; don't reword.** Two small word swaps left A12 at 100% AI. Joel changed the structure of one clause, and it came back 100% Human. [B10.]
- **A run of actions after a colon is loud too.**
  - Joel's whole escuelita paragraph came back 100% AI alone.
  - A version that kept his proposal sentence word for word came back 49% AI. That sentence was "The healing communities I'm proposing should do the same: people live there, heal, learn the relational and practical methods, and some eventually leave to start the next one." The flag ran from it to the end.
  - Rewording only that sentence passed.
  - It's the same shape as the example lists above (community section 1, v3, 2026-09-30).
- **Putting the source's sentence back brings its flag back** (two cases). Community section 2 v2.1 fixed every blind-trace finding by restoring the published sentence, often whole, and 7 of 10 texts flipped to 100% AI. The v3 fixes were one word each ("uptick" to "turn", "is climbing" to "climbed", an added "that"), and the texts kept passing. Splitting a sentence isn't a small fix: it turned a passing pair 100% AI. The first case is the escuelita proposal sentence below. [Section 4, step 4; B10.]
- **Find the loud paragraph with pairs.** In section 2, every version of the AI paragraph that passed alone failed after the old Google Trends line, and passed after a new one. A paragraph under 50 words can only be checked with a neighbor, so pair it with one that passes alone.
- **A meaning fix can pass alone and still flag the section** (community section 3, 2026-10-01). After the gate's meaning fixes, every changed paragraph passed alone, but the section came back 34% AI. The flags were on the two paragraphs whose fixes had put the published wording back ("groups", "stop hating", "was deeply shaped by"). Taking the wording from Emulate's other version instead cleared them: its "heavily influenced by", and its whole version of one paragraph. So after any meaning fix, check the section again, and look for replacement words in Emulate's other version before the published text.
- **Recheck a pair when either paragraph changes.** In section 3, the last paragraph passed with one version of the paragraph before it and failed (37% AI) after a three-word cut to that paragraph.
- **Start the section repair where the flagged span starts** (the gate's step 8) worked twice in section 3. Replacing the sentence where the span started moved the flag to the next paragraph, and putting that paragraph back to Emulate's own wording cleared it.
- **A run of short paragraphs can fail as a run when each one passes** (community section 4, 2026-10-02). The section's second span ran from P13's last sentence to P20 (229 words), and every paragraph and pair inside it passed. The run alone, checked as a window, read 100% AI in three versions: the first rewrite, a second one, and one with a new sentence where the span started (Joel's published text, so that change wasn't the fix). One Emulate call over the whole run (P14 to P19 as one input) gave a version whose window read 100% Human. So when a span covers several short paragraphs that pass alone, send the run to Emulate as one unit. And check a span as a window before checking the section again: a 250-word window costs 3 credits, a section 14.
- **Starting from the start of a span doesn't always fix it.** In the same section, changing the sentence where the span started didn't clear the window; rewriting the run after it did.
- **On a published article's argument paragraphs, Emulate with small fixes beat the writers.** In section 2, every Emulate-based version with small fixes passed alone (7 of 7), while 3 of the 40 writer drafts checked passed (1 of 18, 0 of 13, 2 of 9 by round). Round 3's brief carried Joel's own rewrite of two neighboring paragraphs as the model of his voice (`tools/humanization/JOEL-FIXES-CATALOGUE-20260928.md`, 2026-10-01); both of its passes came from that round, and the section passed with one Emulate-based or writer paragraph in each place (`claude/emulate-lessons-20260930`, `runs/articles/intentional-communities/candidate/s2/`).
- **Near 50 words, a cut at either end can flip a paragraph.** Check a paragraph at the length it will really have.
- **A more human paragraph can expose the next one (Joel, 2026-10-02 21:16).** "when the prior paras get more human it can actually show the ai in the following paragraph better than before." Two cases in community section 4: after his rewrites of P11 and P12, his combination failed when P13 was added (P13's "devoted enough to practice them and secure enough to disagree" had passed in every earlier version), and after his edits the section read 8% AI on a run (P21's second sentence to P24's first) that had passed alone and in v5. Recheck what follows an improved paragraph, not only the paragraph.
- **Context works both ways.** Rewriting a flagged paragraph can move the flag onto its neighbor, as with community section 1's opening. Human neighbors can also carry a paragraph. In that section, three of four flagged paragraphs passed unchanged once the paragraphs around them had been rewritten. So rewrite the fully flagged paragraphs first, recheck, and only then touch the rest.

### Writing from the lessons alone

Claude wrote the first two guide paragraphs of "Love Doesn't Have to Wait for Trust" by hand, from these lessons, without Emulate:
- E1 passed on the second try, alone and after the end of Not Every Hero.
- E2 failed five tries.

**The lessons tell you which sentences are loud. They don't yet tell you how to write a paragraph that passes.**

The Inner Child chat's full system did better on the same section the same day (turn 7, `experiments/LOVE-DOESNT-WAIT-20260930.md` on its branch).
- Of its first six paragraphs, five passed Pangram on the first check.
- The E2 paragraph took three rounds of three fresh writers each. Round two's brief said "don't end on the evidence, and don't list it", and round three's asked for no so-or-because sentence explaining the answer.
- The six took about two and a half hours, 17:03 to 19:40 UTC. E1's passing version (`analysis/transfer-20260930/E1-b.txt`) hasn't been through the gate. Its hug example is Claude's own thought, and Joel hasn't approved it.
- Passing wasn't the end of it (Inner Child chat, 2026-10-01). Joel's read of those six found two meaning problems that the gate and Pangram had both passed. P1 carried the guide's "love and trust don't have to come as a pair" without what the guide left out: love "does require the lover to be honest (trustworthy objectively)". P4 carried the guide's "She did not tell me I wasn't angry" into his own memory ("maybe she did, you don't know"). Both are fixed, and the grounding review now tests carried claims for missing conditions and flags the guide's statements about his life (`HUMANIZATION-GATE.md`, S6). Emulate keeps meaning no better than the loop does, so its output needs the same read.

## 2. When to use Emulate

Use it only when all of these hold:
- **For new writing, the reviewer-writer loop has failed on the paragraph** (Joel, 2026-09-30). Not before. For a published article's flagged paragraph, this condition doesn't apply.
- **The paragraph isn't Joel's own writing.** For new writing, that means one written by Claude or a fresh writer. A published article is the exception the top of this doc makes: its flagged paragraphs can go, AI-assisted as they are. Inside one, though, a passage Joel wrote himself, or marked owner-final, doesn't go; its flagged span goes to him, with the span. Emulate's output never replaces his own words. (Changed 2026-10-01 by the Inner Child chat: this line said Joel's own words never go to Emulate, while the top of the doc sends a published article's flagged paragraphs there, and community section 1 had his remembered thoughts in it. Ask Joel when it isn't clear whose a passage is.)
- **Its meaning is settled.** It has passed the gate's sense steps (S1 to S6, grounding and MISFIRES included) and the preservation trace. Emulate can't fix sense, and it adds errors of its own.
- **Nothing in it is private.** Emulate is a third-party service. Nothing Joel has marked private, and no private detail about another person, goes to it.

## 3. How to call it

- **The key** is on Joel's laptop, at `/home/joel/ai-work/claude-dangerous-lane/secrets/emulate.key`. Never print it, copy it or commit it.
- **The tool** is `tools/humanization/emulate_humanize.py`.
  - It makes one call, saves Emulate's text exactly as returned with the full response, and prints the words charged and the balance.
  - It won't overwrite an earlier result.
  - If a run dies mid-call, it won't repeat the call until someone has checked the balance and the saved files.
  - It sends a named User-Agent. From 2026-10-03 about 04:30 UTC, Emulate's Cloudflare answered Python's default ("Python-urllib/3.12") with error 1010, an HTTP 403 "Access denied", on the balance check too, and I took it for a dead key for two hours. A 403 from Emulate: read the response body before suspecting the key.
- **Run it on the laptop** with Desktop Commander, device `cf376439-4f04-4ddd-aeab-1a1c826fe34c`, from the repo clone in the lane folder. Write the paragraph to a file there with `write_file`, then run the tool with `start_process`:

  ```
  cd /home/joel/ai-work/claude-dangerous-lane/joel-articles
  git fetch -q origin && git status --short   # the clone should be clean and current
  python3 tools/humanization/emulate_humanize.py balance
  python3 tools/humanization/emulate_humanize.py humanize para.txt para-emu1
  python3 tools/humanization/emulate_humanize.py humanize para.txt para-emu2
  ```

  Keep `para.txt` and the results outside the clone (in `/home/joel/ai-work/claude-dangerous-lane/emulate-runs/`, say), so they never get committed by accident. (Changed 2026-10-01 by the Inner Child chat. This said to run a copy in `/tmp/claude-fix-tools/`. But `/tmp` doesn't survive a restart, a copy drifts from the repo, and Joel's rule for this laptop is to stay inside `/home/joel/ai-work/claude-dangerous-lane`. The clone there has the tool since main was merged into the lane branch.)
- **Send the paragraph alone, as plain text,** with no Markdown and no heading. Links and emphasis go back in from the draft afterwards.
  - Emulate needs at least 40 words; Pangram needs 50 to check a text alone.
  - One call gives one version, so make two calls.
- **Costs:**
  - Emulate charges the input's word count per call. Four calls on community section 1 cost 256 words.
  - Pangram costs 1 credit per 100 words, rounded up.
  - **Credits are plentiful now; use Emulate wherever section 2 allows it (Joel, 2026-10-03 04:03).** "you can use emulate api key now if you still need emulate altho i guess you don't, but they gifted me a bunch of credits for some reason... but you can put that rule in for emulate use since i'll be doing another article humanization after these." The balance that morning: 247,539 words on the max plan, 5,000 words a call. So for article humanization the balance is no reason to hold back: two calls per unit, a run of short paragraphs as one unit, and a new round when a gated version still reads AI. Every call is still saved exactly, logged with its balance, and its output still goes through the whole gate before Pangram.

## 4. What to do with what comes back

The aim is a paragraph that keeps as many of our sentences as it can and takes from Emulate only what it needs. Our sentences have been through the gate. Every sentence of Emulate's brings its own small shifts in meaning.

1. **Pick a version.** Check both alone on Pangram. Of those that pass, take the one closest to the draft in meaning. Joel's choosing rule (2026-09-29):
   1. it passes in its section;
   2. nothing is invented or changed;
   3. nothing is reversed or dropped;
   4. it makes at least as much sense in its section and the article;
   5. it has fewer stock phrases and padded lists;
   6. then judgment.
2. **Test our sentences one at a time.** Put each of our sentences alone into the chosen version, in place of the Emulate sentence that carries the same point, and check each on Pangram. Where Emulate merged or split sentences, swap the whole group. A sentence that flips the text is a loud one, and it goes in the lessons (section 5).
3. **Build.** Put back all our sentences that didn't flip it, together, and check. If it flips, take half of them out again and recheck, until it passes.
4. **Fix the Emulate sentences that stay,** with small logged fixes:
   - put back a fact, number, condition, warning, name or link, or the strength of a claim;
   - remove what it invented;
   - fix a changed person or pronoun;
   - finish a cut-off sentence;
   - clean up the noise.

   Joel's own phrasings go back in, or he's asked, with a recommendation. His own paragraphs keep his exact characters, straight apostrophes included (2026-10-02: curling them flipped one from 100% Human to 100% AI).
   - **Fix words, not shapes (community section 5, 2026-10-03).** Emulate's own sentence shapes are what pass. Of eleven paragraphs still reading AI after fresh writers (6 of 17 first picks had passed, none of 5 second picks), Emulate's round 4 with the meaning put back word by word passed 7 of 11; the four where I rebuilt its sentences to carry the meaning read AI, and so did my own spoken rewrites of those four (0 of 4). In round 6, step 1 (which I had skipped in rounds 4 and 5) found 10 of 11 raw versions Human; word-level fixes kept P24 and P25 passing, while a fix that put the published middle sentence back word for word turned P14 AI again, and the next-closest raw version with three words added passed. So check the raw versions first, take the closest passer, and make each fix the smallest change of words that carries the meaning; when a trace finding can only be met by rebuilding a sentence, try another raw version first.
   - **A section can read AI when every paragraph passes (community section 5, 2026-10-03).** All 33 paragraphs passed alone or with a neighbor that passes alone; the section (1,876 words, with its headings) read 77% AI, in four windows, the longest 845 words from P18 to the end. Three seams there had already read AI as pairs (P23P24, P25P26, P27P28) though each paragraph passed alone: a pair that reads AI between two passing paragraphs is an early sign. Section 4's fix for a run is the next step: the flagged run to Emulate as one unit.
   - **Find the sentence before rewriting the paragraph (community section 5, 2026-10-03).** P18 read AI with its heading and P19 through eight tries over a day (mine, the writers', Emulate's), and each try rewrote the whole paragraph. Joel, 20:51: "you're telling me it fails, but why does it fail? the reason that it fails should tell you how to fix it, right? What is the stumbling block exactly, you don't know how to do what?" One batch of five small checks answered it: the paragraph with its neighbors, then the same with one sentence out at a time, and the neighbor alone. Without the last sentence ("I respect what those traditions have preserved and have learned from them", published) the heading, P18 and P19 read 100% Human; with it and without the concession, still 100% AI. The section window that began at the concession was a chunk boundary, not the cause. So when a paragraph keeps failing, ablate it before the next rewrite: about 100 words a check, and the answer names what to fix.
   - **An empty courtesy reads AI in any wording (same paragraph).** That sentence is the respectful nod a model adds after disagreeing with someone. It names a respect and a debt and fills in neither, what they kept or what he learned, so it could close any paragraph that disagrees with any tradition. Every version had reworded it and kept it empty. Reworded again in its place, it took the three paragraphs from 100% AI to 58%; moved up into the concession, it changed whom he says he learned from, and the paragraph then ended on the lineages' authority right before his objection, which reads as a verdict on them. The fix is the author's specific, and only he has it: ask him what, with the passage, instead of rewording it again, and offer the cut (it passes) as the other option.
5. **Run the whole gate on the result.**
   1. The two-way preservation trace, by a fresh agent that hasn't seen the notes.
   2. The whole-article stance check (`tools/humanization/stance_check_prompt.py`), by a fresh agent with the whole published article: Emulate turned "without pretending that people arrive emotionally finished" into "where people don't come in pre-healed" in community section 3, nearly the opposite of what Joel wants, and only a check against the whole article shows that (Joel, 2026-10-02: "Did the reviewers not look at the article?").
   3. Sense (S1 to S6), grounding and MISFIRES, the bans, the tell ledger and architecture.
   4. The reviewer.
   5. Pangram, alone and in the section with its headings, each check with its prediction written down.

   After any fix, check again.
6. **Show Joel the side-by-side page** (`tools/humanization/render_in_context.py`). Mark every sentence that came from Emulate, and give a recommendation for every change of meaning.

## 5. How to learn from each use

1. **Save the case** in `tools/humanization/emulate-cases/<date>-<article>-<paragraph>/`:
   - the failed drafts, with their results and flagged spans;
   - the Emulate versions exactly as returned (the `.txt` and `.json` files);
   - each step of section 4, with its result;
   - the fix log;
   - the final version, with its results.
2. **Pair each loud sentence with its Emulate replacement.** Say what changed in its shape, not its words. For example:
   - a list split into sentences;
   - a summing-up clause dropped;
   - a rule turned into one case;
   - a claim turned into a question;
   - the subject changed;
   - a restatement cut.

   The pairs are the same kind of evidence as Joel's minimal fixes, and they're kept the same way.
3. **Update the lessons.** Each lesson gets the rule, its evidence by case, how sure it is, and what would prove it wrong. A case that goes against a lesson weakens it; the case still stays.
4. **Give the lessons to the writers.** Once two cases back a lesson, it goes into the fresh writers' brief, as an observation beside Joel's fixes. Then every paragraph after that tests it.
5. **Add the texts to the reviewer's calibration set,** so the linter and the reviewer get tested on them too.
6. **Keep a score:** for each paragraph, whether the loop passed it without Emulate.

Joel's fixes stay the model for his voice. Emulate teaches what Pangram catches. It doesn't teach how Joel writes, and its own voice is stock self-help.

## 6. When to stop needing each fallback

- **Emulate.** Stop routine use when the loop has passed ten paragraphs in a row without it. Go back to it if paragraphs start failing again.
- **Pangram.** In this test, all eleven of the reviewer's HUMAN calls matched Pangram, as every one had before. Its AI calls on our own near-the-line drafts were wrong three times in four.
  - Once the reviewer's HUMAN has held on about 50 paragraphs across articles, a reviewer HUMAN can stand in for the Pangram check.
  - The gate runs that reviewer only when a paragraph fails, so its HUMAN calls pile up slowly. To collect the 50, run it, blind, on paragraphs that are going to Pangram anyway, and log its call before the Pangram result in the article's PREDICTIONS file. (Added 2026-10-01 by the Inner Child chat.)
  - An AI verdict on our own draft still goes to Pangram before anything is rewritten.
  - Joel decides when the 50 are in.

## 7. Open questions, with Claude's recommendation on each

1. **Where Emulate goes in the order.** Decided by Joel: after the reviewer-writer loop.
2. **Where cases and lessons live.** Shared, not per chat: cases in `tools/humanization/emulate-cases/`, and lessons in the gate and the writers' brief once two cases back them.
3. **The holdout rule** (E1 to E5 never go to Emulate). Retire it. The score in section 5 makes every paragraph a test, and E2 has already failed five hand-written tries. The tool's `E_holdout` refusal goes with it. (Inner Child chat, 2026-10-01: agreed. The loop wrote and installed the section's first six paragraphs, E1 and E2 among them, without Emulate, so the holdout has done its job. The refusal in the tool is left for Joel to drop.)
4. **Steps 2 and 3 of section 4.** Try them on the first two cases. If they keep fewer than a third of our sentences, drop them and fix Emulate's version in place instead.
5. **The three published articles** (community, hypnosis guide, neuro de-armoring). Run the same gate on them. Before trusting the reviewer on them, add Pangram-checked paragraphs from each article to its calibration and revalidate, since it learned from the Inner Child article only.
