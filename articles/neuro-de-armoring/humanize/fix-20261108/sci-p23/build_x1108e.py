"""Neuro De-Armoring Cards, 8 November (5): potassium, corrected again (SC-106c, replacing SC-106b).

His message of 2026-11-08 17:09 UTC brought GPT's answers on two things SC-106b's "why" said (nerve function; Torres
2008). Both checked against the sources (SCIENCE-P23.md, "SC-106b checked again"); texts in texts_x1108e.py, the fresh
reader's needed read in needed/sp106c/READ.md (nothing unneeded). Published to the same page as x1108d, which it
replaces.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/build_x1108e.py
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
import texts_x1108e as T  # noqa: E402
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

CARD = dict(
    id='SC-106c', title='Potassium: there for blood pressure, with a caution for kidneys and blood pressure drugs',
    what='As on SC-106b, the two labels of the brakes story go (blocks 104 and 105), block 106 gives the reason that holds '
         'for eating potassium (it brings high blood pressure down, which matters with the sodium in Strategy A\'s salts), '
         'and block 115\'s second sentence goes. New: a caution in block 106 for anyone with kidney disease or on a blood '
         'pressure drug that holds on to potassium.',
    why='Your two questions to GPT, checked against the sources. On nerve function GPT and I agree: your nerves need '
        'potassium to work, but eating too little rarely lowers blood potassium on its own ([NIH, 2022](%s)), so eating '
        'more helps the nerves only when something like diarrhea or a water pill has drained it, and blood pressure stays '
        'the reason the paragraph gives. On the mood trial you\'re right, and my card said more than the study found: I '
        'had read only its summary. In full, both test diets raised potassium about equally; the low-salt one lifted '
        'mood a little more, while the DASH-type diet didn\'t change overall mood significantly; more potassium in the '
        'urine went with less fatigue; and the authors name magnesium as another explanation, so potassium\'s own part in '
        'mood is open, not ruled out ([Torres, et al, 2008](%s); lesson neuro-2026-11-08k). The caution is new because '
        'the paragraph now points people with high blood pressure at potassium, and many of them take ACE inhibitors or '
        'ARBs, which keep potassium in ([NIH, 2022](%s)); in kidney disease, cutting potassium slowed nerve damage over two '
        'years ([Arnold, et al, 2017](%s)). The rest of SC-106b\'s reasons stand: your brain keeps the potassium around '
        'its neurons within tight limits whatever your blood does ([Hladky & Barrand, 2016](%s)), so neither stress nor '
        'diet works the KCNQ brakes; and across the trials more potassium brought high blood pressure down ([Aburto, et '
        'al, 2013](%s)).' % (T.NIH, T.TORRES_FULL, T.NIH, T.ARNOLD, D.HLADKY, T.ABURTO),
    stays='"Potassium:", the target (4,700 mg, the FDA\'s Daily Value), the food-only rule, the menu, "Eat 2 large '
          'potatoes and 2 cups of greens every single day.", and your caution at the top ("Electrolytes: Consult a doctor '
          'if you have kidney disease or heart conditions."). Part 3\'s goal line ("Stabilize voltage to prevent the '
          '"Biological Crash" (Headaches/Panic).") goes to the read of the whole protocol.',
    deciding='Whether potassium stays in the protocol for blood pressure, with the caution beside it, instead of the '
             'brakes. If you\'d rather drop the potassium step altogether, say so in the box.',
    advice='Approve. This replaces SC-106b: the same change plus the caution, with the mood trial now read in full.',
    ask='meaning: the reason the section gives for potassium changes from calming the nerves to blood pressure, and a '
        'caution is added beside the step')

SPEC_106 = dict(
    pays=['they learn why to eat potassium on Strategy A: it brings high blood pressure down, and the salts add sodium',
          'they learn to ask a doctor first if they have kidney disease or take a blood pressure drug that keeps potassium '
          'in, since it can build up in their blood'],
    follows=['it opens the paragraph, after "Potassium:" and the sodium line above it, which warns of high blood pressure '
             'on Strategy A',
             'it continues the sentence before: who should check with a doctor before eating more of it'],
    checked=[('low potassium (common in high stress) makes the KCNQ brakes fail, and eating potassium puts them back',
              'the brain keeps the potassium around its neurons within tight limits whatever the blood does (Hladky and '
              'Barrand 2016; dogs: Javaheri and Kazemi 1981), so neither the drop stress brings to the blood (Brown 1983) '
              'nor what you eat sets the brakes',
              'no: the brakes story is cut, with its two labels (blocks 104 and 105)', 'cut'),
             ('eating more potassium brings high blood pressure down',
              'in trials, more potassium lowered systolic pressure by about 3.5 mm Hg, in people with high blood pressure '
              'and not in others (Aburto et al. 2013)',
              'yes: they learn why the target and the foods that follow are there on Strategy A', 'changed'),
             ('kidney disease and drugs that keep potassium in can let it build up',
              'ACE inhibitors and ARBs reduce urinary potassium excretion, which can lead to hyperkalemia, and experts '
              'recommend monitoring (NIH 2022); in kidney disease, restricting potassium slowed neuropathy over two years '
              '(Arnold et al. 2017)',
              'yes: they ask their doctor before eating more potassium if either applies to them', 'kept'),
             ('potassium-rich food supports normal nerve function (GPT\'s version)',
              'the potassium gradient is required for nerve transmission, but hypokalemia is rarely caused by low dietary '
              'intake alone (NIH 2022)',
              'no: eating more doesn\'t change nerve function unless something has drained potassium, so it isn\'t a '
              'reason the paragraph gives', 'cut')])


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
    if t['key'] == 'SP115E':   # what stays of block 115 is his own sentence; the card only cuts the one after it
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
        for x, p, f in zip(sents, SPEC_106['pays'], SPEC_106['follows']):
            x['payoff'] = p
            x['follows'] = f
            if 'link' in x:
                x['link'] = x['s'].split()[0]
        r['opens'] = {'first_sentence': sents[0]['s'], 'why_reading': SPEC_106['pays'][0]}
        r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC_106['checked']]
        r['needed'] = {'reader': FRESH % 'sp106c', 'unneeded': [], 'kept': {}}
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
            'found_by': 'His message of 2026-11-08 17:09 UTC (GPT\'s answers on SC-106b\'s reasons), each point checked '
                        'against the NIH fact sheet, the full text of Torres 2008 and PubMed',
            'receipt': [REL + '%s.receipt.json' % k for k in keys if edits[k]['after']]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261108-x1108e',
        'title': 'Neuro De-Armoring Cards, 8 November (5): potassium, corrected again',
        'intro': ['SC-106b again, after your questions to GPT. I checked both against the sources: on nerve function GPT '
                  'and I agree, and on the mood trial you were right that my card said more than the study found.',
                  'This card replaces SC-106b. It adds one caution beside the potassium step; no compound, dose, unit or '
                  'timing changes.',
                  'After this card, the protocol gets read as a whole against the settled science.'],
        'git_file': REL + 'REVIEW-X1108E.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1108E.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1108E.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1108E.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1108E.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    md += ['## %s: %s' % (card['id'], card['title']), '']
    for e in card['edits']:
        md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
               '**As it would read:**', '', '> %s' % (e['after'] or '(cut)'), '']
    md += ['**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '', '**What stays:** %s' % card['stays'],
           '', '**You\'re deciding:** %s' % card['deciding'], '', '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1108E.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', card['id'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
