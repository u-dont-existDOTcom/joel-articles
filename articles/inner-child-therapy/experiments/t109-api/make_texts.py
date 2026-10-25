#!/usr/bin/env python3
"""Turn 109's API texts, from the installed article (comments removed), copied from experiments/t106-api/make_texts.py.

  python3 make_texts.py BATCH NAME=SPEC [NAME=SPEC ...]

A SPEC is h2:HEADING (the h2 with its paragraphs, heading line first), p:START (one paragraph alone, by its first words), stretch:START (five paragraphs with START in the middle, within its section),
or file:PATH (a draft, read as one paragraph); h2with:HEADING|START|PATH and stretchwith:START|PATH are the same with the
paragraph that starts START swapped for the draft at PATH. Writes TEXTS-BATCH.json, texts/NAME.txt, and adds the names to NAMES.json
(the description is given as NAME=SPEC=DESCRIPTION)."""
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


def line(kind, b):
    t = plain(re.sub(r'^#+\s*', '', b) if kind == 'h' else b)
    return smart(t).replace('‍', '').replace('️', '')


def para(start):
    hits = [i for i, (k, b) in enumerate(seq) if k == 'p' and b.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return line(*seq[hits[0]])


def h2(heading):
    hits = [i for i, (k, b) in enumerate(seq) if k == 'h' and re.sub(r'^#+\s*', '', b) == heading]
    assert len(hits) == 1, (heading, hits)
    i = hits[0]
    out = [line(*seq[i])]
    for k, b in seq[i + 1:]:
        if k == 'h':
            break
        if k == 'p':
            out.append(line(k, b))
    return '\n'.join(out)


def stretch(start):
    hits = [i for i, (k, b) in enumerate(seq) if k == 'p' and b.startswith(start)]
    assert len(hits) == 1, (start, hits)
    i = hits[0]
    lo = i
    while lo > 0 and seq[lo - 1][0] == 'p' and i - lo < 2:
        lo -= 1
    hi = i
    while hi + 1 < len(seq) and seq[hi + 1][0] == 'p' and hi - i < 2:
        hi += 1
    return '\n'.join(line(*seq[k]) for k in range(lo, hi + 1))


def draft(path):
    return smart(plain((HERE.parents[0] / path).read_text(encoding='utf-8').strip()))


def swapped(text, start, path):
    """The text with the paragraph that starts START (one line of it) swapped for the draft at PATH."""
    old = para(start)
    assert text.count(old) == 1, start
    return text.replace(old, draft(path))


def main(argv):
    batch, specs = argv[0], argv[1:]
    texts, names = {}, {}
    for s in specs:
        name, spec, desc = s.split('=', 2)
        kind, arg = spec.split(':', 1)
        if kind == 'h2':
            t = h2(arg)
        elif kind == 'p':
            t = para(arg)
        elif kind == 'stretch':
            t = stretch(arg)
        elif kind == 'h2with':
            heading, start, path = arg.split('|')
            t = swapped(h2(heading), start, path)
        elif kind == 'stretchwith':
            start, path = arg.split('|')
            t = swapped(stretch(start), start, path)
        else:
            t = draft(arg)
        texts[name], names[name] = t, desc
    (HERE / ('TEXTS-%s.json' % batch)).write_text(json.dumps(texts, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    (HERE / 'texts').mkdir(exist_ok=True)
    for n, t in texts.items():
        (HERE / 'texts' / (n + '.txt')).write_text(t, encoding='utf-8')
    allnames = json.loads((HERE / 'NAMES.json').read_text(encoding='utf-8')) if (HERE / 'NAMES.json').exists() else {}
    allnames.update(names)
    (HERE / 'NAMES.json').write_text(json.dumps(allnames, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
    for n, t in texts.items():
        print('%-28s %4d words | %s' % (n, len(t.split()), t[:80].replace('\n', ' / ')))


if __name__ == '__main__':
    main(sys.argv[1:])
