#!/usr/bin/env python3
"""Draft 13: READ-12 acted on (A1-S4 "anxiety about the feeling"; A3-S3 rests on what the doctors found; A3-S4 says
how the attention differs from the all-day noticing)."""
import hashlib, json, pathlib, re, sys, shutil
D = pathlib.Path(sys.argv[1])
prev = json.loads((D / 'ADDITIONS-12.json').read_text(encoding='utf-8'))
by = {a['id']: a for a in prev}
A1 = list(by['A1']['paragraphs'])
o = "It's usually anxiety that makes you slip away"
assert o in A1[1]; A1[1] = A1[1].replace(o, "It's usually anxiety about the feeling that makes you slip away")
A3 = list(by['A3']['paragraphs'])
o3 = ("you learn that the pain, though real, is a false alarm, your brain signaling danger where there isn't any. Part of "
      "how you learn it is by paying close attention to how the pain feels in your body.")
assert o3 in A3[1], A3[1]
A3[1] = A3[1].replace(o3, "you learn to treat the pain, though real, as a false alarm, your brain signaling danger where the "
                          "doctors haven't found any. Part of how you learn that is by paying close attention to how the pain "
                          "feels in your body without fearing it.")
def plain(t):
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
out = []
for aid in ('A1', 'A2', 'A3'):
    a = dict(by[aid])
    if aid == 'A1': a['paragraphs'] = A1; a['draft'] = 13
    if aid == 'A3': a['paragraphs'] = A3; a['draft'] = 13
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest()
    a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-13.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
for a in out:
    print(a['id'], a['words'], a['sha256'][:12], [len(plain(p).split()) for p in a['paragraphs']])
print(A1[1]); print(A3[1])
