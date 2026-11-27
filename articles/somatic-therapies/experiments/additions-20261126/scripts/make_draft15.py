#!/usr/bin/env python3
"""Draft 15: READ-14 acted on."""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-14.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
A1 = list(by['A1']['paragraphs'])
o = "because you start explaining it, or agree with whatever"
assert o in A1[0]; A1[0] = A1[0].replace(o, "by explaining it, or by agreeing with whatever")
o = "whenever it climbs."
assert o in A1[1]; A1[1] = A1[1].replace(o, "whenever the anxiety climbs.")
A1[4] = ("Since in all three the therapist keeps steering you back to your feelings, before booking I'd ask what they do when "
         "you get overwhelmed, and what happens if you tell them they've read you wrong. If there's no room in their answer "
         "for you to slow down or disagree, I'd keep looking.")
A3 = list(by['A3']['paragraphs'])
o = "I haven't found a trial comparing the two."
assert o in A3[5]; A3[5] = A3[5].replace(o, "I haven't found a trial comparing the two therapies.")
def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1': a['paragraphs'] = A1; a['draft'] = 15
    if aid == 'A3': a['paragraphs'] = A3; a['draft'] = 15
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest()
    a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-15.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-5.json').read_text(encoding='utf-8'))
IC['IC1']['add'] = ("If a memory feels too big to redo on your own, there's an actual clinical therapy for that, called [Imagery "
                    "Rescripting](https://ibogaqueen.substack.com/i/201523223/imagery-rescripting), which I only found out "
                    "about after I wrote this section. The therapist has you picture them stepping into the memory as the "
                    "adult you needed, until you learn to be that adult yourself.")
IC['IC1']['note'] = ('"which I only found out about after I wrote this section" is his own, from his card answer of 2026-11-27 '
                     '00:55 UTC: "although I didn\'t know it was a therapy when i wrote about it"')
IC['IC2']['add'] = ("While the investigation goes on, if the tests keep coming back normal, I'd also look into two talk therapies "
                    "that treat the pain as real: Pain Reprocessing Therapy and Emotional Awareness and Expression Therapy. So "
                    "far they've mostly been tested on chronic back pain and other muscle and joint pain, where they helped "
                    "most of the people who got them, so I can't say how they'd do for attacks like these (more on both in "
                    "[my somatic guide](https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit)).")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-6.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], a['words'], [len(plain(p).split()) for p in a['paragraphs']])
for k, v in IC.items():
    print(k, len(v['add_plain'].split()))
