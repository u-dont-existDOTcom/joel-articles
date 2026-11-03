# Brief: read one part of the hypnosis guide for overcompletion

You are reading one part of Joel's self-hypnosis guide ("The Inner Signal", a long informal guide on his Substack). Most
of its paragraphs were rewritten by an AI from his original, and AI writing overcompletes. On 3 November Joel cut two
paragraphs of it and wrote: "cut all this. you didn't notice the massive overcompletion here? prob this whole guide is
full of it then." Your job is to find every place in your part that overcompletes, so it can be cut.

## What overcompletion is (Joel's words and rulings)

**"overcompletion is when you already have it explained and then you explain it again."** The second saying can be in
different words, from another angle, as a summary, as a moral, or as the same point made pair by pair.

**The example he just cut** (blocks 60 to 62 as they were, in the section "Forget the left-brain/right-brain cartoon";
[61] and [62] are gone from the guide now, so the block numbers in your part are the guide's after the cut):

> [60] Let's elicit a high level of co-operation between the verbal, the analytical, the imaginal, the emotional, the
> somatic, the intuitive, the relational, the spiritual … all the modes of your mind. It's not an electoral process.
> Nobody needs to win!
>
> [61] The mind of love and the mind of analysis can both be there, so you can be warm and clear-headed at once. The mind
> of intuition and the mind of rationality can both be there - intuitive signals without dogma, and testing of those
> signals without killing them. Your body has its own yes and no, and sometimes a not yet. Your imagination can open
> things up before the adult in you decides what to do in real life.
>
> [62] Analysis with no love in it gets sterile, and love that never stops to analyze anything drifts off into fantasy.
> The same goes for intuition and testing: signals you never test can turn into delusions, and testing with nothing
> intuitive to test is dead.

[60] had already said it: all the modes co-operate, and nobody needs to win. [61] explains it again pair by pair, and
[62] explains it again from the other side (each pair without its partner). An earlier reader kept [61] and [62] as
"parallel on purpose". Joel called that massive overcompletion and cut both. **Parallel structure, balance, or "it's
said more vividly the second time" are not reasons to keep a second explanation.**

**The shapes it takes** (all of them are the same thing: explaining what's already explained):
- the same point said again in the next sentence or paragraph, in other words ("In other words…", "That is…", "This
  means…", or no marker at all);
- the point said again from the other side ("X helps you… Without X, you…"), or every pair, case or combination spelled
  out when one or two make the point;
- a closing line that sums the paragraph up, draws its moral, or completes the thought when it was already clear a
  sentence earlier ("So…", "That's why…", "This is what…"). Joel, on such a line: "it was way overcompleting itself";
- a concrete image or example followed by a sentence that translates, explains, or moralizes it (the picture already did
  the work);
- a list that names every case when the first few already make the point;
- a caveat or reassurance that repeats one already given a sentence or a paragraph before;
- a section's opening or closing paragraph that only says what the section says (a preview or a recap).

## What is not overcompletion (his rulings)

- **A sentence that does a job the earlier one doesn't.** He kept "Unlimited freedom isn't realistic" against my call
  that it repeated: "it's talking about the specific freedoms that can be given to children as they grow up... It's
  required in that sentence to explain the rest of it." Before you call a sentence a repeat, name what it adds. A new
  claim, case, instruction, condition, example, safety limit, or a different situation is not a repeat.
- **Spelling out what a word means the first time it matters** ("A surprise isn't a secret, because at the end of a
  certain date it has to be told").
- **A script the reader says or follows.** Inside a hypnosis script or induction, repeating a suggestion can be the
  technique. Report only explanation around a script that repeats itself, not the script's own words.
- **A joke or aside** that doesn't explain the point again.

## How to read

1. Read your part's file (the path is in your task). Every paragraph starts with its block number in the guide, like
   `[118]`; headings have `#` marks. Read the context paragraphs before and after your part too, but report only on the
   part itself. The guide's headings, with block numbers, are in `OUTLINE.md` beside this brief, if you need to see where
   your part sits.
2. Read each paragraph against the paragraphs before it in its section and against its heading. Then read each
   paragraph's sentences against each other.
3. For each instance, find the smallest cut that removes the second explanation and loses nothing: usually a whole
   sentence or a whole paragraph; sometimes a clause. If the cut needs a word changed so the rest still reads right
   (a "So" or "This" left dangling, a sentence joined), give the block's full new text.
4. Be thorough: Joel expects the guide is full of it. But every instance must be something already explained. Don't
   report a sentence because it's a list or a last line if it says something new.
5. Don't judge whether a passage sounds AI or human, and don't guess whose words they are. Only overcompletion.

## What to write

Write one JSON file at the path in your task, and no other file. Don't change any other file. The file is:

```json
{"part": <your part number>, "candidates": [
  {"block": 61,
   "cut": "<the exact text to remove, copied character for character from the block (curly quotes, dashes and all), so a script can find it: a whole paragraph, one or more whole sentences, or a clause>",
   "join": "<if the cut leaves the block needing a small change to read right, the block's full new text after the cut; otherwise an empty string>",
   "kind": "<one of: says-again, other-side, every-case, sums-up, aftercare, list, caveat-again, preview-recap>",
   "already_said": "<the block number(s) and the exact words there that already say it>",
   "adds": "<what, if anything, the cut text adds that isn't already said; 'nothing' if nothing>",
   "loses": "<what the guide would lose if it's cut: 'nothing', or name it>",
   "strength": "<clear or borderline>"}
], "notes": "<anything else worth knowing, in a sentence or two>"}
```

Then reply with one line: how many candidates, and how many of them are clear.
