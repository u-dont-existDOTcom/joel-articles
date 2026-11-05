#!/usr/bin/env python3
"""The check texts for r15's changed stretches (plain text, as Pangram reads it: link text kept, blocks joined by a blank
line), and HIS.txt: his words, which a receipt marks as his (r12, the text in his post, which he approved whole, and his
own F9-1 version of glutamine's paragraph)."""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
R = HERE.parents[1]
sys.path.insert(0, str(HERE.parents[5] / 'tools' / 'humanization'))
import suggestion_review as sr  # noqa: E402

plain = lambda b: (''.join(s['t'] for s in b['segs']) if b.get('segs') else b['text']).strip()
b12 = sr.blocks((R / 'r12' / 'r12.md').read_text(encoding='utf-8'))
b15 = sr.blocks((R / 'r15' / 'r15.md').read_text(encoding='utf-8'))
ans = json.loads((R.parent.parent / 'experiments' / 't14-answers' / 'REVIEW-ANSWERS-b9.json').read_text(encoding='utf-8'))
his_f91 = [x for x in ans['items'] if x['id'] == 'F9-1'][0]['your_version']
(HERE / 'HIS.txt').write_text('\n\n'.join(plain(b) for b in b12) + '\n\n' + his_f91 + '\n', encoding='utf-8')
STRETCHES = {'A': [1, 2, 3], 'B': list(range(9, 15)), 'C': list(range(16, 26)), 'D': list(range(26, 32)), 'E': [32, 33],
             'F': [35, 36], 'G': [40, 41, 42, 43], 'H': [45, 46, 47], 'I': list(range(50, 57)), 'J': [58, 59, 60],
             'K': list(range(62, 68)), 'L': [79, 80, 81, 82]}
meta = {}
for k, ids in STRETCHES.items():
    t = '\n\n'.join(plain(b15[i]) for i in ids)
    (HERE / ('CHECK-%s.txt' % k)).write_text(t, encoding='utf-8')
    meta[k] = {'blocks': ids, 'words': len(t.split()), 'section': b15[ids[0]].get('section', '')}
(HERE / 'STRETCHES.json').write_text(json.dumps(meta, indent=1), encoding='utf-8')
print(json.dumps(meta))
