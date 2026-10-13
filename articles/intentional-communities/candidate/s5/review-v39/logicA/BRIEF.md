# Logic audit: one section of an essay on intentional communities, rewrite against the published original

Open only the files in this folder. Don't look for notes, other folders or the web.

- `original-section.md`: the published section, 33 paragraphs under four headings. Number its paragraphs P1 to P33 in order, counting every block of text that isn't a heading or an image.
- `R-section.md`: the rewrite, the same 33 paragraphs in the same order under the same headings.

Your one job is the logic of each paragraph: whether the rewrite keeps the published paragraph's logical relations. Not style, not wording, not what was dropped as such. Compare every paragraph, P1 to P33, and look at:
- connectives between items and clauses: or (one of these), and / also / too (all of these, or both at once), but / though (contrast), because / since / so (cause and effect, and which way it runs), if / unless / when (a condition), rather than / instead of, only, even, still;
- negation and its scope (not, never, no, neither … nor, without);
- quantifiers (all, every, any, most, many, some, a few, none);
- modality (can, may, might, will, would, must, should, has to): a possibility made a certainty, a rule made a suggestion, or the reverse;
- degree and comparison (more, less, especially, even more);
- who does what to whom (who decides, who acts, who is affected);
- sequence and time (first, before, after, until, eventually).

Be skeptical. An earlier review called this pair the same meaning: published "A retreat-circuit facilitator may be wise, or may be unvetted, unaccountable, sexually predatory, … or simply wrong", rewrite "The facilitator on the retreat circuit may be wise. They may also be someone who hasn't been vetted…". It isn't: "or" says the facilitator is one of these and you don't know which (the next sentence depends on it), "also" says they may be wise and a predator at once. The author: "OR is not ALSO". Look for every change of that kind.

For each paragraph, a table: the relation, the published wording, the rewrite's wording, and a verdict: SAME, CHANGED (say what a reader would now believe that the original doesn't say), or AMBIGUOUS (the rewrite can be read either way; give both readings). List only relations that differ in wording; one line saying "no changed relations" is enough for a paragraph where none do.

Keep the report under 1,500 words. Write it to `/home/claude/lessons/articles/inner-child-therapy/experiments/emulate-20260929/runs/articles/intentional-communities/candidate/s5/LOGIC-v39-A.md` with one Write call. Then return only the list of CHANGED and AMBIGUOUS findings, one line each: paragraph, the two wordings, what a reader would wrongly believe.
