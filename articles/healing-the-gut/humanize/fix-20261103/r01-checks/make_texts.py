#!/usr/bin/env python3
"""The causes list in r01 (his own writing, with the G2 phase pointers added), as four API-sized texts of at most six
paragraphs, the way Pangram should see them. Writes TEXTS.json and texts/. No API calls."""
import json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
md = (HERE.parent / 'r01' / 'r01.md').read_text(encoding='utf-8')
src = (HERE.parent / 'b1-protocol' / 'make_texts.py').read_text(encoding='utf-8')
ns = {'__file__': str(HERE.parent / 'b1-protocol' / 'make_texts.py')}
exec(src.split('w = json.loads')[0], ns)
vis = ns['visible']
lines = md.split('\n')


def from_to(start, stop, keep=None):
    i = next(n for n, l in enumerate(lines) if l.lstrip().startswith(start))
    j = next(n for n, l in enumerate(lines) if n > i and l.lstrip().startswith(stop))
    block = '\n'.join(lines[i:j])
    t = vis(block)
    if keep:
        t = '\n'.join(t.split('\n')[:keep])
    return t


T = {'r01-C1': from_to('- Severe stress', '- Years of accumulated') + '\n' + from_to('- Poor diet now', '- SIBO'),
     'r01-C2': from_to('- Years of accumulated', '- Poor diet now'),
     'r01-C3': from_to('- SIBO', '- Leaky gut') + '\n' + from_to('- IBS', '## Concise Recipe'),
     'r01-C4': from_to('- Leaky gut', '- IBS', keep=4)}
(HERE / 'texts').mkdir(exist_ok=True)
for k, t in T.items():
    (HERE / 'texts' / (k + '.txt')).write_text(t, encoding='utf-8')
    n = [p for p in t.split('\n') if len(p.split()) >= 8]
    print(k, len(t.split()), 'words,', len(n), 'paragraphs of 8+ words')
(HERE / 'TEXTS.json').write_text(json.dumps(T, ensure_ascii=False, indent=1), encoding='utf-8')
