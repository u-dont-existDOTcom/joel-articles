#!/usr/bin/env python3
"""Turn 104's API texts, from the installed article (comments removed), the way turn 103's were made.

  python3 make_texts.py BATCH NAME=SPEC [NAME=SPEC ...]

A SPEC is h2:HEADING (the h2 with its paragraphs, heading line first), p:START (one paragraph alone, by its first words),
or file:PATH (a draft, read as one paragraph). Writes TEXTS-BATCH.json, texts/NAME.txt, and adds the names to NAMES.json
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
        else:
            t = smart(plain((HERE.parents[0] / arg).read_text(encoding='utf-8').strip()))
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
