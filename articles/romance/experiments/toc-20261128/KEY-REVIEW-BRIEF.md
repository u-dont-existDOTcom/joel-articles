# Checking the answer key of a table-of-contents test

A table-of-contents test of a long online article (Joel's "Romance Advice I Wish My Parents Taught Me", about 21,000
words) uses situations, each a reader looking for one thing, and an answer key saying which sections answer each one.
Another agent wrote both from the article's text with its headings taken out. Your job is to make the key right.

Read these files in this folder, and no others:

- `TEXT-NO-HEADINGS.md`: the whole article, headings taken out, each section starting with its id in brackets (`[S001]`).
- `SITUATIONS.md`: the numbered situations.
- `EXPECTED.json`: the key, `{"situations": {"1": {"right": [...], "also": [...]}}}`.

For every situation:

1. Check that each `right` section really answers it best, and each `also` section answers part of it. Move or drop
   any that don't.
2. Search the whole text for sections that answer it and the key missed: a section near the end, a short section that
   says it in one paragraph. Add them, to `right` when they answer it as well as the best one does.

Write `EXPECTED-REVIEWED.json` in this folder, in the same form as `EXPECTED.json`, with `"about"` saying it was
reviewed against the full text, and a `"changes"` list: one line per situation you changed, saying what and why
("7: added S041 to right, its second paragraph answers it directly"). Then reply with one line: how many situations
you changed.
