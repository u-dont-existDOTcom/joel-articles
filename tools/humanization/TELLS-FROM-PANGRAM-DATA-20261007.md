# Tells I looked for in our own Pangram results (2026-10-07)

Joel, 2026-10-07 15:44: "i'm surprised it looks like all the ai tells you have are the ones i told you specfically. you haven't found any yourself?"

The bans file only holds his rules, by design. The other tell lists (the inventory's T01–T29, the linter's B and E rules, the writers' "what the detector has shown" notes) came partly from earlier AI work and partly from my own self-audits. The only time I had checked my own tells against data was on 2026-09-27, with 28 texts. Since then the calibration folder has grown to 379 single paragraphs with a Pangram 4.0 verdict, and I hadn't looked at it again. This is that look. The tool is `tools/humanization/find_tells.py`. Rerun it after each batch of results.

## The data

- 379 single paragraphs: 188 failed and 191 passed.
- They fall into 110 families, where a family is the drafts of one paragraph. In 31 families some drafts passed and some failed. Those 31 are the useful ones, because the topic is the same and only the writing differs.
- 62 pairs are close: a failing draft and a passing draft of the same paragraph that share most of their words. What changed between them is the best evidence there is.

## What held up

**1. The passing draft often dropped the failing draft's last sentence.**
- This happened in 13 of the 62 close pairs, across seven different paragraphs.
- The dropped sentence was a second point added after the paragraph had already made its own:
  - a caveat: "It just isn't proof the whole thing's fixed, or even that this was what helped." Also "Nice, but not proof it's fixed, or even that this is what did it."
  - a consequence: "If you do, you might take the accusation as proof your love really is conditional, when it could just be another part talking."
  - a moral: "So an afternoon of coloring badly together might do more than another hour of going over what went wrong."
  - an aphorism: "At some point the method can't ever be wrong, so you always are."
  - a tender beat: "It might be the first time it's heard that from you." The passing version ended "Sometimes it doesn't say anything back for a while."
- Within families, a last sentence opening with That, This, It, So or Which was 10 points more common in the failing drafts (p = 0.04).
- This matches the inventory's T08, T20, T28 and T29 and the writers' note on endings. The data supports them; it isn't a new kind.

**2. A failing paragraph often made a point and then explained it.**
- These pairs went from failing to passing:
  - "notice, the way you'd notice a hug from someone who's checking their phone" became "notice."
  - "The one firing back might only be borrowing that voice, like the six-year-old behind 'But I'm trying!', or the inherited critic" was cut.
  - "Re-evaluation Counseling counts yawning as emotional discharge, which is sort of the opposite" was cut.
- In each, the explanation was an image or an example made up to explain. It wasn't something a reader would need.

**3. "Even" and "actually" go with the failing paragraphs, but they don't cause it.**
- Across families, "even" is in 42% of failing paragraphs and 27% of passing ones. "Actually" is in 30% against 17%. In both cases the 95% interval stays above zero.
- But the passing and failing drafts of the same paragraph use them about equally (+5 points, p = 0.46).
- So they mark the kind of paragraph I write that fails, not what flips it. They're words I add to sound casual, and they don't help.

**4. What goes with passing: the writer reacting in the moment.**
- Within families, the passing drafts more often had:
  - an exclamation (+10 points, p = 0.02);
  - "honestly" (p = 0.002);
  - a sentence opening with "Even" or "Or" (p = 0.005 each);
  - "I'd" (+6 points, p = 0.09).
- That's the march-break Joel described: a sentence that reacts instead of taking the next step.
- The "Or" openers are mostly his own fix for splitting a list ("Maybe it just has something to say."). So that one says his fix works, not that "Or" is magic.

## What didn't hold up

- **Surface counts barely separate passing from failing.** I checked sentence length and its spread, second person, first person, hedges, negations, contractions, conditionals, commas, word length, lists of three and the coach phrases. Inside families none of them separated clearly: the smallest p was 0.04 ("that" a little more often in failing drafts), out of 24 tests, which is about what chance gives. Pangram isn't reacting to words like these. It reacts to what each sentence is doing.
- **A narrow "closing gloss" pattern** (a last sentence opening "So", "That way", "It just", "Then again" and the like) didn't separate: 6 failing paragraphs against 7 passing. So the linter gets no rule for it. A reader has to judge it: read the paragraph without its last sentence.
- **A colon in the middle of a sentence** is in 19% of failing paragraphs and 9% of passing ones. But without the colons that introduce a quote, it's 19 against 12, with the families split evenly. That's not enough for a linter rule.
- **"It isn't X, but it still counts"** is in 10 failing paragraphs and 2 passing. That's too few to rest on. Joel named the shape himself, so the linter flags it (O14) on his word, not on this.

## What I changed

- **The writers' notes** (both prompts) now carry findings 1 and 3. They don't carry 2 and 4, which those notes already say in other words.
- **No new linter rule from this data.** Nothing that held up can be caught by a pattern without catching as much passing text.

## What I'd watch next

- **The waiting rule paragraphs** (B2, F P1, the depth, pleasantness and isolation paragraphs) all cover every case their guide passage lists. Each one gives the rule, its exception, the exception's own exception, and a safety carve-out. The passing paragraphs nearby cover one case and stay with it.
- This is a guess. I haven't measured it. Two ways to test it: draft versions that leave a case to the next paragraph, or that stay with one case, and see whether the verdict changes.
