# Meaning check brief

<!-- tools/humanization/meaning_check_brief.md: the shared core; a lane adds its article's own section after it (the gut lane's are under articles/healing-the-gut/humanize/fix-20261103/). -->

Each item gives an original paragraph by Joel Rosenblum and a rewrite of it. The rewrite was meant to change how the paragraph reads, not what it says. Check whether it kept the meaning.

Compare them claim by claim. A rewrite FAILS if it does any of these:

- drops a claim, fact, number, citation, example that carries a point, qualifier or caveat that changes what is being said;
- changes a relation or strength ("needed" to "wanted", "often" to "always", "may" to "does", a comparison lost);
- turns his uncertainty into a stance, or a stance into uncertainty;
- adds a fact, person, memory, anecdote, experience or opinion that isn't in the original;
- reverses or shifts the stance, or narrows/widens what a term covers;
- drops a joke or quip that carries a point, or makes the paragraph vaguer.

It does NOT fail for different wording, reordering, splitting or merging sentences, or cutting pure repetition, filler or redundant safety language that adds no claim.

A rewrite may also state a link the original leaves implied: what a term means, the step between two sentences, how something does what the sentence says, or why it matters to the reader (gate E343; Joel, 2026-11-04: "just explain stuff to someone who doesn't already know the hidden links in your prose's thinking"). That is not an added fact when it is true and is the original's own reasoning, or plain common knowledge a reader needs to follow it. Name each such link in `issue` as LINK, quoting it, and PASS it. FAIL it, quoting it, only when the link is wrong, contradicts the original, or is a claim the original's reasoning doesn't hold (a new benefit, a dose, a person, an experience, a recommendation).

For each item return:

```json
{"id": "X001", "verdict": "PASS", "issue": ""}
```

`verdict` is PASS or FAIL. For FAIL, `issue` names the exact change in at most 30 words, quoting the words involved. Judge each item on its own. Be strict about meaning and relaxed about wording.

## For this article (Healing the Gut, the fuels under Leaky gut)

The item is one bullet of a nested list about the fuels the cells of the gut lining need. The reader has just read the parts before it, which explain: the gut barrier needs a lot of energy to keep its tight junctions intact; enterocytes line the small intestine and colonocytes the large intestine; glutamine is the enterocytes' main fuel and is turned into alpha-ketoglutarate (α-KG) inside the mitochondria, which goes into the citric acid cycle, where the mitochondria make their energy; butyrate and the other short-chain fatty acids fuel the colonocytes.

Be strict about: every compound and food kept; strength words ("directly", "the exact same", "accelerating"); the claim that these acids are a quick, alternative fuel for the gut lining's cells that speeds up healing by a different biochemical route than glutamine. Dropping a bullet's bold label is a format change. Plain words for Gemini's intensifiers are wording when the claim stays as strong.
