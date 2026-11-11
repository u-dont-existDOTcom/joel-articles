"""Neuro De-Armoring Cards, 11 November (2): potassium, rethought on the science (SC-106e, replacing SC-106d).

His message of 2026-11-11 22:07 UTC: a claim he makes as science rests on science, never recast as his opinion; SC-106d
made potassium look like a one-study artifact; my research was thin; GPT's research; low intakes are common. Sources in
texts_x1111b.py and SCIENCE-P23.md ("Rethought on the science"); two fresh needed reads (needed/sp106e-first, needed/sp106e).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/build_x1111b.py
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[1]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_x1108d as D  # noqa: E402
import texts_x1108e as E  # noqa: E402
import texts_x1111a as A  # noqa: E402
import texts_x1111b as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/sci-p23/'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
RAW = [x for x in re.split(r'\n\s*\n', MD) if x.strip()]
READER = ('someone with trauma or in withdrawal who is anxious, wired, numb or foggy, following the protocol\'s diet and '
          'electrolyte steps and wanting to know why each one is there')
FRESH = 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph (needed/%s/READ.md)'

SHORT = ' '.join([T.plain(T.S1), 'In a diet trial, people who took in more potassium and less salt had better mood and less '
                   'fatigue (Torres, et al, 2008).', T.plain(T.S4), T.plain(T.S7)])
CARD = dict(
    id='SC-106e', title='Potassium, rethought on the science: nerves, low intakes, mood, thinking',
    what='As before, the two labels of the brakes story go (blocks 104 and 105) and block 115\'s second sentence goes. '
         'Block 106 now rests on the science: nerves need potassium and most people eat too little; what raising it has '
         'done for mood and thinking, with the limits; who needs more; blood pressure; your paleo view; the caution.',
    why='You\'re right on both counts. A claim the article makes as science rests on science, and my lesson had that '
        'backwards; SC-106d also made potassium look like one weak study, because my search was thin. Searched again, with '
        'GPT\'s sources checked one by one: only about 3 in 10 Americans eat the recommended amount ([Dietary Guidelines '
        'Advisory Committee, 2024](%s)), which backs your NHANES point (I couldn\'t find the 40%% figure itself). In the '
        'diet trial, more potassium and less salt went with better mood and less fatigue ([Torres, et al, 2008](%s)); '
        'potassium given to children whose steroid drugs had set off mood and behavior problems helped 13 of 16 ([Pariury, '
        'et al, 2019](%s)); older adults who ate more thought and remembered better ([Na, et al, 2022](%s)), though one '
        'cohort found the opposite for mild memory problems ([Cherbuin, et al, 2014](%s)), a fruit trial changed nothing '
        '([Zingales, et al, 2025](%s)), and an older trial found more fatigue on a low-salt, high-potassium diet '
        '([Wassertheil-Smoller, et al, 1991](%s)). People also lose potassium at very different rates: diarrhea, '
        'diuretics and an inherited kidney condition, Gitelman syndrome, drain it, and people with Gitelman report '
        'fatigue, weakness and lower energy and emotional well-being ([Cruz, et al, 2001](%s)). I was wrong to say eating '
        'more helps the nerves only when something has drained it: no study shows that, and low intakes are common. Left '
        'out: the 2025 case report GPT found, since the woman also changed her diet and took leave at the same time and '
        'the author is a relative ([Dai, 2025](%s)). I couldn\'t open your Reddit threads, which are blocked from here; '
        'paste the posts if you want firsthand reports in. The paleo sentence stays as your view, as you wrote it.'
        % (T.DGAC, T.TORRES, T.PARIURY, T.NA, T.CHERBUIN, T.ZINGALES, T.TAIM, T.CRUZ, T.DAI),
    stays='"Potassium:", the target (4,700 mg, the FDA\'s Daily Value), the food-only rule, the menu, "Eat 2 large '
          'potatoes and 2 cups of greens every single day.", and your caution at the top. Part 3\'s goal line goes to the '
          'read of the whole protocol.',
    deciding='Whether block 106 gives potassium\'s reason as this science (nerves, low intakes, mood, thinking, who needs '
             'more, blood pressure), with your paleo view and the caution.',
    advice='Approve. I\'m fairly sure this is the science the card needed, less sure of the length. A fresh reader would '
           'keep only this: "%s"' % SHORT,
    ask='meaning: block 106\'s reason for potassium becomes the science on nerves, mood and thinking, with blood pressure '
        'after it')

CHILDREN = ('and potassium supplements eased mood and behavior problems in 13 of 16 children taking steroid drugs, which '
            'mimic the stress hormone cortisol (Pariury, et al, 2019).')
S3P, S5P, S6P = T.plain(T.S3), T.plain(T.S5), T.plain(T.S6)
SPEC_106 = dict(
    pays=['they learn why potassium matters for their nerves and that they are probably eating less than recommended',
          'they learn what raising potassium has done for mood and fatigue in studies, including with cortisol-like drugs',
          'they learn it may help their thinking too, and how far the evidence goes',
          'they learn whether they may need more than most',
          'they learn the benefit trials have shown and why it matters with the sodium in their salts',
          'they learn the fuller way to raise potassium and the easy start',
          'they learn to ask a doctor first if they have kidney disease or take a blood pressure drug that keeps potassium '
          'in'],
    follows=['it opens the paragraph, after "Potassium:" and the sodium line above it',
             'it turns from why potassium matters to what raising it has done',
             'it adds thinking to mood, with the limit',
             'it turns from what potassium does to who needs more of it',
             'it adds the blood-pressure benefit and ties it to Strategy A',
             'it turns to how to get more, before the target and the foods',
             'it ends on who should check with a doctor first'],
    checked=[('low potassium (common in high stress) makes the KCNQ brakes fail, and eating potassium puts them back',
              'the brain keeps the potassium around its neurons within tight limits whatever the blood does (Hladky and '
              'Barrand 2016)', 'no: the brakes story is cut, with its two labels (blocks 104 and 105)', 'cut'),
             ('most people eat less potassium than recommended',
              '28% of Americans aged 1 and up are above the Adequate Intake (DGAC 2024, Table D.1.6)',
              'yes: they learn they are probably low and the step is for them', 'changed'),
             ('more potassium goes with better mood',
              'urinary potassium went with less fatigue and a lower sodium-to-potassium ratio with less anger and '
              'depression (Torres et al. 2008); potassium chloride helped 13 of 16 children with corticosteroid-induced '
              'neuropsychiatric effects (Pariury et al. 2019, retrospective)',
              'yes: they learn what raising potassium may do for their mood', 'kept'),
             ('more potassium goes with better thinking and memory',
              'higher intake went with higher cognitive scores and less memory decline in 4,213 Chinese adults aged 50 and '
              'up (Na et al. 2022); against: Cherbuin 2014, Zingales 2025',
              'yes: they learn it may help their thinking, with the limit', 'kept'),
             ('some people lose more potassium',
              'diarrhea, vomiting and diuretics cause hypokalemia (NIH 2022); Gitelman syndrome wastes it (Cruz et al. 2001)',
              'yes: they check whether they are among those who need more', 'kept'),
             ('eating more potassium brings high blood pressure down',
              'in trials, systolic pressure fell about 3.5 mm Hg, in people with high blood pressure (Aburto et al. 2013)',
              'yes: they learn why it matters with the salts of Strategy A', 'changed'),
             ('Stone Age diets had far more potassium; a paleo diet probably does more than adding potatoes (his view)',
              '400 +/- 125 mEq a day in retrojected Stone Age diets (Sebastian et al. 2006)',
              'yes: they can eat closer to a paleo diet, with the potatoes and greens as the start', 'kept'),
             ('kidney disease and drugs that keep potassium in can let it build up',
              'ACE inhibitors and ARBs can lead to hyperkalemia (NIH 2022); restricting potassium slowed neuropathy in '
              'kidney disease (Arnold et al. 2017)', 'yes: they ask their doctor first if either applies to them', 'kept')])
# the words in each sentence that tie it to the one before or to the reader's case (gate neuro-2026-11-06b)
LINKS = ['yet most of us', 'took in more potassium', 'also tend to think', 'Some people need more than others, too',
         'also brings high blood pressure down', 'the potatoes and greens below', 'If you have kidney disease']
KEPT = {CHILDREN: 'they learn that potassium itself, given as a supplement, eased mood problems set off by cortisol-like '
                  'drugs, the hormone this protocol is about, which the diet trial alone can\'t show',
        S3P: 'they learn it may also help the fog in their thinking, which this protocol treats, and how far that evidence '
             'goes',
        S5P: 'they learn the one benefit trials have shown and why it matters with the sodium in the salts they take',
        S6P: 'they learn the author\'s view of the fuller way to raise potassium, with the potatoes and greens as the start '
             '(his view, worded as one)'}


def new_block(t):
    (r,) = [k for k, x in enumerate(RAW) if x.startswith(t['start'])]
    if t.get('cut'):
        return RAW[r], ''
    new = RAW[r]
    for old, rep in t['swap']:
        assert new.count(old) == 1, (t['key'], old[:50])
        new = new.replace(old, rep)
    return RAW[r], re.sub(r'  +', ' ', new).strip()


def write_receipt(key, r, text):
    probs = S.check(text, r)
    (HERE / ('%s.receipt.json' % key)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def receipt(t, b, md):
    text = T.plain(md)
    where = sr.where(BL, b).rsplit(',', 1)[0]
    if t['key'] == 'SP115G':   # what stays of block 115 is his own sentence; the card only cuts the one after it
        r = S.make(text, where, READER, his_text=text, whose='his own: block 115\'s first sentence, as his post has it')
        r['opens'] = {'first_sentence': r['sentences'][0]['s'], 'why_reading': 'they learn which foods reach the target'}
        r['checked'] = [{'point': 'eating potassium saturates your cells and lowers your resting voltage, so you are '
                                  'harder to trigger',
                         'found': 'the brain keeps the potassium around its neurons within tight limits whatever the blood '
                                  'does (Hladky and Barrand 2016), and where more potassium does reach excitable cells it '
                                  'moves them toward firing (Campese and Adenuga 2016)',
                         'still_needed': 'no: the claim doesn\'t hold, so the sentence is cut', 'fate': 'cut'}]
        r['needed'] = {'reader': 'none of mine: the text left is his own sentence, unchanged', 'unneeded': [], 'kept': {}}
    else:
        r = S.make(text, where, READER)
        sents = r['sentences']
        assert len(sents) == len(SPEC_106['pays']), (t['key'], len(sents))
        for x, p, f, k in zip(sents, SPEC_106['pays'], SPEC_106['follows'], LINKS):
            x['payoff'] = p
            x['follows'] = f
            if 'link' in x:
                assert k in x['s'], (k, x['s'][:40])
                x['link'] = k
        r['opens'] = {'first_sentence': sents[0]['s'], 'why_reading': SPEC_106['pays'][0]}
        r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC_106['checked']]
        r['needed'] = {'reader': FRESH % 'sp106e', 'unneeded': [CHILDREN, S3P, S5P, S6P], 'kept': dict(KEPT)}
    r['same_point'] = ('none: read the section from its heading to the next for the same point; the caution at the top of '
                       'the article is the general one, this one is beside its step')
    r['placement'] = 'where the block is now (block %d); its place in the section is unchanged' % b
    r['questions'] = dict(Q_ANS)
    return write_receipt(t['key'], r, text)


def main():
    bad, edits = [], {}
    for t in T.T:
        (b,) = [x['i'] for x in BL if x['text'].startswith(t['start'])]
        old, md = new_block(t)
        edits[t['key']] = {'block': b, 'before': sr.block_text(BL, b), 'after': T.plain(md)}
        if md:
            (HERE / ('%s.md' % t['key'])).write_text(md + '\n', encoding='utf-8')
            (HERE / ('%s.txt' % t['key'])).write_text(T.plain(md) + '\n', encoding='utf-8')
            bad += ['%s: %s' % (t['key'], x) for x in receipt(t, b, md)]
    keys = [t['key'] for t in T.T]
    c = CARD
    card = {'id': c['id'], 'type': 'science', 'title': c['title'], 'advice': 'approve',
            'spans': [{'block': edits[k]['block'], 'start': 0, 'end': len(edits[k]['before'])} for k in keys],
            'edits': [edits[k] for k in keys],
            'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
            'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'use it',
            'found_by': 'His message of 2026-11-11 22:07 UTC: the card rests on science; GPT\'s sources and his points checked',
            'receipt': [REL + '%s.receipt.json' % k for k in keys if edits[k]['after']]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261111-x1111b',
        'title': 'Neuro De-Armoring Cards, 11 November (2): potassium, rethought on the science',
        'intro': ['SC-106d again, after your message. The card now rests on the science, searched again with GPT\'s '
                  'sources checked one by one, and the paleo sentence stays as your view.',
                  'This card replaces SC-106d. No compound, dose, unit or timing changes.',
                  'After this card, the protocol gets read as a whole against the settled science.'],
        'git_file': REL + 'REVIEW-X1111B.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1111B.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1111B.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1111B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1111B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    md += ['## %s: %s' % (card['id'], card['title']), '']
    for e in card['edits']:
        md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
               '**As it would read:**', '', '> %s' % (e['after'] or '(cut)'), '']
    md += ['**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '', '**What stays:** %s' % card['stays'],
           '', '**You\'re deciding:** %s' % card['deciding'], '', '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1111B.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', card['id'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
