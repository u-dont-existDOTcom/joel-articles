#!/usr/bin/env python3
"""Draft 14: after the draft-13 checks. Near misses get a word or two (A1-S5 "of it"; A3-S1 "in the first place"; A3's
lower-bar sentence says what 0 or 1 out of 10 is); the texts that read AI get a new try (A1-P1, the booking paragraph,
IC1, IC2)."""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-13.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
ISTDP = 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and'
A1 = list(by['A1']['paragraphs'])
A1[0] = ("Even once you can feel your body just fine, you can still slip away from a feeling the moment it comes up in a "
         "session, because you start explaining it, or agree with whatever the therapist says so you don't have to stay in "
         "it. For that, there's [Intensive Short-Term Dynamic Psychotherapy](%s), where the therapist points out each time "
         "you slip away and helps you turn back toward the feeling." % ISTDP)
o = "you'd get a slower version, where"
assert o in A1[1]; A1[1] = A1[1].replace(o, "you'd get a slower version of it, where")
A1[4] = ("Before booking, I'd ask any of these therapists what they do when you slip away from a feeling or get overwhelmed, "
         "and whether you can tell them they've read you wrong. If there's no room in their answer for you to slow down or "
         "disagree, I'd keep looking.")
A3 = list(by['A3']['paragraphs'])
o = "Maybe pain is what brought you to this guide."
assert o in A3[0]; A3[0] = A3[0].replace(o, "Maybe pain is what brought you to this guide in the first place.")
o = "A 30% drop is a lower bar than 0 or 1 out of 10,"
assert o in A3[4]; A3[4] = A3[4].replace(o, "A 30% drop is a lower bar than getting your pain down to 0 or 1 out of 10,")
def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1': a['paragraphs'] = A1; a['draft'] = 14
    if aid == 'A3': a['paragraphs'] = A3; a['draft'] = 14
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest()
    a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-14.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-4.json').read_text(encoding='utf-8'))
IC['IC1']['add'] = ("It turns out there's an actual clinical therapy for this, called [Imagery Rescripting]"
                    "(https://ibogaqueen.substack.com/i/201523223/imagery-rescripting), though I didn't know it when I wrote "
                    "this. If a memory feels too big to redo on your own, a therapist can step into it as the adult you "
                    "needed, until you learn to be that adult yourself.")
IC['IC1']['note'] = ('"though I didn\'t know it when I wrote this" is his own, from his card answer of 2026-11-27 00:55 UTC: '
                     '"although I didn\'t know it was a therapy when i wrote about it"')
IC['IC2']['add'] = ("While the investigation goes on, if the tests keep coming back normal, I'd also look into two talk therapies "
                    "that treat the pain as real and work on how the brain keeps it going: Pain Reprocessing Therapy and "
                    "Emotional Awareness and Expression Therapy. So far they've mostly been tested on chronic back pain and "
                    "other muscle and joint pain, and they helped (more on both in [my somatic guide]"
                    "(https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit)).")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-5.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts14-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(l for l in lines if l.startswith(('A1-S1', 'A1-S2', 'A1-S5', 'A1-S6', 'A1-S10', 'A1-S11', 'A3-S1', 'A3-S12', 'IC'))))
for a in out:
    print(a['id'], a['words'], [len(plain(p).split()) for p in a['paragraphs']])
for k, v in IC.items():
    print(k, len(v['add_plain'].split()))
