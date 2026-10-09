# Task: before new paragraphs go into an article, check what the article already says

The author of a long self-help article (about inner child work) asked that new material from his guide be added only where it's new: "if it has new stuff add that ... just make sure it's not duplicating stuff". Draft paragraphs were written, but they were only checked against their neighbors, never against the whole article. Your job is that whole-article check.

Read two files with the Read tool, all of each (in several calls if needed):
- ./article_blocks.md: the article as it stands, about 11,000 words, each block numbered [B#].
- ./guide_items.md: three groups of new material. Each group has the guide passage it carries, where the drafts would go, and the draft paragraphs ([D1], [P1], [I1], [C2] and so on). None of the drafts is in the article.

## For each group

1. Split the guide passage into its separate points: one claim, instruction, caution, permission or example each. Number them (G1.1, G1.2, ... for group 1; G2.x; G3.x). Skip the paragraph the group says the article already carries, but check that it really does.
2. For each point, search the whole article, not just the place the drafts would go. Mark it SAID (the article already makes this point, for the same situation or close enough that a reader would feel told twice: give the block number and a short exact quote), PARTLY (say what's there, with the quote, and what's missing), or NEW.
3. For each sentence of each draft paragraph, in order: which guide point it carries, and whether that point is SAID / PARTLY / NEW in the article (with the block), or whether the sentence carries no guide point (something the writer added). If a draft sentence repeats another draft sentence in a different group, say so too.
4. Then, for the group: the guide points that are really left to add (NEW, and the missing part of each PARTLY), in a short list.

Judge by meaning, not by shared words: two passages that use the same words for different points are not a repeat, and two that make the same point in different words are. Where the article makes a point for a different situation (for example, about a relationship with another person, where the guide is about the relationship with your inner child), say so and call it PARTLY or NEW, with a reason.

## Output

Write it all to ./OUT_FILE with the Write tool, in plain English. Don't suggest rewrites and don't comment on style. Don't invent quotes: every quote must be copied exactly from the files. When you're done, reply with one line: for each group, how many points are SAID, PARTLY and NEW.
