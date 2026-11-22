# Task: headings for a narrow contents sidebar

GUIDE.md is a long guide published as one Substack post, section by section, each with an id (S001 and so on), its
heading level and its text. The headings shown are the author's current ones. Many are too long for the contents
sidebar, which leaves this much room on one line (Inter 15px): level 1 217px, level 2 205px, level 3 193px, level 4
181px (about 26, 24, 22 and 20 characters). Level 5 isn't listed.

Give every listed heading (levels 1 to 4, not empty) the heading you'd put in the post, following RULES-HEADINGS.md.
Keep each heading's level and the order of the sections; don't change the text. Measure every heading with
`python3 toc_sidebar.py --text "..." --level N` (run it from this folder) and make sure each one fits or is tight.

Write one JSON object to the output file you were given:
{"headings": {"S001": "Understanding Reparenting", "S002": "...", ...},
 "second_headings": [{"in": "S048", "before_paragraph_starting": "first words of that paragraph", "level": 4, "heading": "..."}],
 "intro_fixes": [{"in": "Sxxx", "from": "exact words", "to": "new words", "why": "..."}]}
"headings" has every listed id. "second_headings" and "intro_fixes" may be empty lists. Check that the JSON parses and
that every listed id is there.
