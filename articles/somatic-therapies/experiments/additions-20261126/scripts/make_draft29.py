#!/usr/bin/env python3
"""Draft 29 (turn of 2026-11-27 22:26 UTC), after A1's section check of draft 28 (22:39 UTC: Human Written, 0% AI;
below High: his first paragraph's second sentence Medium 19, my AEDP paragraph Medium 26, Low 17 and Medium 22, his booking
paragraph's first sentence Low 17): the Low window of mine is "The AEDP therapist stays with you through whatever comes up, so
you're not alone with it.", which says one thing from two sides (READ-27's closest call, way 16); the act stays and the
restatement goes: "The AEDP therapist stays with you through whatever comes up."
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft29.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for a in json.loads((D / 'ADDITIONS-28.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1':
        ps = list(a['paragraphs'])
        o = "The AEDP therapist stays with you through whatever comes up, so you're not alone with it."
        assert o in ps[3], ps[3][-200:]
        ps[3] = ps[3].replace(o, "The AEDP therapist stays with you through whatever comes up.")
        a['paragraphs'] = ps
    a['draft'] = 29
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-29.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
sys.path.insert(0, str(D.resolve().parents[3] / 'tools' / 'humanization'))
import sense_receipt
lines = []
for a in out:
    if a['id'] != 'A1':
        continue
    lines.append('## %s, "%s" (h%d); paragraphs 1 and 5 are his versions from the card (answers of 22:19 UTC)' % (a['id'], a['heading'], a['level']))
    n = 0
    for i, p in enumerate(a['paragraphs'], 1):
        lines.append('[paragraph %d]' % i)
        for s in sense_receipt.sentences(plain(p)):
            n += 1
            lines.append('%s-S%d: %s' % (a['id'], n, s))
(D / 'reads' / 'drafts29-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(open(D / 'reads' / 'drafts29-numbered.txt').read())
