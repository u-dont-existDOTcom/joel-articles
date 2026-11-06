# Lessons, one file per message

From 2026-11-06, a lane's lessons from one message of Joel's go in a file of their own here, not in
`docs/HUMANIZATION-GATE.md`. Read this folder with the gate: it is the same rulebook.

- **The file:** `<date>-<HHMM>-<lane>.md`, from the UTC time of his message and the lane's short name
  (`2026-11-06-2013-gut.md`). One lane writes one file per message, so no two pull requests touch the same file.
- **The name of a lesson:** `<lane>-<date><letter>`, in the order the lane writes them that day (`gut-2026-11-06a`,
  `gut-2026-11-06b`, ...). `python3 tools/humanization/lane_push.py --lesson-id <lane>` prints the next free one. Cite
  it as "gate gut-2026-11-06a". Two lanes can't pick the same name, so no lane renumbers, and nothing like "the next
  lesson in any lane is ..." is kept by hand.
- **The form:** a `#` heading saying whose message it was and when, his words, then each lesson as a bullet that starts
  `- **<name>. <the rule in one sentence>.**`, as in the gate.
- **Numbers:** E1 to E380 keep theirs, in the gate. E379 is here (`2026-11-06-1948-gut.md`). `lane_push.py` still
  refuses a numbered lesson that main already gave another lane's.

Why: lanes kept editing the same lines of the gate, the next number and the note after each section, and their pull
requests conflicted while they waited, three times in a day for the gut lane. Universal-dev-architecture's
`patterns/short-lived-pull-requests.md`, rule 4: "Prefer one file per item to one long shared file. Prefer
collision-free names, such as a date and a slug, to the next number in a sequence." The lesson is
`2026-11-06-2106-gut.md`.
