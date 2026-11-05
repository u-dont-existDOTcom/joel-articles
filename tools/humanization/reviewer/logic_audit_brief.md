# Logic audit: {what}, rewrite against the published original

<!-- The gate's logic audit (docs/HUMANIZATION-GATE.md, "OR is not ALSO", Joel 2026-10-03). Give it to two fresh agents,
each in its own folder holding only `original-section.md` and `R-section.md`: tell one to work forward and the other
backward. Fill {what}, {count} and {report}; delete this comment. First used on community section 5 (2026-10-03),
where the two audits found six changed relations that four rounds of traces had passed. -->

Open only the files in this folder. Don't look for notes, other folders or the web.

- `original-section.md`: the published section, {count} paragraphs. Number its paragraphs P1 to P{count} in order, counting every block of text that isn't a heading or an image.
- `R-section.md`: the rewrite, the same paragraphs in the same order under the same headings.

Your one job is the logic of each paragraph: whether the rewrite keeps the published paragraph's logical relations. Not style, not wording, not what was dropped as such. Compare every paragraph and look at:
- connectives between items and clauses: or (one of these), and / also / too (all of these, or both at once), but / though (contrast), because / since / so (cause and effect, and which way it runs), if / unless / when (a condition), rather than / instead of, only, even, still;
- negation and its scope (not, never, no, neither … nor, without);
- quantifiers (all, every, any, most, many, some, a few, none);
- modality (can, may, might, will, would, must, should, has to, needs): a possibility made a certainty, a rule made a suggestion, or the reverse;
- degree and comparison (more, less, especially, even more);
- who does what to whom (who decides, who acts, who is affected);
- sequence and time (first, before, after, until, eventually).

Be skeptical. An earlier review called this pair the same meaning: published "A retreat-circuit facilitator may be wise, or may be unvetted, unaccountable, sexually predatory, … or simply wrong", rewrite "The facilitator on the retreat circuit may be wise. They may also be someone who hasn't been vetted…". It isn't: "or" says the facilitator is one of these and you don't know which (the next sentence depends on it), "also" says they may be wise and a predator at once. The author: "OR is not ALSO". Look for every change of that kind.

Skeptical is about logic, not register. A plainer, more conversational wording that a reader takes the same way is SAME: "the closest thing to a whole example that I found" for "the closest whole example I found" is not a hedge (Joel, 2026-10-09 22:08 UTC: "doesn't seem like a hedge to me, sounds just more conversational"). Every CHANGED verdict names what a reader would now wrongly believe; if you can't name it, the relation is SAME.

Read the original's own logic too, because a flaw both versions share passes a comparison. Where a paragraph sorts things into groups (kinds, tiers, dos and don'ts, dangerous and less dangerous), check every item against every other group in the passage: an item in two groups has to say how it belongs to both, or it's a contradiction, in the original and the rewrite alike. Report it as SHARED (the item, both groups, what a reader can't tell). The author, on two lists of symptoms that both held sweating, tremor and agitation: "you listed dangerous symptoms and less dangerous symptoms which overlapped" (gate E359).

For each paragraph, a table: the relation, the published wording, the rewrite's wording, and a verdict: SAME, CHANGED (say what a reader would now believe that the original doesn't say), or AMBIGUOUS (the rewrite can be read either way; give both readings). List only relations that differ in wording; one line saying "no changed relations" is enough for a paragraph where none do.

Keep the report under 1,500 words. Write it to `{report}` with one Write call. Then return only the list of CHANGED, AMBIGUOUS and SHARED findings, one line each: paragraph, the two wordings (or, for SHARED, the item and its two groups), what a reader would wrongly believe.
