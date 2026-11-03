#!/usr/bin/env python3
"""Turn 115: the article's paragraphs with the turn notes written above each (the HTML comments right before it), so a
paragraph's history (whose words, which turn, which check) can be read beside a window.
  notes.py "first words"   prints the notes and the paragraph"""
import pathlib
import re
import sys

ART = pathlib.Path(__file__).resolve().parents[2] / 'HUMANIZED-ARTICLE-SO-FAR.md'


def blocks(md=None):
    md = md if md is not None else ART.read_text(encoding='utf-8')
    out, notes = [], []
    pos = 0
    for chunk in re.split(r'\n{2,}', md):
        c = chunk.strip()
        if not c:
            continue
        rest = re.sub(r'<!--.*?-->', '', c, flags=re.S).strip()
        found = re.findall(r'<!--(.*?)-->', c, flags=re.S)
        if not rest:
            notes += [f.strip() for f in found]
            continue
        out.append({'text': rest, 'notes': notes + [f.strip() for f in found]})
        notes = []
    return out


if __name__ == '__main__':
    want = sys.argv[1].replace('’', "'")
    for b in blocks():
        if want in b['text'].replace('’', "'"):
            for n in b['notes']:
                print('NOTE:', n[:1200])
                print()
            print('PARA:', b['text'])
