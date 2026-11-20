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

2. **Keep the meaning.** A new heading says the same thing the author's heading said: not narrower, broader or
   different. Keep qualifiers that carry meaning ("Bad at Sports" is not "Bad"). Keep the word a reader would look for
   ("Back Pain", not "Pain").

3. **Name what the reader came for,** in the words they'd use: their situation, their question, or what the section
   gives them.
   - A section about a situation or a sign ("is this happening to me?"): a short question. "Can't Sleep After Practice?",
     "Is Anger a Warning?", "Stuck?"
   - A section that gives a practice: an imperative or a short noun phrase. "End the Session Gently", "Evening Review".
   - A section that makes one point: the point as a short statement. "Rest Is Part of Training".

4. **Positive and direct.** Say what to do or what it gives rather than what to stop ("Ask for What You Need", not
   "Stop Hinting"; "Rest for the Fun of It", not "Rest for No Reason"). Speak to the reader as "you" where it's natural
   ("Before You Quit").

5. **Don't point to the wrong situation.** Avoid a word that could send a reader somewhere else or alarm them: "ends"
   can read as a death; a normal experience shouldn't be named as a warning sign.

6. **The author's voice.** Keep the author's catchy coinages and turns of phrase where they fit; short parallel
   phrasing is welcome ("Lend, Don't Lose"). Don't add claims the section doesn't make.

7. **Case.** Title Case for a new heading; where the sibling headings under one parent are in sentence case, match them.

8. **Two things, two headings.** If a section holds two different things, so that one heading can only name one of
   them, say so and propose a second heading for the second part instead of a heading that covers half.

9. **After renaming,** read the sentence before the heading (if it runs on into it) and the first sentence after it,
   and fix any that leaned on the old heading's words. Text that names the section by its old heading gets the new
   name, and a link to the section (`tools/humanization/section_links.py`).

## Where all three writers still missed his pick

Each of these got "different" for all three writers. What each seems to show is my reading of his pick; he was asked
why on the inner child questions page (2026-11-20), and his answer replaces the reading here.

- **The reader's own words, in quotes.** The section answers something readers say to themselves; his heading is what
  they say: "“No. I Hate Myself.”" The writers named the advice instead ("The Part That Came Here").
- **The situation the reader arrives with, not the section's advice.** "Attacked by a Demon?" where all three wrote
  "Prepare for Altered States"; "If They Can't Hear You" where they wrote "Others Have Hooks Too".
- **The specific payoff, not a general one.** "Spirit Attacks Teach Love", not "Gain from Spiritual Attack".
- **A part's heading names its main subject.** "Altered States", where all three added a smaller second subject with
  "&" ("Altered States & Intensives").
