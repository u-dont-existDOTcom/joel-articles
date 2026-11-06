#!/usr/bin/env python3
"""r20 = r17 with the two clarity fixes that read Human, High in their stretch (r19-D, #185), and a second, different
try at Phase 5's first two steps, which read Low in the whole article (#183).

The first try (../r19/, #184) joined each step to what it does and made the cut read worse than the same cut without it
(59% AI against 30%, #186), and it pulled sentences I hadn't touched to AI. So this try takes the other fix his own
versions use (E371, the bad trips lane's "They're feeling overwhelmed, so dim the lights"): the reader's situation first,
then the act, and the step's own words otherwise as they were. Phase 4's second organ case stays as it is: its one try
read worse, so it goes on the later list (gate gut-2026-11-06a). Writes r20.md and CHANGES.json."""
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


ch('so come back down once it\'s over.', 'so come back down once the exposure or the stress is over.', 'clarity',
   'the compare read (F1.2): "it" could be the exposure, the stress or the training; r19-D read Human, High (#185)')
ch('like Crohn\'s or colitis, don\'t count on it.', 'like Crohn\'s or colitis, don\'t count on glutamine.', 'clarity',
   'the compare read (F1.4): "it" could be the higher dose or glutamine itself; r19-D read Human, High (#185)')
ch('1. Start by re-seeding with Davis\'s high-dose "SIBO Yogurt", fermented for 36 hours. It contains L. reuteri, to '
   'heal the lining and boost oxytocin, and L. gasseri, to produce bacteriocins that kill SIBO.',
   '1. The purge cleared out good bacteria too, so start re-seeding with Davis\'s high-dose "SIBO Yogurt", fermented for '
   '36 hours. It has L. reuteri, which heals the lining and boosts oxytocin, and L. gasseri, which makes bacteriocins, '
   'natural antibiotics that kill SIBO.', 'window',
   'Low in the whole article (#183): the reader\'s situation first, then the act (E371): Phase 3 already says to take '
   'probiotics during the kill phase "to maintain diversity", so the purge takes good bacteria too; "bacteriocins" '
   'explained where it is first used (E369); "which heals", "which makes" for "to heal", "to produce"')
ch('2. Then feed the new healthy bacteria. Bulsiewicz says to slowly titrate plant diversity back into your diet, '
   'aiming for 30+ different plants per week.',
   '2. The new bacteria feed on plant fiber, so bring plants back into your diet slowly, as Bulsiewicz says, until '
   'you\'re eating 30 or more kinds a week.', 'window',
   'Low in the whole article (#183): what the new bacteria need first, then the act; "bring plants back into your diet '
   'slowly" for "slowly titrate plant diversity back"; his "Does anyone count their plants?" stays as he wrote it')
(HERE / 'r20.md').write_text(md, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(CHANGES, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(CHANGES), 'changes;', len(md.split()), 'words')
