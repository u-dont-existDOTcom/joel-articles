#!/usr/bin/env python3
"""Draft 19 (turn of 2026-11-27 19:25 UTC), after draft 18's checks: A3's opening back to its near miss without the hook
line; A1's booking paragraph back to its near miss ("listen") with his own water-therapy frame; IC1's second sentence in
his own words from his A2 version; IC2 in his run-on voice. A1's opening comes from a fresh writer (writer/).
  python3 scripts/make_draft19.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
d17 = {a['id']: a for a in json.loads((D / 'ADDITIONS-17.json').read_text(encoding='utf-8'))}
d18 = {a['id']: a for a in json.loads((D / 'ADDITIONS-18.json').read_text(encoding='utf-8'))}
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
def swap(s, o, n):
    assert o in s, o
    return s.replace(o, n)
A1 = list(d18['A1']['paragraphs'])
w = (D / 'writer' / 'A1-P1-WRITER-1-READ19.md')  # the fresh writer's paragraph with READ-19's three fixes
if w.exists():
    A1[0] = w.read_text(encoding='utf-8').strip()
A1[4] = swap(d17['A1']['paragraphs'][4], "So before booking, I'd ask the kind of thing I'd ask a water therapist:",
             "I would ask a therapist about that before I booked:")
A3 = list(d17['A3']['paragraphs'])
A3[0] = swap(A3[0], "Maybe physical pain is what brought you here in the first place. If yours has lasted months,",
             "If your pain has lasted months,")
out = []
for a in json.loads((D / 'ADDITIONS-18.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1': a['paragraphs'] = A1; a['draft'] = 19
    if a['id'] == 'A3': a['paragraphs'] = A3; a['draft'] = 19
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-19.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-8.json').read_text(encoding='utf-8'))
IC['IC1']['add'] = swap(IC['IC1']['add'], "The therapist has you picture them stepping into that memory as the adult you needed back then, until you learn to be that adult yourself.",
                        "The therapist steps into the memory as the ideal adult, protecting and nurturing your inner child, until you learn to do that yourself.")
IC['IC1']['note'] = IC['IC1'].get('note', '') + '; the second sentence is in his own words from his Imagery Rescripting version of 2026-11-27 ("they step in as the ideal adult, protecting and nurturing your inner child. Then you learn to do that yourself.")'
IC['IC2']['add'] = ("If the tests keep coming back normal while that investigation goes on, I'd also try one of the two talk "
                    "therapies I go into in [my somatic guide](https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit), "
                    "Pain Reprocessing Therapy or Emotional Awareness and Expression Therapy. They both treat the pain as real, "
                    "and they've helped people with long-lasting back, muscle and joint pain.")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-9.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts19-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], [len(plain(p).split()) for p in a['paragraphs']])
print('IC1', len(IC['IC1']['add_plain'].split()), 'IC2', len(IC['IC2']['add_plain'].split()))
