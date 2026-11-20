# Task: describe how a long guide is built (no changes)

ARTICLE-BY-SECTION.md is a long guide, section by section: each section has an id (N001 to N148), its heading level
(# for level 1, ## for level 2, and so on) and its text. TOC.md lists the same headings as a table of contents.

Read the whole guide, then describe its framework. Don't propose any moves or new headings; another step uses what you
write to decide where sections belong.

Write one JSON object to the output file you were given:

{"parts": [{"id": "N001", "heading": "the heading as written", "job": "one line: what this part does for the reader"}],
 "roles": [{"id": "N0xx", "name": "the role's name in the guide", "work": "one or two lines: the work this role does, in the guide's own terms"}],
 "notes": "at most one paragraph: anything else about how the guide is built that would help decide where a section belongs"}

- "parts": every level-1 heading, in order.
- "roles": if the guide is built around named roles, figures or parts of the self that the reader develops (or tools,
  stages or steps), list each one that has a heading of its own, with the id of the section that introduces it. Use the
  guide's own words for what each does. If it has none, give an empty list.

Check that the JSON parses before you finish.
