# Blind two-way preservation trace: one section of an essay on intentional communities

You're checking a rewrite against the published original. Open only the files in this folder. Don't look for notes, other folders or the web.

Files:
- `original-section.md`: the published section, nine paragraphs under three headings.
- `R-*.md`: the rewritten paragraphs, named by the published paragraph they answer (P1 is the first paragraph after the top heading, P9 the last). Where there's an a and a b, they're alternatives for the same paragraph: trace each.
- `R-section.md`: the rewrite assembled in order (P4b, P6a, P8a and P9a), with the headings in place. Use it for the sense check across paragraphs.

The author's rulings for this rewrite: the wording can change freely as long as the meaning stays: the same claims at the same strength, the same people doing the same things, nothing new about anyone. A quip may go if its point stays, when the point matters.

For each rewrite file:
1. Which original paragraph it answers.
2. **Forward.** Split the original paragraph into units of meaning: one per claim, condition, quantity, time, attribution, hedge, example or link. Mark each SAME, SAME-MEANING (reworded, same meaning and strength), SHIFTED (meaning, scope, strength, voice, tense of a claim or attribution changed; say exactly how) or DROPPED.
3. **Reverse.** List everything in the rewrite that isn't in the original (ADDED): facts, claims, judgments, feelings, causes, people, intensifiers, hedges.
4. **Sources.** Links (same URL, doing the same job), quotation marks, who said or did what, numbers.
5. **Sense.** Every word or pronoun whose referent a reader can't find in the visible text (this paragraph, or what comes before it in `R-section.md`), tense slips, grammar that makes you reread.

Put the marks in tables. Don't judge whether the rewrite is better, and don't suggest rewrites. Be exhaustive: a small shift counts.

Keep the whole report under 3,000 words: terse tables, one row per unit, no prose beyond what a row needs. Write it to `/home/claude/lessons/articles/inner-child-therapy/experiments/emulate-20260929/runs/articles/intentional-communities/candidate/s3/TRACE-v1.md` with one Write call. Then return only a summary table: file, the count of SHIFTED, DROPPED and ADDED, and one line for each change that alters what a reader would believe about a fact, a person, or the author's position.
