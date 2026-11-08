"""Neuro De-Armoring Cards, 8 November (4): potassium, after GPT's critique (SC-106b).

His answer of 2026-11-08 15:45 UTC on x1108c sent SC-106 back to revise, with GPT's critique of it in the box. Each of
GPT's points was checked through PubMed (SCIENCE-P23.md, "SC-106 revised"); texts in texts_x1108d.py, the fresh
reader's needed read in needed/sp106b/READ.md (its unneeded sentence cut).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/build_x1108d.py
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
import texts_x1108d as T  # noqa: E402
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
UNNEEDED_106 = ('It won\'t calm your nerves, though, because your brain keeps the potassium around its neurons within tight '
                'limits, whatever your blood is doing (Hladky & Barrand, 2016), even when stress lowers the potassium in '
                'your blood by pushing it into your cells (Brown, et al, 1983).')

CARD = dict(
    id='SC-106b', title='Potassium: it\'s there for blood pressure, not for the nerves',
    what='The two labels of the brakes story go (blocks 104 and 105), and block 106 gives the reason that holds for eating '
         'potassium: it brings high blood pressure down, which matters with the sodium in Strategy A\'s salts. As on the '
         'first card, "This saturates your cells, lowering your resting voltage ..." goes from block 115.',
    why='GPT is right, and each fact it gives holds when checked: the study my card leaned on measured the arm and leg '
        'nerves of one patient whose blood potassium had fallen to 2.1 ([Kuwabara, et al, 2002](%s)); in guinea-pig brain '
        'slices, dropping potassium from 4 to 2 first quieted the cells, then set off seizure-like bursts ([Gorji, et al, '
        '2001](%s)); broken KCNQ channels do make neurons fire too easily, as in one inherited epilepsy of newborns '
        '([Biervert, et al, 1998](%s)); and the drop adrenaline brings is potassium moving into the cells, not a lack of it '
        '([Brown, et al, 1983](%s)). What settles it is the point my card missed: your brain keeps the potassium around its '
        'neurons within tight limits, whatever your blood is doing ([Hladky & Barrand, 2016](%s); in dogs, the fluid '
        'around the brain stayed the same while blood potassium changed, [Javaheri & Kazemi, 1981](%s)). So neither stress '
        'nor diet works the brakes through potassium. The trial I found on potassium-rich diets and mood doesn\'t show '
        'it either: both diets were high in potassium, and the one lower in salt did better ([Torres, et al, 2008](%s)). '
        'What holds is blood pressure: across the trials, more potassium brought systolic pressure down by about 3.5 '
        'points, an effect seen in people whose pressure was high and not in others, and it goes with a lower risk of '
        'stroke ([Aburto, et al, 2013](%s)). GPT\'s own version '
        'keeps the lab details, which a reader can\'t act on, and says the foods "support normal nerve function", which '
        'no source shows for eating more. My card stated one patient\'s nerves as what all nerve cells do and assumed the '
        'brain follows the blood (lesson neuro-2026-11-08j). A fresh reader found the sentence saying potassium won\'t '
        'calm the nerves unneeded once the brakes story is gone, so it\'s here, not in your article.'
        % (T.KUWABARA, T.GORJI, T.BIERVERT, T.BROWN, T.HLADKY, T.JAVAHERI, T.TORRES, T.ABURTO),
    stays='"Potassium:", the target (4,700 mg, the FDA\'s Daily Value), the food-only rule, the menu, and "Eat 2 large '
          'potatoes and 2 cups of greens every single day." GPT says that amount isn\'t for everyone, especially with kidney '
          'trouble; your article says so at the top ("Electrolytes: Consult a doctor if you have kidney disease or heart '
          'conditions."), and the read of the whole protocol puts it beside the step. Part 3\'s goal line ("Stabilize '
          'voltage to prevent the "Biological Crash" (Headaches/Panic).") goes to that read too.',
    deciding='Whether potassium stays in the protocol for blood pressure, the reason that holds, instead of the brakes, '
             'which don\'t. If you\'d rather drop the potassium step altogether, say so in the box.',
    advice='Approve. If you\'ve seen potassium help people\'s nerves in practice, tell me what you saw and I\'ll look for '
           'what explains it.',
    ask='meaning: the reason the section gives for potassium changes from calming the nerves to blood pressure, and that '
        'reason carries the section')

SPEC_106 = dict(
    pays=['they learn why to eat potassium on Strategy A: it brings high blood pressure down, and the salts add sodium'],
    checked=[('low potassium (common in high stress) makes the KCNQ brakes fail, and eating potassium puts them back',
              'the brain keeps the potassium around its neurons within tight limits whatever the blood does (Hladky and '
              'Barrand 2016; dogs: Javaheri and Kazemi 1981), so neither the drop stress brings to the blood (Brown 1983) '
              'nor what you eat sets the brakes',
              'no: the brakes story is cut, with its two labels (blocks 104 and 105)', 'cut'),
             ('eating more potassium brings high blood pressure down',
              'in trials, more potassium lowered systolic pressure by about 3.5 mm Hg, in people with high blood pressure '
              'and not in others (Aburto et al. 2013)',
              'yes: they learn why the target and the foods that follow are there on Strategy A', 'changed')])


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
    if t['key'] == 'SP115D':   # what stays of block 115 is his own sentence; the card only cuts the one after it
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
        for x, p in zip(sents, SPEC_106['pays']):
            x['payoff'] = p
            x['follows'] = ('it opens the paragraph, after "Potassium:" and the sodium line above it, which warns of high '
                            'blood pressure on Strategy A')
            if 'link' in x:
                x['link'] = x['s'].split()[0]
        r['opens'] = {'first_sentence': sents[0]['s'], 'why_reading': SPEC_106['pays'][0]}
        r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC_106['checked']]
        r['needed'] = {'reader': FRESH % 'sp106b', 'unneeded': [UNNEEDED_106], 'kept': {}}
    r['same_point'] = 'none: read the section from its heading to the next for the same point; it appears once'
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
            'found_by': 'His answer on SC-106 (x1108c, 2026-11-08 15:45 UTC): GPT\'s critique of the card, each point checked '
                        'through PubMed',
            'receipt': [REL + '%s.receipt.json' % k for k in keys if edits[k]['after']]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261108-x1108d',
        'title': 'Neuro De-Armoring Cards, 8 November (4): potassium, after GPT\'s critique',
        'intro': ['SC-106 again. I checked each point GPT made against its source through PubMed: its facts hold, and my '
                  'correction had stretched the one study it leaned on.',
                  'Two labels go and one sentence changes; no compound, dose, unit, timing or warning changes on this page.',
                  'Your SC-97 (protein) is in the article. After this card, the protocol gets read as a whole against the '
                  'settled science.'],
        'git_file': REL + 'REVIEW-X1108D.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1108D.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1108D.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1108D.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1108D.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    md += ['## %s: %s' % (card['id'], card['title']), '']
    for e in card['edits']:
        md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
               '**As it would read:**', '', '> %s' % (e['after'] or '(cut)'), '']
    md += ['**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '', '**What stays:** %s' % card['stays'],
           '', '**You\'re deciding:** %s' % card['deciding'], '', '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1108D.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', card['id'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
