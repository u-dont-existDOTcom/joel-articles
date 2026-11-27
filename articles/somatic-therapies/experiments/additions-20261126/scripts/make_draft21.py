#!/usr/bin/env python3
"""Draft 21 (turn of 2026-11-27 19:25 UTC), after draft 20's checks (19:47 UTC): A1's opening is spent (six tries, all AI;
the merged try read AI in both windows), so A1 keeps draft 18's structure with its best opening (try 18, AI 0.91) until
Joel's version; A1's booking paragraph, from its near miss (try 17, Human Low; try 20 with the question in quotes, Human
Low): the panel's two-beat close cut to "slow down and listen"; IC2 from its near miss (ic2-9; ic2-10's trial line read
Low): "treat the pain as real", which a reader can take as treating the pain, now "see"; A3's opening, its last try, with
the tell panel's agreed sentences fixed (panel/A3-P1-20) and READ-21's mark (a clause after the colon).
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft21.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
d18 = {a['id']: a for a in json.loads((D / 'ADDITIONS-18.json').read_text(encoding='utf-8'))}
d20 = {a['id']: a for a in json.loads((D / 'ADDITIONS-20.json').read_text(encoding='utf-8'))}
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
A1 = list(d18['A1']['paragraphs'])
b = d20['A1']['paragraphs'][3]
assert b.endswith("I'd want them to say they'd slow down, and that they'd listen."), b[-80:]
A1[4] = b.replace("I'd want them to say they'd slow down, and that they'd listen.", "I'd want them to say they'd slow down and listen.")
a3 = list(d20['A3']['paragraphs'])
m = re.search(r'\[Pain Reprocessing Therapy\]\(([^)]+)\)', a3[0])
PRT = m.group(1)
a3[0] = ("If your pain has lasted months, and a doctor has checked and found no injury or disease to explain it, there are "
         "two therapies I'd look into. In the first, [Pain Reprocessing Therapy](%s), you learn to treat the pain as a false "
         "alarm: your brain is making real pain, signaling danger where the doctors haven't found any injury. Part of how you "
         "learn it's a false alarm is by paying close attention to how the pain feels in your body, without being scared of "
         "it. You also slowly go back to things you've been avoiding because of it, like going for walks." % PRT)
out = []
for a in json.loads((D / 'ADDITIONS-20.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1; a['draft'] = 21
    if a['id'] == 'A3': a['paragraphs'] = a3; a['draft'] = 21
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-21.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-10.json').read_text(encoding='utf-8'))
IC9 = json.loads((D / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
o = "They both treat the pain as real, and they've helped people with long-lasting back, muscle and joint pain."
assert o in IC9['IC2']['add']
IC['IC2']['add'] = IC9['IC2']['add'].replace(o, "They both see the pain as real, and they've helped people with long-lasting back, muscle and joint pain.")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-11.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts21-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
