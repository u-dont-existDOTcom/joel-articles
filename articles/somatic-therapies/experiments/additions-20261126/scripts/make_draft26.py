#!/usr/bin/env python3
"""Draft 26 (turn of 2026-11-27 22:26 UTC), after A1's section check with his two paragraphs in (22:30 UTC: 24% AI; the
AEDP paragraph AI Low and Medium in the section, though High by itself): his fixes of this turn applied to the AEDP
paragraph, mine: whose therapist ("The AEDP therapist", as his "The ISTDP therapist"), and the "and" that joined the
therapist's two acts made two sentences (his IC2 note: "\"and\" was a fake connection between clauses").
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft26.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for a in json.loads((D / 'ADDITIONS-25.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1':
        ps = list(a['paragraphs'])
        o = ("The therapist works to keep you from feeling alone with whatever comes up, and when some of their care does get "
             "in, they ask what that's like and where you feel it in your body.")
        assert ps[3].endswith(o), ps[3][-120:]
        ps[3] = ps[3].replace(o, "The AEDP therapist works to keep you from feeling alone with whatever comes up. When some of "
                                 "their care does get in, they ask what that's like and where you feel it in your body.")
        a['paragraphs'] = ps
    a['draft'] = 26
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-26.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts26-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(open(D / 'reads' / 'drafts26-numbered.txt').read())
