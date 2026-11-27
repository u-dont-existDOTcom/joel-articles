#!/usr/bin/env python3
"""Draft 22 (turn of 2026-11-27 19:25 UTC), after draft 21's checks (19:53 UTC), one change a text from each near miss:
A1's booking paragraph (its sixth and last try), from try 20 (Human Low; try 21's cut close read 22% AI): "your feelings"
says which, "the feelings you'd rather slip away from", which also leaves "which" one thing to point at; A3's opening (its
near miss now, High 88 and Medium 18): the last sentence's "it" said, "because of the pain"; IC2 from its near miss (ic2-9;
"see" read Low): "between them", READ-21's note (each therapy has its own trial's pain).
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft22.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
d18 = {a['id']: a for a in json.loads((D / 'ADDITIONS-18.json').read_text(encoding='utf-8'))}
d20 = {a['id']: a for a in json.loads((D / 'ADDITIONS-20.json').read_text(encoding='utf-8'))}
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
A1 = list(d18['A1']['paragraphs'])
b = d20['A1']['paragraphs'][3]
o1 = "All three keep steering you back toward your feelings, which can get to be too much."
assert b.startswith(o1) and b.endswith("I'd want them to say they'd slow down, and that they'd listen."), b[:90]
A1[4] = b.replace(o1, "All three keep steering you back toward the feelings you'd rather slip away from, which can get to be too much.")
d21 = {a['id']: a for a in json.loads((D / 'ADDITIONS-21.json').read_text(encoding='utf-8'))}
a3 = list(d21['A3']['paragraphs'])
o3 = "You also slowly go back to things you've been avoiding because of it, like going for walks."
assert a3[0].endswith(o3), a3[0][-100:]
a3[0] = a3[0].replace(o3, "You also slowly go back to things you've been avoiding because of the pain, like going for walks.")
out = []
for a in json.loads((D / 'ADDITIONS-21.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1; a['draft'] = 22
    if a['id'] == 'A3': a['paragraphs'] = a3; a['draft'] = 22
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-22.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-11.json').read_text(encoding='utf-8'))
IC9 = json.loads((D / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
o = "They both treat the pain as real, and they've helped people with long-lasting back, muscle and joint pain."
assert o in IC9['IC2']['add']
IC['IC2']['add'] = IC9['IC2']['add'].replace(o, "They both treat the pain as real, and between them they've helped people with long-lasting back, muscle and joint pain.")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-12.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts22-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
