#!/usr/bin/env python3
"""make_now.py - the bad trips guide's contents as it stands (NOW.json: each heading's block id, level, heading as the
sidebar shows its words, and its section's own word count), and the article for the headings writer (ARTICLE.md: each
section with its id, level, heading and text). Turn 56 (h64), his message of 2026-11-21 01:06 UTC: "make sure the
headings are fitting in the ToC based on the inner child lane's work on that article".

  python3 make_now.py
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[2]
B = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))


def plain(t):
    t = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = t.replace('**', '').replace('__', '')
    t = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', t)
    return t.strip()


now, art, cur = [], [], None
for b in B:
    if b['kind'] in ('h1', 'h2', 'h3', 'h4'):
        level = int(b['kind'][1])
        head = plain(re.sub(r'^#+\s+', '', b['md']))
        cur = {'id': b['id'], 'level': level, 'heading': head, 'words': 0, 'text': []}
        now.append(cur)
    elif cur is not None and b['kind'] not in ('hr', 'image', 'youtube'):
        t = plain(b['md'])
        cur['text'].append(t)
        cur['words'] += len(t.split())
(HERE / 'NOW.json').write_text(json.dumps([{k: e[k] for k in ('id', 'level', 'heading', 'words')} for e in now],
                                          ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
out = ['# The bad trips guide, section by section', '',
       'Each section: its id, its level (1 to 4, as h1 to h4), its heading as it stands, and its text.', '']
for e in now:
    out += ['## [%s] level %d: %s' % (e['id'], e['level'], e['heading']), ''] + ['\n\n'.join(e['text']) or '(no text of its own)', '']
(HERE / 'ARTICLE.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print(len(now), 'headings;', sum(e['words'] for e in now), 'words under them')
