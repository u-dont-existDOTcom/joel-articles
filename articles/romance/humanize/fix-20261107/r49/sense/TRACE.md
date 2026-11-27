# The sense read's findings, traced (r49, 2026-11-27)

The word-for-sense read of every paragraph changed since the drafts were last pasted for his whole-article check (r39):
30 live paragraphs, 1,993 words, made from [CHANGED-SINCE-R39.md](CHANGED-SINCE-R39.md) (each paragraph as
`whole/REPLACEMENTS.json` has it at b0c80524, under its heading from `whole/FIXED.md`).

| Read | Seed | Planted found | Other findings |
|---|---|---|---|
| Reader 1 (Sonnet), `reads/READ-1-reader1.json` | 1127 | 2 of 3: missed "pacific" (for "specific", block 15) | 1 |
| Reader 2 (Sonnet), `reads/READ-1-reader2.json` | 1127 | 2 of 3: missed "pacific" | 1 (the same) |
| Reader 3 (Sonnet), `../sense-seed1128/reads/READ-1.json` | 1128 | 3 of 3 ("than", "quiet", "glisten") | 0 |

Readers 1 and 2 both judged the planted "pacific" a real choice: "a pacific type of confidence which is produced by deep
relaxation/flow state" reads as "calm confidence", so that canary fits its sentence. Reader 3's read, on new planted
errors, is complete and found every one (`sense_read.py score`, exit 0).

| Block | Words | Fate | Why |
|---|---|---|---|
| 7 (live 46) | "Here's a video that can help understand the long process." | his, fine in place | His live words, carried unchanged through J-B54, which changed only the sentence before it. "Help understand" without "you" is ordinary casual English, and the paragraph before the sentence names the process it points at (learning self-love, and being ready for a relationship). Not a slip; not changed. |

The non-word net (`sense_read.py nonwords`): animalistic, ftw, hypergamous, ontologizing, poppin, teleport, themself,
vid, weaponize. All are his words or his slang in his own paragraphs; none is a typo.

Nothing to fix.
