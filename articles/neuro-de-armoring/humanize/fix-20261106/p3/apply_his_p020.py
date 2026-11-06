#!/usr/bin/env python3
"""His version of block 20 (the section "Psychology is the Software"'s first paragraph), word for word as he checked it
(his message of 2026-11-06 23:01 UTC; https://www.pangram.com/history/0240baf7-ed34-4897-8f3d-db1eab13274b, Human
Written; his reading "all high conf"; the history's windows Medium 22, High 45, Medium 26)."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
OLD_START = 'Standard therapy attempts to rewrite the "code"'
HIS = ('Have you done years of CBT or EMDR and yet you still freeze up or blow up at the same old triggers? One reason to '
       'think about, is that standard therapy is trying to rewrite the "code" (your thoughts and behaviors), while the '
       '"motherboard" (the brain\'s physical structure and chemistry) is often overheating or damaged, and code doesn\'t '
       'run well on a motherboard like that. So to address that, I\'ve designed this protocol to go after four specific '
       'neuro-biological problems before you go working on the psychology (well, alongside).')
assert hashlib.sha256(HIS.encode()).hexdigest().startswith(''), 'text'
text = ART.read_text(encoding='utf-8')
blocks = text.split('\n\n')
hits = [i for i, b in enumerate(blocks) if b.startswith(OLD_START)]
assert len(hits) == 1, hits
old = blocks[hits[0]]
blocks[hits[0]] = HIS
new = '\n\n'.join(blocks)
ART.write_text(new, encoding='utf-8')
(HERE / 'APPLIED-HIS-P020.json').write_text(json.dumps({
    'block': hits[0], 'old': old, 'new': HIS, 'whose': 'his edit of the model text, with my try 3 as its start (E373)',
    'check': 'https://www.pangram.com/history/0240baf7-ed34-4897-8f3d-db1eab13274b',
    'article_sha256_before': hashlib.sha256(text.encode()).hexdigest(),
    'article_sha256_after': hashlib.sha256(new.encode()).hexdigest()}, ensure_ascii=False, indent=1) + '\n')
print('block', hits[0], 'replaced')
