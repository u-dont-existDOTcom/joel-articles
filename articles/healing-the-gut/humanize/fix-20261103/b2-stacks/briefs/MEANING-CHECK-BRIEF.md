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

## For this article (Healing the Gut, batch 2)

Most items are a supplement list and a short section on ready-made supplement stacks; one is a protocol phase. Be strict about: every compound, product, brand, dose, number, condition and warning kept; who should see a clinician (every condition on the list); which kit is recommended for what; the order of reasoning (mechanics first, then diet and motility, antimicrobials only if symptoms persist); strength words ("prevents", "avoid", "must", "may", "only if"); which author or book a step is from; links kept on the same or equivalent words.

Plain words for Gemini's intensifiers are wording, not a FAIL, when the claim stays as strong: "the absolute premier energy substrate" as "the main fuel", "massive amounts" as "a lot", "hyper-proliferative" as "fast-growing". A claim made weaker or vaguer is a FAIL ("prevents" as "may help").

One addition is allowed, in the kits paragraph only: Joel said on 2026-11-03 that these kits were Gemini's suggestions, that so far they are the best kits he has seen, that he has not used them himself, and that people can check the reviews. A rewrite that says exactly that is not adding; anything more about the kits is (a claim he tried them, "I've heard good things", ratings).

The parenthesis "(My own advice is different for H. pylori, where berberine works well: see Parasites, above.)" may be reworded but must keep both claims and the pointer. "My notes" lines must be unchanged. Dropping a nickname in a phase heading ("The Architect & Scientist") is a wording change, not a FAIL; name it in `issue` so it shows.
