# Emulate as a fallback, and how to learn from it

**By Claude, 2026-09-30, for the inner child chat to review. Joel decides.** Branch `claude/emulate-lessons-20260930`, folder `articles/inner-child-therapy/experiments/emulate-20260929/`.

Joel's plan is simple. When you can't get a paragraph past Pangram, send it through Emulate's API and fix what comes back. Each time, store a lesson, so that you need Emulate less and less, and in the end not at all.

This sits inside your gate (`tools/HUMANIZATION-GATE.md`) and replaces none of it. Emulate only changes how a paragraph sounds. What it returns has to pass every step a fresh writer's draft has to pass, and section 1 below shows why that matters more with Emulate than with anyone else.

## 1. What the Emulate run showed

The evidence is in `analysis/`:
- `CLAUDE-LESSONS.md`: the rules, by check id;
- `CLAUDE-SLOP-COMPARISON.md`: Emulate compared with Joel's own fixes;
- `CLAUDE-REVIEW-20260930.md`: GPT's run of 336 versions from three published articles;
- `CLAUDE-PILOT-20260930.md`: the first section assembled from Emulate's versions.

### What Emulate does

- **It passes Pangram almost every time.** 56 of 57 whole outputs came back 100% Human. So did every rewritten paragraph of the community article's first section, alone and in the section, once fixed.
- **It retells rather than paraphrases.** Only 9% of its words sit in runs of four or more words from the draft; in Joel's fixes it's 47%. It keeps the draft's points in the draft's order, one new sentence for each old one.
- **It shifts meaning everywhere, a little at a time.** A fresh agent that hadn't seen my notes traced community section 1 both ways against the original. It found 61 changes of meaning or strength (`runs/articles/intentional-communities/candidate/ic01-blind-trace.md`).
  - Most are small: "roughly eighty" became "maybe eighty", and "I was happy there" became "very happy".
  - About ten matter. A dropped "I'm proposing" left "these healing communities" with nothing to refer to. "Learn autonomy by living it" became "learn how the Zapatistas practice autonomy". Joel's own remembered thought, "I'd rather be sleeping", became "you generally felt like you'd rather be sleeping". A hedged cause ("which seemed to make her unusually difficult to question") became two facts side by side.
  - My own review had logged 12 changes and asked Joel about 4. A careful read by the person who chose the version isn't enough; the blind trace is.
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
- **Its versions survive small fixes.** 13 of 13 small corrections to passing versions stayed 100% Human, and two of them were whole clauses in my words. Community section 1 took 12 logged changes, one of them a splice, and still passed alone and as a section. Nothing yet says how many fixes one paragraph can take.

### What Pangram catches

Where a finding matches a rule you already have, it's named in brackets.
- **Sentences get caught together.** When one of my sentences went back into a passing Emulate version, the text stayed 100% Human 32 times out of 36. So a paragraph can keep most of its sentences once the loud ones change. [Your Chicken-and-Egg P2: Joel's paragraph with one sentence of yours passed.]
- **The loudest sentence is a run of vivid examples in one breath.** Three of the four put-backs that flipped a passing text were that kind of sentence. A five-part list of reasons didn't flip one. Joel keeps one or two examples, each in its own sentence. [B4/E15, and Joel's list style in Borrow One Competency.]
- **A summing-up "what X ends up doing is Y" sentence** turned a 75-word passing text 100% AI. It's one case. [Close to T29/E74, the concluding last sentence.]
- **Reshape; don't reword.** Two small word swaps left A12 at 100% AI. Joel changed the structure of one clause, and it came back 100% Human. [B10.]
- **Near 50 words, a cut at either end can flip a paragraph.** Check a paragraph at the length it will really have.
- **Context works both ways.** Rewriting a flagged paragraph can move the flag onto its neighbor, as it did with community section 1's opening. Human neighbors can also carry a paragraph. In that section, four flagged paragraphs weren't rewritten at first, and three of them passed unchanged once the paragraphs around them had been. So rewrite the fully flagged paragraphs first, recheck, and only then touch the rest.
- **The linter's contrast and coach rules didn't predict Pangram on this data.** Joel's fixes had more hits than the drafts they fixed (2.31 against 2.20 per 100 words). Only packed and list sentences pointed the right way. That fits your calibration: the linter guards, and it doesn't guide.

### What happened when I wrote from the lessons

I wrote the first two guide paragraphs of "Love Doesn't Have to Wait for Trust" by hand, from these lessons, without Emulate:
- E1 passed on the second try, alone and after the end of Not Every Hero.
- E2 failed five tries, including two where I added thoughts of my own.

**The lessons tell you which sentences are loud. They don't yet tell you how to write a paragraph that passes.** That gap is what the loop in section 5 is for.

E1's passing version is `analysis/transfer-20260930/E1-b.txt`. It hasn't been through your gate. Its hug example is my own thought, and Joel hasn't approved it.

## 2. When to use Emulate

Use it only when all of these hold:
- **The paragraph is ours,** written by Claude or a fresh writer. Joel's own words and owner-final passages never go to Emulate, and its output never replaces them. A flagged span in Joel's text still goes to him, as now.
- **Its meaning is settled.** It has passed your sense steps (S1 to S6, grounding and MISFIRES included) and the preservation trace. Emulate can't fix sense, and it adds errors of its own, so what goes in has to be right already.
- **Your own route has failed:** the fast route (three fresh writers) and one transfer try (section 5). I'd call Emulate before a reviewer-writer loop. A loop round takes 5 to 15 minutes, while an Emulate call costs as many words as the paragraph has. The order is Joel's call (question 1).
- **Nothing in it is private.** Emulate is a third-party service. Nothing Joel has marked private, and no private detail about another person, goes to it.
- **It isn't a held-out test** (question 3).

## 3. How to call it

- The API key is on Joel's laptop, at `/home/joel/ai-work/claude-dangerous-lane/secrets/emulate.key`. Never print it, copy it or commit it.
- The tool is `tools/emulate_humanize.py` in this folder. It makes one call. It saves Emulate's text exactly as returned, with the full response, and prints the words charged and the balance. It won't overwrite an earlier result. If a run dies mid-call, it won't repeat the call until someone has checked the balance and the saved files.
- Run it on the laptop with Desktop Commander, device `cf376439-4f04-4ddd-aeab-1a1c826fe34c` (the one you push from):
  - write the paragraph to a file there with `write_file`;
  - then run it with `start_process`:

  ```
  cd /tmp/claude-fix-tools
  python3 emulate_humanize.py balance
  python3 emulate_humanize.py humanize love-e2.txt love-e2-emu1
  python3 emulate_humanize.py humanize love-e2.txt love-e2-emu2
  ```

  A copy is in `/tmp/claude-fix-tools/` on the laptop now. I checked it on 2026-09-30 at 16:39 UTC: the balance read 256,527 words, and a 5-word input was refused without a call. `/tmp` doesn't survive a restart. If the copy is gone, write it there again from the repo.
- **Send the paragraph alone, as plain text:** no Markdown and no heading. Links and emphasis go back in from your draft afterwards.
  - Emulate needs at least 40 words; Pangram needs 50 to check a text alone.
  - One call gives one version, so make two calls to have two to choose from.
- **Costs:**
  - Emulate charges the input's word count per call. Four calls on community section 1 cost 256 words.
  - Pangram costs 1 credit per 100 words, rounded up: 1 credit for a paragraph, 11 for a 1,057-word section.
- Bring the output files back into the repo with the rest of the record (section 5).

## 4. What to do with what comes back

The aim is a paragraph that keeps as many of your sentences as it can and takes from Emulate only what it needs. Your sentences have been through your gate. Every sentence of Emulate's brings its own small shifts in meaning.

1. **Pick a version.** Check both alone on Pangram. Of those that pass, take the one closest to your draft in meaning. Joel's choosing rule (2026-09-29):
   1. it passes in its section;
   2. nothing is invented or changed;
   3. nothing is reversed or dropped;
   4. it makes at least as much sense in its section and the article;
   5. it has fewer stock phrases and padded lists;
   6. then judgment.
2. **Test your sentences one at a time.** Put each of your sentences alone into the chosen version, in place of the Emulate sentence that carries the same point. Check each on Pangram (1 credit). Where Emulate merged two of your sentences or split one, swap the whole group. A sentence that flips the text is a loud one: it goes in the lessons (section 5).
3. **Build.** Put back all your sentences that didn't flip it, together, and check. If it flips, take half of them out again and recheck, until it passes. Nobody has run this step yet (question 4).
4. **Fix the Emulate sentences that stay,** with small logged fixes:
   - put back a fact, number, condition, warning, name or link, or the strength of a claim;
   - remove what it invented;
   - fix a changed person or pronoun;
   - finish a cut-off sentence;
   - clean up the noise.

   Log each fix, with the words before and after. Joel's own phrasings go back in, or he's asked.
5. **Run your whole gate on the result.** First the two-way preservation trace, by a fresh agent that hasn't seen your notes. Then sense (S1 to S6), grounding and MISFIRES, the bans, the tell ledger and architecture. Then Pangram, alone and in the section with its headings, each check with its prediction in `PREDICTIONS.md`. After any fix, check again.
6. **Show Joel** the paragraph in context beside the guide's original (`tools/render_in_context.py`). Mark every sentence that came from Emulate, and list every change of meaning.

## 5. How to learn from each use

1. **Before calling Emulate, make one transfer try.** A fresh writer drafts the paragraph again with the current Emulate lessons in its brief. It can be one of the fast route's three writers, if they haven't run yet. Name the lesson being tested, predict, and check on Pangram. If it passes, you don't need Emulate, and the lesson gets a case. If it fails, go on. This try is how you measure whether the lessons work.
2. **Save the case** in its own folder, for example `tools/emulate-cases/<date>-<paragraph>/`:
   - your failed drafts, with their results and flagged spans;
   - the Emulate versions exactly as returned (the `.txt` and `.json` files);
   - each step of section 4, with its Pangram result;
   - the fix log;
   - the final version, with its results.
3. **Pair each loud sentence with its Emulate replacement.** For each sentence that flipped the text in section 4's step 2, say what changed in its shape, not its words. For example:
   - a list split into sentences;
   - a summing-up clause dropped;
   - a rule turned into one case;
   - a claim turned into a question;
   - the subject changed;
   - a restatement cut.

   These pairs are the same kind of evidence as Joel's minimal fixes, so they go in a catalogue beside `JOEL-FIXES-CATALOGUE-20260928.md`.
4. **Update the lessons.** Each lesson gets the rule, its evidence by case, how sure you are, and what would prove it wrong, as in `analysis/CLAUDE-LESSONS.md`. A case that goes against a lesson weakens it; the case still stays. Once two or more cases back a lesson, it joins what writers are told in the gate.
5. **Add the texts to `tools/calibration/`,** so the linter and the reviewers get tested on them too.
6. **Keep a score.** For each paragraph you got stuck on, record whether the transfer try passed and whether Emulate was needed.

Joel's fixes stay the model for his voice. Emulate teaches what Pangram catches. It doesn't teach how Joel writes, and its own voice is stock self-help.

## 6. When to stop needing it

Emulate passes because of how it was trained, on human writing, and that can't be copied as a rule. What can be learned is which sentence shapes Pangram catches, and Joel's way of keeping what's right and changing the thought where it's generic. So expect gradual progress, and measure it.

I suggest this rule. Once transfer tries pass on four of the last five stuck paragraphs, Emulate becomes a last resort, used only after a reviewer-writer loop has failed too. If the rate drops again, it goes back to routine use.

## 7. For your review and Joel's decision

1. **Where Emulate goes in your order:** before the reviewer-writer loop, as I suggest, or after it?
2. **Where the cases and lessons live:** a folder of cases and a catalogue beside Joel's fixes, with lessons moving into the gate once two cases back them?
3. **The holdout rule.** E1 to E5 were kept away from Emulate to test writing from the lessons. With a transfer try before every Emulate call, each stuck paragraph becomes its own test. So I suggest retiring the rule once Joel agrees; the tool's `E_holdout` refusal would go with it. E2 has already failed five hand-written tries, so it could be the first case.
4. **Steps 2 and 3 of section 4.** The single put-backs are tested: 32 of 36 stayed Human. Putting several back into one paragraph together is untested. The first cases will show whether the build keeps enough of your sentences to be worth the credits.
5. **The three published articles.** I assembled community section 1 without most of your gate, and the blind trace shows what that let through. Should the same procedure, with your gate, govern the community, hypnosis and neuro de-armoring articles, with the published text in the guide's place?
6. **Anything here that clashes with your gate:** the gate wins. Tell Joel what clashed.
