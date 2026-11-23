#!/usr/bin/env python3
"""The sixth marking page (2026-11-23): the whole fixed article (whole/FIXED.md) with my tested fixes of the vetted junk
read (r30/junk/VETTED.md, the eleven passages two readers confirmed don't make sense or follow) where a fix cuts or
changes something, so it is his to decide. The fixes that keep the meaning went in without a card (r35/MINE-R35.json);
three whose fixes read AI by themselves wait for more tries (r35/README.md).

  python3 build_t6.py   ->  REVIEW-T6.json, REVIEW-T6.html, REVIEW-T6.artifact.html, REVIEW-T6.md
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
import suggestion_review as R  # noqa: E402

ART = 'articles/romance/humanize/fix-20261107/whole/FIXED.md'
md = (ROOT / ART).read_text(encoding='utf-8')
sha = hashlib.sha256(md.encode('utf-8')).hexdigest()
bl = R.blocks(md, whole=True)
CARDS = json.loads((ROOT / 'articles/romance/humanize/fix-20261107/r35/CARDS.json').read_text(encoding='utf-8'))


def find_block(text):
    hits = [b['i'] for b in bl if b['kind'] not in ('embed', 'cut') and b['text'] == text]
    assert len(hits) == 1, (text[:60], hits)
    return hits[0]


def span(i, words):
    t = bl[i]['text']
    s = t.find(words)
    assert s >= 0, (i, words)
    return {'block': i, 'start': s, 'end': s + len(words)}


review = {
    'format': R.FORMAT, 'review_id': 'romance-t6', 'built': '2026-11-23',
    'title': 'Romance Advice I Wish My Parents Taught Me: the passages that didn’t make sense',
    'intro': ['The whole article as it reads now. Two readers went through it for passages that don’t make sense or '
              'follow, and eleven held up as real. Each card below is my fix of one of them, tested in Pangram by '
              'itself; these seven cut or change something, so each needs your decision. One more fix kept the meaning '
              'and is already in (in "What I gained from loss"). Three whose fixes read AI so far are here as questions: '
              'I keep trying them, and a line from you on what they mean helps. '
              'Every paragraph, picture and video is here in order: nothing is left out.'],
    'git_file': 'articles/romance/review/teach-20261123/REVIEW-T6.html',
    'article': {'file': ART, 'sha256': sha}, 'whole': {'file': ART, 'sha256': sha},
    'links': {'guide': 'https://ibogaqueen.substack.com/p/romance-advice-i-wish-my-parents', 'guide_label': 'your live post',
              'review': 'https://github.com/u-dont-existDOTcom/joel-articles/blob/claude/romance-20261108/articles/romance/review/teach-20261123/REVIEW-T6.md'},
    'types': {'sense': {'label': 'Doesn’t make sense or follow', 'about': 'two readers found it hard to follow; my fix, tested'}},
    'suggestions': [],
}
for c in CARDS:
    blocks = [find_block(t) for t in c['old']]
    edits = [{'block': i, 'before': R.block_text(bl, i), 'after': a} for i, a in zip(blocks, c['new'])]
    s = {'id': c['id'], 'type': 'sense', 'title': c['title'], 'advice': 'approve',
         'spans': [span(i, w) for i, w in zip(blocks, c['highlight'])],
         'edits': edits, 'what': c['what'], 'why': c['why'], 'stays': c['stays'], 'advice_note': c['advice_note'], 'deciding': c['deciding'],
         'found_by': 'the junk read of 2026-11-22 (four fresh readers) and its vetting by a fifth (r30/junk/VETTED.md, %s)' % c['vetted'],
         'reading': c['reading'], 'tested': c['tested'], 'ask_because': c['ask_because']}
    if c.get('approve_label'):
        s['approve_label'] = c['approve_label']
    if c.get('receipt'):
        s['receipt'] = c['receipt']
    review['suggestions'].append(s)
ASKS = json.loads((ROOT / 'articles/romance/humanize/fix-20261107/r35/ASKS.json').read_text(encoding='utf-8'))
review['types']['ask'] = {'label': 'Doesn’t follow yet', 'about': 'my fix reads AI so far; I keep trying, and a line from you helps'}
for a in ASKS:
    i = find_block(a['block'])
    review['suggestions'].append({'id': a['id'], 'type': 'ask', 'title': a['title'], 'advice': 'ask', 'question': a['question'],
                                  'why': a['why'], 'advice_note': a['advice_note'], 'spans': [span(i, a['highlight'])]})
probs = R.check(review, bl)
if probs:
    sys.exit('\n'.join(probs))
(HERE / 'REVIEW-T6.json').write_text(json.dumps(review, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
html = R.page(review, md, bl)
(HERE / 'REVIEW-T6.html').write_text(html, encoding='utf-8')
(HERE / 'REVIEW-T6.artifact.html').write_text(R.artifact_view(html), encoding='utf-8')
out = ['# The passages that didn’t make sense: the cards (2026-11-23)', '',
       'The page shows the whole article ([FIXED.md](../../humanize/fix-20261107/whole/FIXED.md)); these are its cards.', '']
for a in ASKS:
    out += ['## %s. %s' % (a['id'], a['title']), '', '> ' + a['block'], '', a['question'], '']
for c in CARDS:
    out += ['## %s. %s' % (c['id'], c['title']), '']
    out += ['**Now:**', ''] + ['> ' + t for t in c['old']] + ['']
    out += ['**Would read:**', ''] + (['> ' + t for t in c['new'] if t] or ['> (cut)']) + ['']
    out += [c['why'], '', 'Pangram: ' + c['tested'], '', '**' + c['advice_note'] + '**', '']
(HERE / 'REVIEW-T6.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('REVIEW-T6: %d blocks, %d cards, %d bytes' % (len(bl), len(review['suggestions']), len(html)))
