# Meaning check brief

Each item gives an original paragraph by Joel Rosenblum and a rewrite of it. The rewrite was meant to change how the paragraph reads, not what it says. Check whether it kept the meaning.

Compare them claim by claim. A rewrite FAILS if it does any of these:

- drops a claim, fact, number, citation, example that carries a point, qualifier or caveat that changes what is being said;
- changes a relation or strength ("needed" to "wanted", "often" to "always", "may" to "does", a comparison lost);
- turns his uncertainty into a stance, or a stance into uncertainty;
- adds a fact, person, memory, anecdote, experience or opinion that isn't in the original;
- reverses or shifts the stance, or narrows/widens what a term covers;
- drops a joke or quip that carries a point, or makes the paragraph vaguer.

It does NOT fail for different wording, reordering, splitting or merging sentences, or cutting pure repetition, filler or redundant safety language that adds no claim.

For each item return:

```json
{"id": "X001", "verdict": "PASS", "issue": ""}
```

`verdict` is PASS or FAIL. For FAIL, `issue` names the exact change in at most 30 words, quoting the words involved. Judge each item on its own. Be strict about meaning and relaxed about wording.

## For this article (Healing the Gut, the protocol section)

These are steps of a health protocol. Be strict about: every step, test, compound, product, dose, time and warning kept; which book or author each step is from; the order of the steps and each phase's trigger; strength words ("must", "may", "likely", "only if"); a pairing the original states or implies (which treatment goes with which test). Also check that nothing implies Joel tried or recommends something the original doesn't say he did. Dropping the nicknames in the phase headings ("The Mechanic & Electrician") is a wording change, not a FAIL; name it in `issue` anyway so it shows. The "My notes" lines must be unchanged.
