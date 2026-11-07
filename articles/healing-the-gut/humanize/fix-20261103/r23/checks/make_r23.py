#!/usr/bin/env python3
"""The check texts and making-sense receipts (gate E365, with each sentence's link, neuro-2026-11-06b) for this round's
section checks (gate gut-2026-11-07a: the stretches that tested AI are fixed until they test Human, before any
whole-article check):
- r23-P45: Phase 4 and Phase 5 of r23 (blocks 58-60 and 62-67), the cut that read Phase 5's steps AI unchanged (#186);
- r23-P36: Phases 3 to 6 of r23 (blocks 50-56, 58-60, 62-67, 69-72), the cut that read Phases 4 to 6 AI unchanged (#187);
- r21-P45: try 3 (../../r21/) in the cut of Phases 4 and 5, where it hasn't been checked.
All without headings, as his extension reads the post. Payoffs that earlier receipts had come from them; links are new for
every receipt from 2026-11-06 23:01 UTC. His own aside, "Does anyone count their plants?", is marked his. Writes
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
OLD = {}
for f in sorted(FIX.glob('r1[4-9]/**/RECEIPT-*.json')) + sorted(FIX.glob('r2[0-1]/**/RECEIPT-*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')).get('sentences', []):
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
NEW = {
    'And if bile is spilling into your colon': (
        'the reader knows the second organ case, what Bile Acid Diarrhea is, and how they would test for it and treat it',
        'the second organ to check, after the pancreas'),
    'Cleared the infection?': ('the reader knows this phase is for them once the infection is cleared',
                               'opens Phase 5, after Phase 4\'s notes; picks up Phase 3\'s purge'),
    'Then it\'s time to rebuild a diverse ecosystem': (
        'the reader knows what this phase is for: rebuilding their gut\'s bacteria so the overgrowth doesn\'t come back',
        'after the question that names their case, what to do about it'),
    'Start by re-seeding your gut': ('the reader knows the first step, which yogurt, and that they make it at home over '
                                     '36 hours', 'the first step of the rebuilding'),
    'He picked its bacteria for what they do': ('the reader knows what the yogurt\'s two bacteria do for them, and what '
                                                'oxytocin and bacteriocins are', 'what the yogurt just named does'),
    'Then feed the new healthy bacteria with plants': (
        'the reader knows the second step: feed the new bacteria with plants, a few new kinds at a time, up to 30+ a week',
        'after putting the bacteria back, feeding them'),
    'Keep spacing your meals 4+ hours apart': ('the reader knows to keep Phase 2\'s meal spacing for good',
                                               'the next step, a habit from Phase 2'),
}
LINKS = {
    'This one is from Dr. William Davis': 'This one',
    'AVOID most herbal antibiotics': 'even though Davis recommends',
    'H2O2 actually works better': 'better than the herbal antibiotics',
    'My BFF Pooyan tried candibactin': 'tried candibactin',
    'The H2O2 worked a lot better': 'The H2O2 worked a lot better',
    'There is one herbal antibiotic': 'one herbal antibiotic that works really well tho',
    'If you have an acute infection with something': 'that H2O2 and berberine don\'t clear quickly',
    'BIND the toxins': 'die-off toxins',
    'At the same time, take Ruscio\'s Triple': 'At the same time',
    'That\'s to maintain diversity': 'That\'s to',
    'And if all that failed': 'And if all that failed',
    'That\'s a 2-3 week liquid-only diet': 'That\'s a',
    'My notes: the H2O2 swap above': 'the H2O2 swap above',
    'For berberine and H. pylori see Parasites': 'none: his notes\' pointers, each naming the topic it points from',
    'Benjamin Brown (Digestive Health Solution)': 'this phase',
    'If even the "Nuclear Option" failed': 'If even the "Nuclear Option" failed',
    'The problem is likely an organ': 'The problem is likely',
    'So check your organs (Brown).': 'So check',
    'If your pancreas doesn\'t make enough': 'If your pancreas',
    'And if bile is spilling into your colon': 'And if',
    'If it\'s Bile Acid Diarrhea, the test is SeHCAT': 'If it\'s',
    'My notes: two things the books don\'t cover': 'the books don\'t cover',
    'Cleared the infection?': 'Cleared the infection',
    'Then it\'s time to rebuild a diverse ecosystem': 'Then it\'s time',
    'Once you\'re clear of infection,': 'Once you\'re clear of infection',
    'Dr. William Davis is back': 'is back for that',
    'Start by re-seeding': 'Start by',
    'He picked its bacteria for what they do': 'He picked its bacteria',
    'It contains L. reuteri': 'It contains',
    'Then feed the new healthy bacteria with plants': 'Then feed the new healthy bacteria',
    'Then feed the new healthy bacteria.': 'Then feed',
    'Bulsiewicz says to bring more and more kinds': ('none: the how of the step just named, with the tie left out of the '
                                                     'words (the weakness neuro-2026-11-06b names; try 4 says it)'),
    'Keep spacing your meals 4+ hours apart': 'as in Phase 2',
    'Continue Pimentel\'s strict meal spacing': 'from Phase 2',
    'And fuel the mitochondria': 'And fuel',
    'My notes: see "Leaky gut" above': 'none: his notes close each phase with pointers, under their label',
    'The last phase is from Neil Nathan': 'The last phase',
    'It\'s for people who are': 'It\'s for people who',
    'Check your environment (Nathan).': 'none: the phase\'s first step, which the reader expects after who it is for',
    'Could it be mold/mycotoxins, or Lyme?': 'Could it be',
    'Get assessed for those': 'Get assessed for those',
    'Then check the brain.': 'Then',
    'If you react to everything, Hopper says': 'If you react to everything',
    'My notes: Matt\'s note on mopping up': 'mopping up mycotoxins',
}
Q = {
    'Q1': 'PASS: each changed sentence gives its point first: the reader\'s case as a question, then what to do; the yogurt '
          'step, then what its bacteria do; feeding the bacteria with plants, then how; the second organ case, then its '
          'test and treatment; each term (Bile Acid Diarrhea, oxytocin, bacteriocins) explained where first used',
    'Q2': 'PASS: each instruction is the reader\'s act: test and treat, re-seed, feed with plants, keep spacing meals',
    'Q3': 'PASS: the organs, tests, treatments, yogurt, bacteria and number of plants are named exactly',
    'Q4': 'PASS: Bile Acid Diarrhea, oxytocin and bacteriocins are explained where first used; Exocrine Pancreatic '
          'Insufficiency, SIBO and the MMC earlier; each by what it does for the reader',
    'Q5': 'PASS: each link is in the sentence\'s words (the links field): "And if", "Cleared the infection? Then", "He picked '
          'its bacteria", "Then feed", "as in Phase 2"',
    'Q6': 'PASS: nothing moved; each phase keeps its order, and his aside still follows the number it jokes about',
    'Q7': 'PASS: each change tells the reader what to do in their case, and why where they would ask',
    'Q8': 'PASS: no item moved between groups',
    'Q9': 'PASS: one step per sentence; the small words carry the relations (and if, then, so, as in)',
}
CHECKED = [
    {'point': 'Bile Acid Diarrhea is bile spilling into the colon and giving you diarrhea',
     'found': 'NICE DG44: bile acids that aren\'t absorbed properly travel to the colon, and excess bile there causes '
              'diarrhoea (https://nice.org.uk/guidance/dg44/documents/topic-description)',
     'still_needed': 'yes: it says what the second organ case is', 'fate': 'kept'},
    {'point': 'Davis picked the yogurt\'s bacteria for what they do, and bacteriocins are natural antibiotics that kill SIBO',
     'found': 'Davis, Defiant Health Radio, "Here\'s a microbe you should know about: Bacillus subtilis": the original SIBO '
              'yogurt specified L. reuteri, L. gasseri and B. coagulans, chosen to colonize the small intestine and make '
              'bacteriocins, "natural peptide antibiotics effective in killing the species of SIBO" (https://www.buzzsprout'
              '.com/1795054/episodes/17783323-here-s-a-microbe-you-should-know-about-bacillus-subtilis)',
     'still_needed': 'yes: it is what the yogurt is for', 'fate': 'kept'},
    {'point': 'step 3\'s reason, the MMC sweeping the gut clean, is said in Phase 2',
     'found': 'Phase 2: "Pimentel wants meals 4-5 hours apart, strictly, so the Migrating Motor Complex (MMC) gets to sweep '
              'your gut clean in between"', 'still_needed': 'no: Phase 2 says it; step 3 keeps "forever" and points there',
     'fate': 'cut'},
]
TEXTS = {
    'r23-P45': ('r23', [58, 59, 60, 62, 63, 64, 65, 66, 67], 'Phase 4: The Investigation',
                'Someone whose symptoms survived the diets, the purge and the Elemental Diet, deciding what to check next '
                'and how to rebuild once the infection is gone.'),
    'r23-P36': ('r23', [i for i in range(50, 73) if i not in (57, 61, 68)], 'Phase 3: The Purge',
                'Someone partway through the protocol, deciding how to clear the overgrowth, what to check if that fails, '
                'and how to rebuild once it is gone.'),
    'r21-P45': ('r21', [58, 59, 60, 62, 63, 64, 65, 66, 67], 'Phase 4: The Investigation',
                'Someone whose symptoms survived the diets, the purge and the Elemental Diet, deciding what to check next '
                'and how to rebuild once the infection is gone.'),
}
bad = 0
for name, (src, ids, section, reader) in TEXTS.items():
    b = sr.blocks((FIX / src / (src + '.md')).read_text(encoding='utf-8'))
    assert not any(b[i]['kind'].startswith('h') for i in ids), name
    text = '\n\n'.join(b[i]['text'].strip() for i in ids)
    (HERE / ('CHECK-%s.txt' % name)).write_text(text, encoding='utf-8')
    r = S.make(text, section, reader, HIS, HIS_WHOSE)
    for n, s in enumerate(r['sentences']):
        if s.get('his'):
            continue
        hit = [v for k, v in NEW.items() if s['s'].startswith(k)] or ([OLD[s['s']]] if s['s'] in OLD else [])
        assert hit, (name, s['s'][:80])
        s['payoff'], s['follows'] = hit[0]
        if 'link' in s:
            lk = [v for k, v in LINKS.items() if s['s'].startswith(k)]
            assert lk, (name, 'link', s['s'][:80])
            s['link'] = lk[0]
    r['opens']['why_reading'] = (
        'It tells the reader whose phase this is and that it is for them if even the Elemental Diet failed, the case they '
        'would recognize.' if src == 'r23' and name.endswith('P45') or name == 'r21-P45' else
        'It tells the reader the purge is for them if diet didn\'t clear their symptoms, the case they would recognize.')
    r['same_point'] = ('none: read Phases 3 to 6 from their headings to the stacks: each phase\'s steps are said once; '
                       'step 3 of Phase 5 points to Phase 2 for the meal spacing\'s reason instead of saying it again; '
                       'berberine and the yogurt are pointers to Parasites and SIBO; the fuels point to Leaky gut')
    r['questions'] = dict(Q)
    if name == 'r21-P45':
        r['questions']['Q5'] = ('PASS: the links field quotes each sentence\'s tie; the plants sentence has none in its '
                                'words, said so in its link (what try 4 changes)')
        r['questions']['Q1'] = ('PASS: each term is explained where first used (high-dose by the 36 hours, oxytocin, '
                                'bacteriocins); each step opens on its act')
    r['placement'] = 'The phases in the article\'s order, without their headings, as his extension reads them.'
    r['checked'] = CHECKED if src == 'r23' else []
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, len(text.split()), 'words', 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
