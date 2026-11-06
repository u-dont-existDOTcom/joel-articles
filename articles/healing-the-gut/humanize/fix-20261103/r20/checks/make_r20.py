#!/usr/bin/env python3
"""The check text and making-sense receipt (gate E365) for r20's second try at Phase 5's first steps, checked in a
longer cut than the first try's: Phases 3 to 6 without their headings (blocks 50-56, 58-60, 62-67 and 69-72), as his
extension reads them in the whole article, where the steps read Low (#183). Phase 4 and Phase 5 alone together read AI
even without any fix (#186), so this cut and its control (the same blocks of r17, --unchanged) judge the change. Payoffs
for sentences earlier receipts had come from them; the rest are here. His own aside "Does anyone count their plants?" is
marked his. Writes CHECK-r20-P36.txt, CHECK-r17-P36.txt and RECEIPT-r20-P36.json and checks the receipt."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R20 = HERE.parent
FIX = R20.parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

b20 = sr.blocks((R20 / 'r20.md').read_text(encoding='utf-8'))
b17 = sr.blocks((FIX / 'r17' / 'r17.md').read_text(encoding='utf-8'))
IDS = [i for i in range(50, 73) if not b20[i]['kind'].startswith('h')]
assert [b20[i]['kind'].startswith('h') for i in (49, 57, 61, 68, 73)] == [True] * 5
HIS = 'Does anyone count their plants?'
HIS_WHOSE = ('his own: "Does anyone count their plants?", the aside he added to his own version of Phase 5 '
             '(2026-11-03), not a rewrite of the model\'s text')
OLD = {}
for f in sorted(FIX.glob('r1[4-9]/**/RECEIPT-*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')).get('sentences', []):
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
NEW = {
    'This one is from Dr. William Davis': ('the reader knows whose phase this is', 'opens Phase 3, after its pointer'),
    'AVOID most herbal antibiotics': ('the reader knows to skip most herbal antibiotics, even the ones Davis names',
                                      'his first warning in the purge'),
    'My BFF Pooyan tried candibactin': ('the reader learns why: what one of them did to his friend',
                                        'the reason for the warning'),
    'The H2O2 worked a lot better': ('the reader learns what worked instead', 'after what went wrong, what worked'),
    'There is one herbal antibiotic that works': ('the reader knows the one exception, berberine for H. pylori',
                                                  'the exception to the warning'),
    'If you have an acute infection with something': ('the reader knows when to go further, and to what',
                                                      'the next step if those don\'t clear it'),
    'BIND the toxins': ('the reader knows to bind the toxins the kill releases, and with what', 'the kill\'s side job'),
    'At the same time, take Ruscio\'s Triple': ('the reader knows which probiotic to take during the kill',
                                               'what to take alongside'),
    'That\'s to maintain diversity': ('the reader learns why: to keep good bacteria and avoid C. diff',
                                     'the reason for the probiotic'),
    'And if all that failed': ('the reader knows when to use the Elemental Diet, and why', 'the last resort'),
    'That\'s a 2-3 week liquid-only diet': ('the reader learns what the Elemental Diet is and how it works',
                                           'what the last resort is'),
    'My notes: the H2O2 swap above': ('the reader knows the H2O2 advice is Joel\'s, not the books\'',
                                      'closes Phase 3 with his notes'),
    'For berberine and H. pylori see Parasites': ('the reader knows where berberine and the yogurt are explained',
                                                  'his pointers'),
    'The purge cleared out good bacteria too': ('the reader learns why to re-seed first, and with what',
                                                'the first step of the rebuilding'),
    'It has L. reuteri, which heals': ('the reader knows what the yogurt\'s two bacteria do for them, and what '
                                       'bacteriocins are', 'what the yogurt does'),
    'The new bacteria feed on plant fiber': ('the reader learns why to eat plants now, how to bring them back, and how '
                                             'many to aim for', 'once the bacteria are back, feeding them'),
    'The last phase is from Neil Nathan': ('the reader knows whose phase this is', 'opens Phase 6'),
    'It\'s for people who are': ('the reader learns whether this phase is for them', 'who the phase is for'),
    'Check your environment (Nathan).': ('the reader knows the first check of this phase', 'the first step'),
    'Could it be mold/mycotoxins, or Lyme?': ('the reader knows what to look for', 'what the environment check means'),
    'Get assessed for those': ('the reader knows what to do if it is positive', 'after what to look for, what to do'),
    'Then check the brain.': ('the reader knows the second check', 'the next step'),
    'If you react to everything, Hopper says': ('the reader learns what the brain issue is and how to treat it',
                                                'what the brain check means'),
    'My notes: Matt\'s note on mopping up': ('the reader knows where Matt\'s note is', 'closes Phase 6 with his pointer'),
}
t20 = '\n\n'.join(b20[i]['text'].strip() for i in IDS)
t17 = '\n\n'.join(b17[i]['text'].strip() for i in IDS)
(HERE / 'CHECK-r20-P36.txt').write_text(t20, encoding='utf-8')
(HERE / 'CHECK-r17-P36.txt').write_text(t17, encoding='utf-8')
r = S.make(t20, 'Phase 3: The Purge', 'Someone partway through the protocol, deciding how to clear the overgrowth, what to '
           'check if that fails, and how to rebuild once it is gone.', HIS, HIS_WHOSE)
for s in r['sentences']:
    if s.get('his'):
        continue
    hit = [v for k, v in NEW.items() if s['s'].startswith(k)] or ([OLD[s['s']]] if s['s'] in OLD else [])
    assert len(hit) == 1, s['s'][:80]
    s['payoff'], s['follows'] = hit[0]
r['opens']['why_reading'] = ('It tells the reader whose phase this is, and the next sentence tells them to skip most herbal '
                             'antibiotics, before they buy any.')
r['same_point'] = ('none: read Phases 3 to 6 from their headings to the stacks: each phase\'s steps are said once; berberine '
                   'and the yogurt are pointers to Parasites and SIBO; Phase 5\'s fuels point to the paragraph under Leaky '
                   'gut')
r['questions'] = {
    'Q1': 'PASS: each changed step opens on the reader\'s situation, then the act (the purge cleared out good bacteria '
          'too, so re-seed; the new bacteria feed on plant fiber, so bring plants back)',
    'Q2': 'PASS: each instruction is the reader\'s act: re-seed, bring plants back slowly',
    'Q3': 'PASS: the bacteria and the number of plants are named exactly',
    'Q4': 'PASS: "bacteriocins" is explained where it is first used; SIBO was explained earlier',
    'Q5': 'PASS: each "so" turns the situation into the act; "too" points back to the purge\'s good bacteria',
    'Q6': 'PASS: nothing moved; the steps keep their order',
    'Q7': 'PASS: each change tells the reader why to do the step',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence; the small words carry the relations (so, too, which, until)',
}
r['placement'] = 'Phases 3 to 6 in the article\'s order; Phase 5\'s steps keep theirs.'
r['checked'] = [{'point': 'the purge takes good bacteria too',
                 'found': 'the article\'s own Phase 3: take probiotics during the kill phase "to maintain diversity and '
                          'prevent opportunistic infections (like C. diff)"', 'still_needed': 'yes: it is the step\'s reason',
                 'fate': 'kept'},
                {'point': 'gut bacteria feed on plant fiber',
                 'found': 'the article already says so: the bacteria ferment the fiber (the stacks) and resistant starch '
                          'feeds them (Leaky gut)', 'still_needed': 'yes: it is the step\'s reason', 'fate': 'kept'}]
(HERE / 'RECEIPT-r20-P36.json').write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
probs = S.check(t20, r)
print('r20-P36', len(t20.split()), 'words', 'PASS' if not probs else probs, '| control', len(t17.split()), 'words')
sys.exit(1 if probs else 0)
