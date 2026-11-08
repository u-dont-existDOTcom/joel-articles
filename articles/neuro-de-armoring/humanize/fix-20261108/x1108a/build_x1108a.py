"""Neuro De-Armoring Cards, 8 November: two science points in his own versions of blocks 37 and 38.

His answers of 00:49 UTC (`../ANSWERS-X1107C-20261108-0049.json`) gave his own versions of both paragraphs; both are in
the article and read Human. Gate neuro-2026-11-08c: a new claim in his words gets a science check, and a fix to his words
goes on a card (ask_because "his own: ..."). Two of his claims don't match their sources:

- block 37, "can swell and injure": the swelling seen in glutamate toxicity comes from sodium and chloride, early and in
  toxic doses in a dish; calcium is the slower, killing part (Choi 1987).
- block 38, "NMDA receptor opening is the main spark that starts up neuronal excitation" and "another calcium door":
  AMPA receptors start the excitation, NMDA receptors are held shut by magnesium until it has started and are then the
  main calcium door (Hansen 2018); the GluD channel lets in very little calcium (Schmid 2009).

  python3 articles/neuro-de-armoring/humanize/fix-20261108/x1108a/build_x1108a.py
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parent
H = FIX.parent
ROOT = H.parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

BLOB = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/'
LANE = 'articles/neuro-de-armoring/humanize/'
REL = LANE + 'fix-20261108/x1108a/'
FIXREL = LANE + 'fix-20261108/'
GIT_FILE = REL + 'REVIEW-X1108A.html'
ARTICLE = H / 'HUMANIZED-SO-FAR.md'
MD = ARTICLE.read_text(encoding='utf-8')
SHA = hashlib.sha256(MD.encode('utf-8')).hexdigest()
BL = sr.blocks(MD)
P = 'https://www.pangram.com/history/'
HIS37 = P + '3630663f-3104-4ce7-86f7-462cbb26601d'
HIS38 = P + 'e798ace7-cc92-45ff-973e-ceaf1f5ed2c4'
T37B = P + '755ca0fd-b05f-4092-95b2-6e9da5daa36f'
T38B = P + 'e3845c44-7bf0-4e7d-93a8-706b596c9c4b'
CHOI = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6568907'
GOLDBERG = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6576549'
HANSEN = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6080888'
SCHMID = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2700928'
WANG = 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12520249/'

TYPES = {
    'science': {'label': 'A claim corrected',
                'about': 'Something in your new wording doesn\'t match what the sources show. The card has your '
                         'paragraph with only that part changed, and what it read in Pangram.'},
}
CHECKED = {
    'T37b': [{'point': 'calcium at such high levels caused by stress "can swell and injure the neurons"',
              'found': 'the swelling in glutamate toxicity is early and comes from sodium, chloride and water; calcium '
                       'drives the slower damage (Choi 1987; Goldberg and Choi 1993, both in cultured neurons at toxic '
                       'doses); nothing shows swelling at stress levels',
              'still_needed': 'yes: they learn the calcium can injure the cells, which the next sentence builds on',
              'fate': 'changed'}],
    'T38b': [{'point': 'NMDA receptor opening is "the main spark that starts up neuronal excitation", and GluD is '
                       '"another calcium door"',
              'found': 'AMPA receptors start the excitation; magnesium holds NMDA receptors shut until that '
                       'depolarization frees them, and they are then the main calcium door (Hansen 2018). The GluD2 '
                       'channel passes very little calcium (Schmid 2009)',
              'still_needed': 'yes: they learn GluD is a second door at the same synapse, opened by D-serine and GABA',
              'fate': 'changed'}],
}


def receipts():
    bad = False
    for k, v in CHECKED.items():
        p = FIX / ('%s.receipt.json' % k)
        r = json.loads(p.read_text(encoding='utf-8'))
        r['checked'] = v
        p.write_text(json.dumps(r, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        text = (FIX / ('%s.txt' % k)).read_text(encoding='utf-8').strip()
        for x in S.check(text, r):
            print(k, 'RECEIPT PROBLEM', x)
            bad = True
    return bad


def block(prefix):
    hits = [b['i'] for b in BL if b['text'].startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def card(sid, title, key, prefix, what, why, stays, deciding, note, ask_because, approve_label):
    i = block(prefix)
    after = (FIX / ('%s.txt' % key)).read_text(encoding='utf-8').strip()
    return {'id': sid, 'type': 'science', 'title': title, 'advice': 'approve',
            'spans': [{'block': i, 'start': 0, 'end': len(sr.block_text(BL, i))}],
            'edits': [{'block': i, 'before': sr.block_text(BL, i), 'after': after}],
            'what': what, 'why': why, 'stays': stays, 'deciding': deciding, 'advice_note': note,
            'ask_because': ask_because, 'approve_label': approve_label,
            'found_by': 'The science check on your new wording, 8 November',
            'receipt': [FIXREL + '%s.receipt.json' % key]}


def main():
    bad = receipts()
    S_ = [
        card('SC-37', 'Calcium injures; it isn\'t what swells the cell', 'T37b', 'The Mechanism:',
             'Two words out: "can swell and injure the neurons" becomes "can injure the neurons". Nothing else in your '
             'paragraph changes.',
             'The swelling seen when glutamate poisons neurons comes from sodium, chloride and water rushing in, '
             'within minutes; calcium is the slower part that does the killing, hours later ([Choi, 1987](%s); '
             '[Goldberg and Choi, 1993](%s)). Both are cultured neurons at toxic doses, nothing like stress levels, so '
             '"swell" says more than anything shows for stress, and it pins it on the wrong ion. Your version read '
             '[Human, High 137 and Medium 13](%s); with the two words out it reads [Human, High all 148 words](%s).'
             % (CHOI, GOLDBERG, HIS37, T37B),
             'Everything else as you wrote it: the jammed doors, Bonifacino, Conrad and "kind of common sense", the '
             'amygdala and Boyle.',
             'Whether "swell" goes.',
             'Approve.',
             'his own: these are your words, and "swell" leaves your paragraph',
             'use it without "swell"'),
        card('SC-38', 'NMDA is the main calcium door; AMPA is the spark', 'T38b', 'The Secondary Signal Dial',
             'Your first clause changes: "While NMDA receptor opening is the main spark that starts up neuronal '
             'excitation, another calcium door was recently discovered" becomes "While NMDA receptors are the main '
             'door calcium comes in through when glutamate fires, another door was recently discovered". Your second '
             'sentence stays word for word.',
             'Two things in the clause don\'t hold. The spark is the AMPA receptors: magnesium holds the NMDA door '
             'shut at rest, and only the jolt from AMPA frees it, after which NMDA is the main way calcium gets in '
             '([Hansen, et al, 2018](%s)). That is the same magnesium plug the Lock paragraph is about, so "main '
             'spark" would contradict the guide a few lines down. And the GluD channel lets very little calcium '
             'through ([Schmid, et al, 2009](%s)), so it is another door, not another calcium door; what makes it '
             'matter here is what opens it, D-serine and GABA ([Wang, et al, 2025](%s)), which your second sentence '
             'says. Your version read [Human, High](%s); the corrected one reads [Human, High](%s) too.'
             % (HANSEN, SCHMID, WANG, HIS38, T38B),
             'Your label, "recently discovered in the GluD receptors", and your whole second sentence.',
             'Whether the first clause names NMDA as the calcium door rather than the spark, and drops "calcium" '
             'from GluD.',
             'Approve.',
             'his own: these are your words, and the clause changes what it says NMDA and GluD do',
             'use the corrected clause'),
    ]
    review = {
        'format': 'joel-suggestion-review-v1',
        'review_id': 'neuro-de-armoring-cards-20261108-x1108a',
        'title': 'Neuro De-Armoring Cards, 8 November: two science points in your new versions',
        'intro': [
            'Your versions of the Mechanism and the Signal Dial are in the article, and both read Human: '
            '[the Mechanism, High 137 and Medium 13](%s), [the Signal Dial, High](%s).' % (HIS37, HIS38),
            'Two of their claims don\'t match the sources, so each fix is on a card. Both fixed versions still read '
            'Human at High: [the Mechanism](%s), [the Signal Dial](%s).' % (T37B, T38B),
            'No compound, dose, unit, timing or warning changes on this page.',
        ],
        'git_file': GIT_FILE,
        'article': {'file': LANE + 'HUMANIZED-SO-FAR.md', 'sha256': SHA},
        'built': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'links': {'guide': BLOB + LANE + 'HUMANIZED-SO-FAR.md', 'review': BLOB + REL + 'REVIEW-X1108A.md'},
        'types': TYPES,
        'suggestions': S_,
    }
    probs = sr.check(review, BL)
    for x in probs:
        print('PROBLEM', x)
    (HERE / 'REVIEW-X1108A.json').write_text(json.dumps(review, indent=1, ensure_ascii=False) + '\n',
                                             encoding='utf-8')
    if probs or bad:
        return 1
    page = sr.page(review, MD, BL)
    (HERE / 'REVIEW-X1108A.html').write_text(page, encoding='utf-8')
    (HERE / 'REVIEW-X1108A.artifact.html').write_text(sr.artifact_view(page), encoding='utf-8')
    md = ['# %s' % review['title'], ''] + [p + '\n' for p in review['intro']]
    for s in S_:
        md += ['## %s: %s (%s)' % (s['id'], s['title'], TYPES[s['type']]['label']), '']
        for e in s['edits']:
            md += ['*%s*' % sr.where(BL, e['block']), '', '**Now:**', '', '> %s' % e['before'], '',
                   '**As it would read:**', '', '> %s' % e['after'], '']
        md += ['**What changes:** %s' % s['what'], '', '**Why:** %s' % s['why'], '',
               '**What stays:** %s' % s['stays'], '', '**You\'re deciding:** %s' % s['deciding'], '',
               '**My advice:** %s' % s['advice_note'], '']
    (HERE / 'REVIEW-X1108A.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
    print('ok', [x['id'] for x in S_])
    return 0


if __name__ == '__main__':
    sys.exit(main())
