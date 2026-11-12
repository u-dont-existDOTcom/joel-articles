"""Neuro De-Armoring Cards, 12 November (3): DMSO in the Glutamate Shield (SC-DMSO), after his message of 2026-11-12
21:37 UTC. Texts in texts_x1112c.py, sources in DMSO-PTSD.md; the fresh reads are needed/spdmso/READ.md and
his-fixes/spdmso/READ.md, each with what I did about it. The card adds one paragraph, so it carries the new item as an
insert before block 125 (the Dynorphin Bridge), just after Magnesium.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/dmso/build_x1112c.py
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
sys.path.insert(0, str(HERE.parent / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_x1112c as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/dmso/'
KEY = 'SPDMSO'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
READER = ('someone with trauma whose glutamate storms bring anxiety, rage and racing thoughts, going through the '
          'protocol\'s glutamate tools and wanting to know what each does and whether it is safe for them')
HUANG = 'https://pubmed.ncbi.nlm.nih.gov/42939788/'
TEXT = T.plain(T.NEW)

CARD = dict(
    id='SC-DMSO', title='DMSO in the Glutamate Shield: what it does to glutamate, and who should keep away',
    what='A new item after Magnesium in "2. The Glutamate Shield (Anxiety)": smell DMSO (99.9%), as the Fog table '
         'already says; what your study found, in rat brain cells in a dish; another lab\'s finding at similar '
         'strengths, and in young mice, so keep it away from pregnancy and children; and how far the evidence goes.',
    why='DMSO is already in the protocol in three places, the safety note at the top, the Fog table ("Smell DMSO '
        '(99.9%%)") and the timeline ("Inhale DMSO"), but nowhere does the text say what it does, so the Glutamate Shield '
        'is where your study fits. Your study says what you say: in rat brain cells in a dish, DMSO at 0.5 to 1.5%% '
        'quickly and reversibly damped glutamate\'s NMDA and AMPA signals and the calcium they let in, and kept '
        'glutamate from killing the cells ([Lu & Mattson, 2001](%s)). On the other side, another lab found DMSO at 0.5%% '
        'and 1%% killed rat brain cells in a dish by itself, and injections set off cell death in young mouse brains '
        '([Hanslick, et al, 2009](%s)); given into a vein with frozen stem cells, it has rarely caused seizures and '
        'strokes in people. In people, given into a vein after head injury, it lowered the pressure in the skull in '
        'small series with no comparison group ([Huang & Wang, 2026](%s), a review). I found no study of how much '
        'reaches the brain when it\'s smelled, and no trial of it for anxiety, PTSD or mood, so the people it helps are '
        'in the item as reports.' % (T.LU, T.HANSLICK, HUANG),
    stays='Your safety note at the top, the Fog table and the timeline\'s "Inhale DMSO", as they are.',
    deciding='Whether DMSO goes into the Glutamate Shield with what your study found and the cautions.',
    advice='Approve. I put it with the glutamate tools because that\'s what your study is about; if you\'d rather it sat '
           'by the Fog table, say so in your comment and I\'ll move it.',
    ask='meaning: new text in the protocol: what DMSO does to glutamate, with a caution for pregnancy and children')

SPEC = dict(
    pays=['they learn how the protocol has them take DMSO, and at what purity',
          'they learn what DMSO did to the glutamate signals that drive their storms, and where that was shown',
          'they learn it also protected the cells from glutamate, in the same dish',
          'they learn that at similar strengths it harmed brain cells too, and young brains',
          'they learn who should keep away from it',
          'they learn nobody knows how much reaches the brain by smelling it',
          'they learn it hasn\'t been tested for their condition and rests on reports, which many give'],
    follows=['it opens the item, after Magnesium, the last glutamate tool',
             'it says what the study found',
             'it adds the study\'s second finding',
             'it gives the other side',
             'it turns the other side into what to do',
             'it says how far the dish findings carry to smelling it',
             'it ends on what is known in people'],
    links=[None, 'In rat brain cells', 'It also kept', 'In another lab', 'So keep it away', 'when you smell it',
           'No trial has tested it'],
    checked=[('DMSO suppresses NMDA- and AMPA-mediated excitotoxicity (his study)',
              'in cultured rat hippocampal neurons, DMSO at 0.5 to 1.5% reversibly suppressed glutamate, NMDA and AMPA '
              'currents and calcium influx and prevented excitotoxic death (Lu and Mattson 2001)',
              'yes: they learn what DMSO did to the glutamate signals, in a dish', 'kept'),
             ('DMSO is safe for the brain',
              'DMSO at 0.5% and 1% killed cultured rat neurons, and injections caused widespread apoptosis in the '
              'developing mouse brain (Hanslick et al. 2009); rare seizures and strokes in people given it into a vein '
              'with stem cells (PMID 17353475, 28121745)',
              'yes: they learn who should keep away from it', 'changed'),
             ('DMSO works wonders for many people',
              'no trial of DMSO for anxiety, PTSD or mood found; small uncontrolled series of IV DMSO lowered '
              'intracranial pressure after head injury (Huang and Wang 2026); his firsthand point',
              'yes: they learn it rests on reports, which many give', 'kept')])


def receipt(before):
    where = sr.where(BL, before - 1).rsplit(',', 1)[0]
    r = S.make(TEXT, where, READER)
    sents = r['sentences']
    assert len(sents) == len(SPEC['pays']), len(sents)
    for x, p, f, k in zip(sents, SPEC['pays'], SPEC['follows'], SPEC['links']):
        x['payoff'] = p
        x['follows'] = f
        if 'link' in x:
            assert k and k in x['s'], (k, x['s'][:40])
            x['link'] = k
    r['opens'] = {'first_sentence': sents[0]['s'],
                  'why_reading': 'they learn the protocol has them smell DMSO, and that the item says why, among the '
                                 'glutamate tools for their storms'}
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC['checked']]
    r['needed'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph '
                             '(needed/spdmso/READ.md), of the version before the read against his fixes was acted on',
                   'unneeded': [T.READ[2]], 'kept': {}}
    r['his_fixes'] = {
        'reader': 'a fresh reader (Haiku) given tools/humanization/his_fixes_brief.md and the paragraph, one sentence a '
                  'line (his-fixes/spdmso/READ.md)',
        'marked': [{'s': T.READ[1], 'difference': '1'}, {'s': T.READ[2], 'difference': '1, 4, 8'},
                   {'s': T.READ[3], 'difference': '3'}],
        'kept': {}}
    r['fit'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/fit_read_brief.md, its setting line written for '
                          'this protocol\'s reader, and the text, one sentence a line (fit/spdmso/READ.md)',
                'marked': [{'s': T.plain(T.S5), 'found': 'ANYWAY: tells a reader who isn\'t pregnant and has no children '
                                                       'around nothing new'}],
                'kept': {T.plain(T.S5): 'a caution that holds everywhere, for the readers it applies to (anyone pregnant, '
                                        'or with children who might be given it); the brains harmed in the young mice were '
                                        'developing ones'}}
    r['same_point'] = ('none: read the section from its heading to the next for what DMSO does; the section names no '
                       'DMSO. The safety note at the top (block 7) covers its purity and cleanliness, and the Fog table '
                       'and the timeline (block 179) say when to smell it; this item says what it does and who should '
                       'keep away')
    r['placement'] = ('a new item after Magnesium (block %d), the last of the glutamate tools, before the Dynorphin Bridge '
                      'that turns to the Void' % (before - 1))
    r['questions'] = dict(Q_ANS)
    probs = S.check(TEXT, r)
    (HERE / ('%s.receipt.json' % KEY)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def main():
    (before,) = [x['i'] for x in BL if x['text'].startswith(T.BEFORE)]
    assert sr.block_text(BL, before - 1).startswith(T.AFTER)
    (HERE / ('%s.md' % KEY)).write_text(T.NEW + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % KEY)).write_text(TEXT + '\n', encoding='utf-8')
    bad = ['%s: %s' % (KEY, x) for x in receipt(before)]
    c = CARD
    card = {'id': c['id'], 'type': 'add', 'title': c['title'], 'advice': 'approve',
            'inserts': [{'before': before, 'kind': 'p', 'text': TEXT, 'seq': 1}], 'card_after': before - 1,
            'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
            'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'add it',
            'found_by': 'His message of 2026-11-12 21:37 UTC ("we should include DMSO in the protocol as well"), with his '
                        'study checked and both sides searched through PubMed',
            'receipt': [REL + '%s.receipt.json' % KEY]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261112-x1112c',
        'title': 'Neuro De-Armoring Cards, 12 November (3): DMSO, and the ketone strategies',
        'intro': ['DMSO, as you asked: one new item in the Glutamate Shield, with your study checked and both sides '
                  'searched.',
                  'The ketone-strategy card from earlier tonight is here too, unchanged, since you haven\'t answered it '
                  'yet.',
                  'No compound, dose, unit or timing changes in either.'],
        'git_file': REL + 'REVIEW-X1112C.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1112C.md'},
        'types': {'add': {'label': 'Something added', 'about': 'New text you asked for, with its sources.'},
                  'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [],
    }
    prev = json.loads((HERE.parent / 'coherence' / 'ketone' / 'REVIEW-X1112B.json').read_text(encoding='utf-8'))
    assert prev['article']['sha256'] == review['article']['sha256'], 'the article changed since SC-95 was built'
    review['suggestions'] = prev['suggestions'] + [card]
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1112C.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1112C.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1112C.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['The ketone-strategy card, SC-95, is in [its own page](../coherence/ketone/REVIEW-X1112B.md).', '',
            '## %s: %s' % (card['id'], card['title']), '',
            '*New item after %s*' % sr.where(BL, before - 1), '', '**As it would read:**', '', '> %s' % TEXT, '',
            '**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '',
            '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
            '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1112C.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', card['id'], 'before block', before)
    return 0


if __name__ == '__main__':
    sys.exit(main())
