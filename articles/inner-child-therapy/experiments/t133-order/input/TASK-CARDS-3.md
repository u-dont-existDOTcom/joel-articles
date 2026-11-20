# Task: file each section under a heading (a blind card sort)

FRAME.json says what each part and each role of a long guide is for, in general terms. HEADINGS-FLAT.md lists every
heading in the guide, alphabetically, with no levels and no order. Your batch file holds some of the guide's sections,
shuffled: their order there means nothing.

For each section in your batch, decide which heading in HEADINGS-FLAT.md a reader would expect to find it filed directly
under: the heading whose question it most directly carries on, illustrates, narrows or is a case of. Use what the
section says and FRAME.json; there is no current place to keep. A section that is itself one of the guide's top-level
parts (FRAME.json "parts") is filed under "none".

For each section:
- "sits_under": the id of that heading, or "none".
- "sits_under_confidence": "high", "medium" or "low".
- "role": the id of the role in FRAME.json whose work, as FRAME.json defines it, this section mostly is, or "none".
- "role_confidence": "high", "medium" or "low".

Write one JSON object to the output file you were given: {"cards": [{"id": "N0xx", "sits_under": "...",
"sits_under_confidence": "...", "role": "...", "role_confidence": "..."}]} with every section in your batch. Check that it
parses and that every id in your batch is there.
