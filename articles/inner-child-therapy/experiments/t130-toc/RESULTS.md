# The contents as Substack's sidebar shows it (2026-11-16, turn 130)

Joel, 2026-11-16 02:19 UTC, answering "Say go and I'll run the read here": "go... also, we should be optimizing substack
posts specifrically for their very narrow toc sidebar so we might need to rethink some headings (i hadn't thought about
that til just now)" ([his message and screenshots](../t130-answers/JOEL-20261116-0219.md)).

## What the sidebar does to the headings

Measured in the post's own contents menu on his laptop (the desktop app's browser, 02:30 UTC): each heading is one line
of 15px Inter, cut off with "…" where the room ends: 217px for an h1, 205 for an h2, 193 for an h3, 181 for an h4 (an h5
isn't listed). Brave on the same laptop showed about one character less (his screenshots). `tools/humanization/toc_sidebar.py`
gives the same widths as the browser on all 147 labels.

**Today 105 of the 147 listed headings are cut off** (40 fit, 2 only just). [LIVE-TOC.json](LIVE-TOC.json) is the
contents as it was live at 02:12 UTC.

## How it was read

The method of the bad trips run (`articles/bad-trips/humanize/h39-20261109/toc/`): fresh readers (Sonnet agents) saw only
the contents, each heading at its level with its word count, as the sidebar shows it, and 38 situations a reader comes
with ([SITUATIONS.md](SITUATIONS.md)). For each, they named the heading they'd open first, sure or a guess, and the next.
The sections that answer each situation ([EXPECTED.json](EXPECTED.json), by section id, so a renamed section still
counts) were written from the live text and committed before any new contents was drafted, and the readers never saw
them. [score_reads.py](score_reads.py) scores every read into [SCORES.json](SCORES.json) and [SUMMARY.json](SUMMARY.json).

The options, each read by fresh readers who saw only that one:

- **Yours as it is**, as the sidebar cuts it (two readers), and with whole headings (one reader), to see what the cut costs.
- **B, mine:** your order and levels kept, 105 headings renamed to fit, in your words where they would go
  ([PROPOSAL-B.json](PROPOSAL-B.json)).
- **B2:** B with three headings renamed after B's readers missed them ([PROPOSAL-B2.json](PROPOSAL-B2.json)): "When One
  Life Ends", "Ugly Thoughts Happen", "If They Can't Hear You".
- **C, GPT's:** GPT-6.1 Sol (Codex on your laptop, high effort) from the same brief ([DESIGN-BRIEF.md](gpt/DESIGN-BRIEF.md)),
  without the situations: your order kept, 106 renamed, one level changed ([PROPOSAL-C.json](PROPOSAL-C.json),
  [its notes](gpt/PROPOSAL-GPT-NOTES.md)).

## What they found

| Contents | Readers | First pick right (of 38) | Guesses (of 38) | Right by the 2nd pick |
|---|---|---|---|---|
| Yours, as the sidebar cuts it | 2 | 31, 32 | 26, 21 | 33, 34 |
| Yours, whole headings | 1 | 32 | 18 | 34 |
| B, mine | 2 | 34, 32 | 19, 20 | 35, 33 |
| B2, mine with three fixes | 2 | 32, 33 | 20, 18 | 34, 33 |
| C, GPT's | 2 | 31, 33 | 20, 24 | 31, 34 |

- **The cut-offs make readers unsure more than they send them wrong.** On your sidebar as it is, readers still picked the
  right section first about as often as with the whole headings (31 and 32 against 32), but called it a guess on 26 and
  21 of 38 situations, against 18. With the renamed headings, guesses fell to 18 to 20.
- **Where the renames changed the outcome:** "When It Feels Fake" (the adult voice feels fake: both readers of your
  sidebar went elsewhere; all four readers of B and B2 went right, sure), "Attacked by a Demon?" (the weight on the chest
  at night), "When You're the Danger" (getting a kick out of frightening people) and, in B2 only, "Ugly Thoughts Happen" (an ugly thought makes you feel like a bad person: every other
  reader, yours included, missed it; both B2 readers went there, sure). My "The Gap Between Lives" lost the breakup case
  that your "When One Life Has Ended..." had found; B2's "When One Life Ends" got it back.
- **GPT's headings were found about as often, with more guesses.** Its "Pl/ork With Your Little One" and "When Pl/ork Gets
  Difficult" puzzled both its readers (the word isn't explained in the sidebar), and its quote heading for "Notice the
  Part That Came Here", "“No. I Hate Myself.”", drew both readers of the "I don't believe you" case away from Love Before
  Trust. Seventeen of its headings I'd take over mine, and they're in my picks.
- **What no contents fixed:** the partner who gets upset when you bring up a hurt (34: readers went to Hearthwork or
  Opening Up, not Other Folks Also Have Hooks, renamed or not); and two of my situations: 23 (the 2 a.m. app read as the
  urge to escape, not dating) and 38 (worrying what people think: readers went to Belonging Bargains and Differentiation,
  which do speak to it; my expected list was too narrow). Those count the same against every option.

## My pick, and how sure I am

The options page shows every option as the sidebar would (your laptop's font and widths) and saves your pick per
heading: https://claude.ai/artifact/RjHcYbik7oU9VdHcru1tB6 (a view of [OPTIONS-PAGE.html](OPTIONS-PAGE.html), built by
[make_page.py](make_page.py) from [PAGE-OPTIONS.json](PAGE-OPTIONS.json); only the account that published it opens its store,
so its Copy my answers button carries your picks to any chat).


[PROPOSAL-PICK.json](PROPOSAL-PICK.json): B2, with GPT's heading where it read better (17 headings), and "Altered States"
for the part both versions renamed awkwardly. Your order and levels stay, except Notice the Part That Came Here, which
GPT's version moves up beside Your Body (it isn't about the body; readers of every version said so). 144 of 147 fit; the
three that don't are your "“And So That's the Way It Happened!”" (the phrase is the trick, so it stays whole), and two
that fit with less than two letters to spare.

**How sure:** fairly sure the renames help: every reader of the cut sidebar called out the cut-offs, and the renamed
contents made them sure about four or five more of the 38 situations. Not sure they change where readers land: the right first picks
differ by one or two, which is within the gap between two readers of the same contents.

**Limits:** the readers are AI models reading a contents, not people with a real problem; two readers per option; I wrote
the situations and the expected sections, and drafted B knowing them (GPT didn't see them); B2's three renames were made
after B's misses, so its score on those three is flattered.

## What the readers would move (not tested)

Most readers of every version said:

- "If You Want to Kill Yourself" should come first in Safety and Readiness. Every reader still found it first and sure
  where it is, so I'd leave your order.
- "Therapy Stirs Things Up" isn't about the body; "Betrayed by a Teacher" belongs beside Don't Buy an Outer Adult and Signs
  of Manipulation; "Invite Your Little One In" looks like practice; Conclusion and Appendix could be two parts.
- Lower-case headings ("If no answer comes", "What you mix", "AI therapy") look like a different writer's.

## Words in the text that name a heading

They change with the renames, once you've picked (the page lists them too). Two are already wrong in the live post:
Using Spiritual Attack's "as I explained before" points to the THH story in My Psychedelic Experiences, which comes
after it; For Some People's "in the 'Altered States Can Deepen Therapy or Escapism' section further on" points to the
section it sits in. And "Timing Is Individual" (in What to Do With a Peak) and "Your Loan is PRE-APPROVED!" (in the
conclusion and in Schema Therapy) are no longer headings.
