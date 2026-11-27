#!/usr/bin/env python3
"""Draft 18 (turn of 2026-11-27 19:25 UTC): the checkpoint's next steps.
  python3 scripts/make_draft18.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-17.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
ISTDP = 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and'
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
def swap(s, o, n):
    assert o in s, o
    return s.replace(o, n)
A1 = list(by['A1']['paragraphs'])
# try 4 of the opening: the case as an "if" clause, the way the AEDP paragraph that read Human High opens
A1[0] = ("If you can feel your body just fine by now but still slip away the moment a feeling comes up in a session (you "
         "start explaining it, or agree with whatever the therapist says just to get past it), there's [Intensive "
         "Short-Term Dynamic Psychotherapy](%s). The therapist catches you at it each time and asks what you're feeling "
         "right then." % ISTDP)
A1[4] = swap(A1[4], "and that they'd listen.", "and that they'd hear me out.")
A3 = list(by['A3']['paragraphs'])
A3[0] = swap(A3[0], "Maybe physical pain is what brought you here in the first place. If yours has lasted months,",
             "If physical pain is what brought you here in the first place, and it has lasted months,")
out = []
for a in prev:
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1; a['draft'] = 18
    if a['id'] == 'A3': a['paragraphs'] = A3; a['draft'] = 18
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-18.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-7.json').read_text(encoding='utf-8'))
IC['IC1']['add'] = swap(IC['IC1']['add'], "stepping into the memory", "stepping into that memory")
IC['IC2']['add'] = ("While the investigation goes on, if the tests keep coming back normal, I'd also look into two talk therapies "
                    "that treat the pain as real. In Pain Reprocessing Therapy, you learn to see it as an alarm your brain "
                    "keeps sounding though the doctors haven't found any danger, and Emotional Awareness and Expression Therapy "
                    "has you work on the feelings tied up with it. (More on both in [my somatic guide]"
                    "(https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit).)")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-8.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts18-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
P = D / 'panel' / 'A1-P1-18'
P.mkdir(parents=True, exist_ok=True)
(P / 'TEXT.txt').write_text(plain(A1[0]) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
print('IC1', len(IC['IC1']['add_plain'].split()), 'IC2', len(IC['IC2']['add_plain'].split()))
