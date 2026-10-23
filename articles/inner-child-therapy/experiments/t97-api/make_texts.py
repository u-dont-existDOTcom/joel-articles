#!/usr/bin/env python3
"""Turn 97: the texts for the first API checks (Joel's 86: A, 2026-10-22 23:54 UTC: "you can check paras or sections with
API, not more than like 5-6 paras at a time in general (not half an  article)").

Each text is a heading and its paragraphs, or one paragraph, the way Joel's Substack check reads them: the lane's plain
text (no notes, links as their words, no emphasis marks), quotes curled the way Substack curls them, and the emoji joiners
and presentation selectors gone (tools/humanization/substack_check_text.py, smart()), one line per block.
Writes TEXTS.json beside this file and prints each text's blocks and words.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from paragraphs_alone import reader_blocks  # noqa: E402
from ptext import plain  # noqa: E402  (paragraphs_alone puts its folder on the path)
from substack_check_text import smart  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
md = re.sub(r'<!--.*?-->', '', (ROOT / 'articles/inner-child-therapy/HUMANIZED-ARTICLE-SO-FAR.md').read_text(encoding='utf-8'), flags=re.S)
seq = reader_blocks(md)


def level(b):
    return len(b.split(' ')[0])


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


def section(title, stop_at_any_heading=False):
    i = next(i for i, (k, b) in enumerate(seq) if k == 'h' and re.sub(r'^#+\s*', '', b).startswith(title))
    lvl, out, k = level(seq[i][1]), [seq[i]], i + 1
    while k < len(seq) and not (seq[k][0] == 'h' and (stop_at_any_heading or level(seq[k][1]) <= lvl)):
        out.append(seq[k]); k += 1
    return out


def paragraph(title, n):
    blocks = [x for x in section(title) if x[0] == 'p']
    return [blocks[n - 1]]


TEXTS = {
    't97_parentP4': paragraph('The Parent You Inherited', 4),
    't97_body': section('Your Body Might Need Some Love First'),
    't97_parent': section('The Parent You Inherited'),
    't97_happy': section('How Much Happiness Do You Know Is Possible?', stop_at_any_heading=True),
    't97_shallow': section('When the Practice Feels Real but Stays Shallow'),
    't97_related': section('Related Clinical Work'),
}

out = {name: '\n'.join(line(k, b) for k, b in blocks) for name, blocks in TEXTS.items()}
(HERE / 'TEXTS.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for name, blocks in TEXTS.items():
    print('%-13s %d blocks (%d paragraphs), %d words | %s' % (name, len(blocks), sum(k == 'p' for k, _ in blocks),
                                                          len(out[name].split()), out[name][:70].replace('\n', ' / ')))
