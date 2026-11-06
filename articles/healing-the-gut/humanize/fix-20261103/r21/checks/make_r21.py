#!/usr/bin/env python3
"""The making-sense receipt (gate E365) for r21's third try at Phase 5's first two steps: Phase 5 without its heading
(blocks 62-67), the stretch #165 read Human, High by itself. No cut decides this try: Phase 5 alone read High unchanged
(#165), and Phases 3 to 6 read its steps AI unchanged (#187), where the whole article reads them Human, Low (#183); so the
try goes to Pangram in the whole article (draft D, his extension, against draft C's try 2), and this receipt is its read
for sense. Payoffs for the sentences earlier receipts already had come from them; the three changed ones are here. His own
aside, "Does anyone count their plants?", is marked his. Writes CHECK-r21-P5.txt and RECEIPT-r21-P5.json and checks the
receipt."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R21 = HERE.parent
FIX = R21.parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

b21 = sr.blocks((R21 / 'r21.md').read_text(encoding='utf-8'))
IDS = [62, 63, 64, 65, 66, 67]
assert b21[61]['kind'].startswith('h') and b21[68]['kind'].startswith('h') and b21[62]['text'].startswith('Once you')
HIS = 'Does anyone count their plants?'
HIS_WHOSE = ('his own: "Does anyone count their plants?", the aside he added to his own version of Phase 5 '
             '(2026-11-03), not a rewrite of the model\'s text')
OLD = {}
for f in sorted(FIX.glob('r1[4-9]/**/RECEIPT-*.json')) + sorted(FIX.glob('r20/**/RECEIPT-*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')).get('sentences', []):
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
NEW = {
    'Once you\'re clear of infection,': ('the reader knows when this phase starts and what it is for: rebuilding, so it '
                                        'doesn\'t come back', 'opens Phase 5, after Phase 4\'s pointers'),
    'Dr. William Davis is back': ('the reader knows whose advice this phase is', 'after what the phase is for, whose it is'),
    'Start by re-seeding with Davis\'s high-dose': (
        'the reader knows the first step, which yogurt, and what makes it high-dose: 36 hours of fermenting against a '
        'store yogurt\'s 6 to 12, for hundreds of times the bacteria', 'the first step of the rebuilding'),
    'It contains L. reuteri, to heal the lining': (
        'the reader knows what the yogurt\'s two bacteria do for them, and what oxytocin and bacteriocins are',
        'what the yogurt just named does'),
    'Then feed the new healthy bacteria.': ('the reader knows the second step: once the bacteria are back, feed them',
                                            'after putting them back, feeding them'),
    'Bulsiewicz says to bring more and more kinds': (
        'the reader knows how to feed them: more and more kinds of plants, slowly, so the gut bacteria can adapt without '
        'gas and bloating, up to 30+ a week', 'how to do the step just named'),
    'Continue Pimentel\'s strict meal spacing': ('the reader knows to keep the meal spacing for good, and why',
                                                'the next step, a habit from Phase 2'),
    'And fuel the mitochondria': ('the reader knows the last step and where its fuels are explained', 'the last step'),
}
text = '\n\n'.join(b21[i]['text'].strip() for i in IDS)
(HERE / 'CHECK-r21-P5.txt').write_text(text, encoding='utf-8')
r = S.make(text, 'Phase 5: Restoration & Maintenance (Let\'s Play Gardener!)',
           'Someone whose overgrowth is finally cleared, deciding how to rebuild their gut bacteria so it doesn\'t come '
           'back: what to eat first, how to feed the new bacteria, and what to keep doing.', HIS, HIS_WHOSE)
for s in r['sentences']:
    if s.get('his'):
        continue
    hit = [v for k, v in NEW.items() if s['s'].startswith(k)] or ([OLD[s['s']]] if s['s'] in OLD else [])
    assert len(hit) >= 1, s['s'][:80]
    s['payoff'], s['follows'] = hit[0]
r['opens']['why_reading'] = ('It tells the reader this phase is for once they are clear of infection, the state they would '
                             'recognize, and what it is for: rebuilding so it doesn\'t come back.')
r['same_point'] = ('none: read Phase 5 from its heading to Phase 6: each step is said once; the yogurt\'s 36 hours, its two '
                   'bacteria and the 30 plants are said only here (SIBO, above, links to the yogurt without the recipe); '
                   'the fuels are a pointer to Leaky gut; the meal spacing points back to Phase 2')
r['questions'] = {
    'Q1': 'PASS: each step opens on its act (start by re-seeding; then feed the new healthy bacteria), and each term is '
          'explained in the sentence that first uses it: high-dose by the 36 hours against a store yogurt\'s 6 to 12, '
          'oxytocin as the "love hormone", bacteriocins as natural antibiotics',
    'Q2': 'PASS: each instruction is the reader\'s act: re-seed with the yogurt; bring plants back slowly, up to 30+ a week',
    'Q3': 'PASS: the yogurt, its fermenting time, its two bacteria and the number of plants are named exactly',
    'Q4': 'PASS: oxytocin, bacteriocins and high-dose are explained where first used; SIBO and the MMC were explained '
          'earlier (SIBO, Phase 2); each mechanism is said by what it does for the reader (heal the lining, kill SIBO, '
          'adapt without gas and bloating)',
    'Q5': 'PASS: "so this one ends up with" turns the fermenting time into the dose; "then" puts feeding after re-seeding; '
          '"go too fast and" gives the reason for "slowly"; "until" sets the goal',
    'Q6': 'PASS: nothing moved; the steps keep their order, and his aside still follows the number it jokes about',
    'Q7': 'PASS: each gloss answers what this reader would ask before doing the step: why 36 hours, what the bacteria do, '
          'why slowly',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence pair; the small words carry the relations (so, then, until); "6 to 12" takes its '
          '"hours" from the "36 hours" just before it',
}
r['placement'] = ('Phase 5, after Phase 4\'s pointers and before Phase 6; its first sentence picks up Phase 3 ("clear of '
                  'infection"), and "Davis is back" points to Phase 3, where Davis is first named.')
r['checked'] = [
    {'point': 'store yogurt is fermented for 6 to 12 hours, and 36 hours gives hundreds of times more bacteria',
     'found': 'Davis, Defiant Health Radio, "Will eating yogurt change your life?": "So in a factory they ferment or process '
              'the yogurt for about 6 to 12 hours", and his 36 hours gives "hundreds of times greater numbers of microbes '
              'than you get in conventional yogurt" (https://defianthealthradio.buzzsprout.com/1795054/episodes/'
              '16962045-will-eating-yogurt-change-your-life)',
     'still_needed': 'yes: it says what makes the yogurt high-dose, which the step names and doesn\'t explain',
     'fate': 'kept'},
    {'point': 'adding plants too fast can bring gas and bloating while the gut bacteria adapt',
     'found': 'Bulsiewicz, Plant Based News, 27 April 2025: a switch to a high-fiber diet can bring gas and bloating '
              'because the microbiome is adapted to the old food, "It\'s going to take time for your gut microbes to '
              'adapt" (https://plantbasednews.org/lifestyle/health/gut-doctor-survival-guide-bloating-plant-based-diet/)',
     'still_needed': 'yes: it is why the step says slowly', 'fate': 'kept'},
    {'point': 'oxytocin is called the "love hormone"', 'found': 'its common name in plain writing about it',
     'still_needed': 'yes: the step names oxytocin and a reader may not know it', 'fate': 'kept'},
]
(HERE / 'RECEIPT-r21-P5.json').write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
probs = S.check(text, r)
print('r21-P5', len(text.split()), 'words', 'PASS' if not probs else probs)
sys.exit(1 if probs else 0)
