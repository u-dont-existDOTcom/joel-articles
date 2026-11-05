#!/usr/bin/env python3
"""apply_r06.py - round 6's answers (Joel, exported 2026-11-05 15:14 UTC; ANSWERS-R06-20261105-1514.json) put into the
guide: all three cards Revise.

Starts from the guide after round 5 (../../GUIDE-SO-FAR-blocks.json as main has it after pull request 280; PAGE-R06.md's
SHA-256 is the one his export names) and writes the guide after round 6 (GUIDE-AFTER-R06.md and
GUIDE-AFTER-R06-blocks.json beside this script), which becomes ../../GUIDE-SO-FAR.md.

- CBD-TRIAL: his version is four paragraphs, which go in as he wrote them: the warning-stage paragraph (round 6's first
  SEIZ-WARN paragraph with his humic/fulvic sentence added), two cannabis paragraphs (his, from his research and my last
  try), and the topical CBD paragraph, which replaces N-CBD-2. My 7-OH-CBD sentences are gone ("nobody asked why CBD is
  better or worse than 7-OH-CBD"): a meant cut, KEEP-AS-IS C9.
- SEIZ-WARN: no words of his; his comment places the warning-stage paragraph "after p2 before p3" ("we should move the
  non-cannabis para above all the cannabis info"): it goes after B110 (the rescue benzodiazepine) and before B111.
  The cannabis paragraphs follow B111, then the topical one, then the DMSO paragraph (N-CBD-3) and the call-for-help line.
- MOVE-YOURS: his paragraph replaces B236 and B237, his dangers paragraph with my first movement draft inside it, two
  words changed and the ideas in their natural order ("now it's all high conf human").

Changes that aren't to his words: the trailing spaces at the ends of his lines go; the single line break inside his
first cannabis paragraph becomes a space (Markdown renders it so; his paragraph breaks are the blank lines); his typo
"comapny" becomes "company"; his link "[testified in Congress] (https://...)", broken by the space before the
parenthesis, is joined; the 12-week trial keeps its link; and the two studies his forums paragraph describes get links
on the words that describe them, as round 5 did: "one woman whose EEG" (Sivakumar et al. 2017) and "rats that get the
brief staring seizures called absence seizures" (Roebuck et al. 2022). His bare video link stays as he pasted it
(checked 2026-11-05 from his laptop: "Beni utilizando o Spray Nasal (THC Abrace) produzido no Brasil", Leandro Ramires).

Each block's old Markdown must be what round 6's page showed, or the script stops.

  python3 apply_r06.py            write the guide after round 6 and print what changed
"""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BLOCKS = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
REVIEW = json.loads((HERE / 'REVIEW-R06.json').read_text(encoding='utf-8'))
ANSWERS = json.loads((HERE / 'ANSWERS-R06-20261105-1514.json').read_text(encoding='utf-8'))
OUT = HERE / 'GUIDE-AFTER-R06.md'
OUT_BLOCKS = HERE / 'GUIDE-AFTER-R06-blocks.json'

assert ANSWERS['review_id'] == REVIEW['review_id'] == 'bad-trips-r06', (ANSWERS['review_id'], REVIEW['review_id'])
assert hashlib.sha256((HERE / 'PAGE-R06.md').read_bytes()).hexdigest() == ANSWERS['article']['sha256']
ITEM = {x['id']: x for x in ANSWERS['items']}
assert set(ITEM) == {s['id'] for s in REVIEW['suggestions']} == {'CBD-TRIAL', 'SEIZ-WARN', 'MOVE-YOURS'}
assert all(x['status'] == 'revise' for x in ITEM.values())

EEG = 'https://pubmed.ncbi.nlm.nih.gov/27763968/'
RATS = 'https://pubmed.ncbi.nlm.nih.gov/33370468/'
GEL = 'https://pubmed.ncbi.nlm.nih.gov/35802375/'
CAMARA = 'https://escriba.camara.leg.br/escriba-servicosweb/html/58445'
VIDEO = 'https://www.youtube.com/watch?v=bgVi5o_2v_w'

UNIT = {b['id']: b for b in BLOCKS}
LOG = []


def link(md, words, url):
    assert md.count(words) == 1, (words, md)
    return md.replace(words, '[%s](%s)' % (words, url))


def block(bid, md):
    return {'id': bid, 'kind': 'p', 'md': md, 'text': None}


# ---------------------------------------------------------------- CBD-TRIAL (with SEIZ-WARN's placement)
old = UNIT['N-CBD-2']['md']
assert old.startswith("And topical CBD hasn't been well-studied.") and '7-OH-CBD' in old, old
his = ITEM['CBD-TRIAL']['your_version']
paras = [re.sub(r'[ \t]+\n', '\n', p).strip() for p in his.split('\n\n')]
assert len(paras) == 4, [p[:40] for p in paras]
warn, canna1, canna2, topical = paras
assert warn.startswith('Some people get a warning before a seizure takes hold') and 'humic/fulvic' in warn, warn
assert canna1.startswith('As for CBD/cannabis') and canna1.count('\n') == 1, canna1
canna1 = canna1.replace('\n', ' ')
assert canna1.count('comapny') == 1
canna1 = canna1.replace('comapny', 'company')
assert canna1.count('[testified in Congress] (%s)' % CAMARA) == 1
canna1 = canna1.replace('[testified in Congress] (%s)' % CAMARA, '[testified in Congress](%s)' % CAMARA)
assert VIDEO in canna1
assert canna2.startswith('I also read on forums')
canna2 = link(canna2, 'one woman whose EEG', EEG)
canna2 = link(canna2, 'rats that get the brief staring seizures called absence seizures', RATS)
assert topical.startswith('As for topical CBD') and '7-OH' not in topical
topical = link(topical, '12-week trial', GEL)
for p in (warn, canna1, canna2, topical):
    assert '\n' not in p, p

UNIT['N-CBD-2']['md'] = topical
LOG.append('N-CBD-2: CBD-TRIAL, his topical paragraph (the 7-OH-CBD sentences gone, his cut); the trial link kept')
at = BLOCKS.index(UNIT['B111'])
BLOCKS.insert(at + 1, block('N-CANNA-1', canna1))
BLOCKS.insert(at + 2, block('N-CANNA-2', canna2))
LOG.append('N-CANNA-1, N-CANNA-2 after B111: his two cannabis paragraphs ("comapny" fixed, his Congress link joined, '
           'the EEG and rat studies linked on the words that describe them)')
at = BLOCKS.index(UNIT['B110'])
BLOCKS.insert(at + 1, block('N-WARN', warn))
LOG.append('N-WARN after B110, before B111: the warning-stage paragraph with his humic/fulvic sentence (SEIZ-WARN: '
           '"after p2 before p3")')

# ---------------------------------------------------------------- MOVE-YOURS
assert UNIT['B236']['md'].startswith('Anything that could let someone hurt themselves'), UNIT['B236']['md']
assert UNIT['B237']['md'] == 'Movement is allowed. Unsafe movement is not. No driving, redosing, confrontations, or leaving alone.'
his = ITEM['MOVE-YOURS']['your_version'].strip()
assert his.startswith('Anything that could let someone hurt themselves') and 'have someone go with them' in his
assert '\n' not in his
UNIT['B236']['md'] = his
BLOCKS.remove(UNIT['B237'])
LOG.append('B236: MOVE-YOURS, his paragraph (his dangers paragraph with the movement lines inside it); B237 out, merged')

# ---------------------------------------------------------------- write
text = '\n\n'.join(b['md'] for b in BLOCKS) + '\n'
OUT.write_text(text, encoding='utf-8')
OUT_BLOCKS.write_text(json.dumps([{'id': b['id'], 'kind': b['kind'], 'md': b['md'], 'text': None} for b in BLOCKS],
                                 ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
before = (ART / 'GUIDE-SO-FAR.md').read_text(encoding='utf-8')
w0, w1 = len(re.findall(r'\S+', before)), len(re.findall(r'\S+', text))
print('\n'.join(LOG))
print('3 cards applied (his versions and placement); %d words -> %d (%+d); %s sha256 %s' % (
    w0, w1, w1 - w0, OUT.name, hashlib.sha256(text.encode()).hexdigest()))
