#!/usr/bin/env python3
"""Draft 25, the final texts (turn of 2026-11-27 22:26 UTC): his versions from the cards of 20:12 UTC (his answers of 22:19
and 22:26 UTC, answers/ANSWERS-C1127-*.json), each read back from his Pangram history (pangram/HIS-CHECKS-C1127.json):
A1's first paragraph and booking paragraph his (the other three as they read Human High by themselves); A2 his (as
before); A3 his whole section; IC1 approved as it stood; IC2 his, with the somatic guide's link put back on "my somatic
guide" (the link changes no word he checked).
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft25.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
his = json.loads((D / 'pangram' / 'HIS-CHECKS-C1127.json').read_text(encoding='utf-8'))['items']
som = {i['id']: i for i in json.loads((D / 'answers' / 'ANSWERS-C1127-SOMATIC-20261127-2219.json').read_text(encoding='utf-8'))['items']}
inn = {i['id']: i for i in json.loads((D / 'answers' / 'ANSWERS-C1127-INNER-20261127-2226.json').read_text(encoding='utf-8'))['items']}
d23 = {a['id']: a for a in json.loads((D / 'ADDITIONS-23.json').read_text(encoding='utf-8'))}
ISTDP = re.search(r'\[Intensive Short-Term Dynamic Psychotherapy\]\(([^)]+)\)', d23['A1']['paragraphs'][0]).group(1)
P1 = ("If you can feel your body just fine by now but you still slip away the moment a feeling comes up in a session (you "
      "start explaining it, or agree with whatever the therapist says just to get past it), there's [Intensive Short-Term "
      "Dynamic Psychotherapy](%s). The ISTDP therapist catches you each time they notice you slipping, and asks what you're "
      "feeling right then." % ISTDP)
P5 = ("All three keep steering you back toward your feelings, which can get to be too intense sometimes. So before booking, "
      "I'd ask the kind of thing I'd ask a water therapist: \"What happens if I get overwhelmed, or if you say I'm dodging a "
      "feeling and I don't think I am?\" I'd want to hear that they would change the approach, listen to me and be gentler.")
A1 = [P1] + list(d23['A1']['paragraphs'][1:4]) + [P5]
assert A1[1].startswith("It's usually anxiety about the feeling") and A1[3].startswith("And if what you can't let in is kindness")
a3 = som['A3-TEACH']['your_version']
head, _, body = a3.partition('\n\n')
assert head == "# Pain That Won't Quit?"
A3 = body.split('\n\n')
out = []
for a in json.loads((D / 'ADDITIONS-23.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1
    if a['id'] == 'A3': a['paragraphs'] = A3
    a['draft'] = 25
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-25.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
assert inn['IC1']['status'] == 'approved' and inn['IC1']['my_version'] == IC['IC1']['add']
v = inn['IC2-TEACH']['your_version']
assert 'I go into in my somatic guide,' in v
IC['IC2']['add'] = v.replace('I go into in my somatic guide,', 'I go into in [my somatic guide](https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit),')
for k, x in IC.items():
    x['add_plain'] = plain(x['add'])
    x['sha256_pair'] = hashlib.sha256((x['his_before'] + '\n\n' + x['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-25.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
# each final text against the text of the check that read it High
checks = {'A1-P1': plain(P1), 'A1-P5': P5, 'IC2': IC['IC2']['add_plain']}
print({k: len(t.split()) for k, t in checks.items()})
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
