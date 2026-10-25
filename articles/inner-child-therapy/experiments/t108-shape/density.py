#!/usr/bin/env python3
"""Turn 108: how many turns each section's paragraphs take, beside Lucia Capacchione's Recovery of Your Inner Child. A turn
is one of: but, though, although, unless, if, or, maybe, perhaps, instead, still, yet, however, otherwise, except, even,
while, whether, depending, sometimes. Paragraphs of 20 words or more (30 for the book-wide comparison, as in
experiments/t105-readers-edit/ENGAGING.md). Her book's text isn't in the repository (it's copyrighted); its numbers are
from the EPUB's text, given as BOOK below. The article's word count is its round 6 text (experiments/t107-substack/).
Writes DENSITY.md."""
import pathlib
import re
import statistics

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[3]
TURN = re.compile(r"\b(but|though|although|unless|if|or|maybe|perhaps|instead|still|yet|however|otherwise|except|even|while|whether|depending|sometimes)\b", re.I)
BOOK = {'paragraphs': 608, 'words': 38065, 'mean': 0.9, 'median': 1, 'per100': 1.5, 'four_plus': 4, 'total_words': 50897}
md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
secs, cur = [], None
for block in re.split(r'\n\s*\n', md):
    b = block.strip()
    if not b:
        continue
    if re.match(r'^#{1,5} ', b):
        cur = [b.split('\n')[0], []]
        secs.append(cur)
        continue
    if cur and not b.startswith('>') and len(b.split()) >= 20:
        cur[1].append(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', b))
allp = [p for _, ps in secs for p in ps if len(p.split()) >= 30]
turns = [len(TURN.findall(p)) for p in allp]
rows = []
for h, ps in secs:
    if len(ps) < 2:
        continue
    w = sum(len(p.split()) for p in ps)
    t = sum(len(TURN.findall(p)) for p in ps)
    rows.append((t / len(ps), len(ps), w, re.sub(r'^#+\s*', '', h)))
rows.sort(reverse=True)
out = ['# Turns per paragraph, section by section (turn 108)', '',
       'A turn is a word that bends the sentence: but, though, although, unless, if, or, maybe, perhaps, instead, still, yet, '
       'however, otherwise, except, even, while, whether, depending or sometimes. Counted by [density.py](https://github.com/u-dont-existDOTcom/joel-articles/blob/handoff/claude-dangerous-adult-20260924-1631/articles/inner-child-therapy/experiments/t108-shape/density.py).', '',
       '| | this article | Recovery of Your Inner Child |', '|---|---|---|',
       '| paragraphs of 30 words or more | %d | %d |' % (len(allp), BOOK['paragraphs']),
       '| turns per paragraph, on average | %.1f | %.1f |' % (statistics.mean(turns), BOOK['mean']),
       '| paragraphs with four turns or more | %d%% | %d%% |' % (round(100 * sum(1 for x in turns if x >= 4) / len(turns)), BOOK['four_plus']),
       '| words in all | about %s | about %s |' % ('{:,}'.format(round(sum(len((HERE.parent / 't107-substack' / f).read_text(encoding='utf-8').split()) for f in ('TEXT-A.txt', 'TEXT-B.txt')), -2)), '{:,}'.format(round(BOOK['total_words'], -3))),
       '', '## Sections with two paragraphs or more, densest first', '', '| turns per paragraph | paragraphs | words | section |', '|---|---|---|---|']
out += ['| %.1f | %d | %d | %s |' % r for r in rows]
(HERE / 'DENSITY.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\n'.join(out[:12]))
