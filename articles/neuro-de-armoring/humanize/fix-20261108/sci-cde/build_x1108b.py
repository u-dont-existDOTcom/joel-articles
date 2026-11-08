"""Neuro De-Armoring Cards, 8 November (2): the science of sections C, D and E, and the relational-density figure.

Texts in texts_cde.py, the claims and sources in SCIENCE-CDE.md, the fresh readers' needed reads in needed/<key>/READ.md.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-cde/build_x1108b.py
"""
import datetime
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_cde as T  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/sci-cde/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
READER = ('someone with trauma or in withdrawal who is anxious, wired, numb or foggy, wanting to know what is going on in '
          'their brain and which of the protocol\'s tools does what')
FRESH = 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph (needed/%s/READ.md)'

Q_ANS = {
    'Q1': 'PASS: each sentence opens on its point',
    'Q2': 'N/A: no instruction here, or the one instruction says what it is for',
    'Q3': 'PASS: each thing is named exactly',
    'Q4': 'PASS: each unfamiliar term is said in plain words where it is first used',
    'Q5': 'PASS: each "and", "so" and "but" turns on the clause before it',
    'Q6': 'PASS: the claim, then what the evidence shows, then its limit',
    'Q7': 'PASS: each fact is about the reader\'s own symptom or the tool they are deciding on',
    'Q8': 'N/A: no group or list inside this paragraph',
    'Q9': 'PASS: one step a clause, with the small words that carry the relation kept',
}

SPEC = {
    'S24': dict(
        pays=['they learn how far short of what they need their social world is', 'they hear the empty feeling is real',
              'they learn why going back to a lonely life won\'t hold after de-armoring', 'they learn what to build'],
        checked=[('less than 1/24th of the relational density our biology requires',
                  'Perry\'s own figure is one-sixteenth (four mature people per young child then, one adult per four '
                  'children now); 1/24th is from a training summary of his work',
                  'yes: they learn how far short their social world is, by the figure its author gives')],
        unneeded=['The "Void" you feel is real.'],
        kept={'The "Void" you feel is real.': 'they hear that the empty feeling they have is real, the feeling the rest '
              'of the paragraph tells them how to answer'}),
    'S47': dict(
        pays=['they hear the failure was not theirs', 'they learn what the Prozac finding actually was',
              'they learn SSRIs help some people and not others', 'they learn the side effects that also make people quit'],
        checked=[('Ipser & Stein 2012 showed Prozac had zero effect on male combat veterans with calcified PTSD',
                  'the no-better-than-placebo result is Hertzberg 2000, 12 male combat veterans; later trials are mixed '
                  'and the 2023 VA/DoD guideline recommends paroxetine and sertraline; "calcified PTSD" is not a term in '
                  'the literature',
                  'yes: they learn that SSRIs failing them is common, from one small trial and mixed results since')],
        unneeded=['In a small trial of male combat veterans with severe, long-term PTSD, Prozac did no better than a '
                  'placebo (Hertzberg, et al, 2000).',
                  'And the side effects are well-known, including anhedonia, zombification, and sexual dysfunction: nearly '
                  'half of people on antidepressants report feeling emotionally blunted (Goodwin, et al, 2017).'],
        kept={'In a small trial of male combat veterans with severe, long-term PTSD, Prozac did no better than a '
              'placebo (Hertzberg, et al, 2000).': 'they learn the finding this paragraph was built on, Prozac failing '
              'combat veterans, at its real size: one small trial',
              'And the side effects are well-known, including anhedonia, zombification, and sexual dysfunction: nearly '
              'half of people on antidepressants report feeling emotionally blunted (Goodwin, et al, 2017).':
              'they learn the side effects, the other way these drugs fail people that the heading promises; the '
              'blunting figure and its source after the colon were cut'}),
    'S48': dict(
        pays=['they get the question the paragraph answers', 'they get the honest answer to it',
              'they learn the protocol takes another route', 'they learn what ketones may do and where that was shown',
              'they learn it is untested in people'],
        checked=[('SSRIs treat the "software" and cannot penetrate the "hardware"; ketones and HDAC inhibitors remodel '
                  'the brain\'s structure',
                  'paroxetine grew the hippocampus 4.6% in PTSD (Vermetten 2003), so SSRIs do change structure; BHB '
                  'inhibits HDACs in mice (Shimazu 2013) and HDAC inhibitors made extinction last in mice (Whittle and '
                  'Singewald 2014); nothing shows remodeling in people',
                  'yes: they learn why ketones are in the protocol and that the reason is from mice')],
        unneeded=['Nobody knows for sure, and it isn\'t that they can\'t touch the brain\'s structure: in people with PTSD, '
                  'a year on paroxetine grew the hippocampus, a memory center that is often smaller in PTSD, by about 5% '
                  '(Vermetten, et al, 2003).'],
        kept={'Nobody knows for sure, and it isn\'t that they can\'t touch the brain\'s structure: in people with PTSD, '
              'a year on paroxetine grew the hippocampus, a memory center that is often smaller in PTSD, by about 5% '
              '(Vermetten, et al, 2003).': 'they get the honest answer to the opening question, "Nobody knows for sure"; '
              'the paroxetine finding after it was cut'}),
    'S50': dict(
        pays=['they learn why waiting it out doesn\'t work', 'they learn which tools the guide uses',
              'they learn what each was shown to do, and in which animal', 'they learn it is untested for this'],
        checked=[('You cannot "wait" for this to pass; shrooms and iboga stimulate GDNF, which rewires the brain',
                  'DeltaFosB\'s half-life is up to about 8 days in rodents (Robison and Nestler 2022), so it fades '
                  'slowly; iboga raised GDNF in rats (He 2005); psilocybin grew spines in mice (Shao 2021), not GDNF',
                  'yes: they learn why the guide doesn\'t tell them to wait, and what the two tools were shown to do')],
        unneeded=['(in rodents it takes up to about eight days for half of it to clear; Robison & Nestler, 2022)'],
        kept={}),
    'S52': dict(
        pays=['they learn their fog may be a fuel problem', 'they learn the evidence for that, in PTSD'],
        checked=[('Trauma causes cerebral insulin resistance; neurons swim in glucose but cannot burn it',
                  'brain insulin resistance is reported after head injury, not psychological trauma; in PTSD some regions '
                  'take up less glucose, less with worse symptoms (Jeong 2019)',
                  'yes: they learn their fog may come from parts of the brain burning less fuel')],
        unneeded=[], kept={}),
    'S53': dict(
        pays=['they hear the plan in one line', 'they learn why ketones', 'they learn why PQQ, and how far that goes'],
        checked=[('PQQ boosts ATP; ketones bypass the broken glucose pathways; it turns the lights back on immediately; '
                  'hot and cold showers boost p131 and heat shock proteins',
                  'PQQ built mitochondria in mouse cells (Chowanadisai 2010); low-glucose brains take up ketones normally '
                  '(Cunnane 2016); nothing shows "immediately"; nothing tests showers for PI31, and heat-shock proteins '
                  'took 40 to 60 minutes in hot water',
                  'yes: they learn what ketones and PQQ are for and how far each is shown')],
        unneeded=['The Fix: If the brain is burning less sugar, we give it another fuel.'],
        kept={'The Fix: If the brain is burning less sugar, we give it another fuel.': 'they hear the plan in one line, '
              'another fuel when sugar burns low, before the two the paragraph names'}),
    'S56': dict(
        pays=['they learn why a visual task can weaken a memory', 'they learn what to do and what it does',
              'they learn the reminder is part of it'],
        checked=[('The memory is restored, but the emotional "sting" is permanently reduced',
                  'reminder plus Tetris cut how often a memory intruded over the next week (James 2015; Iyadurai 2018); '
                  'nothing shows the sting is permanently reduced',
                  'yes: they learn what Tetris after a flashback does: fewer flashbacks')],
        unneeded=['After car crashes, people who briefly recalled the crash and then played about 20 minutes of Tetris in '
                  'the emergency room had 62% fewer intrusive memories over the next week (Iyadurai, et al, 2018).'],
        kept={}),
    'S57': dict(
        pays=['they learn the no-phone alternative', 'they learn it is untested and why it might work',
              'they learn what to avoid and why'],
        checked=[('Color-Path Connect is more effective than simple counting',
                  'no study tests it; a verbal quiz after a trauma film increased flashbacks (Holmes 2010)',
                  'yes: they learn to choose a visual task and skip verbal ones')],
        unneeded=[], kept={}),
}

CARDS = {
    'S24': dict(id='SC-24', title='The relational density figure is Perry\'s one-sixteenth',
                what='"less than 1/24th" becomes "about one-sixteenth", with Perry as the source. Nothing else changes.',
                why='Perry\'s own number, in his book and [his 2023 piece](%s), is one-sixteenth: four mature people '
                    'around every young child then, one adult for every four children now. "1/24th" comes from a '
                    '[training summary of his work](https://csa.virginia.gov/Content/doc/Trauma_Informed_Care_2022.pdf). '
                    'This was flag F-4 of the fact check of 5 November.' % T.PERRY,
                stays='The rest of the paragraph, word for word.',
                deciding='Whether the figure is Perry\'s own.',
                ask='meaning: the figure changes'),
    'S47': dict(id='SC-47', title='Prozac in veterans: one small trial, and mixed results since',
                what='"Ipser & Stein 2012 study showed that Prozac had zero effect on male combat veterans with calcified '
                     'PTSD" becomes the trial it comes from, and a sentence that SSRIs help some people.',
                why='The no-better-than-placebo result is [Hertzberg, et al, 2000](%s): twelve male Vietnam combat '
                    'veterans for twelve weeks. A [2008 review for the VA](https://nap.nationalacademies.org/read/11955/chapter/15) '
                    'found SSRIs looked ineffective in mostly male veterans with chronic PTSD, but veterans recruited '
                    'outside the VA later improved as much as civilians, and the [2023 VA/DoD guideline](%s) recommends '
                    'paroxetine, sertraline and venlafaxine. Ipser & Stein 2012 is a review I couldn\'t open. "Calcified '
                    'PTSD" isn\'t a term in the literature. A fresh reader flagged the trial sentence and the side '
                    'effects as not needed; I kept both (the trial is what your paragraph was built on, and the side '
                    'effects are what the heading promises) and cut only a figure I had added.' % (T.HERTZBERG, T.VADOD),
                stays='"If you have tried SSRIs (antidepressants) and failed, you are not crazy", and your side-effects '
                      'sentence word for word.',
                deciding='Whether the paragraph says what the Prozac trial was, and that SSRIs help some people.',
                ask='meaning: the claim about Prozac changes, and a sentence says SSRIs help some'),
    'S48': dict(id='SC-48', title='Why SSRIs fail some people: nobody knows; why ketones: a mouse finding',
                what='The software and hardware explanation goes. In its place: nobody knows why these drugs fail some '
                     'people, and why the protocol tries ketones, with that reason\'s limit.',
                why='"They cannot penetrate the hardware" doesn\'t hold: a year of paroxetine grew the hippocampus about '
                    '5%% in people with PTSD ([Vermetten, et al, 2003](%s)). Nothing shows ketones or HDAC inhibitors '
                    'remodel the amygdala in people. What there is: the ketone BHB blocks HDAC enzymes in mice '
                    '([Shimazu, et al, 2013](%s)), and an HDAC blocker made extinction learning last in mice that '
                    'couldn\'t keep it ([Whittle & Singewald, 2014](%s)). Your note on SB-38 said not to argue with the '
                    'guide, so the paroxetine finding is here and not in the text.' % (T.VERMETTEN, T.SHIMAZU, T.WHITTLE),
                stays='The question that opens it, and "This protocol" as the turn.',
                deciding='Whether the paragraph drops the software and hardware claim and gives the mouse finding with its '
                         'limit.',
                ask='meaning: the explanation of why SSRIs fail is replaced, and so is the claim about what ketones do'),
    'S50': dict(id='SC-50', title='DeltaFosB fades, slowly; what iboga and psilocybin were shown to do',
                what='"You cannot \'wait\' for this to pass" becomes "DeltaFosB does fade on its own, but slowly, and '
                     'the same fears keep making more". "To stimulate GDNF, which physically rewires the brain" becomes '
                     'what each was shown to do, and that it\'s untested for this.',
                why='DeltaFosB\'s half-life in the brain is up to about eight days ([Robison & Nestler, 2022](%s)), so it '
                    'does fade; your block 46 says the same fears keep making more, and the timeline (block 182) has it '
                    'degraded by week 8. "You cannot wait" contradicted both. Iboga raised GDNF in rats '
                    '([He, et al, 2005](%s)); psilocybin grew new spines in mice that lasted a month '
                    '([Shao, et al, 2021](%s)), which isn\'t GDNF (flag F-8).' % (T.ROBISON, T.HE, T.SHAO),
                stays='"The Fix (The Unlock)" and "System Reformats" (Shrooms/Iboga).',
                deciding='Whether the paragraph says DeltaFosB fades slowly, and what each tool was shown to do.',
                ask='meaning: the waiting claim and the GDNF claim change'),
    'S52': dict(id='SC-52', title='Brain fog: some regions burn less glucose in PTSD',
                what='"Trauma causes cerebral insulin resistance--your neurons are swimming in glucose (sugar) but cannot '
                     'burn it. The engine is flooded." becomes what scans of people with PTSD show.',
                why='Brain insulin resistance is reported after [head injury](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6114023/), '
                    'not psychological trauma, and nothing shows neurons "swimming in glucose". In people with PTSD, '
                    'parts of the insula, prefrontal cortex and striatum take up less glucose, the less the worse the '
                    'symptoms ([Jeong, et al, 2019](%s)) (flag F-9).' % T.JEONG,
                stays='"The Problem: \'Brain Fog\'" and the fuel idea.',
                deciding='Whether the fog paragraph rests on the PTSD scans instead of insulin resistance.',
                ask='meaning: the cause the paragraph gives for brain fog changes'),
    'S53': dict(id='SC-53', title='Ketones and PQQ, as far as they\'re shown; the shower sentence out',
                what='Ketones and PQQ are said as far as the studies go; "This turns the lights back on immediately" and '
                     'the hot and cold showers sentence come out.',
                why='Brains that take up less glucose (in mild cognitive impairment and early Alzheimer\'s) still take up '
                    'ketones normally ([Cunnane, et al, 2016](%s)). PQQ made mouse cells build mitochondria '
                    '([Chowanadisai, et al, 2010](%s)); nothing shows it in the human brain, and nothing shows '
                    '"immediately". The PI31 study raised it by gene therapy in mice; nothing tests showers, and the '
                    'heat-shock protein studies keep people in hot water 40 to 60 minutes (flag F-10). The shower routine '
                    'in Part 3 comes up again in the read of the whole protocol.' % (T.CUNNANE, T.CHOWANADISAI),
                stays='"The Fix" and the switch of fuels.',
                deciding='Whether the shower sentence leaves this paragraph, and ketones and PQQ are said as far as shown.',
                ask='meaning: claims come out (the showers, "immediately") and two are narrowed'),
    'S56': dict(id='SC-56', title='The Jammer: fewer flashbacks, not a permanently reduced sting',
                what='"The memory is restored, but the emotional \'sting\' is permanently reduced" becomes "the memory '
                     'flashes back less often", with the study that shows it.',
                why='What the Tetris studies measure is how often a memory intrudes: a reminder followed by Tetris cut '
                    'flashbacks of a day-old memory, and neither alone did ([James, et al, 2015](%s)); after real car '
                    'crashes, a reminder and about 20 minutes of Tetris cut intrusive memories over the next week, but not '
                    'other symptoms or the count at one month ([Iyadurai, et al, 2018](%s)). Nothing shows a permanent '
                    'change in the sting. A fresh reader said the car-crash sentence wasn\'t needed, so it\'s here and not '
                    'in the text; the lab study is the closer one for an old memory.' % (T.JAMES, T.IYADURAI),
                stays='"Memories require visual processing power to be restored" and the Tetris instruction.',
                deciding='Whether the Jammer promises fewer flashbacks rather than a permanently reduced sting.',
                ask='meaning: what the Jammer promises changes'),
    'S57': dict(id='SC-57', title='Color-Path Connect is untested; skip verbal tasks',
                what='"This is more effective than simple counting" becomes that it\'s untested and built on the same '
                     'idea as Tetris, plus why to skip counting and word games.',
                why='No study tests Color-Path Connect, so "more effective" can\'t be said. What is known: a verbal quiz '
                    'game after a trauma film increased flashbacks, while Tetris cut them '
                    '([Holmes, et al, 2010](%s)).' % T.HOLMES10,
                stays='The method, its name, and the 3D-space reason.',
                deciding='Whether the method stays with an honest label (you could also cut it and keep only Tetris).',
                ask='meaning: the "more effective" claim goes and an untested label comes in'),
}


def receipt(t, b):
    text = T.plain(t['md'])
    sp = SPEC[t['key']]
    r = S.make(text, sr.where(BL, b).rsplit(',', 1)[0], READER)
    sents = r['sentences']
    assert len(sents) == len(sp['pays']), (t['key'], len(sents), len(sp['pays']))
    for i, (x, p) in enumerate(zip(sents, sp['pays'])):
        x['payoff'] = p
        x['follows'] = 'it opens the paragraph' if i == 0 else 'it continues the sentence before'
        if 'link' in x:
            x['link'] = x['s'].split()[0]
    r['opens'] = {'first_sentence': sents[0]['s'], 'why_reading': sp['pays'][0]}
    r['same_point'] = 'none: read the section from its heading to the next for the same point; it appears once'
    r['placement'] = 'where the block is now (block %d); its place in the section is unchanged' % b
    r['questions'] = dict(Q_ANS)
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': 'changed'} for a, f, s in sp['checked']]
    r['needed'] = {'reader': FRESH % t['key'].lower(), 'unneeded': sp['unneeded'], 'kept': sp['kept']}
    probs = S.check(text, r)
    p = HERE / ('%s.receipt.json' % t['key'])
    p.write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % t['key'])).write_text(text + '\n', encoding='utf-8')
    (HERE / ('%s.md' % t['key'])).write_text(t['md'] + '\n', encoding='utf-8')
    return probs


def main():
    bad = []
    cards = []
    for t in T.T:
        b = [x['i'] for x in BL if x['text'].startswith(t['start'])]
        assert len(b) == 1, (t['key'], b)
        b = b[0]
        bad += ['%s: %s' % (t['key'], x) for x in receipt(t, b)]
        c = CARDS[t['key']]
        cards.append({'id': c['id'], 'type': 'science', 'title': c['title'], 'advice': 'approve',
                      'spans': [{'block': b, 'start': 0, 'end': len(sr.block_text(BL, b))}],
                      'edits': [{'block': b, 'before': sr.block_text(BL, b), 'after': T.plain(t['md'])}],
                      'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
                      'advice_note': 'Approve.', 'ask_because': c['ask'], 'approve_label': 'use it',
                      'found_by': 'The science pass of sections C to E, 8 November',
                      'receipt': [REL + '%s.receipt.json' % t['key']]})
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261108-x1108b',
        'title': 'Neuro De-Armoring Cards, 8 November (2): the science of sections C to E',
        'intro': ['The science of the Hardened Circuit, the Fog and the Save Button, plus the relational-density figure '
                  'from Part 1. Each card changes only what the sources don\'t support, and a fresh reader checked each '
                  'new paragraph for sentences the reader doesn\'t need.',
                  'No compound, dose, unit, timing or warning changes on this page. Block 61 (10 to 20 minutes right '
                  'after a trigger) matches the studies and has no card.',
                  'Once every section\'s science is settled, the protocol gets read as a whole, as you asked.'],
        'git_file': REL + 'REVIEW-X1108B.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1108B.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': cards,
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1108B.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1108B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1108B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for s in cards:
        e = s['edits'][0]
        md += ['## %s: %s' % (s['id'], s['title']), '', '*%s*' % sr.where(BL, e['block']), '', '**Now:**', '',
               '> %s' % e['before'], '', '**As it would read:**', '', '> %s' % e['after'], '',
               '**What changes:** %s' % s['what'], '', '**Why:** %s' % s['why'], '', '**What stays:** %s' % s['stays'],
               '', '**You\'re deciding:** %s' % s['deciding'], '', '**My advice:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1108B.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [c['id'] for c in cards])
    return 0


if __name__ == '__main__':
    sys.exit(main())
