#!/usr/bin/env python3
"""Reader-visible text of each candidate unit, as Pangram should see it: the heading line, then each paragraph or list
item on its own line, link markup and bold/italic marks removed, list markers dropped (Substack draws them).
Usage: python3 make_texts.py writer_A.json A  -> TEXTS-A.json {"b1-P1-A": text, ...}. No API calls."""
import json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent


def visible(md):
    out = []
    for block in md.split('\n\n'):
        for line in block.split('\n'):
            t = line.strip()
            if not t:
                continue
            t = re.sub(r'^#+\s*', '', t)
            t = re.sub(r'^(?:[-*]|\d+\.)\s+', '', t)
            t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
            t = re.sub(r'(\*\*|__)(.+?)\1', r'\2', t)
            t = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'\1', t)
            out.append(t)
    return '\n'.join(out)


w = json.loads((HERE / sys.argv[1]).read_text(encoding='utf-8'))
tag = sys.argv[2]
texts = {'b1-%s-%s' % (k, tag): visible(v['text']) for k, v in w.items()}
(HERE / ('TEXTS-%s.json' % tag)).write_text(json.dumps(texts, ensure_ascii=False, indent=1), encoding='utf-8')
(HERE / 'texts').mkdir(exist_ok=True)
for k, t in texts.items():
    (HERE / 'texts' / (k + '.txt')).write_text(t, encoding='utf-8')
print(tag, {k: len(t.split()) for k, t in texts.items()})
