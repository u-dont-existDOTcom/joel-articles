# Task: the same small questions about each section

FRAME.json describes how a long guide is built: its parts (level-1 headings) and the job each does, and its roles and
the work each does. TOC.md is its whole table of contents, with ids. Your batch file holds some of its sections, each
with its id, level, heading and full text.

Answer the questions below about every section in your batch, one section at a time. Judge each section by its own text
and what it does for a reader, not by where it sits now and not by words it happens to share with a heading. Don't think
about the outline as a whole; another step puts the answers together.

For each section:
- "reader_question": the question, objection or curiosity a reader brings that this section answers, in one line, in
  the reader's words.
- "kind": one of "concept", "practice", "problem", "story", "safety", "special-situation", "relationships", "closing",
  "grouping" ("grouping" is a heading with no text of its own).
- "role": the id of the role in FRAME.json whose work this section mostly describes, teaches or practices, or "none" when
  no one role's work is its subject.
- "role_confidence": "high" when the section is clearly that role's work, "medium" or "low" otherwise ("high" with
  "none" when clearly no role's).
- "part": the id of the part in FRAME.json whose job this section serves best.
- "part_confidence": "high", "medium" or "low".
- "continues": the id of a section this one only continues or illustrates (it makes little sense without it), or "none".
- "needs_first": the ids of up to three sections a reader must have read before this one makes sense, or [].

Write one JSON object to the output file you were given: {"cards": [{"id": "N0xx", "reader_question": "...", "kind": "...",
"role": "...", "role_confidence": "...", "part": "...", "part_confidence": "...", "continues": "...", "needs_first": []}]}
with every section in your batch, in order. Check that it parses and that every id in your batch is there.
