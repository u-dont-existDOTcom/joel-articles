# Round 3 of the blind test (2026-11-23)

His standing rule (2026-11-22 23:43 UTC): "make sure whenever you learn lessons in this repo you see if you can apply them
to pass pangram on the paragraphs that i fixed yourself without seeing my fixes exactly."

**Set-up.** The four paragraphs round 2 didn't get to Human (M-73, M-214, M-252 with M-253, M-346) and the end of "The
conversation about flaws" as it stood before his fix of 2026-11-23 ([PARAS.md](PARAS.md), [KEY.json](KEY.json)). The
brief ([BRIEF.md](BRIEF.md)) is round 2's with what round 2 and his flaws fix taught: way 19, a list of concrete things
from life stays whole; way 21, a two-part question nobody could answer becomes the dilemma itself; way 22, a contrast
said in general words keeps its concrete half and a pivot names what it points back to; way 23, a run of questions is
fixed by order, one plain statement and one frame. None of its examples come from these paragraphs. Three Opus writers
(the model of rounds 1 and 2) gave no answer in 20 to 27 minutes each, so a Sonnet writer did this round
([OUT.md](OUT.md)). Predictions were written and committed before the checks ([PREDICTIONS.json](PREDICTIONS.json)).

**Against his versions:**

| Card | What his fix fixed | Round 3's rewrite | Score |
|---|---|---|---|
| M-73 | the point first (fixer types); the general half of the contrast cut | kept the order and the general half; added "again and again" | missed |
| M-214 | "I like that idea." joined; both lists kept | the point first, the list of concrete things kept whole, joined with a colon; cut "sensuality, and inspiration" | partly |
| M-252 | "Everything ... so far" (not true there); the pivot named ("that liberal modern philosophy") | "So far I’ve been putting forward ..."; the pivot named ("those three don’t by themselves explain") | fixed |
| M-253 | "safety gives the space" | "Still, for me, feeling safe doesn’t spark desire, but it makes space for it." (both halves kept) | fixed |
| M-346 | the dilemma itself ("Is that, in and of itself, a betrayal ...") | the vague question made a statement ("We’d need to say what counts as betrayal ..."), still not the dilemma | missed |
| flaws 126-127 | order, one plain statement, the reader's frame, the consequence folded in | the frame and the folded consequence ("And if you shut down, did that mean ..., so they felt abandoned?"); the questions made reported ("Then ask whether ..."); no reorder, no statement | partly |

**Pangram** ([CHECKS-R3.txt](CHECKS-R3.txt); each by itself, his main account, 2026-11-23 16:04 to 16:05 UTC):

| Card | Round 1 | Round 2 | Round 3 | His version |
|---|---|---|---|---|
| M-73 | [Mixed, 59% AI](https://www.pangram.com/history/18aaaff3-a2e3-4585-b59c-3efc3fcd20c2) | [Mixed, 42% AI](https://www.pangram.com/history/53794e29-8e5c-46fd-b614-ee6aa13d74f4) | [Human, High](https://www.pangram.com/history/c65e536b-e589-4439-9a44-f53c3ae94c17) | [Human, High](https://www.pangram.com/history/c12ff059-dc9e-432d-bc7f-bddb2219ebaf) |
| M-214 (with the next paragraph) | [Human (High, Medium, Low)](https://www.pangram.com/history/ed4bc254-0634-445f-a1c6-b3ddaf75304c) | [Mixed](https://www.pangram.com/history/c2d2d3c5-2147-46f9-afdc-647e59d98225): the rewrite Low, the next paragraph AI (Medium) | [Mixed](https://www.pangram.com/history/4a5f3b06-48ad-422d-a7c0-37b3187dddc0): the rewrite Human (Medium), the next paragraph AI (High) | (no check named) |
| M-252 with M-253 | [Human (Low)](https://www.pangram.com/history/785f4cde-8a0c-4e02-ace9-011fa3996dbd) | [AI, High](https://www.pangram.com/history/d84b2b09-0763-4822-bd77-69248654ef8a) | [Human (High, Medium)](https://www.pangram.com/history/da5c670e-0a19-4fb1-a60e-0fe1de260e23) | (no check named) |
| M-346 | [AI, Low](https://www.pangram.com/history/0bfa46e8-7b65-42ae-b3f8-7a9439bc966b) | [Mixed, 75% AI](https://www.pangram.com/history/76f05eb5-e2af-4b86-9af5-dae6c9b916b4) | [Mixed, 77% AI](https://www.pangram.com/history/33ef19a3-6b9b-4ef2-aa54-a3d51fba9718) | [Human, High](https://www.pangram.com/history/7df7a85b-4246-428d-b83a-34028f9a938b) |
| flaws 126-127 | | (my tries: [Mixed](https://www.pangram.com/history/b5b7c639-2eab-4690-bd28-f5e1977de060), [AI](https://www.pangram.com/history/60ab811a-eaac-4802-aad7-978b87e9f6cd)) | [AI, 100%](https://www.pangram.com/history/5fa5bc28-a67f-45b7-86c5-d31211495094) | [Human, High](https://www.pangram.com/history/e7fa9711-caf2-469b-9c1a-6f4422e6ec39) |

**Result.** Over the three rounds, 9 of the 14 paragraphs he fixed read Human High by themselves from the lessons alone
(4, 73, 119, 125, 149, 160, 343, 361, 409), and two more read Human with one Medium window and no Low (437, and 252 with
253), which his rule for done allows. 214's rewrite reads Human (Medium) itself, but the paragraph after it, which it
needs to reach 50 words and which reads Human in its section, read AI beside it in rounds 2 and 3. Two still don't:
346, where no round asked the dilemma (the writer turns the vague question into a statement, which still reads AI), and
the flaws stretch, where turning the questions into reported ones ("Then ask whether ...") read AI for the third time.
What held: a pivot that names what it points back to with both halves of the turn kept (252 with 253), and a list of
concrete things kept whole (214's own window, Medium where round 2's cut list was Low). What I had wrong: 73 read High
with the general half of its contrast still in, so that half wasn't what read AI; and I predicted 3 of 5 (Brier 0.247).
The next lesson (romance-2026-11-23d): the dilemma line needs an example of asking one, from outside these paragraphs,
and reported questions go into way 23 as what not to do. `tools/humanization/his_fixes_brief.md` now has ways 22 and 23
and the concrete-list line in way 19.
