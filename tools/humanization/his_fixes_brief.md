# The read against his fixes: which of my sentences still read the way he fixes?

Gate bad-trips-2026-11-12g. Joel, 2026-11-12 14:45 UTC, after my carries of his fixes read AI in eight tries of eight:
"have you systematically looked at all of the fixes i've shown you and what are the idfferences in how you write vs how
i fix? because when i look at how you try to implement my fixes, it's laughable, like you're not really learning much.
you still use a lot of ai patterns like "this is different. that's different, this other thing is also different" and
"x but not y" and so forth, like you're not even trying". The eight differences below come from reading 112 of his fixes
against the texts they replaced (`articles/bad-trips/humanize/h46-20261112/his-fixes/HOW-HE-FIXES.md`).

Give this brief to a fresh reader (a new agent that has seen nothing else) with the text, one sentence a line, before the
needed read and before any Pangram check of a text of mine. Their answer goes in the receipt's `his_fixes` field
(`tools/humanization/sense_receipt.py`): each sentence they mark is changed before the check, or the receipt says why it
stays.

---

You are reading a draft against the way one writer, Joel, fixes drafts like it. Below are eight ways his fixes differ
from the drafts he fixed, each with a sentence he fixed and what he wrote instead. Read the draft and mark every sentence
that still reads the first way.

1. **Compressed.** A run of category words or noun phrases, or several ideas packed into one sentence, where he gives each
   its own clause with what happens or what to do. He fixed "respiratory depression, stimulant toxicity, serotonin
   toxicity, seizure, dangerous overheating, cardiovascular symptoms, ..." into "are they suffering from slow and shallow
   breathing (respiratory depression, from opioids, benzos and alcohol)? Or is it rapid breathing, heart rate, and
   agitation, signs of stimulant toxicity?"
2. **Built the same way as its neighbours.** Items or sentences that repeat one shape: the same opening, the same
   connector, a term in brackets at the same place in each, or the same comparing word ("is a different problem from ...,
   and both are different from ..."). He builds each one differently: "would be one full pattern", "would be counted as one
   pattern altogether", "another pattern together", "Another is ... along with ...", "Lastly, ... as well as ...".
3. **Correcting or contrasting.** "X does not mean Y; it means Z", "a Y rather than a Z", "not X but Y", "X but not Y",
   "isn't X, it's Y", or a pair set against each other ("severely altered but physically stable"), where the sentence
   could say the thing itself. He fixed "This is a recognition aid rather than a command to wait for every criterion
   before acting." into "So if you see any of these patterns, call medics." Mark it unless the contrast answers a worry
   the reader really has ("Just because it's unplanned doesn't mean it will be more shocking" is his).
4. **Vague about who, what, or what counts.** He fixed "whatever could hurt somebody" into "Anything that could let
   someone hurt themselves", "water" into "pools of water", "adjunct" into "adjunct remedy", and spelled out that each
   combination "would be counted as one pattern altogether".
5. **Opening on a rule or an authority, with the reader outside it.** He fixed "Clinicians often use the Hunter criteria"
   into "We can use the same Hunter criteria that clinicians use", "Get urgent help when somebody may harm themselves"
   into "the moment you think they might hurt themselves or anybody else, get urgent help", "Dim the lights. Lower the
   sound." into "They're feeling overwhelmed, so dim the lights".
6. **Ending on a summing-up or a line that sounds wise.** "If all of that's true, calming and stabilizing the trip may be
   enough."; "An emergency means act now."; "The response is care rather than blame." He ends on what to do ("call
   medics", "reach out") or cuts the line ("you were overcompleting, repeating yourself on the last line").
7. **True but no use to the reader**, or missing what the reader needs to act. He cut a study detail with "there's NO
   PAYOFF" and added "Slow breathing is normal with iboga, but if cardiac irregularities come along with it, that's an
   extra danger sign."
8. **Joined and worded the way a model joins and words.** Two short sentences he would join with ", but" or "so"; a comma
   pair he writes with "and" ("Slow and shallow", not "Slow, shallow"); "one" where "a" would do.

THE DRAFT (what it is for: [one line: what the reader is about to do with it]):
[the text, one sentence a line, numbered S1, S2, ...]

Answer in this shape:

MARKED:
- S3: 2 — [one line: what in the sentence is the first way, and what his way would do instead]
- S5: 3 — ...
- (or "none")

Mark only what the draft shows; don't stretch a difference to fit. A sentence can have more than one number.
