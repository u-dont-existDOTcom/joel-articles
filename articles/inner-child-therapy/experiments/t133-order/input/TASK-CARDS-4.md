# Task: file each section under a heading (a blind card sort, with the author's own view)

FRAME.json says what each part and each role of a long guide is for. Its "joel_view" is the author's own account of how
he sorts things into his roles, and where it speaks, it decides: love accepts (the Nurturer), protection blocks (the
Protector), the guide directs (the Guide). Shame and forgiveness need acceptance, so they are the Nurturer's work. A
catch-all part (like one about healing old patterns) is not the home for something that meets a primary obstacle. A
practice can be done by any role: it goes under a role only when that role must do it, and otherwise where the reader's
path would bring it up (the heading of the situation it helps with).

HEADINGS-FLAT.md lists every heading in the guide, alphabetically, with no levels and no order. Your batch file holds
some of the guide's sections, shuffled: their order there means nothing.

For each section in your batch, decide which heading in HEADINGS-FLAT.md the author would file it directly under, by his
view above: the heading whose role must do this work, or, when no role must, the heading of the situation in the
reader's path where it helps. A section that is itself one of the guide's top-level parts (FRAME.json "parts") is filed
under "none".

For each section:
- "sits_under": the id of that heading, or "none".
- "sits_under_confidence": "high", "medium" or "low".
- "role": the id of the role whose work it is by the author's view, or "none".
- "role_confidence": "high", "medium" or "low".

Write one JSON object to the output file you were given: {"cards": [{"id": "N0xx", "sits_under": "...",
"sits_under_confidence": "...", "role": "...", "role_confidence": "..."}]} with every section in your batch. Check that it
parses and that every id in your batch is there.
