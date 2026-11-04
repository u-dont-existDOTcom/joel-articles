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

A rewrite may also state a link the original leaves implied: what a term means, the step between two sentences, how something does what the sentence says, or why it matters to the reader (gate E345; Joel, 2026-11-04: "just explain stuff to someone who doesn't already know the hidden links in your prose's thinking"). That is not an added fact when it is true and is the original's own reasoning, or plain common knowledge a reader needs to follow it. Name each such link in `issue` as LINK, quoting it, and PASS it. FAIL it, quoting it, only when the link is wrong, contradicts the original, or is a claim the original's reasoning doesn't hold (a new benefit, a dose, a person, an experience, a recommendation).

An item may list `changed_points`: changes to a supporting point that the rewrite makes on purpose, each with its reason, because the point didn't hold up or didn't help the reader (gate E348; Joel, 2026-11-04: "you are always totally free to change up what is being said if you can make it more helpful and clear"). Those changes are not FAILs. Check that the rewrite makes exactly the listed changes, accurately, and FAIL any other change of meaning, or a listed change that also changes the larger argument the item supports.

For each item return:

```json
{"id": "X001", "verdict": "PASS", "issue": ""}
```

`verdict` is PASS or FAIL. For FAIL, `issue` names the exact change in at most 30 words, quoting the words involved. Judge each item on its own. Be strict about meaning and relaxed about wording.

## For this article (Healing the Gut: the glutamine paragraph in the Leaky gut cause)

The item is one paragraph, a sub-item of the "Leaky gut" cause, in a list of the fuels the gut lining runs on. The
paragraph just before it (unchanged) says: the gut barrier needs a lot of energy to keep its tight junctions intact; if the
cells lining the small intestine (called enterocytes) or the colonocytes lining the large intestine don't get that energy,
the barrier loosens up and LPS and other endotoxins leak into the bloodstream; the fuels each type of cell prefers are
glutamine and butyrate. Later paragraphs give glutamine's dose, a cancer caution (the blood from the gut goes straight to
the liver), butyrate for the colon, and malic and citric acid, which "are made and used by that mitochondrial energy cycle,
also called the TCA or Krebs cycle".

The original is Joel's approved wording. Only its second to fourth sentences were rewritten; the others are his, word for
word. Be strict about what glutamine does, which cells, what it turns into, and the claim that pure glutamine gives those
cells energy faster than eating food.
