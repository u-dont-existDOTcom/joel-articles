#!/usr/bin/env python3
"""The making-sense receipts for the two checks of his new opening of "Primal attraction" (r40/HIS-T9.json, his message of
2026-11-24 16:23 UTC): his words, with obvious corrections only. Each sentence's payoff, why it follows and the words that
tie it on, as I read them; his words need no rewrite read (the fresh sense read is r40/sense/)."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[5]
HIS = 'PASS: his words, as he wrote them in his message of 2026-11-24 16:23 UTC (obvious corrections only)'
S52 = [
    ('the section turns from the fairness the article has argued for to what keeps desire going', 'the section heading', None),
    ('they see the question the section answers: fairness doesn\'t explain why two people keep wanting each other',
     'it says what the fairness of the sentence before leaves out', 'I do believe in that'),
    ('safety makes room for desire but doesn\'t start it', 'it starts his answer with safety, the part of fairness he keeps',
     'For me, feeling safe'),
    ('one thing safety lets in: telling each other fantasies without fear', 'an example of the room safety gives',
     'When I feel safe'),
    ('a second thing safety lets in: enjoying the thought of making a baby', 'another example of the same room',
     'We can imagine pregnancy'),
    ('fear does the opposite: it made the sex boring', 'the other side of the enjoyment just described',
     'Whenever I was scared'),
    ('the puzzle: if safety helps, why does advice push distance', 'it asks why advice says the opposite of what he found',
     'So why is it'),
    ('his answer: the distance stands in for difference', 'it answers the question before', 'I suspect they are'),
    ('the rule he draws: the closer two people are, the more polarity they need', 'it widens his answer into a rule',
     'The more safety there is'),
    ('one example of that polarity: women wanting a man who is dangerous, but to others', 'an example of the polarity just named',
     'One controversial example of'),
    ('the old story everyone knows shows the same wish', 'it illustrates the wish just named',
     'none: the fairy tale is the example of the wish just named, and its title says so'),
    ('it explains shit-testing as a woman testing whether her man is powerful', 'a consequence of the same wish',
     'And this can sometimes'),
    ('an evolutionary reason for the wish, from the video above', 'it says why women would have the wish just described',
     'One evolutionary reason for this'),
    ('the selection behind it: women not drawn to powerful men had fewer children', 'it finishes the war-bride reasoning',
     'So the women who'),
    ('what Cooper concludes for men: women trade up, so stand out', 'what the video draws from that reason',
     'Cooper tells men that'),
    ('how many men react: they give up on romance', 'the reaction to the advice just given', 'As you can see'),
    ('how far it has gone, South Korea as the extreme', 'it widens from the comments to whole societies',
     'And the gender wars'),
]
S53 = [
    ('his view of Cooper: partly right, but not far enough', 'it answers the depressing take that ends the paragraph before',
     None),
    ('why Cooper\'s way stops working: anyone can copy it', 'it says how Cooper doesn\'t go far enough',
     'Anyone can watch his video'),
    ('it is posturing, as Cooper\'s own photo shoots show', 'the second thing wrong with it', 'But that\'s superficial posturing'),
    ('his answer: stand out by being yourself, where there\'s no competition', 'the alternative to posturing',
     'I believe the real way'),
    ('the reason, as a joke', 'why there\'s no competition there', 'Nobody can ever beat me'),
    ('the objection that this isn\'t what attracts most women, and why he doesn\'t mind', 'the counter-argument to his answer',
     'Cooper might retort'),
    ('what he has seen attract women: the confidence of deep relaxation', 'it turns from conceding to what he has seen',
     'On the other hand'),
    ('his evidence: women stopping their cars when he was most relaxed', 'an example of what he has noticed',
     'When I\'ve been at'),
    ('the deeper key: the nastiness in us is dust over a gem', 'it widens from attraction to life in general',
     'none: it opens a new paragraph that widens from attraction to life in general'),
    ('how to get past it: through the heart', 'it says how to reach the gem just named', 'It is by touching'),
    ('what that maturity did to his attraction: far more selective', 'what touching the heart changes in who attracts him',
     'It doesn\'t mean we'),
    ('the cost he accepts: alone rather than settling', 'it answers the objection to being so selective',
     'And while it\'s hard'),
    ('his conclusion against Cooper: the best mate knows you can\'t be replaced', 'it sums up his answer to Cooper',
     'So while Cooper thinks'),
    ('where he does agree with Cooper, which leads into the roles that follow', 'it closes his objections and turns to roles',
     'Having explained my objections'),
]
WHY = {'52': 'It asks why two people keep wanting each other when fairness can\'t explain it.',
       '53': 'It says where Cooper\'s answer falls short and what stands out instead.'}
for k, FILL in (('52', S52), ('53', S53)):
    text = next((HERE.parent / 'checks').glob('CHECK-r40-%s-*.txt' % k))
    out = HERE / ('R-%s.json' % k)
    subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'make', str(text), '--section',
                    'Primal attraction: channeling the Divine Masculine & Feminine', '--reader',
                    'Someone in or wanting a relationship who wonders why safety and fairness don\'t keep desire alive, '
                    'and what to make of the manosphere\'s answer', '--out', str(out)], check=True, capture_output=True)
    R = json.loads(out.read_text(encoding='utf-8'))
    assert len(R['sentences']) == len(FILL), (k, len(R['sentences']), len(FILL))
    for s, (pay, fol, link) in zip(R['sentences'], FILL):
        s['payoff'], s['follows'] = pay, fol
        if link is not None:
            s['link'] = link
    R['placement'] = 'His new opening of the section (his paste of 2026-11-24 16:23 UTC), part %s of 2 of its check' % (
        1 if k == '52' else 2)
    R['opens']['why_reading'] = WHY[k]
    R['same_point'] = ('none: read the section from its heading to the next for safety and desire, polarity, the '
                        'dangerous-man wish, Cooper\'s hypergamy and standing out; each is made once, here')
    R['needed'] = {'reader': 'his own words; the fresh sense read of them (r40/sense, all three planted errors found) '
                             'found nothing to change in them', 'unneeded': [], 'kept': {}}
    R['his_fixes'] = {'reader': 'N/A: his own words, as he wrote them; the brief reads my text', 'marked': [], 'kept': {}}
    R['fit'] = {'reader': 'N/A: his own words, as he wrote them; the fit read is for my text', 'marked': [], 'kept': {}}
    R['questions'] = {q: HIS for q in R['questions']}
    out.write_text(json.dumps(R, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    r = subprocess.run([sys.executable, str(ROOT / 'tools/humanization/sense_receipt.py'), 'check', str(text), str(out)],
                       capture_output=True, text=True)
    print(k, (r.stdout + r.stderr).strip().replace('\n', ' | ')[:900])
