# Writing situations for a table-of-contents test

You're helping test the table of contents of a long online guide on Substack, "Inner Signal Guide to Self-Hypnosis
(& APP), including Reparenting, Conscious-Subconscious Spiritual Communion", by Joel (about 29,500 words). Readers
will later see only the guide's contents and say where they'd look for each situation you write; how often they land
on the right section tells us which headings work.

You get the guide's text with every heading taken out: `TEXT-NO-HEADINGS.md`. Each section starts with its id in
brackets, `[S001]`, and some sections have no text of their own (their id is followed by "(no text of its own)").
Don't look for the headings anywhere else, and don't open any other file in this folder or the repository.

Write 64 situations. Each is a real person, in a real moment, looking for one thing this guide gives them:

- Second person, one or two sentences, in the words that person would use, not the guide's own terms. Someone who has
  never read the guide doesn't know its names for things ("guards", "the inner adult's three jobs", "de-hypnosis",
  "capacity before content"); write what they'd feel, want or ask instead ("a part of you that gets defensive
  whenever...").
- One need each, specific enough that one or two sections answer it best. No situation that the whole guide answers.
- Spread them over the whole guide, in proportion: the practical steps (starting out, the daily practice, inductions,
  coming back), the inner child work, the warnings and limits, the troubleshooting, the spiritual and altered-state
  parts, the app, and the appendices all get some. Use sections near the end as much as near the start.
- Include about eight situations someone would bring when something has gone wrong or feels off, and about six from
  someone deciding whether this guide is for them at all.

For each situation, give its answer key: `right`, the one section id that answers it best (two only if they answer it
equally well), and `also`, any sections that answer part of it (up to four). Read the text closely enough to be sure:
a wrong key spoils the test.

Write two files in this folder and nothing else:

1. `SITUATIONS.md`: `# Situations`, a blank line, then the numbered situations, one per line (`1. You ...`).
2. `EXPECTED.json`: `{"about": "<one line on how you wrote the key>", "situations": {"1": {"right": ["S0xx"],
   "also": ["S0yy"]}, ...}}`, with every situation number as a string key.

Then reply with two lines only: how many situations you wrote, and any section you found hard to key.
