#!/usr/bin/env python3
"""Draft 20 (turn of 2026-11-27 19:25 UTC), after draft 19's checks: A1's opening merged into the ISTDP paragraph (the
sixth and last try of ADD-A1-P1: no stand-alone problem-then-therapy unit); A1's booking paragraph back to try 17 with its question in quotes (READ-20; near-miss rule); IC2's
second sentence says how many got better; A3's opening merged into the paragraph after it (its last try). READ-20's and READ-20b's marks applied.
  python3 scripts/make_draft20.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
d17 = {a['id']: a for a in json.loads((D / 'ADDITIONS-17.json').read_text(encoding='utf-8'))}
d19 = {a['id']: a for a in json.loads((D / 'ADDITIONS-19.json').read_text(encoding='utf-8'))}
ISTDP = 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and'
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
p17 = d17['A1']['paragraphs']
merged = ("If, as soon as a feeling starts in a session, you're already explaining where it comes from, or agreeing with "
          "whatever the therapist says so the moment will pass, [Intensive Short-Term Dynamic Psychotherapy](%s) would say "
          "it's anxiety about the feeling that makes you slip away like that. In that therapy, the therapist points it out "
          "as you do it and "
          "keeps pushing for the feeling, while watching for signs of that anxiety, like tense muscles, sighing, or your "
          "thinking going foggy, to tell when it's getting to be too much for you. If you can only take a little of it, like "
          "most people who try this therapy, you'd get a slower version, where the therapist stops to help you settle "
          "whenever the anxiety climbs." % ISTDP)
# READ-20 and the near-miss rule (lesson bad-trips-2026-11-19b): the booking paragraph goes back to try 17 (Human Low),
# its best, and changes only what a reader could take two ways: the "you" of the question is the therapist, so the
# question is in quotes (READ-20, A1-S9: "nothing marking it as still the question to ask").
p17b = d17['A1']['paragraphs'][4]
assert p17b.startswith("All three keep steering you back"), p17b[:60]
qo = "water therapist: what happens if I get overwhelmed, or if you say I'm dodging a feeling and I don't think I am? I'd"
assert qo in p17b
booking = p17b.replace(qo, 'water therapist: "What happens if I get overwhelmed, or if you say I\'m dodging a feeling and I don\'t think I am?" I\'d')
A1 = [merged, p17[2], p17[3], booking]
a3 = d17['A3']['paragraphs']
o = "Maybe physical pain is what brought you here in the first place. If yours has lasted months,"
assert o in a3[0]
first = a3[0].replace(o, "If your pain has lasted months,")
assert a3[1].startswith("In [Pain Reprocessing Therapy]")
second = a3[1].replace("In [Pain Reprocessing Therapy]", "In the first, [Pain Reprocessing Therapy]", 1)
# READ-20, A3-S2 (light): "though real" wedged into a five-comma sentence, and "haven't found any" pointing at "danger".
so = "you learn to treat the pain, though real, as a false alarm, your brain signaling danger where the doctors haven't found any."
assert so in second
second = second.replace(so, "you learn to treat the pain as a false alarm. It's real, but it's your brain signaling danger where the doctors haven't found any injury.")
A3 = [first + " " + second] + list(a3[2:])
out = []
for a in json.loads((D / 'ADDITIONS-19.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1; a['draft'] = 20
    if a['id'] == 'A3': a['paragraphs'] = A3; a['draft'] = 20
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-20.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-9.json').read_text(encoding='utf-8'))
o = "They both treat the pain as real, and they've helped people with long-lasting back, muscle and joint pain."
assert o in IC['IC2']['add']
IC['IC2']['add'] = IC['IC2']['add'].replace(o, "They both treat the pain as real, and in their trials most people with long-lasting back, muscle and joint pain got better.")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-10.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts20-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
