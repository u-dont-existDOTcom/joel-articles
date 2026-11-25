# Headings brief: naming a guide's headings for a narrow contents sidebar

Give this brief, with the article (each section's id, level, heading and text) and `tools/humanization/toc_sidebar.py`,
to the writer of a contents' headings. Lesson inner-child-2026-11-20b. Joel, 2026-11-20 16:39 UTC: "also see if you can
make universal instructions that would have produced my heading picks here. or as close to them as possible. if unsure
why i picked something you can ask me."

How close it gets: in turn 132 three fresh writers that had never seen his picks named the inner child guide's 147
listed headings with rules 1 to 9 below. Against his picks, a blind reader found Fable's headings the same or close on
134 and different on 13; Sonnet's and GPT's 129 and 18 each (`articles/inner-child-therapy/experiments/t132-toc-links/RESULTS.md`).
That was one run per model, so the lead is small but real: give Fable this brief, and read its result against the
misses below before it goes to him.

1. **Fit.** Every heading must fit its level's room. Measure it (`python3 tools/humanization/toc_sidebar.py --text "..."
   --level N` prints fits, tight or cut). If the author's heading already fits and does its job, keep it as it is.

2. **Keep the meaning.** A new heading promises the same section the author's heading did: not narrower, broader or
   different. Keep qualifiers that carry meaning ("Bad at Sports" is not "Bad"). Keep the word a reader would look for
   ("Back Pain", not "Pain"). Same meaning is not the author's words reshuffled: rule 3 decides the words.

3. **Name what the reader came for,** in the words they'd use: the question, objection or curiosity they bring to the
   contents, which this section answers. Think like the reader scanning the sidebar, not like someone who has read the
   section: a heading that sums up the section, or makes sense only once you've read it, fails there (Joel, 2026-11-20
   21:49 UTC: "'the part that came here' does presage the content, but it's not what someone is looking for in the ToC,
   and that's the key we were trying to fix. so we are thinking like the reader [...] wondering what question or
   objection or curiosity we are answering for them"; on "Others Have Hooks Too": "good in context, but not in the ToC").
   - A section about a situation or a sign ("is this happening to me?"): a short question. "Can't Sleep After Practice?",
     "Is Anger a Warning?", "Stuck?"
   - A section that gives a practice: an imperative or a short noun phrase. "End the Session Gently", "Evening Review".
   - A section that makes one point: the point as a short statement. "Rest Is Part of Training".

4. **Positive and direct.** Say what to do or what it gives rather than what to stop ("Ask for What You Need", not
   "Stop Hinting"; "Rest for the Fun of It", not "Rest for No Reason"). Speak to the reader as "you" where it's natural
   ("Before You Quit").

5. **Don't point to the wrong situation.** Avoid a word that could send a reader somewhere else or alarm them: "ends"
   can read as a death; a normal experience shouldn't be named as a warning sign. A word that reads two ways alone in
   the sidebar gets the specific word ("Gain" reads as money or fame: "Spirit Attacks Teach Love"), and a word a reader
   can't parse alone gets spelled out ("Intensives": intensive what? "Meditating Intensely"). Name the section's main
   idea, not its most vivid example ("Attacked by a Demon?" named one example of a section whose point is to prepare).

6. **The author's voice.** Keep the author's catchy coinages and turns of phrase where they fit; short parallel
   phrasing is welcome ("Lend, Don't Lose"). Don't add claims the section doesn't make.

7. **Case: AP title case, every heading** (Joel, 2026-11-20 22:32 UTC: "there should be a rule that the headings follow").
   Capitalize every word except articles (a, an, the) and conjunctions and prepositions of three letters or fewer (and,
   but, for, if, or, so, as, at, by, in, of, on, to, up), which stay lower case unless first or last, or after a colon;
   "With", "From", "Into" are capitalized. "Earning Trust, Day to Day", "How to Let People In". A small word that belongs
   to a verb is capitalized ("Show Up Just for Joy", "Dip Your Toes In First"). `python3 tools/humanization/heading_case.py
   "..."` gives the case, and `--catalog SECTION-LINKS.json` lists every heading that doesn't follow it; it leaves "in",
   "on", "up", "off", "by", "so" and "yet" written with a capital for a reader to judge. A change of case doesn't change
   the section's link.

10. **Quote marks for words someone says or thinks, and for a word used as a word.** "Shame Says “Unlovable”" parses;
   "Shame Says Unlovable" doesn't (Joel, 2026-11-20 22:32 UTC: "if you just say "Shame says unlovable" it doesn't parse
   for humans at all"). What a person, a feeling or an inner voice says goes in quote marks, in a heading as in the text
   ("“No. I Hate Myself.”"), and so does a word being talked about rather than used. The Chicago Manual puts a word used
   as a word in italics or quote marks; a heading can't rely on italics in the sidebar, so it takes quote marks. In his
   text they are his straight quote marks (his typographic swap); in headings, as he wrote them.

8. **Two things, two headings.** If a section holds two different things, so that one heading can only name one of
   them, say so and propose a second heading for the second part instead of a heading that covers half. A part that
   covers two things a reader wouldn't guess go together names both, even when it's cut off in the sidebar ("Altered
   States & Meditating Intensely": readers looking for intense meditation wouldn't know it's under Altered States).

9. **After renaming,** read the sentence before the heading (if it runs on into it) and the first sentence after it,
   and fix any that leaned on the old heading's words. Text that names the section by its old heading gets the new
   name, and a link to the section (`tools/humanization/section_links.py`).

11. **Never say or ask the same thing twice in a row** (lesson bad-trips-2026-11-21a; Joel, 2026-11-21 13:04 UTC: "why
   would you put 2 serotonin syndrome headings in a row"). Read the contents as the sidebar lists it: a parent's own text
   doesn't show there, so a heading and the first heading under it sit on two lines in a row. The parent names the topic
   once, and each child names its own part of it: "Serotonin Syndrome (SS)?", then "How to Recognize It" and "What to Do
   Right Away", not "Is It Serotonin Toxicity?" under it. The same holds for any two headings in a row ("Who to Contact"
   under "When to Get Outside Help", not "Who to Contact, and When"). A child needn't repeat its parent's word ("What Else
   Helps" under "Active Seizure"), but it must still say what it holds without it: "Some Need More Caution" under the
   remedies said nothing of what needs it.

12. **Read each heading with the lines above and below it** (lesson toc-2026-11-25a; Joel, 2026-11-25 01:24 UTC:
   "sometimes the headings above or below could give context to this one we're choosing"). The sidebar never shows a
   heading alone, so a heading that reads two ways by itself can be the right one when a neighbour settles it. He took
   "De-Hypnosis: Wake Up" over "Wake Up Inside the Influence" because the next line, "Are You Being Influenced?", says
   what you wake up from ("now we don't think you're waking up from a dream"). So before changing a heading because a
   word in it is unclear alone (rule 5), or because a reader called it hard, read it in its place: if the line before
   or after supplies the missing word, the shorter heading can stay, and its fate names that neighbour. It holds the
   other way too: a heading that leans on a neighbour is read again whenever that neighbour is renamed, moved or
   dropped. Rule 11 is the mirror of this one.

## Before the contents goes to him

- Every reader of a contents writes its hardest headings into its read file ("HARD: line number | why"), and marks any
  heading that says or asks the same thing as the one before it or its parent.
- `python3 tools/humanization/toc_check.py CONTENTS.json --reads DIR --name NAME --fates FATES.json` lists every heading
  that shares a content word with its parent or the heading before it, and every heading the readers marked HARD, and
  fails until each has a fate: "changed: ..." or "kept: why it stays" (lesson bad-trips-2026-11-21b: both readers of round
  47's pick had said the two serotonin headings read as one, in the chat, and the page went out with them).
- A changed heading is read again by fresh readers before the page goes out (gate inner-child-2026-11-17a).
- A page that saves his picks declares its database before it goes out, sends what he saved in his browser when he
  opens it, and saves the headings themselves, not only which column he clicked (lesson bad-trips-2026-11-21c): the
  round-47 page didn't, so his "done" reached nothing that could be read.

## Where all three writers missed his pick, and why (his answers of 2026-11-20 21:49 UTC)

Each of these got "different" for all three writers in turn 132. He said why, and rules 3, 5 and 8 now say it. Before
asking him why he picked a heading, look up who wrote it: most of his picks came from earlier runs' lists (Opus, Fable,
GPT), whose notes may already say why (lesson inner-child-2026-11-20f).

- **"“No. I Hate Myself.”"** (Opus's and GPT's in turn 130; the writers wrote "The Part That Came Here"): the objection
  the reader brings, not a summary of the section (rule 3).
- **"If They Can't Hear You"** (they wrote "Others Have Hooks Too"): theirs was "good in context, but not in the ToC"
  (rule 3).
- **"Spirit Attacks Teach Love"** (his own; they wrote "Gain from Spiritual Attack"): "gain what like money or fame..."
  (rule 5).
- **"Prepare for Altered States Now"**: the writers were right here. His pick, "Attacked by a Demon?", named one example;
  "the main idea is you have to prepare for them even before you think you are ready for them since they can come
  without your request" (rule 5). He changed it in the post on 20 November.
- **"Altered States & Meditating Intensely"**: the writers were half right to name both ("& Intensives"), but
  "Intensives is hard to parse... intensive whats?" (rules 5 and 8). He kept it although the sidebar cuts it; the
  versions that fit drop "intense" ("Altered States & Meditation", which would also pull readers looking for the gentle
  meditation section) or change it ("& Retreats").
