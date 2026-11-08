#!/usr/bin/env python3
"""drug_fixes.py - the guide stops assuming a drug where it speaks generally (run after merge_why.py).

Joel, 2026-11-08, on round 24's TEACH-LABELS: "also let's make sure this guide is not assuming people are taking a drug,
since it's not called the bad drug trips guide." A fresh reader listed the sentences (DRUG-READ.md beside this script, its
prompt in DRUG-READ-PROMPT.md); each change below is the smallest that fits a state from a practice too. Left as they are:
the sections about a drug or remedy on purpose; sentences whose next sentence covers the practice case (the first five
minutes' "more of any substance" and its reminder, followed by the practice paragraph); "coming down" said of the other
people at a ceremony. Three lines are his humanized versions of the model's text (gate E373: the fixing is mine), so
each change there was tested first and goes in because it read Human (gate bad-trips-2026-11-07a): his (Re)defining's
causes (alone, Human: f99fb1f0), his Give the Session's opening (the section, Human High as one window: 14a16456; the
paragraph alone read AI either way, 53 words: d7b3540f), and No Rash Actions' bold rule, in a stretch that read Mixed
before (h28 N4), so its check comes with that stretch's humanizing. Receipts: NEW-B330b, TEST-DRUG-START, NEW-B319.

  python3 drug_fixes.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
FIXES = [
    # (section, old, new)
    ('Acute Medical and Neurological Rescue', 'for a physiologically stable psychedelic crisis',
     'for a physiologically stable psychedelic or practice-induced crisis'),
    ('Acute Medical and Neurological Rescue', 'who doesn\'t know what was taken', 'who doesn\'t know what was taken, if anything'),
    ('Grounding Menu', 'Remember that substance effects usually rise, peak, and change.',
     'Remember that these states usually rise, peak, and change.'),
    ('Grounding Menu', 'Choose it while sober and regulated', 'Choose it ahead of time, while calm and regulated'),
    ('Grounding Menu', 'Walk slowly with a sober person in a safe environment.',
     'Walk slowly with a clear-headed person in a safe environment.'),
    ('No Rash Actions', 'it can wait for you to be sober.', 'it can wait until the state has passed.'),
    ('No Rash Actions', 'belongs in the notebook until sober review.', 'belongs in the notebook until you can review it with a clear head.'),
    ('The Fear/Panic Loop', 'no metaphysics, diagnosis, or life decisions while peaking.',
     'no metaphysics, diagnosis, or life decisions at the peak.'),
    ('The Fear/Panic Loop', 'I don\'t have to solve it while peaking.', 'I don\'t have to solve it at the peak.'),
    ('Abuse Memories', 'Psychedelics can bring up true trauma', 'Psychedelics and intense practices can bring up true trauma'),
    ('Abuse Memories', 'Don\'t treat intoxicated certainty as evidence either.',
     'Don\'t treat the certainty you feel in that state as evidence either.'),
    ('After the Storm', 'engage in some sober prayer or gentle meditation', 'engage in some calm prayer or gentle meditation'),
    ('What Kind of Aftermath Is This?', 'sleep hygiene, no more substances, and professional help',
     'sleep hygiene, no more substances or intense practice, and professional help'),
    # his humanized lines (tested)
    ('(Re)defining "Bad Trip"', 'the dose of what drug(s) you took and how your body handles them.',
     'the dose of what drug(s) you took and how your body handles them, or how hard you pushed a practice.'),
    ('Give the Session a Beginning and an End', 'think through how it will start and end, and what happens in between, before you take anything.',
     'think through beforehand how it will start and end, and what happens in between.'),
    ('No Rash Actions', 'go back over it sober with one grounded person.', 'go back over it with one grounded person once your head is clear.'),
]
blocks = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in blocks) + '\n' == MD.read_text(encoding='utf-8')
for sec, old, new in FIXES:
    hits = [b for b in blocks if old in b['md']]
    assert len(hits) == 1 and hits[0]['md'].count(old) == 1, (sec, old, len(hits))
    hits[0]['md'] = hits[0]['md'].replace(old, new)
    print('%-38s %s  ->  %s' % (sec, old, new))
MD.write_text('\n\n'.join(b['md'] for b in blocks) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
