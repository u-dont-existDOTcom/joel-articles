#!/usr/bin/env python3
"""The check text and making-sense receipt (gate E365, each sentence's link per neuro-2026-11-06b) for r32: r31 with
Joel's news about Pooyan (2026-11-07) as a sub-item of "Years of accumulated shit in your guts":
- r32-acc: that item with its four sub-items, the new one fourth, before the CAUTION.
His two sentences kept word for word are marked his; the rest of the new item is mine, written from his message.
Writes CHECK-r32-acc.txt and RECEIPT-r32-acc.json and checks them."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

HIS = ('Apparently he didn\'t need the insane treatments he was doing on himself. My other friend, Acacea, is also '
       'benefitting from this flower.')
HIS_WHOSE = ('his own: two sentences of his message of 2026-11-07, word for word ("Apparently he didn\'t need the insane '
             'treatments he was doing on himself." and "My other friend, Acacea, is also benefitting from this flower."), '
             'in the item he asked for about Pooyan')
OLD, LINK = {}, {}
for f in sorted(FIX.glob('r1[4-9]/**/RECEIPT-*.json')) + sorted(FIX.glob('r2[0-1]/**/RECEIPT-*.json')) + \
        sorted(FIX.glob('r2[3-9]/checks/RECEIPT-*.json')) + sorted(FIX.glob('r30/checks/RECEIPT-*.json')) + sorted(FIX.glob('r1[0-3]/**/RECEIPT-*.json')):
    for x in json.loads(f.read_text(encoding='utf-8')).get('sentences', []):
        if x.get('payoff'):
            OLD[x['s']] = (x['payoff'], x['follows'])
        if x.get('link'):
            LINK[x['s']] = x['link']
NEW = {
    'Years of accumulated shit in your guts': ('the reader learns the cause, that the books leave it out, and why it matters '
                                               'even if they eat well now', 'the next cause in the list'),
    'My friend Pooyan got incredibly healthier': ('the reader sees the cause in a friend\'s case: flushing the old impaction '
                                                  'made him healthier and happier', 'an example of the cause just named'),
    'This is likely caused by diverticulosis': ('the reader learns what may cause the impaction, diverticulosis, and what it '
                                                'is', 'why the stuff gets stuck'),
    'There\'s no known cure for this disease': ('the reader learns there is no known cure, only a possible one, glutamine, '
                                                'from one trial', 'what can be done about diverticulosis'),
    'Glutamine is an amino acid': ('the reader learns why glutamine could help', 'why the trial result makes sense'),
    '10% of people get side effects': ('the reader knows glutamine\'s side effects', 'the cost of trying it'),
    'Butyrate, a fatty acid': ('the reader learns the colon cells\' fuel, butyrate', 'the colon\'s counterpart to glutamine'),
    'I would also suggest diosmin': ('the reader gets one more thing to try, diosmin, and what it does',
                                     'Joel\'s own addition after the fuels'),
    'However, while we don\'t know if Pooyan has diverticulosis': (
        'the reader learns what Pooyan\'s relapse showed: A1 dairy took his peak health away',
        'back to Pooyan after the diverticulosis aside'),
    'CAUTION: If you have severe diverticulosis': (
        'the reader with severe diverticulosis knows colonic irrigation could rupture their intestine, and that clinics '
        'may turn them away', 'the danger of the treatment the item described'),
    'Make sure you get cleared first': ('the reader knows to see a gastroenterologist first, and what one is',
                                        'what to do about that danger'),
    'Update: Pooyan is actually all better now': ('the reader learns how Pooyan\'s story ends: he is well now, after gut '
                                                  'issues nobody could fix', 'the latest news after his relapse on A1 dairy'),
    'What worked was some Bombax ceiba flower': ('the reader learns what did help him, and what Bombax ceiba is',
                                                 'after the treatments he didn\'t need, the one that worked'),
    'It\'s sold on Amazon, cheap.': ('the reader knows where to get it and that it is cheap', 'where to find the flower'),
    'AskRigor, my research tool, is what told me about it': ('the reader knows how Joel found the flower and what AskRigor '
                                                             'is', 'where the idea came from'),
    'He picked its bacteria for what they do': ('the reader knows what the yogurt\'s two bacteria do for them, and what '
                                                'oxytocin and bacteriocins are', 'what the yogurt just named does'),
    'Or is it your bile?': ('the reader is asked whether bile is their problem, the second organ to check',
                            'the second organ to check, after the pancreas'),
    'If too much of it reaches your colon': ('the reader knows what happens when too much bile reaches the colon, and the '
                                             'name for it, Bile Acid Diarrhea', 'what the question is asking about'),
    'Get a SeHCAT test for it': ('the reader knows the test to get, and to take bile binders if it comes back positive',
                                 'how to find out, and what to do'),
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
    'If too much of your bile is reaching your colon': (
        'the reader knows the second organ case, what Bile Acid Diarrhea is, and that Brown has them tested with SeHCAT '
        'and put on bile binders', 'the second organ to check, after the pancreas'),
    'Do your stools look oily or greasy?': ('the reader can tell from their own stools whether the pancreas is worth '
                                            'checking', 'the check\'s first question, about their own case'),
    'So check your organs, starting with your pancreas': (
        'the reader knows to check their organs, starting with the pancreas, and how they would test for and treat '
        'Exocrine Pancreatic Insufficiency', 'after "the problem is likely an organ", which organ first'),
    'So check your organs.': ('the reader knows the next step is checking their organs', 'after "the problem is likely an '
                              'organ", what to do about it'),
    'Then it\'s often your pancreas not making enough digestive enzymes': (
        'the reader knows what oily stools often mean, and the name doctors give it', 'what the answer to the question means'),
    'A Stool Elastase test will tell you': ('the reader knows the test that tells, and to take high-dose enzymes with every '
                                            'meal if it\'s positive', 'how to find out, and what to do'),
    'If it\'s diarrhea that keeps coming back instead': (
        'the reader with recurring diarrhea knows Brown\'s other organ case and what happens in it',
        'the second case, after the pancreas'),
    'He has you tested for that with SeHCAT': ('the reader knows the test for it and what the binders do',
                                              'how to find out, and what helps'),
    'So check your organs (Brown), starting with your pancreas': (
        'the reader knows to check their organs, starting with the pancreas, and how they would test for and treat '
        'Exocrine Pancreatic Insufficiency', 'after "the problem is likely an organ", which organ first'),
}
NEW_LINKS = {
    'My friend Pooyan got incredibly healthier': 'to flush that stuff out',
    'This is likely caused by diverticulosis': 'This is likely caused by',
    'There\'s no known cure for this disease': 'this disease',
    'Glutamine is an amino acid': 'so this makes some sense',
    '10% of people get side effects': 'from it',
    'Butyrate, a fatty acid': 'the fuel for the colon cells',
    'I would also suggest diosmin': 'also',
    'However, while we don\'t know if Pooyan has diverticulosis': 'However, while we don\'t know if Pooyan has diverticulosis',
    'CAUTION: If you have severe diverticulosis': 'If you have severe diverticulosis',
    'Make sure you get cleared first': 'cleared first',
    'Update: Pooyan is actually all better now': 'Update: Pooyan',
    'What worked was some Bombax ceiba flower': 'What worked was',
    'It\'s sold on Amazon, cheap.': 'It\'s',
    'AskRigor, my research tool, is what told me about it': 'told me about it',
    'He picked its bacteria for what they do': 'He picked its bacteria',
    'Or is it your bile?': 'Or is it',
    'If too much of it reaches your colon': 'If too much of it',
    'Get a SeHCAT test for it': 'for it, and if it comes back positive',
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
    'If too much of your bile is reaching your colon': 'If too much of your bile',
    'Do your stools look oily or greasy?': 'none: the check\'s first question, asked about the reader\'s own case',
    'Then it\'s often your pancreas not making enough digestive enzymes': 'Then',
    'A Stool Elastase test will tell you': 'will tell you, and if that\'s it',
    'If it\'s diarrhea that keeps coming back instead': 'instead',
    'He has you tested for that with SeHCAT': 'He has you tested for that',
    'So check your organs (Brown).': 'So check',
    'So check your organs.': 'So check',
    'So check your organs, starting with your pancreas': 'So check your organs, starting with',
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
    'Q9': 'PASS: one step per sentence; the small words carry the relations (starting with, or, if, and if, then, as in)',
}
CHECKED = json.loads((FIX / 'r23' / 'checks' / 'RECEIPT-r23-P36.json').read_text(encoding='utf-8'))['checked']
for c in CHECKED:
    if c['point'].startswith('Bile Acid Diarrhea'):
        c['point'] = 'Bile Acid Diarrhea is too much bile reaching the colon, which gives you diarrhea'
CHECKED.insert(0, {'point': 'oxytocin is a bonding hormone', 'found': 'Cleveland Clinic, "Oxytocin": its roles include '
                   'trust, romantic attachment and parent-infant bonding, and the "love hormone" nickname comes from them '
                   '(https://my.clevelandclinic.org/health/articles/22618-oxytocin); Joel, 2026-11-07: "oxytocin is a '
                   'bonding hormone not the love hormone exactly"', 'still_needed': 'yes: it says what oxytocin is where '
                   'the step names it', 'fate': 'changed'})
b = sr.blocks((FIX / 'r32' / 'r32.md').read_text(encoding='utf-8'))
H = {k: next(i for i, x in enumerate(b) if x['kind'].startswith('h') and x['text'].startswith(k))
     for k in ('Phase 3', 'Phase 4', 'Phase 6', 'Optional Ready-Made')}
START = next(i for i, x in enumerate(b) if x['text'].startswith('This protocol is meant'))
body = lambda a, z: [i for i in range(a, z) if not b[i]['kind'].startswith('h')]
P36 = body(H['Phase 3'] + 1, H['Optional Ready-Made'])
P4 = H['Phase 4'] + 1
assert b[P4]['text'].startswith('Benjamin Brown') and 'So check your organs, starting with your pancreas' in b[P4]['text']
ACC = list(range(9, 14))
assert b[ACC[0]]['text'].startswith('Years of accumulated shit') and b[ACC[3]]['text'].startswith('Update: Pooyan') \
    and b[ACC[4]]['text'].startswith('CAUTION')
TEXTS = {
    'r32-acc': (ACC, 'Some Causes of poor gut health',
                'Someone with gut trouble reading Joel\'s list of causes, deciding whether old impaction could be theirs and '
                'what his friend\'s story says about it.',
                'It names the cause, says it isn\'t in the books, and tells the reader why it matters even if they eat '
                'well now.'),
}
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
    r['same_point'] = ('none: read the causes section from its heading to the next for Pooyan\'s story and the old impaction: '
                       'each told once, here; Phase 3 mentions him only for candibactin' if name == 'r32-acc' else 'none: read the protocol from its first line to the stacks: each phase\'s steps are said once; '
                       'Phase 5\'s meal spacing points to Phase 2 for its reason; berberine and the yogurt point to '
                       'Parasites and SIBO; the fuels point to Leaky gut; his notes point back to the causes')
    if name == 'r32-acc':
        r['checked'] = [
            {'point': 'Bombax ceiba is the red silk-cotton tree', 'found': 'Flora of Qatar, "Bombax ceiba": common names '
             '"Kapok, red cotton tree, red silk-cotton" (https://www.floraofqatar.com/bombax_ceiba.htm)',
             'still_needed': 'yes: a reader won\'t know the Latin name', 'fate': 'kept'},
            {'point': 'Pooyan is well now; the flower worked, not the treatments; it is cheap on Amazon; AskRigor found it; '
             'Acacea is benefitting too', 'found': 'Joel\'s message of 2026-11-07, his own report of his friends\' cases',
             'still_needed': 'yes: it is the news he asked to add', 'fate': 'kept'}]
        r['questions'] = {
            'Q1': 'PASS: the new sub-item opens on its point ("Update: Pooyan is actually all better now"), then says what '
                  'he didn\'t need and what worked',
            'Q2': 'N/A: the new sub-item reports a friend\'s recovery and gives no instruction; the CAUTION after it is '
                  'unchanged',
            'Q3': 'PASS: the flower is named exactly (Bombax ceiba, from the red silk-cotton tree), with where it is sold and '
                  'what found it (AskRigor)',
            'Q4': 'PASS: Bombax ceiba and AskRigor are explained where first used; glutamine is his old order, in late_ok',
            'Q5': 'PASS: each new sentence\'s tie is in its words (the links field), or it is his own sentence',
            'Q6': 'PASS: the new sub-item follows the relapse it updates and comes before the CAUTION; nothing else moved',
            'Q7': 'PASS: it tells the reader what helped Pooyan and where to find it; the CAUTION still says to get cleared '
                  'first',
            'Q8': 'PASS: no item moved between groups',
            'Q9': 'PASS: one point per sentence; the small words carry the relations (Apparently, What worked was, also)'}
        r['late_ok'] = {'Glutamine': 'his own text, unchanged by this update: the trial sentence names glutamine as the '
                                     'possible cure and the next one says what it is; the new sub-item is what this '
                                     'check is for'}
    if name != 'r32-acc':
        r['questions'] = dict(Q)
    r['placement'] = ('The causes list\'s item on old impaction with its sub-items, in the article\'s order.' if name == 'r32-acc' else
                      'The protocol\'s phases in the article\'s order, without their headings, as his extension reads them.')
    if name != 'r32-acc':
        r['checked'] = CHECKED
    (HERE / ('RECEIPT-%s.json' % name)).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    probs = S.check(text, r)
    bad += bool(probs)
    print(name, len(text.split()), 'words', 'PASS' if not probs else probs)
sys.exit(1 if bad else 0)
