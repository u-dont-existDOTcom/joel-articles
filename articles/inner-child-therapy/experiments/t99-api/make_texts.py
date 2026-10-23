#!/usr/bin/env python3
"""Turn 99: texts for the API checks of this turn's drafts (experiments/t99-tries/drafts/), each draft alone and in a stretch
of its neighbors (at most five paragraphs, Joel's 86), built the way experiments/t97-api/make_texts.py builds them (the
lane's plain text, quotes curled as Substack curls them, the emoji joiners gone, one line per block). The drafts are not
in the article yet: a stretch swaps a draft in for the paragraph it replaces, or adds the two new PGQ-046 paragraphs after
his memoir paragraph in Untangling the Belonging Bargains. Writes TEXTS.json and texts/<name>.txt."""
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
D = HERE.parent / 't99-tries' / 'drafts'
draft = lambda n: ('p', (D / n).read_text(encoding='utf-8').strip())


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


def find(start):
    hits = [i for i, (k, b) in enumerate(seq) if b.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


i_loy = find('Some families run on a bargain like')
assert seq[i_loy + 1][1].startswith("That's exactly why I was crying for 14 years") and seq[i_loy + 2][1].startswith("I'd still try a small good thing")
i_g5 = find('Once a need does show, after all that hiding')
i_e1 = find('Your little one can get really loud in the gap after one life ends')
i_i7 = find('And the parts just keep coming: managers, firefighters')
assert seq[i_i7 - 2][0] == 'p' and seq[i_i7 - 1][0] == 'p' and seq[i_i7 + 1][0] == 'h'
TEXTS = {
    't99_bb_new1': [draft('f01-bargain-new1.txt')],
    't99_bb_new2': [draft('f02-bargain-new2.txt')],
    't99_bb_stretch': [seq[i_loy], seq[i_loy + 1], draft('f01-bargain-new1.txt'), draft('f02-bargain-new2.txt'), seq[i_loy + 2]],
    't99_guide5': [draft('f03-guide-P5.txt')],
    't99_guide_stretch': [seq[i_g5 - 1], draft('f03-guide-P5.txt'), seq[i_g5 + 1]],
    't99_ended1': [draft('f04-ended-P1.txt')],
    't99_ended_stretch': [seq[i_e1 - 1], draft('f04-ended-P1.txt'), seq[i_e1 + 1], seq[i_e1 + 2]],
    't99_ifs7': [draft('f05-ifs-P7.txt')],
    't99_ifs_stretch': [seq[i_i7 - 2], seq[i_i7 - 1], draft('f05-ifs-P7.txt')],  # P7 ends the section
}
out = {n: '\n'.join(line(k, b) for k, b in blocks) for n, blocks in TEXTS.items()}
(HERE / 'TEXTS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for n, t in out.items():
    (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    print('%-18s %4d words | %s' % (n, len(t.split()), t[:70].replace('\n', ' / ')))
