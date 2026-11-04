#!/usr/bin/env python3
"""Turn 122: Joel's answers on the round-9 marking page (his export of 2026-11-04 13:44 UTC,
experiments/t122-answers/ANSWERS-20261104-1344.json, made on experiments/t121-review/GUIDE-PAGE.md, whose SHA-256 it names)
put into HUMANIZED-ARTICLE-SO-FAR.md, his words exactly as he typed them, with only the standard swap (straight quote marks,
spaced en dashes; E337 (gut)) and these, none of which changes a word:
  - a link whose words are still in his version goes back on them: the marking page's "Your version" box is plain text, so
    his versions carry no links (Hearthwork's, the Serenity Prayer's, the romance guide's);
  - his line breaks inside a paragraph (the Serenity Prayer, set as lines) become Markdown hard breaks, as the guide's others are;
  - spaces he left at the end of a paragraph go.
What each answer does:
  - HW-1, with HW-2 and HW-3 "delete": "i rewrote teh whole section, so remove and replace the whole hearthwork section. it
    tests human and sounds better". The section's heading and three paragraphs become his heading and four paragraphs; his
    first line, "Hearthwork: Taking Turns Lending & Borrowing Adulthood", is the heading.
  - M-B13: his two paragraphs replace the section's P3 and P4 ("also edited the prior para"), and P5 goes ("i want you to
    delete P5").
  - M-B9: his version ends the list item at its question.
  - M-B28: his version is two paragraphs.
  - the other twelve: his version replaces the paragraph.
  - M-A15, M-B11 and M-B15: kept as they are.
Writes the article, CHANGES.json (each card: the paragraph before, after, and what was placed back), and the OWNER-EDITS.json
entries. Run once; it refuses to run on an article it has already changed.

  python3 articles/inner-child-therapy/experiments/t122-apply/apply_t122.py"""
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
ART = ART_DIR / 'HUMANIZED-ARTICLE-SO-FAR.md'
LEDGER = ART_DIR / 'OWNER-EDITS.json'
ANS = HERE.parent / 't122-answers' / 'ANSWERS-20261104-1344.json'
PAGE = HERE.parent / 't121-review' / 'GUIDE-PAGE.md'
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from typography_swap import swap_text  # noqa: E402

A = json.loads(ANS.read_text(encoding='utf-8'))
assert A['review_id'] == 'inner-child-t121-round9-spots'
assert A['article']['sha256'] == hashlib.sha256(PAGE.read_bytes()).hexdigest(), 'his answers were made on another page copy'
ITEMS = {it['id']: it for it in A['items']}
WHEN = '2026-11-04 13:44 UTC (experiments/t122-answers/ANSWERS-20261104-1344.json)'
LINKS = {'HW-1': [('Hearthwork', 'https://hearthwork.u-dont-exist.com')],
         'M-A13': [('Serenity Prayer', 'https://www.archspm.org/the-serenity-prayer/')],
         'M-B28': [('romance guide', 'http://romance.u-dont-exist.com')]}
STRAIGHT = str.maketrans({'’': "'", '‘': "'", '“': '"', '”': '"'})

md = ART.read_text(encoding='utf-8')
if 'Hearthwork: Taking Turns Lending & Borrowing Adulthood' in md:
    sys.exit('already applied')
parts = re.split(r'(\n\s*\n)', md)   # blocks and the exact blank lines between them, so the rest stays byte for byte
blocks, seps = parts[0::2], parts[1::2] + ['']
assert ''.join(b + s for b, s in zip(blocks, seps)) == md


def vis(b):
    t = re.sub(r'<!--.*?-->', '', b, flags=re.S)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'^#+\s*', '', t.strip()).replace('**', '').replace('*', '')
    return re.sub(r'\s+', ' ', t.translate(STRAIGHT)).strip()


def block_of(card):
    before = re.sub(r'\s+', ' ', ITEMS[card]['before'].translate(STRAIGHT)).strip()
    hits = [i for i, b in enumerate(blocks) if vis(b) == before]
    assert len(hits) == 1, (card, hits)
    return hits[0]


def his(card):
    """His version as paragraphs: the standard swap, his in-paragraph line breaks as hard breaks, no trailing spaces."""
    text, _ = swap_text(ITEMS[card]['your_version'])
    paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    return [re.sub(r'[ \t]*\n[ \t]*', '  \n', p) for p in paras]


def relink(card, paras):
    placed = []
    for words, url in LINKS.get(card, []):
        hits = [(k, m.start()) for k, p in enumerate(paras) for m in re.finditer(re.escape(words), p)]
        assert hits, (card, words)
        k, s = hits[0]
        paras[k] = paras[k][:s] + '[%s](%s)' % (words, url) + paras[k][s + len(words):]
        placed.append({'words': words, 'url': url, 'paragraph': k + 1})
    return paras, placed


changes, new = {}, {}
# the Hearthwork section: its heading and three paragraphs, his heading and four paragraphs
i1 = block_of('HW-1')
assert blocks[i1 - 1] == '### Hearthwork: Taking Turns' and block_of('HW-2') == i1 + 1 and block_of('HW-3') == i1 + 2
assert blocks[i1 + 3].startswith('### Dating While You Heal')
hw = his('HW-1')
assert hw[0] == 'Hearthwork: Taking Turns Lending & Borrowing Adulthood' and len(hw) == 5, hw[:1]
body, placed = relink('HW-1', hw[1:])
new[i1 - 1] = ['### ' + hw[0]] + body
for j in (i1, i1 + 1, i1 + 2):
    new[j] = []
changes['HW-1'] = {'before': blocks[i1 - 1:i1 + 3], 'after': new[i1 - 1], 'links_back': placed,
                   'joel': ITEMS['HW-1']['comment']}
changes['HW-2'] = changes['HW-3'] = {'deleted': 'with HW-1 ("delete")'}
# When Being Happy Feels Like Abandoning Someone: P3 and P4 his, P5 out
i4 = block_of('M-B13')
p34 = his('M-B13')
assert len(p34) == 2 and blocks[i4 - 1].startswith('What I found, once I started cultivating my own happiness')
assert blocks[i4 + 1] == "I'd still try a small good thing, like a nice meal, and see what actually happens."
new[i4 - 1], new[i4], new[i4 + 1] = [p34[0]], [p34[1]], []
changes['M-B13'] = {'before': blocks[i4 - 1:i4 + 2], 'after': p34, 'joel': ITEMS['M-B13']['comment']}
# the list item that ends at its question
li = [i for i, b in enumerate(blocks) if "- Whose approval suddenly feels like I can't live without it? It isn't always who you'd guess." in b]
assert len(li) == 1
old_item = "- Whose approval suddenly feels like I can't live without it? It isn't always who you'd guess."
new[li[0]] = [blocks[li[0]].replace(old_item, '- ' + his('M-B9')[0])]
changes['M-B9'] = {'before': old_item, 'after': '- ' + his('M-B9')[0]}
# the paragraphs replaced one for one (M-B28's is two)
for card in ('M-A3', 'M-A7', 'M-A9', 'M-A11', 'M-A13', 'M-B2', 'M-B5', 'M-B7', 'M-B28', 'M-B30', 'M-B32', 'M-B34', 'M-B36'):
    i = block_of(card)
    assert i not in new, card
    paras, placed = relink(card, his(card))
    old_links = re.findall(r'\[([^\]]*)\]\(([^)]*)\)', blocks[i])
    assert len(old_links) == len(placed), (card, old_links, placed)
    new[i] = paras
    changes[card] = {'before': blocks[i], 'after': paras, 'links_back': placed, 'joel': ITEMS[card]['comment']}
for card in ('M-A15', 'M-B11', 'M-B15'):
    assert ITEMS[card]['status'] == 'rejected' and block_of(card) not in new
    changes[card] = {'kept': 'Keep it as it is'}
assert set(changes) == set(ITEMS), set(ITEMS) - set(changes)

out = []
for i, (b, sep) in enumerate(zip(blocks, seps)):
    rep = new.get(i, [b])
    for k, r in enumerate(rep):
        out.append(r + (sep if k == len(rep) - 1 else '\n\n'))
text = ''.join(out)
ART.write_text(text, encoding='utf-8')
(HERE / 'CHANGES.json').write_text(json.dumps(changes, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')


def first_sentence(p, n=140):
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', p).replace('  \n', ' ')
    return t[:n].rsplit(' ', 1)[0]


led = json.loads(LEDGER.read_text(encoding='utf-8'))
have = {e['id'] for e in led['entries']}
entries = []
for card, c in changes.items():
    if 'after' not in c:
        continue
    after = c['after'] if isinstance(c['after'], list) else [c['after']]
    musts = [first_sentence(p) for p in after if not p.startswith('### ')]
    e = {'id': 'joel-122-%s' % card.lower(), 'status': 'applied',
         'what': 'His version on the round-9 marking page, card %s (%s), word for word.' % (card, ITEMS[card]['title']),
         'joel': WHEN + ((': "%s"' % ITEMS[card]['comment']) if ITEMS[card]['comment'] else ''),
         'where': ITEMS[card]['where'], 'must_contain': musts}
    if card == 'HW-1':
        e['must_not_contain'] = ['The basic premise of Hearthwork, my peer-counseling framework, is: Equal time.',
                                 'Some of what the three grown-up jobs do can come from outside you, too.',
                                 "The peer doesn't become your permanent parent, though."]
        e['must_have_line'] = ['### Hearthwork: Taking Turns Lending & Borrowing Adulthood']
    if card == 'M-B13':
        e['must_not_contain'] = ["I'd still try a small good thing, like a nice meal, and see what actually happens."]
    if card == 'M-B9':
        e['must_not_contain'] = ["It isn't always who you'd guess."]
    for p in c.get('links_back', []):
        e.setdefault('must_link', []).append({'text': p['words'], 'url': p['url']})
    assert e['id'] not in have
    entries.append(e)
led['entries'] += entries
LEDGER.write_text(json.dumps(led, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied %d cards (%d kept), %d owner-edit entries; %d -> %d words' % (
    sum(1 for c in changes.values() if 'after' in c), sum(1 for c in changes.values() if 'kept' in c), len(entries),
    len(md.split()), len(text.split())))
