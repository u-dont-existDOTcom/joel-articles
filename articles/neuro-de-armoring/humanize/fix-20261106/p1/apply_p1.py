#!/usr/bin/env python3
"""Round P1: the three rewrites that read Human in their own check go into the article (Part 1's opening and section A,
blocks 30, 32 and 33: STRETCH-030-033 read Human Written, windows High, Medium, Low on "Dr." alone, Medium, High;
https://www.pangram.com/history/b1594a9f-6c90-4dcd-b117-68c50f21df5e; P032 alone Human, Medium,
https://www.pangram.com/history/eeb2d730-ca9e-41ea-815e-6163350f8aee). In the whole check all three read AI. The others
read AI twice and wait for the tell panel (RESULTS.md)."""
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1] / 'HUMANIZED-SO-FAR.md'
STARTS = {30: 'Before applying the tools, you must understand the specific', 32: 'We often assume we can "think" our way out',
          33: 'In this state, functional IQ drops substantially'}
text = ART.read_text(encoding='utf-8')
before = hashlib.sha256(text.encode()).hexdigest()
blocks = text.split('\n\n')
done = {}
for b, start in STARTS.items():
    assert blocks[b].startswith(start), (b, blocks[b][:60])
    new = (HERE / ('P%03d.txt' % b)).read_text(encoding='utf-8').rstrip('\n')
    done[b] = {'old': blocks[b], 'new': new}
    blocks[b] = new
out = '\n\n'.join(blocks)
ART.write_text(out, encoding='utf-8')
(HERE / 'APPLIED-P1.json').write_text(json.dumps({'article_sha256_before': before,
    'article_sha256_after': hashlib.sha256(out.encode()).hexdigest(), 'blocks': done}, ensure_ascii=False, indent=1) + '\n')
print(before[:12], '->', hashlib.sha256(out.encode()).hexdigest()[:12])
