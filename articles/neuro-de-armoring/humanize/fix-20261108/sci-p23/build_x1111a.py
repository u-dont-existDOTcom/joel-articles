"""Neuro De-Armoring Cards, 11 November: potassium, with your view in it (SC-106d, replacing SC-106c).

His answer of 2026-11-11 21:01 UTC on x1108e sent SC-106c back to revise, with his comment (the potassium-to-sodium ratio
and the brain; the paleo diet; confounding) and GPT's research on diet trials for PTSD. His points checked through
PubMed (SCIENCE-P23.md, "SC-106c and his comment"); texts in texts_x1111a.py, the fresh reader's needed read in
needed/sp106d/READ.md (its two unneeded sentences carry his view: kept, and the card shows him the paragraph without
them).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/sci-p23/build_x1111a.py
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
import texts_x1111a as T  # noqa: E402
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
    id='SC-106d', title='Potassium: blood pressure, your view on the brain and paleo, and the caution',
    what='As on SC-106c, the two labels of the brakes story go (blocks 104 and 105) and block 115\'s second sentence goes. '
         'Block 106 now carries your view: after the blood-pressure reason, that more potassium for the salt you eat helps '
         'the brain too, with the mood trial and the limit you named, and the paleo point, with the potatoes and greens as '
         'the easy start. The kidney and drug caution stays.',
    why='Your comment, checked through PubMed. For mood it holds as far as one small trial goes, as you said: the low-salt, '
        'high-potassium diet lifted mood a little, and it can\'t separate potassium from the salt or the rest of the food '
        '([Torres, et al, 2008](%s)). For memory and thinking the studies are mixed: in older adults a higher '
        'sodium-to-potassium ratio went with more decline over about seven years, though neither alone did and the '
        'authors don\'t take it as a reason to change diet ([Nowak, et al, 2018](%s)); more potassium went with faster '
        'thinking in a US survey ([Zhao, et al, 2025](%s)); a genetic study found no clear link to Alzheimer\'s ([Yoshida, '
        'et al, 2026](%s)). So block 106 gives the brain point as your view, with the mood trial, rather than as what the '
        'science shows. On paleo you\'re right, and 10 g is if anything low: Stone Age diets are estimated at 400 mEq of '
        'potassium a day, about 16 g, more than four times what we eat now ([Sebastian, et al, 2006](%s)), and in nine '
        'people, ten days of a paleo-type diet lowered blood pressure and insulin without weight loss ([Frassetto, et al, '
        '2009](%s)). A fresh reader found the brain and paleo sentences not needed to know why to eat potassium; they\'re '
        'your view, so they\'re in, and the advice below shows the paragraph without them. GPT\'s research on diet trials '
        'for PTSD goes to the read of the whole protocol, since one of them bears on Strategy A\'s salts: 21 people on '
        'ketone salts or placebo, no difference between the groups ([Youssef, et al, 2022](%s)).'
        % (T.TORRES, T.NOWAK, T.ZHAO, T.YOSHIDA, T.SEBASTIAN, T.FRASSETTO, T.YOUSSEF),
    stays='"Potassium:", the target (4,700 mg, the FDA\'s Daily Value), the food-only rule, the menu, "Eat 2 large '
          'potatoes and 2 cups of greens every single day.", the kidney and drug caution from SC-106c, and your caution at '
          'the top. Part 3\'s goal line ("Stabilize voltage to prevent the "Biological Crash" (Headaches/Panic).") goes to '
          'the read of the whole protocol.',
    deciding='Whether block 106 says your view on the brain and on paleo, as written here, or keeps only the '
             'blood-pressure reason and the caution.',
    advice='Approve, if it says your view the way you\'d put it: I\'m fairly sure you want both points in, less sure of '
           'the wording. Without them, block 106 would read: "%s"' % T.plain(T.WITHOUT),
    ask='meaning: block 106 gives your view on the brain and on paleo in my words, and its reason for potassium grows from '
        'blood pressure to the brain')

S2P, S3P = T.plain(T.S2), T.plain(T.S3)
SPEC_106 = dict(
    pays=['they learn why to eat potassium on Strategy A: it brings high blood pressure down, and the salts add sodium',
          'they learn what the author thinks potassium does for the brain, the trial behind it and its limit',
          'they learn that eating closer to a paleo diet is the fuller way to raise their potassium, with the potatoes and '
          'greens as the start',
          'they learn to ask a doctor first if they have kidney disease or take a blood pressure drug that keeps potassium '
          'in, since it can build up in their blood'],
    follows=['it opens the paragraph, after "Potassium:" and the sodium line above it, which warns of high blood pressure '
             'on Strategy A',
             'it adds what the author thinks potassium does beyond blood pressure',
             'it turns from why to how much: the ancestral amount and the fuller way to get it, before the target and the '
             'foods',
             'it ends on who should check with a doctor before eating more of it'],
    checked=[('low potassium (common in high stress) makes the KCNQ brakes fail, and eating potassium puts them back',
              'the brain keeps the potassium around its neurons within tight limits whatever the blood does (Hladky and '
              'Barrand 2016), so neither the drop stress brings to the blood (Brown 1983) nor what you eat sets the brakes',
              'no: the brakes story is cut, with its two labels (blocks 104 and 105)', 'cut'),
             ('eating more potassium brings high blood pressure down',
              'in trials, more potassium lowered systolic pressure by about 3.5 mm Hg, in people with high blood pressure '
              'and not in others (Aburto et al. 2013)',
              'yes: they learn why the target and the foods that follow are there on Strategy A', 'changed'),
             ('a higher potassium-to-sodium ratio helps the brain, mood included (his view)',
              'one small randomized trial: a low-sodium, high-potassium diet lifted mood a little, not separable from the '
              'salt or the food (Torres et al. 2008); memory and thinking mixed (Nowak et al. 2018, Zhao et al. 2025, '
              'Yoshida et al. 2026)',
              'yes: they learn what the author thinks potassium does for the brain and how far the evidence goes', 'kept'),
             ('Stone Age diets had far more potassium; a paleo diet probably does more than adding potatoes (his view)',
              'retrojected Stone Age diets: 400 +/- 125 mEq a day, more than four times current intakes (Sebastian et al. '
              '2006); ten days of a paleo-type diet improved blood pressure and insulin in nine people (Frassetto et al. '
              '2009)',
              'yes: they can eat closer to a paleo diet as the fuller way, with the potatoes and greens as the start',
              'kept'),
             ('kidney disease and drugs that keep potassium in can let it build up',
              'ACE inhibitors and ARBs reduce urinary potassium excretion, which can lead to hyperkalemia (NIH 2022); in '
              'kidney disease, restricting potassium slowed neuropathy over two years (Arnold et al. 2017)',
              'yes: they ask their doctor before eating more potassium if either applies to them', 'kept')])
# the words in each sentence that tie it to the one before or to the reader's case (gate neuro-2026-11-06b)
LINKS = ['which matters on Strategy A', 'helps the brain too', 'the potatoes and greens below', 'If you have kidney disease']
KEPT = {S2P: 'they learn what the author believes potassium does for the brain, with the one trial behind it and its '
             'limit, which is why a potassium step sits in a protocol for their nervous system (his view, from his comment '
             'of 2026-11-11, which his revise asked for)',
        S3P: 'they can choose to eat closer to a paleo diet as the fuller way to raise their potassium, with the potatoes '
             'and greens as the start (his view, from the same comment)'}


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
    if t['key'] == 'SP115F':   # what stays of block 115 is his own sentence; the card only cuts the one after it
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
        r['needed'] = {'reader': FRESH % 'sp106d', 'unneeded': [S2P, S3P], 'kept': dict(KEPT)}
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
            'found_by': 'His answer of 2026-11-11 21:01 UTC on SC-106c: his comment, each point checked through PubMed',
            'receipt': [REL + '%s.receipt.json' % k for k in keys if edits[k]['after']]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261111-x1111a',
        'title': 'Neuro De-Armoring Cards, 11 November: potassium, with your view in it',
        'intro': ['SC-106c again, with your comment, which I checked through PubMed. On paleo you\'re right; on the brain, '
                  'one small trial backs the mood part and the studies of memory and thinking are mixed, so the '
                  'paragraph gives it as your view.',
                  'This card replaces SC-106c. No compound, dose, unit or timing changes.',
                  'After this card, the protocol gets read as a whole against the settled science.'],
        'git_file': REL + 'REVIEW-X1111A.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1111A.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1111A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1111A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1111A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    md += ['## %s: %s' % (card['id'], card['title']), '']
    for e in card['edits']:
        md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
               '**As it would read:**', '', '> %s' % (e['after'] or '(cut)'), '']
    md += ['**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '', '**What stays:** %s' % card['stays'],
           '', '**You\'re deciding:** %s' % card['deciding'], '', '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1111A.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', card['id'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
