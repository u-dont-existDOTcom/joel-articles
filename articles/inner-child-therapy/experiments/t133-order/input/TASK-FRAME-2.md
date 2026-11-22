# Task: say what each part and role of a guide is for, in general terms

FRAME2-SOURCE.md holds a long guide's introduction, the own text of each top-level part (most have none), and the own
section of each of its three roles, without the sections under them. TOC.md is its whole table of contents.

Describe what each part and each role is FOR, in general terms that would let someone decide whether any passage of the
guide, wherever it sits now, is that role's work or serves that part's job. Describe the function, the kind of need it
meets or the stage of the reader's path it serves. Don't describe a part or role by listing the sections under it in the
contents, and don't use where sections sit now as evidence of what belongs there: the point is to be able to say that a
section somewhere else belongs to it.

Write one JSON object to the output file you were given:
{"parts": [{"id": "N001", "heading": "...", "job": "one or two lines"}], "roles": [{"id": "N021", "name": "...", "work": "two or three lines"}]}
with every level-1 heading in "parts" (ids from TOC.md) and the three roles (N021, N028, N045). Check that it parses.
