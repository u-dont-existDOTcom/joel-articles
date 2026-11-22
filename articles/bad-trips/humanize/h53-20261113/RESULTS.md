# Turn 43 (2026-11-13): his call list in, Lu & Mattson said once, the DMSO fixes, Chest Pain's evidence paragraph checked

His messages of 2026-11-13 14:56 UTC ("and yes i want the dmso fixes you mentioned", "continue") and 14:59 UTC ("also i
wasn't clear on why Lu & Mattson need to be described in 2 places, maybe we can merge that?"). The link to his computer
came back during the turn, so his Pangram history was read and every check below ran in his account, in the desktop app's
browser pane (tab "seed").

## His call list version, in whole (`../../review/r39/apply_r39c.py`)

f6b4e35a, read from his history: Human Written, 0% AI, one window Human High 102. It replaces Active Seizure's call list.
Its second item now says which seizure the 5 minutes is for and why, so the paragraph after the list that said the same
(mine, from his points of 2026-11-12 22:34 UTC) is cut; the apply script keeps its text. In place, the section with his
first aid, his list and his rescue medicine paragraph: [0b8cef89](https://www.pangram.com/history/0b8cef89-4089-4ba7-9750-225ad39074be),
Human Written, 0% AI, Human High 243 (seize-c12, predicted Human at 0.75).

## The DMSO fixes and Lu & Mattson said once (`apply_h53.py`)

- "organ or stem cell transplants" made "stem cell transplants" (his yes of 14:56 UTC; `apply_r39c.py`).
- The DMSO section's description of Lu & Mattson 2001 is cut: the study is said once, in My Brain Feels Damaged's evidence
  paragraph, in his round-39 sentence ("DMSO calms NMDA- and AMPA-mediated excitotoxicity that kills brain cells").
- Hanslick et al. 2009 said as its abstract has it (PubMed 19100327, read 2026-11-13): mice from birth to 30 days old,
  damage at every age, worst at 7 days, at the lowest dose tested; rat neurons in a dish. It says nothing about how long
  the exposure lasted, so "when they are exposed for too long" became who was at risk: "Young brains may be at risk from
  DMSO, though: it killed brain cells in mice up to a month old, even at a low dose, and in a dish of rat neurons".
  Checked with its neighbour, the 1967 paragraph: [c6e7b513](https://www.pangram.com/history/c6e7b513-a4d2-43e0-88dd-a4b950d1fc96),
  Human Written, 0% AI, Human High 146 (dmso-h2; the first draft, dmso-h1, read three ways and changed before any check).

## Not in

- brainev-m2: his evidence paragraph with its last sentence saying the study was rat brain cells in a dish and what the
  term means ("in rat brain cells in a dish, DMSO quickly calmed the overstimulation by glutamate (through its NMDA and AMPA
  receptors) that kills brain cells"): [6172bd9e](https://www.pangram.com/history/6172bd9e-4ac4-4b48-8079-da639dbeb7f6),
  Human Written, 0% AI, but Human High 69, Human Low 33 (his "In one human trial ..." sentence, alone in a window now),
  Human Medium 36 (my sentence). Below High, so his sentence stays as it was (apply_gate.py).
- cp-c4, Chest Pain's evidence paragraph after the reads of cp-c3 (where the research was done; the rats' three days
  before, and that the study didn't give it after, PubMed 19904216's abstract; "so" for the clot's link; platelets
  explained): [2c13fbe7](https://www.pangram.com/history/2c13fbe7-3693-4dcf-9726-cf6fea660532), AI Assisted, 50%: AI-Assisted
  Low 15, Medium 34, Low 36. The guide keeps its paragraph.

## The reads (`reads/`)

Three fresh readers (needed, against his fixes, fit) read brainev-m1, dmso-h1 and cp-c3. What they marked in my sentences
changed before the second drafts' checks: the receptor names and the missing reason glutamate matters (brainev), "how
long is too long?" and "is 30 days their age?" (dmso; the abstract answers both: age, and no duration), and before vs
after the heart attack, "the same way as what?", "in people or a dish?" (cp). What they marked in his sentences goes to
him or stays as his: the 1967 sentence's two "although"s (and the 1967 paper had anxiety patients: the neuro lane's
lesson neuro-2026-11-13a), "One famous", Kortleve's 10% vs 5%.

## Next

My Brain Feels Damaged's last sentence (rat cells in a dish, the term explained) to Human High by itself, a diagnosis
first: in brainev-m2 the windows split so his "In one human trial" sentence stood alone and read Low. Chest Pain's
evidence paragraph, try 3 after a diagnosis of cp-c4's AI-Assisted windows (every sentence of it; his first person near
it in B122 read Human). Then the other evidence paragraphs and the Medium windows of `../h42-20261111/RESULTS.md`.
