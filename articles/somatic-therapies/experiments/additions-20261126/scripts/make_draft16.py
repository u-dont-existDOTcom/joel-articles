#!/usr/bin/env python3
"""Draft 16: after the draft-15 checks and the tell panel on A1's opening."""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-15.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
ISTDP = 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and'
A1 = list(by['A1']['paragraphs'])
A1[0] = ("By this layer you can probably feel your body just fine. You might still slip away the moment a feeling shows up in "
         "a session, though: you start explaining it, or you agree with whatever the therapist says just to get past it. In "
         "[Intensive Short-Term Dynamic Psychotherapy](%s), the therapist catches you at it, with something like \"Notice how "
         "you just started explaining?\", and asks what you're feeling right then." % ISTDP)
o = "If you can only handle a little of that anxiety"
assert o in A1[1]; A1[1] = A1[1].replace(o, "If you can only take a little of that anxiety")
A1[4] = ("All three keep steering you back toward your feelings, which can get to be too much. So before booking, I'd ask the "
         "kind of thing I'd ask a water therapist: what happens if I get overwhelmed, or if I think you've got my feelings "
         "wrong? I'd want them to say they'd slow down, and that they'd listen.")
A3 = list(by['A3']['paragraphs'])
o = "Maybe pain is what brought you to this guide in the first place."
assert o in A3[0]; A3[0] = A3[0].replace(o, "Maybe pain is what brought you here in the first place.")
def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1': a['paragraphs'] = A1; a['draft'] = 16
    if aid == 'A3': a['paragraphs'] = A3; a['draft'] = 16
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest()
    a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-16.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-6.json').read_text(encoding='utf-8'))
o = "as the adult you needed, until"
assert o in IC['IC1']['add']; IC['IC1']['add'] = IC['IC1']['add'].replace(o, "as the adult you needed back then, until")
IC['IC2']['add'] = ("While the investigation goes on, if the tests keep coming back normal, I'd also look into two talk therapies "
                    "that treat the pain as real: Pain Reprocessing Therapy and Emotional Awareness and Expression Therapy. "
                    "(More on both in [my somatic guide](https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit).)")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-7.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
sys.path.insert(0, str(D.parents[3] / 'tools' / 'humanization'))
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
(D / 'reads' / 'drafts16-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(l for l in lines if l.startswith(('A1-S1:', 'A1-S2:', 'A1-S3:', 'A1-S5:', 'A1-S10', 'A1-S11', 'A1-S12', 'A3-S1:', 'IC'))))
for a in out:
    print(a['id'], a['words'], [len(plain(p).split()) for p in a['paragraphs']])
for k, v in IC.items():
    print(k, len(v['add_plain'].split()))
P = D / 'panel' / 'A1-P1-16'
P.mkdir(parents=True, exist_ok=True)
(P / 'TEXT.txt').write_text(plain(A1[0]) + '\n', encoding='utf-8')
