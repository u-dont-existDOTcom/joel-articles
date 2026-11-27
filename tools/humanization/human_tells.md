# What counts as a human tell

**A human tell is something a model tends not to write.** His own writing is where to look for one (words a model wrote
never hold one, however rough: lesson neuro-2026-11-26a), but that he wrote a phrase is not the test. On card W-LMA-73A I
named his "it's the same kind of thing" and "I'm not advising lion's mane" as human tells because they were his and sat in
windows that read High. Joel, 2026-11-27 19:16 UTC: "\"it's the same kind of thing\" isn't a human tell, ai can write that
also. we should have some better heuristics to understand human tells. same for \"advising lion's mane\" how would that be
a human tell? what is your rule i don't understand", and "post-ashwa is a human tell bc ai doesn't tend to reduce the
full name" (lesson neuro-2026-11-27g).

**The test, for each candidate: what would a model write in its place?** If a model would write the same words, it is not
a human tell, whoever wrote it. Name a human tell only with the answer: `"Post-ashwa" (a model writes the full name,
"post-ashwagandha syndrome")`. When you can't say what a model would write instead, it isn't one you can name.

## His examples

| What it is | His words | What a model writes instead | Where he said it |
|---|---|---|---|
| A clipped name | "Post-ashwa and post-lion's mane syndrome are rare" | the full name: "post-ashwagandha syndrome" | Joel, 2026-11-27 19:16 UTC, card W-LMA-73A (neuro de-armoring): "ai doesn't tend to reduce the full name" |
| A rough catch-all | "or to do whatever helps you come back a bit" | a polished one: "make one minimal repair", "take one gentle step" | E208 ([HUMANIZATION-GATE.md](../../docs/HUMANIZATION-GATE.md)): "AI will tend to make the catch-all more polished than that" |

Add a row when he names one, with his words and where.

## Not human tells

- Anything a model wrote, mine or the post's (his posts were drafted with AI), however casual or rough: lesson
  neuro-2026-11-26a ("if AI wrote it, it can't be a human tell, right?") and neuro-2026-11-24d (my colloquial add-ons).
- A plain phrase of his that any model writes: "it's the same kind of thing", "I'm not advising lion's mane" (2026-11-27).
- A tidy image or metaphor: that is an AI tell (E251: "i'd say your human tell should be an ai tell tho").
- A missing comma (HUMANIZATION-GATE.md: "A missing comma is not a human tell").
- A phrase a fresh reader called human: their impression (E251; `tell_panel.py`).
- A phrase in a window that read High: the window reads High for its whole text, so that alone names no tell.

## Where it is used

- **A prediction** (`pangram_ledger.py predict --human-tells`): a human tell that quotes words says what a model would
  write in their place ("a model writes ..."); the ledger refuses one that doesn't. "His writing: his card version of ..."
  is still evidence for a call (his versions read Human more often than mine), but it names no tell.
- **A help request or a teaching card** ("I can't find AI tells here, and here are the human tells I see"): only what
  passes the test, each with what a model would write. When nothing does, say so: "I can't find any more AI tells here
  that I know how to fix, and I can't point to a human tell in it. Can you help show me the tells I'm missing?"
