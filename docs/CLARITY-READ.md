# The clarity read: what passes Pangram but is hard to understand

Two parts, run together: part 1, the passages a reader has to reread or won't get; part 2, the reader's edit, what a reader
has to work through even where every sentence is clear.

**ACTIVE, standard for every article (Joel, 2026-10-23 16:55 UTC):** "let's make sure this kind of check is standard for
articles as we write them and as we finalize before publishing in future, i thought it already was".

It wasn't. Two reads came close and neither is this one:
- the section cold read (`tools/humanization/reviewer/sense_section.txt`) reads text a worker drafted, a section at a time,
  for where the sense breaks, and lets a passage stand that a reader gets on a second look ("a reader who pauses and then
  gets it isn't lost");
- the reader-question audit (`docs/READER-QUESTION-AUDIT.md`) is optional, offered, and looks for the questions an article
  leaves open, not for passages that are hard to follow.
Nothing read a whole article, Joel's own words included, for what a smart general reader would have to reread. The first
whole-article clarity read was Nibbāna's, after his question of 2026-10-23 14:14 UTC ("is there any other stuff in the
nibbana guide that's hard to understand but still passing pangram?"): three fresh readers found 29 passages, 12 of them
hard enough that most readers wouldn't get them (`articles/nibbana/humanize/fix-20261023/clarity/CLARITY.md`).

## Part 1: what a reader has to reread

### When

1. **As an article is written:** once a full draft of a new article, or a long new section, is complete, before its
   whole-article Pangram check. The section cold read still runs on each drafted section as it is written; this read comes
   once the whole thing exists, because what a reader needs explained depends on what came before.
2. **Before publishing:** on the final candidate, once every other change is in, and before the final whole-article
   Pangram check, so that the passages it changes are read in place by that check.
3. **After a large batch of changes to a published article** (a humanization pass, a restructure), at the next stable
   point.

A short piece, a typo fix or a one-paragraph change doesn't need it.

### How

1. `python3 tools/humanization/clarity_read.py make ARTICLE DIR --parts 3 --about "..." [--question "..."]` writes the
   reading text, the parts (split at headings, about 30,000 characters each) and a brief for each part. The brief carries
   Joel's own fixes as the examples of what counts (`tools/humanization/clarity_examples.json`; add one each time he fixes a
   passage for clarity, with his words).
2. Give each `BRIEF-k.txt` to a fresh reader: a new agent that has seen nothing else (Sonnet is enough; Opus for an article
   whose argument is technical). Each writes `READER-k.md`: each passage, what's hard, a score (3: most readers wouldn't get
   it; 2: most would have to reread; 1: a small snag) and a plainer version.
3. `clarity_read.py collect DIR` puts them in `ITEMS.json`, each found in the article (or marked not found).
4. **Check every item against the whole article yourself**, since each reader saw only its part. An item explained
   elsewhere gets `"status": "drop"` and a note saying where; a small one `"minor"`; `"my_score"` overrides a reader's
   score; `"check"` names any step of a plain version that guesses at his reasoning. In Nibbāna's read, 7 of 36 flags were
   things another part explained. For a term a reader says is never defined, search the whole article for its first
   mention: the definition belongs there, and a later one becomes a reference (gate E243, "saṃsāra"); and check each plain
   version for a definition it adds.
5. **He decides on one review page, not on lists** (Joel, 2026-10-25 14:40 UTC, after four lists: "you're giving me half
   suggestion that are out of context. why don't you give me the full HTML guide with highlighting ... and then my comment
   box on your suggestion with approve reject reivse buttons"; gate E265). A lane script gathers every checked item of the
   check's parts into `REVIEW.json`, each with its exact change as (old words, new words) in its paragraph, and
   `tools/humanization/suggestion_review.py page REVIEW.json REVIEW.html` makes the page: the whole article, each
   suggestion highlighted in its type's colour, its card under the paragraph (the paragraph as it would read, why, what
   stays, my advice, Approve / Reject / Revise and a comment box). The ones I'd leave are on it too, hidden until he asks.
   Run `tools/humanization/suggestion_review_browser_test.py REVIEW.html`, publish the page as an artifact with
   `{"db": {}, "downloads": true}`, and read his answers from its store (`ArtifactData`, collection `decisions`) or from
   the JSON he sends. The hypnosis guide's is `articles/inner-signal/humanize/fix-20261025/review/build_review.py`.
   (`clarity_read.py page` still writes a list, for a record or a short check.)

For all four parts (2026-10-25, the hypnosis guide, 29,500 words, 36 readers' reports):
- **A reader that runs out of output gets its part in two halves**, with a brief for each (`BRIEF-k.txt` for the next
  free k, saying "part 1 (its first half) of 6"), never a second try at the same size (gate E262).
- **The same cut flagged twice is listed once.** Readers overlap, the repeats readers most (each reads the whole article):
  48 of the guide's 295 items were the same words twice or on two of the four lists. Give the second one `"status":
  "dup"` and a note saying where it is offered ("On the caveats page as 17.8."); `clarity_read.numbers(items)` gives each
  offered item its number on its page. A pure repeat goes on the repeats list; a heading, move or label on the reader's
  edit; a warning or qualifier on the caveats list. The guide's record of my check is a script with every item's status,
  pick and note (`articles/inner-signal/humanize/fix-20261025/my_checks.py`), so the pages can be made again.
- **Inner child and hypnosis writing is checked against the InnerSignal protocol**, loaded in the main thread: a line
  that states one of its rules in his words (a stop rule, consent, an image isn't a memory, the first thing noticed isn't
  truer, spirituality is optional, care in altered states) stays, with the reason in the note (gate, the 2026-10-25
  section).
- **A cut made to pass Pangram leaves words that point at it.** Look for "the first example", "above", "below" and the
  like whose target an approved cut took out (gate E263).
6. Put his answers in word for word (his rewrites, and the plain versions he passes), with every link, italic and bold back
   on the same words, and each changed passage read in place in the next whole-article Pangram check with a part forecast
   (`tools/humanization/part_forecast.py`; gate E238).

**What doesn't count, and how a plain version is written** (gate E264; Joel, 14:40: ""do that" is clearly referring to
"remove anything from the laws of nature" directly before it ... and it's actually harder to read now with these 2
parentheticals"). A "this", "that", "it" or "do that" whose meaning is in the words right before it is not a stop; the
reader reads the sentence before a passage before flagging it. A plain version replaces the words that stop a reader, as
his own fixes do, and adds a bracket only for a term a reader can't know, at most one per passage. Both are in the brief,
and his fix is its last example. My check holds every item to the same: on the hypnosis guide's second reread I'd leave
32 of 80, and most of the 47 I offer are a smaller change than the reader's.

### What the plain versions are for

A reader's plain version says what a reader needs; it is rarely the text that goes in. Of Nibbāna's 28 plain versions that
he checked, he called 13 AI and rewrote them (and one more without a verdict), and passed 14 (3 of them as "possibly
human"). His rewrites passed. The plain versions that read AI were neutral and complete: every step explained, every
conclusion stated. His kept what they explained and changed how it was said (the gate's E241): a conversational register
("it's pretty clear that", "that's a relief", "loosened up" for "dissolved"), a judgment word ("tellingly", "more
obviously"), attribution where the plain version asserted ("referred to as"), a concrete or playful image ("Suppose light
buys a mirror from the local mirror shop"), more precision (an exception, a cause, a fact), an ending that stops where
the point lands, with no summing-up line ("Put together, that says ...", "That's why, in this article, ..."), and one
personal reference (his dad's favorite oxymoron, "military intelligence"). These are things the words do, not him
putting himself in (he asked, 2026-10-23 18:13 UTC: "how does "tellingly" or "it's pretty clear that" put "me " in the
explanation?"; gate E247). So the brief asks for the smallest change to his own words, and the list goes to him
expecting his rewrites, not as text to install.

## Part 2: the reader's edit

**ACTIVE, part of the same standard (Joel, 2026-10-23 18:13 UTC):** "the clarity check for articles should also include the
readability check from GPT that i started doing in the inner child article."

Part 1 finds the passages a reader has to reread. The reader's edit finds what an article makes a reader work through even
when each sentence is clear. It is GPT's proposal for the Inner Child guide (its reply of 2026-10-23 11:41 UTC,
`articles/inner-child-therapy/experiments/t100-answers/GPT-READERS-EDIT-20261023.md`): keep the depth, but stop making every
reader process every complication the moment an idea comes up. Its questions:

1. **How many decisions does one passage ask for?** A main path with its alternatives and troubleshooting mixed in makes a
   simple invitation feel like something to troubleshoot before starting. The main invitation comes first; an
   alternative for one difficulty goes in a short part beside it, with a label that tells the reader it's for them.
2. **Has a second subject got its own space?** Where a section turns to a different reading task, try a subheading there.
   Nothing has to be cut to try it.
3. **What is each warning's job?** GPT's test: "Does this change what the reader should do here, or is it explaining why
   the instruction has qualifications?" A safeguard that changes what the reader does stays next to the step it belongs
   to; the reasons behind it can go to a note. A compassionate permission ("You don't have to feel warmth today") belongs
   to the invitation, and isn't clutter; saying again and again that something needn't be perfect can become one more
   thing to think about.
4. **Can this paragraph be ordinary?** Not every transition needs a joke, every distinction a metaphor, or every paragraph a
   memorable last line. His own humor and stories stay; connecting material that only makes the prose sound casual gets
   looked at. A repeat can deepen a scene; re-explaining its conditions has to bring a new distinction.
5. **What would an attentive reader still genuinely need here?** (GPT's words.) Sometimes a missing mechanism or a concrete
   example; sometimes nothing, and the last reassurance or qualification adds nothing new. Different audiences (the
   background, the instructions, the exercises) can be kept apart.

### When

With part 1, at the same three times. The proposals go to him as a list to pick from, and nothing goes in without his pick.
The Inner Child guide started with one test section (Borrow One Competency at a Time, his 91.1), because the method was
new; after it he chose to have the next sections proposed the same way (91.5 A).

### How

1. `python3 tools/humanization/clarity_read.py make ARTICLE DIR --kind edit --parts 6 --max-items 4 --about "..."` writes
   the same reading text, in parts of about 15,000 characters, and a reader's-edit brief for each part, with GPT's
   questions and his answers so far as the examples (`tools/humanization/readers_edit_examples.json`; add one each time he
   answers a proposal). Keep the parts small and the brief's "work quickly" line: on 2026-10-23 three Sonnet readers given
   a third of Nibbāna each spent all 64,000 tokens of their output on thinking, three times over, and wrote nothing.
2. Give each `BRIEF-k.txt` to a fresh reader. Each writes `READER-k.md`: each proposal a move (paragraphs moved, a heading
   or a label added, a repeat cut, a warning's reasons moved to a note, a last line that adds nothing cut), with the
   section, the passage, the exact change, the reader's problem it solves and what stays as it is. The brief allows no new
   jokes, examples, metaphors or teaching, and no new wording beyond a heading, a label or the few words a move needs
   (the test's "For warmth,"). A cut must quote both places, or say what the reader already has.
3. `clarity_read.py collect DIR` puts them in `ITEMS.json`, each found in the article or marked not found.
4. **Check each proposal yourself against the whole article and his earlier answers:** a cut that takes out a point he
   kept, or a safeguard that changes what a reader does, is dropped, or goes to him with his earlier words (E242 (Inner
   Child)); a move gets each paragraph's new neighbours read for a repeat (E241 (Inner Child)). Give each proposal
   `"my_pick"` ("A" to put it in, "B" to leave it) and a `"note"` with the reason.
5. `clarity_read.py page DIR --out READERS-EDIT.md` writes the list for him, numbered in the article's order, each with its
   options and my pick. Send it to him as a link he can click.
6. Put in what he picks word for word. Pangram doesn't decide whether a paragraph belongs (GPT: "it should not decide
   whether a paragraph belongs"): a moved paragraph keeps its own checks, changed words get new ones, and each move's
   stretch is read in place in the next whole-article check with a part forecast.

### His answers so far

The Inner Child guide, question 91 of its questions page (his message of 2026-10-23 14:05 UTC, turn 101):

- **91.1 B:** the test section with its opening and one borrowing for each job first, then the troubleshooting under its own
  heading, "If the Love Isn't Coming Yet", in the order it had, and a near-repeat cut ("Most of us wouldn't open up to
  somebody who'd only just stopped being mean, or let them take care of us.").
- **91.2 A:** a heading, "Instead of Blame", where the second subject starts ("Your little one might not be the only one
  getting accused.").
- **91.3 A:** no label for a one-paragraph fallback whose first line already says what it's for ("And what if all that
  writing leaves you more confused than when you started?").
- **91.4 A:** the false-photo study stays where it is, three short sentences in his words: it's the concrete case that
  makes the warning land.
- **91.5 A:** after the test, the next sections are proposed the same way, as moves, labels and real repeats; he picks;
  they go in word for word, and only what changed gets checked.

GPT's review of the test (13:55 UTC, `articles/inner-child-therapy/experiments/t101-answers/GPT-REVIEW-20261023-1355.md`):
nothing was cut in the first test, and that was right for a test but isn't the rule; the next step is "small, justified
reductions in commentary", with his approval for changes to protected wording (question 94 there, open).

Nibbāna's reader's edit (question N4 of its questions page, his answer of 2026-10-23 20:35 UTC): A on 17 of 18 proposals,
including four where my pick had been B (gate E250); `tools/humanization/readers_edit_examples.json` has those four and his
one B.

## Part 3: safety lines and caveats a reader doesn't need

**ACTIVE, part of the same standard (Joel, 2026-10-23 22:29 UTC):** "did we already look at whether there's too much
safety language in this article? just cut out a ton of obnoxious safety language and caveats from inner child article.
same question for community and hypnosis articles. noticing more and more how bad my articles read."

We hadn't, as its own check: part 2's third question asks what each warning's job is, but it proposes moves, not cuts, and
part 1 looks at understanding. The Inner Child lane did the first pass on its own (its turn 102, his 95.6 B: "all the extra
extra ridiculous safety language which gets repeated everywhere. want to look at the books we have as examples, especially
ones made for public audiences"). This part makes it standard.

- **The test** (GPT's, which he uses): does the line change what the reader should do right here, or does it only explain
  why an instruction has qualifications, reassure, or protect the writer? Public books put general safety in one place
  (a note on pace and stopping, a section on getting help) and keep, inside an exercise, only the cautions that change
  what you do there, once.
- **What counts:** a warning said again; a blanket add-on that changes nothing where it's tacked on; a warning against a
  step nobody suggested; a reassurance after the point is made; a takeback, or an answer to an objection nobody raised;
  a hedge that weakens a claim for no reader benefit; a disclaimer that protects the writer.
- **What stays:** a caution that changes what the reader does at that step; a section whose subject is safety or crisis;
  a marker of whose claim it is when an article reports texts or science; a hedge that is the claim itself (he really
  isn't sure, or he allows an exception); his jokes and stories; and a qualifier that tells the reader something they'd
  otherwise lack: where a rule stops working, a softening that adds a point, context that keeps a group from being
  demonized, the other side of something he praises, an objection a reader would raise right there (his N6 and 64
  answers, 2026-10-24; E257). A line that only comments on the text or on his own caution goes even when it's his joke
  or his lead-in ("As you can see this is going to be a little abstract, but", "jokingly", "That's my own CYA showing.").
- **How:** `tools/humanization/clarity_read.py make ARTICLE DIR --kind caveats --parts N` (examples:
  `tools/humanization/caveat_examples.json`, from the Inner Child lane's cuts), a fresh reader per part, `collect`, then
  every item checked against the whole article and his earlier answers: "my_pick", "note", "whose" (his published words,
  his rewrite of a given message, or a batch's), and "status": "drop" for a line that changes what a reader does or whose
  cut breaks the text. `page` shows each cut struck through in its paragraph, the paragraph after it as it will read
  (`cut_text`: the capital back, no dash or comma left hanging; a word the cut makes necessary goes in the After itself,
  never in a note, E258), why, and what a reader loses. Every cut that goes in is checked in Pangram in place (a cut once made a paragraph read AI: E248 (Inner
  Child)).
- **When:** with parts 1 and 2. First run: Nibbāna (`articles/nibbana/humanize/fix-20261023/caveats/`) and the community
  article (`articles/intentional-communities/candidate/joel-20261023/caveats/`), 2026-10-23.

## Part 4: what the article says more than once

**ACTIVE (Joel, 2026-10-23 22:29 UTC):** "as much as possible we should be deduplicating because i feel the article is
really too redundant"; "everyone says my articles are too long (and hard to read because of the excessive redundancy and
details which are from the AI writing)."

A repeat can be pages apart, so each reader reads the whole article and owns one part's points: for each point made in its
part, it finds every other place that makes it again, says which place keeps it, and which words to cut elsewhere. Short
callbacks that build on an earlier point and pointers to other sections stay.

- **How:** `tools/humanization/clarity_read.py make ARTICLE DIR --kind repeats --parts N`, a fresh reader per part (each
  gets the whole article and its part), `collect`, every cut checked (the kept place really says it; the paragraph still
  reads), `page` (each cut struck through, with where the point is kept). Cuts go to Pangram in place. My pick on each
  (his 65, 2026-10-24; E260): a line that previews or announces what a later section tells is cut, even when it sets
  that section up; a definition or a thesis is kept where a reader who jumps in or stops there needs it.
- **First run:** the community article after its move into essay and manual
  (`articles/intentional-communities/candidate/joel-20261023/repeats/`), 2026-10-23. Of four Sonnet readers, each with
  the whole article (about 97,000 characters) and a quarter of it, one finished in 14 minutes; the other three spent their
  whole output thinking, three times in a row each, and wrote nothing (the same happened to a whole-section repeats check
  on 2026-10-17). They were stopped, their parts split in two (`resplit.py`: six readers, at most 6 items each), and the
  brief's "Work quickly" line now says not to compare every paragraph with every other. For a long article, give each
  reader about an eighth of it.
