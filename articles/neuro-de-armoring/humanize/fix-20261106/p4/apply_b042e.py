#!/usr/bin/env python3
"""Block 42 (section B, the Repair): round 4's try read Human Written, one window High, 80 words
(https://www.pangram.com/history/e06f6f0d-f215-4c45-8c5a-9b76a2f96120). In the whole check it read AI."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
text = ART.read_text(encoding='utf-8')
blocks = text.split('\n\n')
hits = [i for i, b in enumerate(blocks) if b.startswith('The Repair (Leucine/L-Serine)')]
assert len(hits) == 1, hits
old = blocks[hits[0]]
blocks[hits[0]] = (HERE / 'B042e.txt').read_text(encoding='utf-8').rstrip('\n')
out = '\n\n'.join(blocks)
ART.write_text(out, encoding='utf-8')
(HERE / 'APPLIED-B042E.json').write_text(json.dumps({'block': hits[0], 'old': old, 'new': blocks[hits[0]],
    'article_sha256_before': hashlib.sha256(text.encode()).hexdigest(),
    'article_sha256_after': hashlib.sha256(out.encode()).hexdigest()}, ensure_ascii=False, indent=1) + '\n')
print('block', hits[0])
