#!/usr/bin/env python3
"""Draft 11 of the somatic additions: A1 from the draft-10 reads (P2 reworded; Affect Phobia kept word for word as its
own paragraph, the near miss's Human High sentence; Accelerated Experiential Dynamic Psychotherapy its own paragraph,
rewritten; the booking question asks about being read wrong), A3 as draft 9 plus "though real", and the inner child
sentences' third draft. Writes ADDITIONS-11.json, INNER-CHILD-ADDS-3.json and reads/drafts11-numbered.txt."""
import hashlib, json, pathlib, re, sys

D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-10.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
ISTDP = 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and'
APT = 'https://psykologtidsskriftet.no/node/15971/pdf'
AEDP = 'https://www.apa.org/pubs/videos/4310759'

A1 = [
    by['A1']['paragraphs'][0],
    "The therapist also watches for signs of the anxiety that's making you slip away, like tense muscles, sighing, or "
    "your thinking going foggy. Most people who try this therapy can't take much of that anxiety, so they get a slower "
    "version, where the therapist stops to help them settle whenever it climbs.",
    "If it's one feeling in particular that scares you, like grief, [Affect Phobia Therapy](%s) treats that fear a lot "
    "like a phobia, getting you used to the feeling bit by bit, at a pace your anxiety can handle." % APT,
    "And if what you can't let in is kindness, when someone cares about you and it just bounces off, there's "
    "[Accelerated Experiential Dynamic Psychotherapy](%s). The therapist makes sure you don't feel alone with whatever "
    "comes up, and when some of their care does get in, they ask what that's like and where you feel it in your body."
    % AEDP,
    "As with water therapy, I'd ask before booking: \"What do you do when I start slipping away from a feeling, or get "
    "overwhelmed? And what if I think you've read me wrong?\" If the answer leaves no room for you to slow down or to "
    "disagree, keep looking.",
]
A3 = list(by['A3']['paragraphs'])
old = "you learn that the pain is a false alarm,"
assert old in A3[1]
A3[1] = A3[1].replace(old, "you learn that the pain, though real, is a false alarm,")

def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)

out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1':
        a['paragraphs'] = A1; a['draft'] = 11
    if aid == 'A3':
        a['paragraphs'] = A3; a['draft'] = 11
    text = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['text'] = text
    a['sha256'] = hashlib.sha256(text.encode('utf-8')).hexdigest()
    a['words'] = len(text.split())
    out.append(a)
(D / 'ADDITIONS-11.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

IC = json.loads((D / 'INNER-CHILD-ADDS-2.json').read_text(encoding='utf-8'))
IC['IC1']['add'] = ("If a memory feels too big to redo on your own, there's a clinical therapy for this called [Imagery "
                    "Rescripting](https://ibogaqueen.substack.com/i/201523223/imagery-rescripting), where a therapist "
                    "steps into the memory with you as the adult you needed, until you learn to do that yourself.")
IC['IC2']['add'] = ("If the tests keep coming back normal, you might look into Pain Reprocessing Therapy and Emotional "
                    "Awareness and Expression Therapy while the investigation goes on. Both treat the pain as real, and in "
                    "trials they've helped people with chronic back pain and other muscle and joint pain. (For more on "
                    "both, check [my somatic guide](https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit).)")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-3.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

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
(D / 'reads' / 'drafts11-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('\n'.join(lines))
for a in out:
    print(a['id'], a['words'], a['sha256'][:12], [len(plain(p).split()) for p in a['paragraphs']])
