#!/usr/bin/env python3
"""Turn 97, second API round: the sections again with my tries in (experiments/t97-tries/), the same way make_texts.py
builds its texts. Joel's own paragraphs are sent two ways where my try changes them: as he wrote them (so his words stay
if they pass alone) and with my try (drafts e04 and e06, not installed); a section lineage has two tries, so How Much Happiness goes once more with my try in it, and his P4 goes alone. Writes TEXTS-2.json.
"""
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
DRAFTS = HERE.parent / 't97-tries' / 'drafts'


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


def swap(blocks, n, draft):
    """Paragraph N (1-based) of the blocks replaced by a draft's text."""
    out, seen = [], 0
    for k, b in blocks:
        if k == 'p':
            seen += 1
            if seen == n:
                b = (DRAFTS / draft).read_text(encoding='utf-8').strip()
        out.append((k, b))
    return out


happy = section('How Much Happiness Do You Know Is Possible?', stop_at_any_heading=True)
TEXTS = {
    't97b_parent': section('The Parent You Inherited'),
    't97b_happy_P4his': [x for x in happy if x[0] == 'p'][3:4],
    't97b_happy_try': swap(happy, 4, 'e04-happy-P4.txt'),
    't97b_shallow': section('When the Practice Feels Real but Stays Shallow'),
    't97b_related_try': swap(section('Related Clinical Work'), 1, 'e06-related-P1.txt'),
}
out = {name: '\n'.join(line(k, b) for k, b in blocks) for name, blocks in TEXTS.items()}
(HERE / 'TEXTS-2.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for name, t in out.items():
    (HERE / 'texts' / (name + '.txt')).write_text(t, encoding='utf-8')
    print('%-17s %d words | %s' % (name, len(t.split()), t[:70].replace('\n', ' / ')))
