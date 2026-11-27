#!/usr/bin/env python3
"""Draft 23 (turn of 2026-11-27 19:25 UTC), after draft 22's checks (19:58 UTC): A1's booking paragraph is spent (six tries;
its best, try 17 and try 20, Human Low), so A1 keeps try 20's; A3's opening (try 8 of 10, near miss a3-p1-21: High 88,
Medium 18 over its last sentence; "the pain" for "it" read the same): the last sentence joined to the one it draws on, both
being how you learn it's a false alarm (lesson neuro-2026-11-27e); IC2's last try, from its near miss (ic2-9: High 38,
Medium 20 over its second sentence; every change to that sentence read lower): the second sentence joined to the first, with READ-23's "between them" (each therapy has its own trial's pain).
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft23.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
d20 = {a['id']: a for a in json.loads((D / 'ADDITIONS-20.json').read_text(encoding='utf-8'))}
d22 = {a['id']: a for a in json.loads((D / 'ADDITIONS-22.json').read_text(encoding='utf-8'))}
A1 = list(d22['A1']['paragraphs'])
A1[4] = d20['A1']['paragraphs'][3]
assert A1[4].startswith('All three keep steering you back toward your feelings,') and A1[4].endswith("that they'd listen.")
a3 = list(d22['A3']['paragraphs'])
o3 = ("Part of how you learn it's a false alarm is by paying close attention to how the pain feels in your body, without "
      "being scared of it. You also slowly go back to things you've been avoiding because of the pain, like going for walks.")
assert a3[0].endswith(o3), a3[0][-200:]
a3[0] = a3[0].replace(o3, "Part of how you learn it's a false alarm is by paying close attention to how the pain feels in your body, "
                          "without being scared of it, and by slowly going back to things you've been avoiding because of "
                          "the pain, like going for walks.")
out = []
for a in json.loads((D / 'ADDITIONS-22.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1; a['draft'] = 23
    if a['id'] == 'A3': a['paragraphs'] = a3; a['draft'] = 23
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-23.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-12.json').read_text(encoding='utf-8'))
IC9 = json.loads((D / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
o = (" Pain Reprocessing Therapy or Emotional Awareness and Expression Therapy. They both treat the pain as real, and they've "
     "helped people with long-lasting back, muscle and joint pain.")
assert IC9['IC2']['add'].endswith(o), IC9['IC2']['add'][-200:]
IC['IC2']['add'] = IC9['IC2']['add'].replace(o, " Pain Reprocessing Therapy or Emotional Awareness and Expression Therapy, which both "
                                               "treat the pain as real and between them have helped people with long-lasting back, muscle "
                                               "and joint pain.")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-13.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
sys.path.insert(0, str(D.resolve().parents[3] / 'tools' / 'humanization'))
import sense_receipt
lines = []
for a in out:
    if a['id'] == 'A2':
        continue
    lines.append('## %s, "%s" (h%d)' % (a['id'], a['heading'], a['level']))
    n = 0
    for i, p in enumerate(a['paragraphs'], 1):
        lines.append('[paragraph %d]' % i)
        for s in sense_receipt.sentences(plain(p)):
            n += 1
            lines.append('%s-S%d: %s' % (a['id'], n, s))
    lines.append('')
for k, v in IC.items():
    lines.append('## %s, in "%s"' % (k, v['section']))
    lines.append('Where: ' + v['where'])
    for j, s in enumerate(sense_receipt.sentences(v['add_plain']), 1):
        lines.append('%s-S%d: %s' % (k, j, s))
    lines.append('')
(D / 'reads' / 'drafts23-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
