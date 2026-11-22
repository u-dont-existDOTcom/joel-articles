# Task: file each section under a heading (a blind card sort, with the guide's own words and the author's view)

FRAME-5B.json says what the guide's parts and roles are for, in the guide's own words: its opening and its five stages
("overview"), and the text each part and each role has of its own ("own_text", empty where it has none). Read a part or
role with no text of its own by its name, the overview and the author's view; never by guessing what sections it holds.

Its "joel_view" is the author's own account of how he sorts things, and where it speaks, it decides: love accepts (the
Nurturer), protection blocks (the Protector), the guide directs (the Guide). Shame and forgiveness need acceptance, so
they are the Nurturer's work. The Nurturer gives the love of the nurturer (taking care of the little one, hugging them,
being with them, listening); divine love is beyond that, and it is what the Inner Guide can bring the little one to. A problem goes where the reader meets it. A practice can be done
by any role: it goes under a role only when that role must do it, and otherwise where the reader's path would bring it up
(the heading of the situation it helps with). The part about healing old patterns is for techniques that don't fit
cleanly into just one role, and it is not the home for something that meets a primary obstacle.

HEADINGS-FLAT.md lists every heading in the guide, alphabetically, with no levels and no order. Your batch file holds
some of the guide's sections, shuffled: their order there means nothing.

For each section in your batch, decide which heading in HEADINGS-FLAT.md the author would file it directly under, by the
guide's words and his view above: the heading whose role must do this work, or, when no role must, the heading of the
situation in the reader's path where it helps. A section may belong directly under another section's heading. A section
that is itself one of the guide's top-level parts (FRAME-5B.json "parts") is filed under "none".

For each section:
- "sits_under": the id of that heading, or "none".
- "sits_under_confidence": "high", "medium" or "low".
- "second_home": the id of the heading it would go under if not there (the closest alternative), or "none" if no other
  heading is a real option.
- "role": the id of the role whose work it is by the author's view (N021, N028 or N045), or "none".
- "role_confidence": "high", "medium" or "low".

Write one JSON object to the output file you were given: {"cards": [{"id": "N0xx", "sits_under": "...",
"sits_under_confidence": "...", "second_home": "...", "role": "...", "role_confidence": "..."}]} with every section in
your batch. Check that it parses and that every id in your batch is there.
