#!/usr/bin/env python3
"""fix_hypnosis_link.py - item 1 of the guide's contradictions check (EXTRACT.md): the Self-Hypnosis guide was linked as
http://hypnoisis.u-dont-exist.com in the Shadow Work part (from his post) and as http://hypnosis.u-dont-exist.com/ in the
guide's first paragraph. The typo is fixed as an obvious correction (Joel, 2026-11-12: "no need to ask me for obvious
corrections").

  python3 articles/bad-trips/humanize/h61-20261120/contradictions/fix_hypnosis_link.py     (from the repo root)
"""
import json, pathlib

ART = pathlib.Path(__file__).resolve().parents[3]
BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
OLD, NEW = '(http://hypnoisis.u-dont-exist.com)', '(http://hypnosis.u-dont-exist.com)'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
hits = [b for b in B if OLD in b['md']]
assert len(hits) <= 1
for b in hits:
    b['md'] = b['md'].replace(OLD, NEW)
MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('fixed', len(hits))
