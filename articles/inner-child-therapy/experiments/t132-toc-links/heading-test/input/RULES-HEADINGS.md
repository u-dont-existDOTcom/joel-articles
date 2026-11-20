# How to name a guide's headings for a narrow contents sidebar

For any long guide or article whose headings readers use to find their way. On Substack the contents sidebar lists
levels 1 to 4 on one line each and cuts a heading that is too wide with "…". These rules decide each heading's words;
where sections go is a separate step.

1. **Fit.** Every heading must fit its level's room. Measure it (`python3 toc_sidebar.py --text "..." --level N`
   prints fits, tight or cut). If the author's heading already fits and does its job, keep it as it is.

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
   name, and a link to the section.
