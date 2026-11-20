# Task: organize a guide's table of contents

A long guide is published as one Substack post. Substack lists the post's headings (levels 1 to 4) in a narrow table of contents beside the text, and readers use it to find the part they need; level-5 headings are not listed. The guide as it stands is in ARTICLE-BY-SECTION.md, section by section, each with an id (N001 to N148), its heading level and its full text.

Organize the contents the way you think serves the guide's readers best. You may:
- move a section (it moves with all its text) anywhere;
- change a heading's level (1 to 4; 5 if it shouldn't be listed);
- merge a section into another one: its heading disappears and its text joins the end of the other section;
- add a new heading between sections (a grouping heading with no text of its own), with a title you choose;
- drop an empty heading (one with no text).

You may not rewrite, cut or add text, and you may not rename existing headings: the names are tested separately, so judge each heading by what its section says.

Write your answer as one JSON object to the output file you were given, in exactly this shape:
{"outline": [ {"id": "N001", "level": 1}, {"new": "A title you add", "level": 2}, {"id": "N036", "merge_into": "N035"}, {"id": "N016", "drop": true} ],
 "reasons": ["one short line per change that matters, saying why"]}
The outline lists the guide from top to bottom: every id from N001 to N148 exactly once (merged and dropped ids where you like; they are not placed). Check that your JSON parses and that every id is there before you finish.
