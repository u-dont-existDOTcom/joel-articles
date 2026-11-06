#!/usr/bin/env python3
"""REVIEW.json for batch 13, marked on r17 (the article with every answer in): the two clarity fixes the pre-publication
compare read found in the glutamine dose paragraph (../../r17/prepublish/FINDINGS.md, F1.2 and F1.4), tested in their
stretch (r19-D, #185). Not a window fix: draft B read the paragraph Human, High; a fresh reader couldn't tell what two of
its "it"s meant. Gate E363 (gut): the page goes out the turn its cards are written; E364: a new review id. Phase 5's
card waits for his extension on drafts C and D (../README.md)."""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R21 = HERE.parent
FIX = R21.parent
REPO = HERE.parents[5]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import sense_receipt as S  # noqa: E402
import suggestion_review as sr  # noqa: E402

MD = FIX / 'r17' / 'r17.md'
b17 = sr.blocks(MD.read_text(encoding='utf-8'))
b21 = sr.blocks((R21 / 'r21.md').read_text(encoding='utf-8'))
assert len(b17) == len(b21)
GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/healing-the-gut/humanize/fix-20261103/'
PG = 'https://www.pangram.com/history/'
REL = 'articles/healing-the-gut/humanize/fix-20261103/r21/b13/'
DOSE = 28
assert b17[DOSE]['text'].startswith('Take 5g a day as a baseline')


def block_receipt(name, stretch_receipt, i, why_reading):
    st = json.loads(stretch_receipt.read_text(encoding='utf-8'))
    text = b21[i]['text'].strip()
    by = {x['s']: x for x in st['sentences']}
    sents = S.sentences(text)
    r = dict(st, text=text, text_sha256=S.sha256(text), sentences=[by[s] for s in sents],
             opens={'first_sentence': sents[0], 'why_reading': why_reading})
    probs = S.check(text, r)
    assert not probs, (name, probs)
    (HERE / name).write_text(json.dumps(r, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    return REL + name


before, after = b17[DOSE]['text'], b21[DOSE]['text']
spans = []
for phrase in ('once it\'s over', 'don\'t count on it'):
    k = before.find(phrase)
    assert k >= 0 and before.count(phrase) == 1, phrase
    spans.append({'block': DOSE, 'start': k, 'end': k + len(phrase)})
S_ = [{
    'id': 'F13-1', 'type': 'mine', 'title': 'Two "it"s in the glutamine dose paragraph say what they mean',
    'advice': 'approve', 'spans': spans, 'edits': [{'block': DOSE, 'before': before, 'after': after}],
    'reads': [{'text': after, 'kind': 'p'}], 'reads_label': 'As it would read',
    'what': 'Each "it" named',
    'why': 'A fresh reader, reading the article beside your published version, couldn\'t tell what two "it"s meant. '
           '"So come back down once it\'s over": the exposure, the stress, or the training the paragraph mentioned '
           'earlier? It\'s the exposure or the stress, so it now says that. "Like Crohn\'s or colitis, don\'t count on '
           'it": the higher dose, or glutamine at all? The trials it cites gave glutamine itself and it didn\'t help, so '
           'it now says "don\'t count on glutamine".',
    'stays': 'Every dose, the training note, the safety limit and the Crohn\'s trials, word for word.',
    'whose': 'My fix of a sentence a reader couldn\'t follow.',
    'deciding': 'Whether it says what you meant.', 'advice_note': 'Approve, Reject, or Revise.',
    'reading': 'Pangram already read this paragraph Human, High in the whole article ([draft B](https://www.pangram.com/'
               'feed/bb64a934-cf2c-47b3-ae93-af2a363a0644), one 1,110-word window); this is a clarity fix.',
    'tested': 'The glutamine paragraph and its dose paragraph with both fixes: [Human Written](%sb6fbb475-af67-4e35-aed4-'
              'b45ded49271c), High (#185).' % PG,
    'receipt': [block_receipt('RECEIPT-F13-1.json', FIX / 'r19' / 'checks' / 'RECEIPT-r19-D.json', DOSE,
                              'The reader knows how much glutamine to take as a baseline before anything else.')],
    'found_by': 'the pre-publication compare read (a fresh reader, sentence by sentence beside your published text)',
}]
review = {
    'format': 'joel-suggestion-review-v1', 'review_id': 'healing-the-gut-b13-r21-20261106',
    'title': 'Gut Article, Two Clarity Fixes (Batch 13)',
    'intro': ['The read before publishing found two places in the glutamine dose paragraph where a reader couldn\'t tell '
              'what "it" meant. Both are fixed on the card below, and the paragraph still reads Human, High.',
              'Phase 5\'s first two steps, the last sentences that read Low, get their card once your extension has read '
              'drafts C and D.'],
    'git_file': REL + 'REVIEW-PAGE.html',
    'article': {'file': 'articles/healing-the-gut/humanize/fix-20261103/r17/r17.md',
                'sha256': hashlib.sha256(MD.read_bytes()).hexdigest()},
    'built': '2026-11-06',
    'links': {'guide': GH + 'r21/r21.md', 'review': GH + 'r21/b13/REVIEW-CARDS.md'},
    'types': {'mine': {'label': 'My fix', 'about': 'A sentence a reader couldn\'t follow, fixed'}},
    'suggestions': S_,
}
(HERE / 'REVIEW.json').write_text(json.dumps(review, ensure_ascii=False, indent=1), encoding='utf-8')
out = ['# ' + review['title'], ''] + [p + '\n' for p in review['intro']]
for s in S_:
    out += ['## %s. %s' % (s['id'], s['title']), '', '*%s*' % s['whose'], '']
    for r in s['reads']:
        out += ['**%s:**' % s['reads_label'], '', '> ' + r['text'], '']
    out += ['**Why:** ' + s['why'], '', '**Pangram read:** ' + s['reading'], '',
            '**Pangram on the suggestion:** ' + s['tested'], '', '**What stays:** ' + s['stays'], '']
(HERE / 'REVIEW-CARDS.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(S_), 'cards')
