# Task: the same small questions about each section (run 2)

FRAME.json says what each part (level-1 heading) and each role of a long guide is for, in general terms. TOC.md is the
guide's whole table of contents, with ids. Your batch file holds some of its sections, each with its id, level, heading
and full text.

Answer the questions below about every section in your batch, one section at a time. Judge each section by its own text
and what it does for a reader. Where it sits now is not evidence of where it belongs: a section can belong to a role or
part far from where it is. Don't think about the outline as a whole; another step puts the answers together.

For each section:
- "reader_question": the question, objection or curiosity a reader brings that this section answers, in one line.
- "kind": one of "concept", "practice", "problem", "story", "safety", "special-situation", "relationships", "closing",
  "grouping" ("grouping" is a heading with no text of its own).
- "role": the id of the role in FRAME.json whose work, as FRAME.json defines it, this section mostly describes, teaches or
  practices, or "none".
- "role_confidence": "high", "medium" or "low".
- "part": the id of the part in FRAME.json whose job this section serves best.
- "part_confidence": "high", "medium" or "low".
- "sits_under": the id of the one section anywhere in TOC.md that a reader scanning the contents would expect this
  section to sit directly under (the heading whose question it most directly carries on, illustrates or narrows), or
  "none" for a top-level part.
- "sits_under_confidence": "high", "medium" or "low".

Write one JSON object to the output file you were given: {"cards": [{"id": "N0xx", ...}]} with every section in your
batch, in order. Check that it parses and that every id in your batch is there.
