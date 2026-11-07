#!/usr/bin/env python3
"""The check texts and making-sense receipts (gate E365, each sentence's link per neuro-2026-11-06b) for r24:
- r24-P36: Phases 3 to 6 (blocks 50-56, 58-60, 62-67, 69-72), the second try of the r23-P36 stretch (#192 read Mostly
  Human, AI Low on Phase 4's first organ case);
- r24-P45: Phases 4 and 5 (blocks 58-60, 62-67), the second try of r23-P45 (#191 Human), to see the join keeps it Human;
- r24-org: Phase 4's organ paragraph by itself (block 59), the paragraph #192 read AI Low, narrowed before the stretch
  is tried again (E343);
- r24-PR: the protocol section, "Text Summary of the Protocol", from its first line through Phase 6 (blocks 38-72 without
  headings), checked once before any whole-article check (gate gut-2026-11-07a).
Payoffs, follows and links come from the receipts already made for the same sentences (r23's, then earlier ones); the
changed and the not-yet-read sentences are here. His own aside, "Does anyone count their plants?", is marked his. Writes
CHECK-<name>.txt and RECEIPT-<name>.json and checks each."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

HIS = 'Does anyone count their plants?'
HIS_WHOSE = ('his own: "Does anyone count their plants?", the aside he added to his own version of Phase 5 '
             '(2026-11-03), not a rewrite of the model\'s text')
OLD, LINK = {}, {}
for f in sorted(FIX.glob('r1[4-9]/**/RECEIPT-*.json')) + sorted(FIX.glob('r2[0-1]/**/RECEIPT-*.json')) + \
        sorted(FIX.glob('r23/checks/RECEIPT-*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')).get('sentences', []):
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
        if x.get('link'):
            LINK[x['s']] = x['link']
NEW = {
    'This protocol is meant to be done in phases.': ('the reader knows the protocol goes in phases',
                                                     'opens the protocol\'s summary'),
    'Don\'t skip ahead, since': ('the reader knows to go phase by phase, and when to move on',
                                 'how to use the phases just named'),
    'Before you throw supplements or antimicrobials at your gut, the system mechanics': (
        'the reader knows Phase 1 comes before any supplement or antimicrobial: the body\'s mechanics first',
        'opens Phase 1'),
    'Diet-wise, go Paleo-Low FODMAP': ('the reader knows which two diets to choose between', 'the first step of the reset'),
    'And no snacking!': ('the reader knows not to snack', 'the second step of the reset, after the diet'),
    'Pimentel wants meals 4-5 hours apart': ('the reader learns how far apart to space meals, and why: the MMC sweeps the '
                                             'gut clean between them', 'why no snacking'),
    'My notes: see "Poor diet now" and "Plant foods"': ('the reader knows where Joel\'s notes on diet and plant foods are',
                                                       'closes Phase 2 with his pointers'),
    'So check your organs (Brown), starting with your pancreas': (
        'the reader knows to check their organs, starting with the pancreas, and how they would test for and treat '
        'Exocrine Pancreatic Insufficiency', 'after "the problem is likely an organ", which organ first'),
}
NEW_LINKS = {
    'Don\'t skip ahead, since': 'Don\'t skip ahead, since',
    'Before you throw supplements or antimicrobials at your gut, the system mechanics': (
        'Before you throw supplements or antimicrobials at your gut'),
    'This part is from T.C.': 'This part',
    'Hale (Kick Your Fat in the Nuts)': 'none: the rest of the sentence before it, cut at "T.C." by the splitter',
    'Are your pupils dilated all the time?': 'none: the first check, a question to the reader after whose part it is',
    'Are you missing your gag reflex?': 'none: the same check\'s second question, in the same form as the first',
    'Then according to Hale': 'Then',
    'Rosenberg\'s fix is his Basic Exercise': 'Rosenberg\'s fix',
    'Both of those help to': 'Both of those',
    'Now let\'s have a look at your bile function.': 'Now let\'s have a look',
    'Do you burp extra': 'none: the first question of the bile check just announced',
    'Do your stools float': 'none: the next question of the same check, in the same form',
    'Then your bile is stagnant': 'Then',
    'So thin the bile first': 'So thin the bile first',
    'My notes: for stress and sleep': 'for stomach acid and bile',
    'Once the mechanics work': 'Once the mechanics work',
    'This one\'s from Dr. Michael Ruscio': 'This one\'s',
    'Diet-wise, go Paleo-Low FODMAP': 'Diet-wise',
    'Either way you stop feeding': 'Either way',
    'And no snacking!': 'And',
    'Pimentel wants meals 4-5 hours apart': 'Pimentel wants meals 4-5 hours apart',
    'My notes: see "Poor diet now" and "Plant foods"': 'none: his notes\' pointers, under their label',
    'If diet didn\'t clear your symptoms': 'If diet didn\'t clear your symptoms',
    'So check your organs (Brown), starting with your pancreas': 'So check your organs (Brown), starting with',
    'Benjamin Brown (Digestive Health Solution)': 'this phase',
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first: the check, then which organ first and its case; each term '
          '(Exocrine Pancreatic Insufficiency, Bile Acid Diarrhea, oxytocin, bacteriocins) explained where first used',
    'Q2': 'PASS: each instruction is the reader\'s act: check, test and treat, re-seed, feed with plants, keep spacing meals',
    'Q3': 'PASS: the organs, tests, treatments, yogurt, bacteria and number of plants are named exactly',
    'Q4': 'PASS: each term is explained where first used, by what it does for the reader',
    'Q5': 'PASS: each sentence\'s tie is in its words (the links field), or the link says why it needs none',
    'Q6': 'PASS: nothing moved; each phase keeps its order, and his aside still follows the number it jokes about',
    'Q7': 'PASS: each change tells the reader what to do in their case, and why where they would ask',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence; the small words carry the relations (starting with, and if, then, as in)',
}
CHECKED = json.loads((FIX / 'r23' / 'checks' / 'RECEIPT-r23-P36.json').read_text(encoding='utf-8'))['checked']
P36 = [i for i in range(50, 73) if i not in (57, 61, 68)]
TEXTS = {
    'r24-P36': (P36, 'Phase 3: The Purge',
                'Someone partway through the protocol, deciding how to clear the overgrowth, what to check if that fails, '
                'and how to rebuild once it is gone.',
                'It tells the reader the purge is for them if diet didn\'t clear their symptoms, the case they would '
                'recognize.'),
    'r24-P45': ([58, 59, 60, 62, 63, 64, 65, 66, 67], 'Phase 4: The Investigation',
                'Someone whose symptoms survived the diets, the purge and the Elemental Diet, deciding what to check next '
                'and how to rebuild once the infection is gone.',
                'It tells the reader whose phase this is and that it is for them if even the Elemental Diet failed, the '
                'case they would recognize.'),
    'r24-org': ([59], 'Phase 4: The Investigation',
                'Someone whose symptoms survived the diets, the purge and the Elemental Diet, deciding which organ to '
                'check and how.',
                'It tells the reader the next step is checking their organs, starting with the pancreas, the case they '
                'would recognize.'),
    'r24-PR': ([i for i in range(38, 73) if i not in (39, 44, 49, 57, 61, 68)], 'Text Summary of the Protocol',
               'Someone with gut symptoms working through the books\' protocol phase by phase, deciding what to do first '
               'and when to move on to the next phase.',
               'It tells the reader the protocol goes in phases, so they know to read it as steps for their own case.'),
}
b = sr.blocks((FIX / 'r24' / 'r24.md').read_text(encoding='utf-8'))
bad = 0
for name, (ids, section, reader, why) in TEXTS.items():
    assert not any(b[i]['kind'].startswith('h') for i in ids), name
    text = '\n\n'.join(b[i]['text'].strip() for i in ids)
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    r = S.make(text, section, reader, HIS, HIS_WHOSE)
    for s in r['sentences']:
        if s.get('his'):
            continue
        hit = [v for k, v in NEW.items() if s['s'].startswith(k)] or ([OLD[s['s']]] if s['s'] in OLD else [])
        assert hit, (name, s['s'][:80])
        s['payoff'], s['follows'] = hit[0]
        if 'link' in s:
            lk = [v for k, v in NEW_LINKS.items() if s['s'].startswith(k)] or (
                [LINK[s['s']]] if s['s'] in LINK else [])
            assert lk, (name, 'link', s['s'][:80])
            s['link'] = lk[0]
    r['opens']['why_reading'] = why
    r['same_point'] = ('none: read the protocol from its first line to the stacks: each phase\'s steps are said once; '
                       'Phase 5\'s meal spacing points to Phase 2 for its reason; berberine and the yogurt point to '
                       'Parasites and SIBO; the fuels point to Leaky gut; his notes point back to the causes')
    r['questions'] = dict(Q)
    r['placement'] = 'The protocol\'s phases in the article\'s order, without their headings, as his extension reads them.'
    r['checked'] = CHECKED
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, len(text.split()), 'words', 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
