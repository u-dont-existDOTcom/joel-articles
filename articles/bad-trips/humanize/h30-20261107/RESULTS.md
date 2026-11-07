# Checks of 2026-11-07 (from 22:38 UTC): his round-23 answers, and his list moves carried

He sent his round-23 export at 22:38 UTC (`../../review/r23/ANSWERS-R23-20261107-2238.json`; his words in
`../../experiments/t25-answers/`). Each test below is on the Human first half of Psychological First Aid, then the
section's heading and its part, using Pangram's web app on his account through the Claude desktop app's browser pane.

## His answers

| card | what he sent | in the guide |
|---|---|---|
| TEACH-DONTS, No Rash Actions' don't list | his own version ("Until you have slept and eaten, maybe don't drive, travel, break up, make up, ... you can still change your mind the next day"), [Human, High](https://www.pangram.com/history/e1537940-bdb9-4b2e-9220-141df65fb47a) by his own check | **in**, as he sent it. In its place after the Human base, [his paragraph reads Human, High](https://www.pangram.com/history/f14f541b-8df3-4ad3-927a-ab79bce78b57) (its own 93-word window); the two AI windows there are the base's first sentence (Low) and the base's reminder read together with the bold lock line (Low) |
| TEACH-STEPS, Minimum Viable Integration | no version: "you want me to correct only that one line? ... why?" and "i also feel like this has been said at least twice already" | **cut** as the repeat he saw: step 1 is After the Storm's first paragraph and No Rash Actions' lock, steps 3 and 4 are the questions and the fruit of insight after it, step 2 is the questions' "what actually happened" and No Rash Actions' "Write it down" (`apply_r23.py`) |

The steps card covered only the list's first line. That was a bug in the card builder, not a choice: the four steps
are four page blocks, and `P()` took the first when given the section's id. `../../review/r23/build_r23.py` now refuses a
list's id unless the card names the item or takes them all (`PALL()`); the published page stays as he answered it.

What only step 2 said is the list of facts to write down (what you took, how much, the setting, what set it off, what
helped and what made it worse). My merge of it into the questions paragraph read AI (QF below), so it went out with
the section. It comes back where it reads Human; the reply of 2026-11-07 tells him so.

## His list moves carried by me

The moves, from his version: "maybe don't" for a flat don't; the list broken into sentences with their own verbs ("Think
twice before ..."); items made concrete, specific and a little funny ("giving away your BMW, buying a new BMW", "explained
the whole universe to your parents in 42 seconds"); and an ending that gives the reader slack ("you can still change your
mind the next day"). Each try first had a fresh reader's sense read and the linter.

| stretch | before | this try | reading |
|---|---|---|---|
| the questions paragraph with Minimum Viable Integration's facts merged in (QF) | | [82%](https://www.pangram.com/history/b9142e56-744b-4da7-a3f1-b64c48d7f117) | the merged paragraph AI, High |
| Dealing With Shadow Thoughts: during a trip (SH3) | [100%](https://www.pangram.com/history/d6661bf9-2bb8-4a7f-a6e5-f38fa4cdfbf1) | [99%](https://www.pangram.com/history/5e5902d7-c676-496c-bdaf-847b4a98df9b) | no gain |
| Abuse Memories: don't confront tonight (AB3) | 58% | [68%](https://www.pangram.com/history/39ebd4d5-0d14-47eb-8a81-947ebd5b8e48) | no gain |
| After the Storm: no "another ceremony" (AF3) | | not run | the ledger wants a tell panel after two AI reads on that stretch |

He was right that my tries didn't take the list apart. Each kept its list whole, in one sentence, with category words
for items ("abuse, betrayal, murder, past lives, hidden crimes or cosmic plots"; "what you took and how much, if you
know, where you were, what happened, what set it off, what helped and what made it worse"), and changed only the words
around it. His version keeps a list too, but a short one of plain verbs, then two more sentences built differently, every
item something a reader can picture. Lesson bad-trips-2026-11-07j (`../../../../docs/lessons/2026-11-07-2238-bad-trips.md`).
