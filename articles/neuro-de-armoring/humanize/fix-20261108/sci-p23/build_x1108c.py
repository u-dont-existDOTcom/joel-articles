"""Neuro De-Armoring Cards, 8 November (3): the science of Parts 2 and 3, flags F-1 and F-11.

Texts in texts_p23.py (only the sentences each flag touches change; the rest of each block is copied from the article
here), the claims and sources in SCIENCE-P23.md, the fresh readers' needed reads in needed/<key>/READ.md.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/build_x1108c.py
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
import texts_p23 as T  # noqa: E402
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

SPEC = {
    'SP97': dict(
        pays=['they learn what Strategy B is and its carb limit', 'they learn what to eat on it',
              'they learn what not to fill up on, and the reason that holds', 'they learn what to expect when switching '
              'and where to get help with it'],
        checked=[('lean protein turns into sugar through gluconeogenesis, and that keeps you out of ketosis',
                  'very little dietary protein becomes glucose (3.9 g of 50.4 g over 8 hours after 23 g of egg protein, '
                  'Fromentin 2013); past about 35% of energy, protein makes people sick (Bilsborough and Mann 2006)',
                  'yes: they learn not to fill up on lean protein, for the reason the studies give')],
        unneeded=['Switching over often brings on the keto flu, and to avoid it, refer to my Keto Adaptation Guide.'],
        kept={'Switching over often brings on the keto flu, and to avoid it, refer to my Keto Adaptation Guide.':
              'they expect the keto flu when they switch over and know where his guide to avoiding it is (his sentence, '
              'which this card doesn\'t touch)'}),
    'SP106': dict(
        pays=['they learn what the KCNQ "brakes" are and what potassium has to do with them',
              'they learn that stress lowers blood potassium, and that low potassium makes nerve cells harder to fire, '
              'not easier'],
        checked=[('low potassium (common in high stress) makes the KCNQ brakes fail',
                  'adrenaline lowers blood potassium (Brown 1983); low blood potassium makes human axons rest more '
                  'negative and harder to excite (Kuwabara 2002)',
                  'yes: they learn what stress does to potassium and which way it moves their nerves')],
        unneeded=[], kept={}),
}

CARDS = {
    'SP97': dict(id='SC-97', title='Protein and ketosis: little of it becomes sugar; the limit is how much you can take',
                 what='"because your body turns the extra protein into sugar through gluconeogenesis, and that keeps you '
                      'out of ketosis" becomes the reason that holds: your body can only take so much protein, so the rest '
                      'of your energy has to come from fat.',
                 why='Very little of the protein you eat becomes sugar: after 23 g of egg protein, only about 3.9 g of the '
                     '50.4 g of glucose the body made over the next 8 hours came from it, even after an overnight fast '
                     '([Fromentin, et al, 2013](%s)). What does limit protein is the liver\'s capacity to clear its '
                     'nitrogen: past about 35%% of your calories it brings nausea and diarrhea, the "rabbit starvation" of '
                     'lean-meat diets ([Bilsborough & Mann, 2006](%s)). So your instruction stands, for the reason the '
                     'studies give (flag F-1). A fresh reader said the keto-flu sentence wasn\'t needed; it\'s yours and '
                     'this card doesn\'t touch it.' % (T.FROMENTIN, T.BILSBOROUGH),
                 stays='Strategy B, its carb limit, "eat fat until you\'re full", the instruction itself, and your keto '
                       'flu sentence with its link.',
                 deciding='Whether the instruction keeps the reason the protein studies give, instead of gluconeogenesis.',
                 advice='Approve.',
                 ask='meaning: the reason the paragraph gives for one instruction changes'),
    'SP106': dict(id='SC-106', title='Potassium and the KCNQ brakes: low potassium makes nerves harder to fire, not easier',
                  what='The brakes-fail story goes from blocks 106 and 115: what KCNQ channels do stays, with what stress '
                       'does to blood potassium and which way low potassium moves nerve cells; "This saturates your cells, '
                       'lowering your resting voltage so you become physically harder to trigger" is cut.',
                  why='KCNQ channels are potassium channels that keep a neuron from firing over and over, so "brakes" '
                      'holds. The direction doesn\'t: during low blood potassium, human nerves rest more negative and are '
                      'harder to excite ([Kuwabara, et al, 2002](%s)), and more potassium outside cells moves them toward '
                      'firing ([Campese & Adenuga, 2016](%s)). So "if you are low on potassium, your brakes fail" and '
                      '"lowering your resting voltage so you become harder to trigger" are both reversed. Stress does lower '
                      'blood potassium: adrenaline pushes it into cells ([Brown, et al, 1983](%s)). Blocks 104 and 105 '
                      '("Install the Brake Pads", "Potassium Channels (KCNQ)") rest on the same story, and the target '
                      '(block 107) matches the FDA\'s Daily Value; the read of the whole protocol takes those up with your '
                      'answer here (flag F-11).' % (T.KUWABARA, T.CAMPESE, T.BROWN),
                  stays='"The Science:", "brakes" and KCNQ; the target, the food-only rule, the menu and "Eat 2 large '
                        'potatoes and 2 cups of greens every single day."',
                  deciding='Whether the potassium section stops saying low potassium takes the brakes off.',
                  advice='Approve the correction, and tell me in the box what you\'ve seen potassium do in practice. '
                         'Without the brakes story, this section gives no reason for its target, so the potassium part goes '
                         'to the read of the whole protocol with what you say.',
                  ask='meaning: the reason the section gives for potassium is reversed, and that reason carries the section'),
}


def new_block(t):
    (r,) = [k for k, x in enumerate(RAW) if x.startswith(t['start'])]
    new = RAW[r]
    for old, rep in t['swap']:
        assert new.count(old) == 1, (t['key'], old[:50])
        new = new.replace(old, rep)
    return RAW[r], re.sub(r'  +', ' ', new).strip()


def receipt(t, b, md):
    text = T.plain(md)
    if t['key'] == 'SP115':   # what stays of block 115 is his own sentence; the card only cuts the one after it
        r = S.make(text, sr.where(BL, b).rsplit(',', 1)[0], READER, his_text=text,
                   whose='his own: block 115\'s first sentence, as his post has it')
        r['opens'] = {'first_sentence': r['sentences'][0]['s'], 'why_reading': 'they learn which foods reach the target'}
        r['same_point'] = 'none: read the section from its heading to the next for the same point; it appears once'
        r['placement'] = 'where the block is now (block %d); its place in the section is unchanged' % b
        r['questions'] = dict(Q_ANS)
        r['checked'] = [{'point': 'eating potassium saturates your cells and lowers your resting voltage, so you are '
                                  'harder to trigger',
                         'found': 'more potassium outside excitable cells moves them toward firing (Campese and Adenuga '
                                  '2016)', 'still_needed': 'no: the claim is reversed, so the sentence is cut',
                         'fate': 'cut'}]
        r['needed'] = {'reader': 'none of mine: the text left is his own sentence, unchanged', 'unneeded': [], 'kept': {}}
        probs = S.check(text, r)
        (HERE / ('%s.receipt.json' % t['key'])).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n',
                                                           encoding='utf-8')
        return probs
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
    (HERE / ('%s.receipt.json' % t['key'])).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def main():
    bad, cards = [], []
    by = {t['key']: t for t in T.T}
    edits = {}
    for t in T.T:
        (b,) = [x['i'] for x in BL if x['text'].startswith(t['start'])]
        old, md = new_block(t)
        (HERE / ('%s.md' % t['key'])).write_text(md + '\n', encoding='utf-8')
        (HERE / ('%s.txt' % t['key'])).write_text(T.plain(md) + '\n', encoding='utf-8')
        edits[t['key']] = {'block': b, 'before': sr.block_text(BL, b), 'after': T.plain(md)}
        bad += ['%s: %s' % (t['key'], x) for x in receipt(t, b, md)]
    for key, parts in (('SP97', ['SP97']), ('SP106', ['SP106', 'SP115'])):
        c = CARDS[key]
        cards.append({'id': c['id'], 'type': 'science', 'title': c['title'], 'advice': 'approve',
                      'spans': [{'block': edits[k]['block'], 'start': 0, 'end': len(edits[k]['before'])} for k in parts],
                      'edits': [edits[k] for k in parts],
                      'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
                      'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'use it',
                      'found_by': 'The science pass of Parts 2 and 3, 8 November (flags F-1 and F-11 of the fact check of '
                                  '5 November)',
                      'receipt': [REL + '%s.receipt.json' % k for k in parts]})
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261108-x1108c',
        'title': 'Neuro De-Armoring Cards, 8 November (3): the science of Parts 2 and 3',
        'intro': ['The two flags left in Parts 2 and 3: protein on the keto plan, and potassium. Each card changes only what '
                  'the sources don\'t support, and a fresh reader checked each new sentence for what the reader doesn\'t '
                  'need.',
                  'No compound, dose, unit, timing or warning changes on this page. The potassium card asks what you\'ve '
                  'seen in practice, because the reason that section gives turns out to be backwards.',
                  'After these, the protocol gets read as a whole against the settled science, as you asked.'],
        'git_file': REL + 'REVIEW-X1108C.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1108C.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': cards,
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1108C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1108C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1108C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for s in cards:
        md += ['## %s: %s' % (s['id'], s['title']), '']
        for e in s['edits']:
            md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
                   '**As it would read:**', '', '> %s' % e['after'], '']
        md += ['**What changes:** %s' % s['what'], '', '**Why:** %s' % s['why'], '', '**What stays:** %s' % s['stays'],
               '', '**You\'re deciding:** %s' % s['deciding'], '', '**My advice:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1108C.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [c['id'] for c in cards])
    return 0


if __name__ == '__main__':
    sys.exit(main())
