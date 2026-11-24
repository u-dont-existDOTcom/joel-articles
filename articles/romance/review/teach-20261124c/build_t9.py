#!/usr/bin/env python3
"""The ninth marking page (2026-11-24, after his message of 16:23 UTC): the whole fixed article (whole/FIXED.md) with the junk pass's fixes that might
change the meaning (r38/junk/CARDS-T8.json), each tested in its section, and two passages whose meaning is his to say.
The fixes that keep the meaning went in without a card (r38/junk/MINE-R38J.json).

  python3 build_t8.py   ->  REVIEW-T8.json, REVIEW-T8.html, REVIEW-T8.artifact.html, REVIEW-T8.md
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as R  # noqa: E402

FIX = 'articles/romance/humanize/fix-20261107'
ART = FIX + '/whole/FIXED.md'
md = (ROOT / ART).read_text(encoding='utf-8')
sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
bl = R.blocks(md, whole=True)
H = 'https://www.pangram.com/history/'


def find_block(text):
    hits = [b['i'] for b in bl if b['kind'] not in ('embed', 'cut') and R.block_text(bl, b['i']) == text]
    if len(hits) != 1:
        import re
        plain = lambda t: re.sub(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))+\)', r'\1', t)
        hits = [b['i'] for b in bl if b['kind'] not in ('embed', 'cut') and plain(b['text']) == text]
    assert len(hits) == 1, (text[:60], hits)
    return hits[0]


def find_words(words):
    hits = [(b['i'], b['text'].find(words)) for b in bl if b['kind'] not in ('embed', 'cut') and words in b['text']]
    assert len(hits) == 1, (words[:60], hits)
    i, s = hits[0]
    return {'block': i, 'start': s, 'end': s + len(words)}


CARDS = {}
CHANGES = {}
RECEIPTS = {}
ASKS = [
    {'id': 'Q-C1', 'title': 'Promising help: a red flag, or an honest vow?',
     'words': 'I don’t need to promise that on paper, and if I did, that would be more like a red flag.',
     'question': 'A fresh reader of the whole article found two places that pull against each other. In “Labels Are '
                 'Descriptive, Not Prescriptive”: “I don’t need to promise that on paper, and if I did, that would be more '
                 'like a red flag.” In “Which marriage vows are honest?”: “you can promise actions if you really believe '
                 'you’re capable of delivering them”, like “to keep showing up emotionally”. So is promising to be there a '
                 'red flag, or an honest vow? My reading: the red flag is a promise standing in for the closeness that should '
                 'make it unnecessary, while an honest vow promises actions on top of that closeness. If that’s it, a few '
                 'words in the Labels paragraph could say so, and I’ll test them in its section.',
     'why': 'The contradictions check (a fresh reader of the whole article), item 1: the article doesn’t say how the two fit.',
     'advice_note': 'A line on how they fit is enough.'},
    {'id': 'Q-C7', 'title': 'Who sets the direction?',
     'words': 'Where I like the polarity is when she sees the Big Picture, and I help fill in the details to make our plan workable.',
     'question': 'In “Muses & Directors” you’re the steering wheel (“I help give it direction and make it operational”), and '
                 'women want you to say “This is where I want to go”. But in between: “she sees the Big Picture, and I help '
                 'fill in the details to make our plan workable.” The reader couldn’t tell who sets the direction. My guess: '
                 'she sees where life could go, and you choose the route and propose the plan. If that’s it, a few words '
                 'could say so, and I’ll test them in the section.',
     'why': 'The contradictions check, item 7: the article doesn’t say how the two fit.',
     'advice_note': 'A line on who does what is enough.'},
    {'id': 'Q-S5', 'title': '“In modern years”?', 'words': 'gone to real extremes in modern years',
     'question': 'In your new opening of “Primal attraction”, a fresh reader stumbled on “the gender wars have gone to real '
                 'extremes in modern years”: the usual phrase is “in recent years”. Keep yours, or change it? (Your new '
                 'opening read Human High in both of its checks as you wrote it.)',
     'why': 'The word-for-sense read of your new opening (all three planted errors found), block 5.',
     'advice_note': 'Keep it or change it: either is fine with me.'},
    {'id': 'Q-S12', 'title': '“Worth doing” or “worth living”?', 'words': 'this feeling that life is worth doing',
     'question': 'The same reader read “She brings inspiration, beauty, intuition, creativity, and this feeling that life is '
                 'worth doing” (“Muses & Directors”) as a slip for “worth living”. Did you mean “worth doing”?',
     'why': 'The word-for-sense read of your new opening and the paragraphs around it, block 12.',
     'advice_note': 'If you meant it, it stays.'},
]
review = {
    'format': R.FORMAT, 'review_id': 'romance-t9', 'built': '2026-11-24',
    'title': 'Romance Advice I Wish My Parents Taught Me: four questions',
    'intro': ['The whole article as it reads now, with your new opening of “Primal attraction”, J-B54 and Senegal in. A '
              'fresh reader read the whole article for statements that pull against each other: of seven, three the article '
              'already explains, two weren’t real (a pointer with the wrong section name, now fixed, and the FM Laeti song, '
              'which is one of the videos), and two need your answer on what you meant. The other two questions are '
              'words a reader stumbled on. Every paragraph, picture and video is here in order: nothing is left out.'],
    'git_file': 'articles/romance/review/teach-20261124c/REVIEW-T9.html',
    'article': {'file': ART, 'sha256': sha}, 'whole': {'file': ART, 'sha256': sha},
    'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents', 'guide_label': 'your live post',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261108/articles/romance/review/teach-20261124c/REVIEW-T9.md'},
    'types': {'meaning': {'label': 'What do you mean?', 'about': 'a reader couldn’t tell; a line from you is enough'}},
    'suggestions': [],
}
order = []
for cid, spec in CARDS.items():
    chs = CHANGES[cid]
    blocks = [find_block(ch['before']) for ch in chs]
    order.append((min(blocks), cid, spec, chs, blocks))
for _, cid, spec, chs, blocks in sorted(order):
    edits = [{'block': i, 'before': R.block_text(bl, i), 'after': ch['after'][0]} for i, ch in zip(blocks, chs)]
    spans = []
    for w in spec['highlight']:
        hit = [i for i in blocks if w in bl[i]['text']]
        assert len(hit) == 1, (cid, w)
        t = bl[hit[0]]['text']
        s = t.find(w)
        spans.append({'block': hit[0], 'start': s, 'end': s + len(w)})
    review['suggestions'].append({
        'id': cid, 'type': 'sense', 'title': spec['title'], 'advice': 'approve', 'spans': spans, 'edits': edits,
        'what': spec['what'], 'why': spec['why'], 'stays': spec['stays'], 'deciding': spec['deciding'],
        'advice_note': spec['advice_note'], 'found_by': FOUND % spec['items'], 'reading': spec['reading'],
        'tested': spec['tested'], 'ask_because': spec['ask_because'], 'receipt': RECEIPTS[cid]})
for a in ASKS:
    review['suggestions'].append({'id': a['id'], 'type': 'meaning', 'title': a['title'], 'advice': 'ask',
                                  'question': a['question'], 'why': a['why'], 'stays': 'The sentence as it is, until your answer.',
                                  'advice_note': a['advice_note'], 'spans': [find_words(a['words'])]})
probs = R.check(review, bl)
if probs:
    sys.exit('\n'.join(probs))
(HERE / 'REVIEW-T9.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
html = R.page(review, md, bl)
(HERE / 'REVIEW-T9.html').write_text(html, encoding='utf-8')
(HERE / 'REVIEW-T9.artifact.html').write_text(R.artifact_view(html), encoding='utf-8')
out = ['# Four questions: the cards (2026-11-24)', '',
       'The page shows the whole article ([FIXED.md](../../humanize/fix-20261107/whole/FIXED.md)); these are its cards.', '']
for s in review['suggestions']:
    out += ['## %s. %s' % (s['id'], s['title']), '']
    if s['advice'] == 'ask':
        out += [s['question'], '', s['why'], '', '**' + s['advice_note'] + '**', '']
        continue
    out += ['**Now:**', ''] + ['> ' + e['before'] for e in s['edits']] + ['']
    out += ['**Would read:**', ''] + ['> ' + (e['after'] or '(cut)') for e in s['edits']] + ['']
    out += [s['why'], '', 'Pangram: ' + s['reading'] + ' ' + s['tested'], '', '**' + s['advice_note'] + '**', '']
(HERE / 'REVIEW-T9.md').write_text('\n'.join(out).rstrip('\n') + '\n', encoding='utf-8')
print('REVIEW-T9: %d blocks, %d cards, %d bytes' % (len(bl), len(review['suggestions']), len(html)))
