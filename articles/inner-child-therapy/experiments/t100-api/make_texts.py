#!/usr/bin/env python3
"""Turn 100: texts for the API checks of this turn's drafts (experiments/t100-tries/drafts/), built the way
experiments/t99-api/make_texts.py builds them (the lane's plain text, quotes curled as Substack curls them, the emoji joiners
gone, one line per block). Each draft goes alone first; a stretch of at most five paragraphs around it (Joel's 86: "not more
than like 5-6 paras at a time") goes only after the draft reads Human alone (docs/PANGRAM-PRODUCTION-BUDGET-20261020.md).
The PGQ-046 stretch keeps turn 99's five blocks with g01 for f01; the others are wider than turn 99's three paragraphs, closer
to the halves where these paragraphs' neighbors read Human. Writes TEXTS.json and texts/<name>.txt."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)
D = HERE.parent / 't100-tries' / 'drafts'
D99 = HERE.parent / 't99-tries' / 'drafts'
draft = lambda n, d=D: ('p', (d / n).read_text(encoding='utf-8').strip())


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


def find(start):
    hits = [i for i, (k, b) in enumerate(seq) if b.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


i_loy = find('Some families run on a bargain like')
assert seq[i_loy + 2][1].startswith("I'd still try a small good thing")
i_g5 = find('Once a need does show, after all that hiding')
i_e1 = find('Your little one can get really loud in the gap after one life ends')
i_i7 = find('And the parts just keep coming: managers, firefighters')
assert seq[i_e1 - 1][0] == 'h' and seq[i_i7 + 1][0] == 'h' and all(seq[i_i7 - k][0] == 'p' for k in range(1, 5))
assert all(seq[i_g5 + k][0] == 'p' for k in (-2, -1, 1, 2))
TEXTS = {
    't100_bb_new1': [draft('g01-bargain-new1.txt')],
    't100_guide5': [draft('g02-guide-P5.txt')],
    't100_ended1': [draft('g03-ended-P1.txt')],
    't100_ifs7': [draft('g04-ifs-P7.txt')],
    # stretches, sent only for drafts that read Human alone
    't100_bb_stretch': [seq[i_loy], seq[i_loy + 1], draft('g01-bargain-new1.txt'), draft('f02-bargain-new2.txt', D99), seq[i_loy + 2]],
    't100_guide_stretch': [seq[i_g5 - 2], seq[i_g5 - 1], draft('g02-guide-P5.txt'), seq[i_g5 + 1], seq[i_g5 + 2]],
    't100_ended_section': [seq[i_e1 - 1], draft('g03-ended-P1.txt'), seq[i_e1 + 1], seq[i_e1 + 2]],
    't100_ifs_stretch': [seq[i_i7 - 4], seq[i_i7 - 3], seq[i_i7 - 2], seq[i_i7 - 1], draft('g04-ifs-P7.txt')],  # P7 ends the section
}
out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
(HERE / 'TEXTS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, t in out.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    print('%-20s %4d words | %s' % (n, len(t.split()), t[:70].replace('\n', ' / ')))
