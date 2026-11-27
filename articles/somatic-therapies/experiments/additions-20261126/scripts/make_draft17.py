#!/usr/bin/env python3
"""Draft 17: draft 16 with READ-16's two fixes (the booking question ties to the therapist catching you; "physical pain").
  python3 scripts/make_draft17.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-16.json').read_text(encoding='utf-8'))
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
for a in prev:
    if a['id'] == 'A1':
        o = "what happens if I get overwhelmed, or if I think you've got my feelings wrong?"
        a['paragraphs'][4] = a['paragraphs'][4].replace(o, "what happens if I get overwhelmed, or if you say I'm dodging a feeling and I don't think I am?")
        a['draft'] = 17
    if a['id'] == 'A3':
        o = "Maybe pain is what brought you here in the first place."
        a['paragraphs'][0] = a['paragraphs'][0].replace(o, "Maybe physical pain is what brought you here in the first place.")
        a['draft'] = 17
    a['text'] = '\n\n'.join(plain(x) for x in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode()).hexdigest(); a['words'] = len(a['text'].split())
(D / 'ADDITIONS-17.json').write_text(json.dumps(prev, indent=1, ensure_ascii=False), encoding='utf-8')
