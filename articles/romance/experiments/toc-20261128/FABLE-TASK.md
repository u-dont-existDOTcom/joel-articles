# Naming the romance article's headings

You're naming the headings of Joel's long Substack article, "Romance Advice I Wish My Parents Taught Me", for the
post's narrow contents sidebar. Work in this folder:
`/home/claude/joel-articles/articles/romance/experiments/toc-20261128/`.

Read, and use:

- `/home/claude/joel-articles/tools/humanization/headings_brief.md`: the rules. Follow every one of them, and read its
  last section (where earlier writers missed his picks) before you start.
- `ARTICLE-SECTIONS.md` in this folder: the article, section by section, each with its id, level and heading, then its
  own text. Read all of it, in parts if you need to.
- `CONTENTS-NOW.json` in this folder: the 71 headings the sidebar lists (h1 to h4), with their ids, levels and words.
- To measure a heading: `python3 /home/claude/joel-articles/tools/humanization/toc_sidebar.py --text "..." --level N`
  (fits, tight or cut). For title case: `python3 /home/claude/joel-articles/tools/humanization/heading_case.py --help`.

Don't open other files or folders (no situations, answer keys or readers' results), and don't use git.

Two of his headings are calls to action, not sections: S001 "Interactive guide-based convo here." (a link to an AI
chat about the article) and S002 "Try my Couples card game app based on the guide! (good for singles also)" (a link to
his card game), with the article's opening text under S002. Name them as headings like the others only if they should
stay headings; say in your notes what you'd do with them.

Keep every section's level and place: you're naming, not moving. Write two files in this folder:

1. `PROPOSAL-FABLE.json`: a list with one entry per heading of `CONTENTS-NOW.json`, in its order:
   `{"id": "S001", "level": 1, "heading": "<your heading>", "was": "<his heading>", "kind": "kept" or "renamed",
   "why": "<one short line, for a renamed heading>"}`. Every heading you give must fit its level (measure it).
2. `PROPOSAL-FABLE-NOTES.md`: what renaming can't fix and he should decide: a heading that is a note to the reader
   rather than a section, a parent with no text of its own whose name repeats another, a section at the wrong level or
   under the wrong parent, two things under one heading, a heading level skipped (an h3 straight under an h1). One
   numbered item each, with the ids, what you'd suggest and why. Nothing in the notes is done.

Reply in two lines: how many headings you renamed, and how many notes you wrote.
