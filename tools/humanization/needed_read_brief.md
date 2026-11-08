# The needed read: what does the reader of this paragraph need?

Gate neuro-2026-11-08a. Joel, 2026-11-08 00:49 UTC, after cutting a five-sentence paragraph of mine to its first two
facts: "did you even read what you had there? it was making no sense. i removed most of it and just put the basic facts.
it seems like you're doing anything possible to preserve prose even if it doesn't help the reader. fix that durably."

Give this brief to a fresh reader (a new agent that has seen nothing else; a cheaper model is enough), with three things
filled in: the paragraph, its heading, and one line on what the paragraph is for in the article (what its reader is
about to do with it). Their answer goes in the receipt's `needed` field (`tools/humanization/sense_receipt.py`).

---

You are reading one paragraph of an article for the person it is written for. Here is what the paragraph is for:

WHAT IT IS FOR: [one line: what the reader is about to do with this paragraph]

HEADING: [the heading]

PARAGRAPH:
[the paragraph, one sentence a line, numbered S1, S2, ...]

For each sentence, answer in one line: what does the reader need this sentence for, given what the paragraph is for?
Then list the sentences the reader doesn't need.

A sentence the reader doesn't need is one they could lose and still do what the paragraph is for, with nothing
missing. These are not reasons to keep a sentence: it is true; it has a source; it is interesting; it is a careful
hypothesis or a testable guess; it explains a disease or a case the reader doesn't have; it qualifies another claim the
reader didn't need either; it was already in the text. Read also for sense: a sentence whose words don't make sense
together, or that mixes pictures (a dial, a door, a floor and a leak for one thing), goes on the list too, with why.

Answer in this shape:

NEEDS:
S1: [what the reader needs it for, or "nothing"]
S2: ...

UNNEEDED:
- S2: [the sentence, copied exactly] — [why the reader can lose it]
- (or "none")
