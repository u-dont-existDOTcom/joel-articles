#!/usr/bin/env python3
"""r19 = r17 (every answer in; draft B read Human Written as a whole, #183) with the windows that whole-article check
left below High fixed, as Joel set the bar (gate gut-2026-11-06a: a Low window is fixed, a Medium one tried, Pangram's
bugs left), and the two clarity snags the compare read found (../r17/prepublish/FINDINGS.md). His answer of 2026-11-06,
when I asked whether to update his post first: "update the rules, you don't need to ask me about this. i will tell you
if i want an incremental publish, otherwise keep working on the fixes" (gate gut-2026-11-06e). Under E373 these are the
model's words he kept or approved, so the fixes are mine, tested, on approve cards. His usual fixes first (E368): the
point first, the reader's reason then the act (E371), a term explained where it is first used (E369), joins, the plain
word. Writes r19.md and CHANGES.json."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r17' / 'r17.md').read_text(encoding='utf-8')
CHANGES = []


def ch(old, new, kind, why):
    global md
    assert md.count(old) == 1, (old[:60], md.count(old))
    md = md.replace(old, new)
    CHANGES.append({'old': old, 'new': new, 'kind': kind, 'why': why})


ch('1. Start by re-seeding with Davis\'s high-dose "SIBO Yogurt", fermented for 36 hours. It contains L. reuteri, to '
   'heal the lining and boost oxytocin, and L. gasseri, to produce bacteriocins that kill SIBO.',
   '1. Start by re-seeding your gut with Davis\'s high-dose "SIBO Yogurt", fermented for 36 hours: its L. reuteri heals '
   'the lining and boosts oxytocin, and its L. gasseri makes bacteriocins, natural antibiotics that kill SIBO.', 'window',
   'Low twice in the whole article (#183): the step and what its bacteria do joined into one sentence; "bacteriocins" '
   'explained where it is first used (E369); the purposes as plain verbs, "heals", "makes", not "to heal", "to produce"')
ch('2. Then feed the new healthy bacteria. Bulsiewicz says to slowly titrate plant diversity back into your diet, '
   'aiming for 30+ different plants per week.',
   '2. Then feed the new bacteria with plants: Bulsiewicz says to add different plants back into your diet slowly, '
   'aiming for 30 or more kinds a week.', 'window',
   'Low in the whole article (#183): the step and whose advice it is joined, the point first (feed them with plants); '
   '"add different plants back slowly" for "slowly titrate plant diversity back"; his "Does anyone count their plants?" '
   'stays as he wrote it')
ch('If it\'s Bile Acid Diarrhea, the test is SeHCAT, and the treatment is bile binders.',
   'If it\'s Bile Acid Diarrhea instead, where your gut doesn\'t take its bile back up and it spills into your colon, a '
   'SeHCAT scan will show it, and bile binders treat it.', 'window',
   'Medium in the whole article (#183), High in its stretch (#176): Bile Acid Diarrhea explained where it is named '
   '(E369), the test and treatment as what they do for the reader; NICE: when bile acids are not absorbed properly they '
   'travel to the colon, and excess bile there causes diarrhoea; SeHCAT is a capsule traced with a gamma camera '
   '(https://nice.org.uk/guidance/dg44/documents/topic-description)')
ch('so come back down once it\'s over.', 'so come back down once the exposure or the stress is over.', 'clarity',
   'the compare read (F1.2): "it" could be the exposure, the stress or the training')
ch('like Crohn\'s or colitis, don\'t count on it.', 'like Crohn\'s or colitis, don\'t count on glutamine.', 'clarity',
   'the compare read (F1.4): "it" could be the higher dose or glutamine itself')
(HERE / 'r19.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
