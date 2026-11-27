#!/usr/bin/env python3
"""Draft 30 (turn of 2026-11-27 22:26 UTC), after A1's section check of draft 29 (22:42 UTC: Human Written, 0% AI; High 47,
Medium 19, High 143, Medium 49, High 55, https://www.pangram.com/history/089bbeb6-7fe6-4961-b18f-7d54fd474d5b).

Diagnosis: each Medium window starts on a short form the reader was never given. The first, 19 words, is his "The ISTDP
therapist catches you each time ..."; the second, 49 words, starts on my "The AEDP therapist stays with you ...". Both
therapies are named in full ("there's Intensive Short-Term Dynamic Psychotherapy", "there's Accelerated Experiential
Dynamic Psychotherapy") and the next sentence calls them by letters the text hasn't said. His own fix in A3 is the other
half of lesson somatic-2026-11-27k: where a therapy is named, its short form follows in brackets ("[Pain Reprocessing
Therapy](...) (PRT)"), and the short form is used after that. Draft 29 took the first half ("The AEDP therapist") without
the second. The fix: " (ISTDP)" after the first name, in his paragraph, and " (AEDP)" after the second, in mine; nothing
else changes. His words with the brackets go to him on a card (his own), whatever the check reads.
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft30.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
ISTDP = ('[Intensive Short-Term Dynamic Psychotherapy](https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-'
         'dynamic-psychotherapy-methods-evidence-indications-and).')
AEDP = '[Accelerated Experiential Dynamic Psychotherapy](https://www.apa.org/pubs/videos/4310759).'
out = []
for a in json.loads((D / 'ADDITIONS-29.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1':
        ps = list(a['paragraphs'])
        assert ps[0].count(ISTDP) == 1 and ps[3].count(AEDP) == 1
        ps[0] = ps[0].replace(ISTDP, ISTDP[:-1] + ' (ISTDP).')
        ps[3] = ps[3].replace(AEDP, AEDP[:-1] + ' (AEDP).')
        a['paragraphs'] = ps
    a['draft'] = 30
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-30.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
sys.path.insert(0, str(D.resolve().parents[3] / 'tools' / 'humanization'))
import sense_receipt
lines = []
for a in out:
    if a['id'] != 'A1':
        continue
    lines.append('## %s, "%s" (h%d); paragraphs 1 and 5 are his versions from the card (answers of 22:19 UTC), paragraph 1 '
                 'with " (ISTDP)" added after the therapy\'s name' % (a['id'], a['heading'], a['level']))
    n = 0
    for i, p in enumerate(a['paragraphs'], 1):
        lines.append('[paragraph %d]' % i)
        for s in sense_receipt.sentences(plain(p)):
            n += 1
            lines.append('%s-S%d: %s' % (a['id'], n, s))
(D / 'reads' / 'drafts30-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(open(D / 'reads' / 'drafts30-numbered.txt').read())
