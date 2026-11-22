"""Neuro De-Armoring Cards, 11 November (3): ketosis in people with PTSD (SC-48b).

His message of 2026-11-11 22:53 UTC: "ok and also ketones do seem to help ppl with ptsd idk why youre research is always
wrong", with GPT's review of ketogenic diets and ketone salts for PTSD. Block 48 ended on my "Whether ketosis does that
in people hasn't been tested.", which reads as if ketosis had never been tried in people with PTSD. Sources in
texts_x1111c.py and KETO-PTSD.md; the fresh needed read is needed/sp48b/READ.md.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/keto/build_x1111c.py
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
import texts_x1111c as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/keto/'
KEY = 'SP48B'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
RAW = [x for x in re.split(r'\n\s*\n', MD) if x.strip()]
READER = ('someone with trauma or in withdrawal who is anxious, wired, numb or foggy, wanting to know what is going on in '
          'their brain and which of the protocol\'s tools does what')
FRESH = 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph (needed/%s/READ.md)'
WHOSE = ('his own: block 48\'s first four sentences, as he wrote them in his answer on SC-48 (2026-11-08 15:08 UTC, '
         'APPLIED-X1108B.json)')
INTEGRATIVE = 'https://pubmed.ncbi.nlm.nih.gov/42780737/'
NCT_DE = 'https://clinicaltrials.gov/study/NCT07415590'
UKRAINE = 'https://pubmed.ncbi.nlm.nih.gov/41345238/'

BENGAY = 'That\'s a bit like putting some Bengay on a broken leg.'
MOUSE = ('and in mice that couldn\'t hold on to extinction learning (learning that a cue is now safe), an HDAC blocker made '
         'the new learning last (Whittle & Singewald, 2014).')
HIS = T.plain(T.HIS)
SHORT = ' '.join(['Why don\'t these drugs work on calcified PTSD?', 'Because even if they did work for mood by modulating '
                  'serotonin transmission, PTSD is not a mood disorder.', 'This protocol tries to get at the underpinnings '
                  'of the problem.', 'The ketone BHB blocks enzymes called HDACs (Shimazu, et al, 2013).',
                  T.plain(T.S6), T.plain(T.S7), T.plain(T.S8)])

CARD = dict(
    id='SC-48b', title='Ketosis in people with PTSD: what has been seen, and how far it goes',
    what='Block 48\'s last sentence, mine ("Whether ketosis does that in people hasn\'t been tested."), becomes three: '
         'the first small study of a keto diet with BHB supplements in people with PTSD, where both people who finished '
         'improved; two case reports of PTSD that treatment hadn\'t helped, nearly or fully gone after months on the diet; '
         'and the limit, that the diet has had no controlled trial yet and the one placebo-controlled trial of BHB '
         'supplements was too small to tell.',
    why='You\'re right. My sentence was true of the HDAC route, but it reads as if ketosis had never been tried in people '
        'with PTSD, and it has. GPT\'s sources check out. In Oslo, of three people who started four weeks of a keto diet '
        'with BHB salts, the two who finished went from 70 to 50 and from 50 to 40 on the PCL-5, the standard 80-point '
        'PTSD checklist, which its authors call a reliable and clinically meaningful improvement ([Edwards, et al, '
        '2024](%s)). A woman whose PTSD three years of trauma-focused therapy hadn\'t notably improved went from 80, the '
        'checklist\'s maximum, to 0 by week 12 ([Bellamy & Laurent, 2025](%s)), and a woman whose PTSD therapy and drugs '
        'hadn\'t helped went from 32 to 2 at 27 weeks ([Laurent, 2026](%s)). This year\'s review of all of it finds only '
        'minimal reliable information from human studies so far ([Frontiers in Psychiatry, 2026](%s)), and the studies '
        'registered have no comparison group: [a six-person one in Munich](%s) finished in August with no results posted '
        'yet. In chat I also said the one placebo-controlled trial of ketone salts ended with the two groups no '
        'different ([Youssef, et al, 2022](%s)). That made a trial too small to tell sound like a negative. Its ketone '
        'group\'s scores fell (a median of 58.5 to 54) while the placebo group\'s didn\'t move, but with 21 people the '
        'difference between the groups wasn\'t significant, which its authors put down to the small size. Left out: two '
        'rat studies, which add nothing to the mouse finding already there, and [a Ukrainian survey](%s) that found '
        'people with PTSD more often on restrictive diets, keto among them, which says nothing about what the diet does '
        'to PTSD.' % (T.EDWARDS, T.BELLAMY, T.LAURENT, INTEGRATIVE, NCT_DE, T.YOUSSEF, UKRAINE),
    stays='Your four sentences on why the drugs fall short, the Bengay line among them, and the HDAC and mouse sentence. '
          'Strategy A\'s "need the fog gone fast" with the salts, and the other ketone steps, go to the read of the whole '
          'protocol.',
    deciding='Whether block 48 ends on what has been seen in people with PTSD on a keto diet, with its limit, in place '
             'of "hasn\'t been tested".',
    advice='Approve. I\'m sure of the facts, less sure of the length. A fresh reader kept all three new sentences and '
           'would also lose the Bengay line and the mouse half of the HDAC sentence, which I\'d keep: the Bengay line is '
           'how you put it, and the mouse finding is the one place the article says why blocking HDACs matters for '
           'PTSD. That reader\'s version: "%s"' % SHORT,
    ask='meaning: what block 48 tells readers about ketosis in people with PTSD changes, from untested to early signs '
        'with no controlled trial yet')

SPEC = dict(
    pays=['they learn what the protocol\'s ketones do in the brain that a mood drug doesn\'t, and that the learning '
          'result comes from mice',
          'they learn that people with PTSD on a keto diet with BHB supplements have improved, and by how much',
          'they learn that PTSD treatment hadn\'t helped has nearly or fully gone on the diet in two people',
          'they learn how far this evidence goes, so they take it as early signs, not proof'],
    follows=['it says what "the underpinnings" are and how the protocol gets at them',
             'it turns from the mouse finding to people with PTSD',
             'it adds two longer cases to the four-week study',
             'it ends on the limit of the human evidence'],
    links=['The ketone BHB', 'In people with PTSD', 'on the diet', 'No controlled trial of the diet'],
    checked=[('the ketone BHB blocks HDACs; in mice an HDAC blocker made extinction learning last',
              'as on SC-48 (Shimazu et al. 2013; Whittle and Singewald 2014)',
              'yes: they learn why the protocol uses ketones for PTSD rather than for mood', 'kept'),
             ('whether ketosis does that in people hasn\'t been tested',
              'true of the HDAC route, but ketosis has been tried in people with PTSD: a four-week keto diet with BHB '
              'salts, PCL-5 down 20 and 10 points in the two who finished (Edwards et al. 2024); two case reports, PCL-5 '
              '80 to 0 at 12 weeks and 32 to 2 at 27 weeks (Bellamy and Laurent 2025; Laurent 2026)',
              'yes: they learn what has been seen when people with PTSD tried ketosis, in place of a sentence that '
              'reads as if it never had been', 'changed'),
             ('how far the human evidence goes',
              'no controlled trial of the diet (the registered studies are single-arm: NCT05415982, NCT07415590); a 2026 '
              'integrative review finds only minimal reliable information from human studies; the one placebo-controlled '
              'trial of BHB salts found no difference between its groups with 21 people, which its authors put down to '
              'its size (Youssef et al. 2022)',
              'yes: they take the human results as early signs, not proof', 'changed')])
KEPT = {BENGAY: 'they get the author\'s own picture of a mood drug used on a broken structure, his words, which only he '
                'can cut',
        MOUSE: 'they learn why blocking HDACs matters for PTSD: it made the learning that a cue is now safe last, shown '
               'so far in mice with another HDAC blocker'}


def new_block():
    (r,) = [k for k, x in enumerate(RAW) if x.startswith(T.START)]
    assert RAW[r].count(T.OLD) == 1
    return RAW[r].replace(T.OLD, T.NEW)


def receipt(b, md):
    text = T.plain(md)
    where = sr.where(BL, b).rsplit(',', 1)[0]
    r = S.make(text, where, READER, his_text=HIS, whose=WHOSE)
    mine = [x for x in r['sentences'] if not x.get('his')]
    assert len(mine) == len(SPEC['pays']), len(mine)
    for x, p, f, k in zip(mine, SPEC['pays'], SPEC['follows'], SPEC['links']):
        x['payoff'] = p
        x['follows'] = f
        assert k in x['s'], (k, x['s'][:40])
        x['link'] = k
    r['opens'] = {'first_sentence': r['sentences'][0]['s'],
                  'why_reading': 'they learn the paragraph answers why the drugs they tried haven\'t fixed their PTSD'}
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC['checked']]
    r['needed'] = {'reader': FRESH % 'sp48b', 'unneeded': [BENGAY, MOUSE], 'kept': dict(KEPT)}
    (c,) = [x['i'] for x in BL if x['text'].startswith('If your cortisol is normal or low')]
    r['same_point'] = ('none: read section C from its heading to the next for what ketosis has done in people with PTSD; '
                       'it appears once. Block %d gives three adults whose depression and anxiety went on a keto diet '
                       '(Calabrese 2024), another condition, and stays where it is' % c)
    r['placement'] = ('where the block is now (block %d), after the reasons the drugs fall short; the new sentences end '
                      'it, after the mouse finding they answer for people' % b)
    r['questions'] = dict(Q_ANS)
    probs = S.check(text, r)
    (HERE / ('%s.receipt.json' % KEY)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def main():
    (b,) = [x['i'] for x in BL if x['text'].startswith(T.START)]
    md = new_block()
    edit = {'block': b, 'before': sr.block_text(BL, b), 'after': T.plain(md)}
    (HERE / ('%s.md' % KEY)).write_text(md + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % KEY)).write_text(T.plain(md) + '\n', encoding='utf-8')
    bad = ['%s: %s' % (KEY, x) for x in receipt(b, md)]
    c = CARD
    card = {'id': c['id'], 'type': 'science', 'title': c['title'], 'advice': 'approve',
            'spans': [{'block': b, 'start': 0, 'end': len(edit['before'])}], 'edits': [edit],
            'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
            'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'use it',
            'found_by': 'His message of 2026-11-11 22:53 UTC ("ketones do seem to help ppl with ptsd"), with GPT\'s '
                        'review; every source checked through PubMed and ClinicalTrials.gov',
            'receipt': [REL + '%s.receipt.json' % KEY]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261111-x1111c',
        'title': 'Neuro De-Armoring Cards, 11 November (3): ketosis in people with PTSD',
        'intro': ['After your message on ketones. My last sentence in block 48 read as if ketosis had never been tried in '
                  'people with PTSD; this card puts in what has been seen, with GPT\'s sources checked one by one.',
                  'One card. No compound, dose, unit or timing changes.',
                  'Strategy A\'s promise and the other ketone steps go to the read of the whole protocol.'],
        'git_file': REL + 'REVIEW-X1111C.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1111C.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1111C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1111C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1111C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['## %s: %s' % (card['id'], card['title']), '', '*%s*' % sr.where(BL, b), '', '**Now:**', '',
            '> %s' % edit['before'], '', '**As it would read:**', '', '> %s' % edit['after'], '',
            '**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '',
            '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
            '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1111C.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', card['id'], 'block', b)
    return 0


if __name__ == '__main__':
    sys.exit(main())
