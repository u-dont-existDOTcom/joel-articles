#!/usr/bin/env python3
"""The check texts and making-sense receipts (gate E365) for r19's changed stretches, each checked with what it leans on
(E349) and without headings, as his extension reads the post:
- r19-P45: Phase 4 and Phase 5 (blocks 58-60 and 62-67). The whole-article check read Phase 5's first steps Low and
  Phase 4's second organ case Medium (#183), while each phase alone read High (#165, #176), so they are checked together.
- r19-D: the glutamine paragraph with its dose paragraph (27-28), for the two clarity fixes.
Payoffs for sentences earlier receipts already had come from them; the new ones are here. Under E373 the article's
sentences are the model's words he humanized, so each gets a payoff, except his own aside, "Does anyone count their
plants?". Writes CHECK-<name>.txt and RECEIPT-<name>.json and checks each."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R19 = HERE.parent
FIX = R19.parent
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

b19 = sr.blocks((R19 / 'r19.md').read_text(encoding='utf-8'))
TEXTS = {'r19-P45': [58, 59, 60, 62, 63, 64, 65, 66, 67], 'r19-D': [27, 28]}
assert b19[58]['text'].startswith('Benjamin Brown') and b19[62]['text'].startswith('Once you')
assert b19[27]['text'].startswith('L-Glutamine') and b19[28]['text'].startswith('Take 5g')
HIS = 'Does anyone count their plants?'
HIS_WHOSE = ('his own: "Does anyone count their plants?", the aside he added to his own version of Phase 5 '
             '(2026-11-03), not a rewrite of the model\'s text')
OLD = {}
for f in sorted(FIX.glob('r1[4-8]/**/RECEIPT-*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')).get('sentences', []):
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
NEW = {
    'If it\'s Bile Acid Diarrhea instead,': (
        'the reader knows the second case, what Bile Acid Diarrhea is, the test that shows it and the treatment',
        'the second organ to check'),
    'Once you\'re clear of infection,': ('the reader knows when this phase starts and what it is for: rebuilding, so it '
                                        'doesn\'t come back', 'opens Phase 5, after Phase 4\'s pointers'),
    'Dr. William Davis is back': ('the reader knows whose advice this phase is', 'after what the phase is for, whose it is'),
    'Start by re-seeding your gut': ('the reader knows the first step, what the yogurt\'s two bacteria do for them, and '
                                     'what bacteriocins are', 'the first step of the rebuilding'),
    'Then feed the new bacteria with plants': ('the reader knows the second step, how to bring plants back, and how many '
                                               'to aim for', 'once the bacteria are back, feeding them'),
    'Continue Pimentel\'s strict meal spacing': ('the reader knows to keep the meal spacing for good, and why',
                                                'the next step, a habit from Phase 2'),
    'And fuel the mitochondria': ('the reader knows the last step and where its fuels are explained', 'the last step'),
    'L-Glutamine (watch Dr. Rhonda vid)': ('the reader learns what glutamine is for: fuel for their gut lining and immune '
                                           'cells', 'opens the glutamine paragraph under the fuels'),
    'It doesn\'t have to go through': ('the reader learns why it works fast: no digestion needed', 'how it fuels them'),
    'Inside the mitochondria, it gets converted': ('the reader learns how the cells turn it into energy',
                                                   'the step after it is absorbed'),
    'They then use their extra energy': ('the reader learns what the energy does: repairs the lining and keeps LPS out',
                                         'what the energy is used for'),
    'Glutamine also provides nitrogen': ('the reader learns glutamine also builds new cells', 'its other use'),
    'Up to 14g a day is known to be safe': ('the reader knows how long the high dose is safe, and to come back down once '
                                            'the exposure or the stress is over', 'the limit on the high dose'),
    'If you have an active inflammatory bowel disease': ('the reader with active Crohn\'s or colitis knows not to count on '
                                                         'glutamine', 'the case where it doesn\'t help'),
}
READER = {
    'r19-P45': 'Someone whose symptoms survived the diets, the purge and the Elemental Diet, deciding what to check next and '
               'how to rebuild once the infection is gone.',
    'r19-D': 'Someone with a leaky or worn-down gut lining, deciding whether to take glutamine, how much, and when not to.',
}
OPENS = {
    'r19-P45': 'It tells the reader whose phase this is; the next sentence says it is for them if even the Elemental Diet '
               'failed, which is the case they would recognize.',
    'r19-D': 'It tells the reader what glutamine does for them, fuel for their gut lining and immune cells, before how it '
             'works.',
}
SAME = {
    'r19-P45': 'none: read Phase 4 and Phase 5 from their headings to Phase 6: the organ cases are named once; Phase 5\'s '
               'fuels are a pointer to the paragraph under Leaky gut; the meal spacing points back to Phase 2',
    'r19-D': 'none: read the fuels under Leaky gut from "Mitochondrial" to the butyrate paragraph: glutamine\'s mechanism and '
             'its dose are each said once; Phase 5 points back here',
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first: the yogurt step then what its bacteria do; feeding the '
          'bacteria then how; the second organ case then its test and treatment; the dose limit then when to come down',
    'Q2': 'PASS: each instruction is the reader\'s act: re-seed, feed with plants, add plants back slowly, come back down',
    'Q3': 'PASS: the bacteria, the test and the treatment are named exactly; "30 or more kinds a week" keeps the number',
    'Q4': 'PASS: bacteriocins and Bile Acid Diarrhea are explained where they are first used; SIBO and the MMC were '
          'explained earlier; "it" in the dose lines is now "the exposure or the stress" and "glutamine"',
    'Q5': 'PASS: the colons join each step to what it does; "instead" turns the second organ case against the first',
    'Q6': 'PASS: nothing moved; the steps keep their order',
    'Q7': 'PASS: each change tells the reader what to do or what a term means for them',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence; the small words carry the relations (its, then, instead, once)',
}
CHECKED = [{'point': 'bile acid diarrhoea: bile acids not absorbed reach the colon and cause diarrhoea; SeHCAT measures it',
            'found': 'NICE DG44 topic description: when bile acids are not absorbed properly, they travel to the colon, and '
                     'excess bile there causes diarrhoea; SeHCAT is a capsule that measures how well the body absorbs bile '
                     'acids (https://nice.org.uk/guidance/dg44/documents/topic-description)',
            'still_needed': 'yes: the reader was given the name and no meaning', 'fate': 'kept'},
           {'point': 'bacteriocins are substances bacteria make that kill other bacteria',
            'found': 'the word as the article already uses it ("bacteriocins that kill SIBO"); "natural antibiotics" says it '
                     'in plain words, no new claim', 'still_needed': 'yes: the term was unexplained', 'fate': 'kept'}]
PLACEMENT = {
    'r19-P45': 'Phase 4 then Phase 5, in the article\'s order; Phase 5\'s steps keep theirs.',
    'r19-D': 'The glutamine paragraph and its dose under the fuels, as before.',
}
ok = True
for name, ids in TEXTS.items():
    t = '\n\n'.join(b19[i]['text'].strip() for i in ids)
    (HERE / ('CHECK-%s.txt' % name)).write_text(t, encoding='utf-8')
    his = HIS if HIS in t else ''
    r = S.make(t, b19[ids[0]].get('section', ''), READER[name], his, HIS_WHOSE if his else '')
    for s in r['sentences']:
        if s.get('his'):
            continue
        hit = [v for k, v in NEW.items() if s['s'].startswith(k)] or ([OLD[s['s']]] if s['s'] in OLD else [])
        assert len(hit) == 1, (name, s['s'][:80])
        s['payoff'], s['follows'] = hit[0]
    r['opens']['why_reading'] = OPENS[name]
    r['same_point'] = SAME[name]
    r['questions'], r['placement'], r['checked'] = dict(Q), PLACEMENT[name], CHECKED
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(t, r)
    ok = ok and not probs
    print(name, len(t.split()), 'words', 'PASS' if not probs else probs)
sys.exit(0 if ok else 1)
