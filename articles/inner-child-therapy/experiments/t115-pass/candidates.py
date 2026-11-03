#!/usr/bin/env python3
"""Turn 115: each article paragraph that round 8 read below High-confidence Human somewhere (experiments/t115-results/
WINDOWS.json), with its windows marked, its Markdown as installed and the turn notes above it, so whose words they are
can be read off the notes. Writes CANDIDATES.json and CANDIDATES.md beside this file.
  candidates.py"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
EXP = HERE.parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / 'tools' / 'humanization'))
from notes import blocks  # noqa: E402
from paragraphs_alone import plain  # noqa: E402
from substack_check_text import smart  # noqa: E402

STRAIGHT = str.maketrans({'“': '"', '”': '"', '‘': "'", '’': "'", '‍': None, '️': None})


def norm(s):
    return re.sub(r'\s+', ' ', s.translate(STRAIGHT)).strip()


def main():
    W = json.loads((EXP / 't115-results' / 'WINDOWS.json').read_text(encoding='utf-8'))['items']
    texts = {h: json.loads((EXP / 't115-results' / ('RESULT-%s.json' % h)).read_text(encoding='utf-8'))['text'].split('\n') for h in 'AB'}
    B = blocks()
    keyed = [(norm(smart(plain(b['text']))), b) for b in B if not b['text'].startswith('#')]
    paras = {}
    for x in W:
        for p in x['paragraphs']:
            if not p['window'].strip():
                continue
            k = (x['half'], p['line'])
            line = texts[x['half']][p['line']]
            if k not in paras:
                n = norm(line)
                hits = [b for kk, b in keyed if kk == n] or [b for kk, b in keyed if kk[:60] == n[:60]]
                paras[k] = {'half': x['half'], 'line': p['line'], 'section': x['section'], 'text': line,
                            'md': hits[0]['text'] if hits else None, 'notes': hits[0]['notes'] if hits else [],
                            'found': len(hits), 'windows': []}
            paras[k]['windows'].append({'id': x['id'], 'label': x['label'], 'confidence': x['confidence'],
                                        'calibrated': x['calibrated_confidence'], 'words': x['words'], 'kind': x['kind'],
                                        'whose': x['whose'], 'round6': x['round6_text'], 'span': p['window'].strip()})
    out = sorted(paras.values(), key=lambda r: (r['half'], r['line']))
    for n, r in enumerate(out, 1):
        r['pid'] = 'p%02d' % n
    (HERE / 'CANDIDATES.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    md = ['# Turn 115: paragraphs with windows below High-confidence Human in round 8', '']
    for r in out:
        md += ['## %s. %s%d, %s' % (r['pid'], r['half'], r['line'], ' › '.join(r['section'][-2:])), '']
        for w in r['windows']:
            md.append('- %s: %s %s (%.3f), %d words, %s; round 6: %s; %s: "%s"' % (
                w['id'], w['label'], w['confidence'], w['calibrated'] or 0, w['words'], w['kind'], w['round6'], w['whose'], w['span'][:200]))
        md += ['', 'Notes:', ''] + ['- ' + n[:700].replace('\n', ' ') for n in r['notes']] + ['', '> ' + (r['md'] or '(not found)'), '']
    (HERE / 'CANDIDATES.md').write_text('\n'.join(md), encoding='utf-8')
    print(len(out), 'paragraphs;', sum(1 for r in out if not r['md']), 'not found;', sum(1 for r in out if r['found'] > 1), 'ambiguous')


if __name__ == '__main__':
    main()
