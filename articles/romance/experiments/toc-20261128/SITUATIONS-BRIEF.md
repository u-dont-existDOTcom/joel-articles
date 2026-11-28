# Writing situations for a table-of-contents test

You're helping test the table of contents of a long online article on Substack, "Romance Advice I Wish My Parents
Taught Me", by Joel (about 21,000 words). Readers will later see only the article's contents and say where they'd
look for each situation you write; how often they land on the right section tells us which headings work.

You get the article's text with every heading taken out: `TEXT-NO-HEADINGS.md`. Each section starts with its id in
brackets, `[S001]`, and some sections have no text of their own (their id is followed by "(no text of its own)").
Don't look for the headings anywhere else, and don't open any other file in this folder or the repository.

Write 44 situations. Each is a real person, in a real moment, looking for one thing this article gives them:

- Second person, one or two sentences, in the words that person would use, not the article's own terms. Someone who
  hasn't read the article doesn't know its names for things ("the window of clarity", "anti-PTSD", "muses and
  directors", "de-ontologizing", "two pillars"); write what they'd feel, want or ask instead ("you just met someone
  and can't see their faults yet...").
- One need each, specific enough that one or two sections answer it best. No situation that the whole article answers.
- Spread them over the whole article, in proportion: what love is, sex and talking about it, casual sex and
  situationships, whether to be in a relationship at all, finding someone, the start of a relationship, idealizing,
  pace, the hard middle of a relationship, attraction and polarity, twin flames, community, commitment and jealousy,
  psychedelics, an existing relationship in trouble, children, endings and after. Use sections near the end as much as
  near the start.
- Include about six situations someone would bring when something has gone wrong in a relationship, and about four
  from someone deciding whether this article is for them at all.

For each situation, give its answer key: `right`, the one section id that answers it best (two only if they answer it
equally well), and `also`, any sections that answer part of it (up to four). Read the text closely enough to be sure:
a wrong key spoils the test.

Write two files in this folder and nothing else:

1. `SITUATIONS.md`: `# Situations`, a blank line, then the numbered situations, one per line (`1. You ...`).
2. `EXPECTED.json`: `{"about": "<one line on how you wrote the key>", "situations": {"1": {"right": ["S0xx"],
   "also": ["S0yy"]}, ...}}`, with every situation number as a string key.

Then reply with two lines only: how many situations you wrote, and any section you found hard to key.
