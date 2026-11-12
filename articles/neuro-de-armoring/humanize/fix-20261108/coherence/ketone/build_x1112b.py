"""Neuro De-Armoring Cards, 12 November (2): the two ketone strategies (SC-95), the first card of the read of the whole
protocol (coherence/EXTRACT.md, 2.4, with Strategy A's promise).

Texts and sources in texts_x1112b.py and KETONE-STRATEGY.md; the fresh reads are needed/sp95/READ.md and
his-fixes/sp95/READ.md, each with what I did about it.

  python3 articles/neuro-de-armoring/humanize/fix-20261108/coherence/ketone/build_x1112b.py
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
H = HERE.parents[2]
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[1] / 'sci-cde'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402
import texts_x1112b as T  # noqa: E402
from build_x1108b import Q_ANS  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/coherence/ketone/'
KEY = 'SP95'
MD = (H / 'HUMANIZED-SO-FAR.md').read_text(encoding='utf-8')
BL = sr.blocks(MD)
READER = ('someone with trauma or in withdrawal who is anxious, wired, numb or foggy, about to choose how to get ketones '
          'and wanting to know what each way asks of them and does')
SHORT = ' '.join(T.plain(x) for x in (T.S1, T.S2, T.S3))
S3P, S4P = T.plain(T.S3), T.plain(T.S4)

CARD = dict(
    id='SC-95', title='The two ketone strategies: what the choice decides, and what the salts do for the fog',
    what='Block 95 no longer says you must pick one strategy: it says your strategy decides how you handle salt. "Need '
         'the fog gone fast" becomes "need the fog to lift fast", and a sentence gives what trials found ketone '
         'supplements do for thinking.',
    why='Reading the protocol as a whole, block 95 says you must pick one strategy, but the timeline starts you on the '
        'salts, moves you to the diet in Weeks 3 to 5, and still has you "Drink BHB" when foggy on the diet. Your post '
        'said the choice "determines your electrolyte protocol", and that\'s what holds: one after the other, the two '
        'don\'t clash, and the salts\' sodium on the diet just goes toward what the diet drains. The Oslo PTSD study, which '
        'measured ketosis three times a day, gave both together ([Edwards, et al, 2024](%s)). On the fog, in a 2026 meta-analysis of 29 '
        'trial protocols (1,117 people), ketone esters, salts and MCT oil improved thinking a little against a placebo, '
        'about as much after a single dose as over two weeks or more, and more at higher daily doses ([Bonnechère, et al, '
        '2026](%s)). Some found nothing, such as one in adults with type 2 diabetes ([Baranowski, et al, 2025](%s)) and one '
        'in low oxygen ([Stalmans, et al, 2025](%s)). So "gone" becomes "lift", with the size the trials found.'
        % (T.EDWARDS, T.BONNECHERE, T.BARANOWSKI, T.STALMANS),
    stays='Strategy A, the "Crisis Mode", with the salts and a standard low-sugar diet; Strategy B below it; and the '
          'timeline as it is, starting on the salts, moving to the diet, the salts when foggy.',
    deciding='Whether block 95 says what the choice of strategy decides, instead of that you must pick one, and gives '
             'what the salts do for thinking at the size trials found.',
    advice='Approve. I\'m sure of what the trials found. A fresh reader would drop the trials sentence as not needed to '
           'choose; I\'d keep it, since the promise that the fog lifts is made as science and the reader learns how much '
           'to expect. That reader\'s version: "%s"' % SHORT,
    ask='meaning: block 95 no longer says you must pick one strategy, and the fog promise gets the size trials found')

SPEC = dict(
    pays=['they learn their strategy decides how they handle salt, and why',
          'they learn Strategy A is the one for a crisis, when the fog has to lift fast',
          'they learn what Strategy A asks of them: drink the salts and keep a standard low-sugar diet',
          'they learn how much lift to expect for their thinking and how soon, so they don\'t count on the fog being '
          'gone'],
    follows=['it opens the choice between the two strategies, after the ATP paragraph',
             'it turns from the salt plan to the first strategy',
             'it says what the strategy just named asks',
             'it backs the strategy\'s promise with what trials found'],
    links=[None, 'there\'s Strategy A', 'You drink BHB', 'In trials'],
    checked=[('you must pick one of two ketone strategies',
              'his post: "You must choose your fuel strategy. This determines your electrolyte protocol."; the timeline '
              'uses both in turn (blocks 169, 177) and "Drink BHB" on the diet (block 179); the Oslo PTSD study gave a '
              'keto diet and BHB salts together (Edwards et al. 2024)',
              'yes: they learn the choice decides their salt plan, so they can follow the timeline from one to the other',
              'changed'),
             ('BHB salts clear the fog fast',
              'exogenous ketones improved cognition against placebo, SMD 0.29 over 29 protocols and 1,117 people, single '
              'doses and use over 13 days alike (Bonnechere et al. 2026); no effect in type 2 diabetes (Baranowski et al. '
              '2025) or in hypoxia (Stalmans et al. 2025)',
              'yes: they learn how much lift to expect and how soon', 'changed')])


def receipt(b):
    text = T.plain(T.NEW)
    where = sr.where(BL, b).rsplit(',', 1)[0]
    r = S.make(text, where, READER)
    sents = r['sentences']
    assert len(sents) == len(SPEC['pays']), len(sents)
    for x, p, f, k in zip(sents, SPEC['pays'], SPEC['follows'], SPEC['links']):
        x['payoff'] = p
        x['follows'] = f
        if 'link' in x:
            assert k and k in x['s'], (k, x['s'][:40])
            x['link'] = k
    r['opens'] = {'first_sentence': sents[0]['s'],
                  'why_reading': 'they learn the choice they are about to make decides how they handle salt'}
    r['checked'] = [{'point': a, 'found': f, 'still_needed': s, 'fate': fate} for a, f, s, fate in SPEC['checked']]
    keep4 = ('they learn how much lift to expect for their thinking and how soon, the size behind the promise that the '
             'fog lifts fast')
    r['needed'] = {'reader': 'a fresh reader (Haiku) given tools/humanization/needed_read_brief.md and only this paragraph '
                             '(needed/sp95/READ.md), of the version before the read against his fixes was acted on',
                   'unneeded': [T.S4_READ, S4P], 'kept': {S4P: keep4, T.S4_READ: 'reworded as the next entry; ' + keep4}}
    r['his_fixes'] = {
        'reader': 'a fresh reader (Haiku) given tools/humanization/his_fixes_brief.md and the paragraph, one sentence a '
                  'line (his-fixes/sp95/READ.md)',
        'marked': [{'s': T.S1_READ, 'difference': '1, 3'}, {'s': S3P, 'difference': '4'},
                   {'s': T.S4_READ, 'difference': '4, 7'}],
        'kept': {S3P: 'his post\'s own wording ("You eat a standard low-sugar diet"), which the reader knows'}}
    r['same_point'] = ('none: read the section from its heading to the next for what each strategy does to the salt plan; '
                       'the electrolytes section (blocks 102 and 114) gives each plan, which this sentence leads to, and '
                       'the timeline (blocks 169, 177, 179) uses the strategies in turn')
    r['placement'] = ('where the block is now (block %d), after the ATP paragraph that brings in ketones and before '
                      'Strategy B' % b)
    r['questions'] = dict(Q_ANS)
    probs = S.check(text, r)
    (HERE / ('%s.receipt.json' % KEY)).write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    return probs


def main():
    (b,) = [x['i'] for x in BL if x['text'].startswith(T.START)]
    assert sr.block_text(BL, b) == T.plain(T.OLD)
    edit = {'block': b, 'before': sr.block_text(BL, b), 'after': T.plain(T.NEW)}
    (HERE / ('%s.md' % KEY)).write_text(T.NEW + '\n', encoding='utf-8')
    (HERE / ('%s.txt' % KEY)).write_text(T.plain(T.NEW) + '\n', encoding='utf-8')
    bad = ['%s: %s' % (KEY, x) for x in receipt(b)]
    c = CARD
    card = {'id': c['id'], 'type': 'science', 'title': c['title'], 'advice': 'approve',
            'spans': [{'block': b, 'start': 0, 'end': len(edit['before'])}], 'edits': [edit],
            'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'deciding': c['deciding'],
            'advice_note': c['advice'], 'ask_because': c['ask'], 'approve_label': 'use it',
            'found_by': 'The read of the whole protocol (coherence/EXTRACT.md, 2.4), with the ketone research of lessons '
                        'neuro-2026-11-11b and 11c',
            'receipt': [REL + '%s.receipt.json' % KEY]}
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261112-x1112b',
        'title': 'Neuro De-Armoring Cards, 12 November (2): the two ketone strategies',
        'intro': ['The first card of the read of the whole protocol, where the text disagrees with itself. Block 95 says '
                  'to pick one ketone strategy, while the timeline uses both; and the salts\' promise gets what trials '
                  'found.',
                  'One card. No compound, dose, unit or timing changes.',
                  'The other places the protocol disagrees with itself come next, one card each.'],
        'git_file': REL + 'REVIEW-X1112B.html',
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': hashlib.sha256(MD.encode('utf-8')).hexdigest()},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1112B.md'},
        'types': {'science': {'label': 'A claim corrected',
                              'about': 'Something the sources don\'t support, changed as little as the science allows.'}},
        'suggestions': [card],
    }
    bad += ['PROBLEM ' + x for x in sr.check(review, BL)]
    (HERE / 'REVIEW-X1112B.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for x in bad:
        print(x)
    if bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1112B.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1112B.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    out = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    out += ['## %s: %s' % (card['id'], card['title']), '', '*%s*' % sr.where(BL, b), '', '**Now:**', '',
            '> %s' % edit['before'], '', '**As it would read:**', '', '> %s' % edit['after'], '',
            '**What changes:** %s' % card['what'], '', '**Why:** %s' % card['why'], '',
            '**What stays:** %s' % card['stays'], '', '**You\'re deciding:** %s' % card['deciding'], '',
            '**My advice:** %s' % card['advice_note'], '']
    (HERE / 'REVIEW-X1112B.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('ok', card['id'], 'block', b)
    return 0


if __name__ == '__main__':
    sys.exit(main())
