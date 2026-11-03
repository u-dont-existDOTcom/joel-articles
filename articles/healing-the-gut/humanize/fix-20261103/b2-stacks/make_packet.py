#!/usr/bin/env python3
"""Blind meaning packet for batch 2: every writer's LGF, ST1 and ST2 against its r01 original, plus the Phase 2 polish
(b1-P2-D) against Phase 2's r01 original, shuffled under neutral ids. MEANING-PACKET.json goes to the checker;
MEANING-KEY.json stays here. No API calls."""
import json, pathlib, random
HERE = pathlib.Path(__file__).resolve().parent
units = json.loads((HERE / 'UNITS-r01-b2.json').read_text(encoding='utf-8'))
b1 = json.loads((HERE.parent / 'b1-protocol' / 'UNITS-r01.json').read_text(encoding='utf-8'))
D = json.loads((HERE.parent / 'b1-protocol' / 'polish' / 'writer_D.json').read_text(encoding='utf-8'))
items = []
for wr in 'ABC':
    w = json.loads((HERE / ('writer_%s.json' % wr)).read_text(encoding='utf-8'))
    for k in ('LGF', 'ST1', 'ST2'):
        items.append({'unit': k, 'writer': wr, 'original': units[k], 'rewrite': w[k]['text']})
items.append({'unit': 'P2', 'writer': 'D', 'original': b1['P2'], 'rewrite': D['P2']['text']})
random.Random(20261103).shuffle(items)
packet, key = [], []
for n, it in enumerate(items, 1):
    i = 'M%02d' % n
    packet.append({'id': i, 'original': it['original'], 'rewrite': it['rewrite']})
    key.append({'id': i, 'unit': it['unit'], 'writer': it['writer']})
(HERE / 'briefs' / 'MEANING-PACKET.json').write_text(json.dumps(packet, ensure_ascii=False, indent=1), encoding='utf-8')
(HERE / 'MEANING-KEY.json').write_text(json.dumps(key, indent=1), encoding='utf-8')
print(len(packet), 'items')
