#!/usr/bin/env python3
"""Draft 12: the draft-11 reads acted on (A1-P2 keeps the reader in and names anxiety as the cause; A1-P4's "works to
keep you from feeling alone"; A3-S3 split so "partly by" can't hang on the brain; IC1 first/later; IC2 says what kind of
thing the two are and the trials' scope)."""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-11.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
A1 = list(by['A1']['paragraphs'])
A1[1] = ("It's usually anxiety that makes you slip away, so the therapist also watches for its signs, like tense muscles, "
         "sighing, or your thinking going foggy, to tell when it's getting to be too much for you. If you can only handle a "
         "little of that anxiety, like most people who try this therapy, you'd get a slower version, where the therapist "
         "stops to help you settle whenever it climbs.")
old = "The therapist makes sure you don't feel alone with whatever comes up"
assert old in A1[3]
A1[3] = A1[3].replace(old, "The therapist works to keep you from feeling alone with whatever comes up")
A3 = list(by['A3']['paragraphs'])
old3 = ("you learn that the pain, though real, is a false alarm, your brain signaling danger where there isn't any, partly "
        "by paying close attention to how it feels in your body.")
assert old3 in A3[1], A3[1]
A3[1] = A3[1].replace(old3, "you learn that the pain, though real, is a false alarm, your brain signaling danger where there "
                            "isn't any. Part of how you learn it is by paying close attention to how the pain feels in your body.")
def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1':
        a['paragraphs'] = A1; a['draft'] = 12
    if aid == 'A3':
        a['paragraphs'] = A3; a['draft'] = 12
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest()
    a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-12.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
IC = json.loads((D / 'INNER-CHILD-ADDS-3.json').read_text(encoding='utf-8'))
IC['IC1']['add'] = ("If a memory feels too big to redo on your own, there's a clinical therapy for this called [Imagery "
                    "Rescripting](https://ibogaqueen.substack.com/i/201523223/imagery-rescripting), where a therapist first "
                    "steps into the memory as the adult you needed, and later you learn to be that adult yourself.")
IC['IC2']['add'] = ("While the investigation goes on and the tests keep coming back normal, you might look into two talk "
                    "therapies, Pain Reprocessing Therapy and Emotional Awareness and Expression Therapy. Both treat the pain "
                    "as real, and in trials they've helped people with mild to moderate chronic back pain and with other "
                    "long-lasting muscle and joint pain. (For more on both, check [my somatic guide]"
                    "(https://ibogaqueen.substack.com/i/201523223/pain-that-wont-quit).)")
for k, v in IC.items():
    v['add_plain'] = plain(v['add'])
    v['sha256_pair'] = hashlib.sha256((v['his_before'] + '\n\n' + v['add_plain']).encode('utf-8')).hexdigest()
(D / 'INNER-CHILD-ADDS-4.json').write_text(json.dumps(IC, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
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
(D / 'reads' / 'drafts12-numbered.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], a['words'], a['sha256'][:12], [len(plain(p).split()) for p in a['paragraphs']])
for k, v in IC.items():
    print(k, len(v['add_plain'].split()))
