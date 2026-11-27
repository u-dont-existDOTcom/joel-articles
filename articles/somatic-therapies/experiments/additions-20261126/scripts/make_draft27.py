#!/usr/bin/env python3
"""Draft 27 (turn of 2026-11-27 22:26 UTC), after A1's section check of draft 26 (22:35 UTC: 17% AI, AI Low over "The
AEDP therapist works to keep you from feeling alone with whatever comes up." and over the sentence after it with his booking
sentence): that sentence says what the therapist does, not their aim (his IC2 note: say how it helps), without READ-26's
near misread "keep you from feeling": "The AEDP therapist stays with you through whatever comes up, so you're not alone
with it." (the source's "undoing aloneness").
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft27.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for a in json.loads((D / 'ADDITIONS-26.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1':
        ps = list(a['paragraphs'])
        o = "The AEDP therapist works to keep you from feeling alone with whatever comes up."
        assert o in ps[3], ps[3][-160:]
        ps[3] = ps[3].replace(o, "The AEDP therapist stays with you through whatever comes up, so you're not alone with it.")
        a['paragraphs'] = ps
    a['draft'] = 27
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-27.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts27-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(open(D / 'reads' / 'drafts27-numbered.txt').read())
