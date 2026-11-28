#!/usr/bin/env python3
"""Draft 31 (turn of 2026-11-28 09:44 UTC), the final A1: his answer on card A1-TEACH-2 (Revise, his version of the whole
section, answers/ANSWERS-C1127B-A1-20261128-0944.json), read back from his Pangram history by its link (Human Written, one
High window over all 328 words, https://www.pangram.com/history/f8c3bc68-d6eb-4694-ba54-2671741ab8c6; its text has the same
SHA-256 as his version). The three therapy names get their links back, as the card had them; the links change no word he
checked. Everything else in ADDITIONS-29.json stays as it is (A2 and A3 are live).
  python3 articles/somatic-therapies/experiments/additions-20261126/scripts/make_draft31.py articles/somatic-therapies/experiments/additions-20261126"""
import hashlib, json, pathlib, re, sys
D = pathlib.Path(sys.argv[1])
def plain(t): return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)
ans = json.loads((D / 'answers' / 'ANSWERS-C1127B-A1-20261128-0944.json').read_text(encoding='utf-8'))
item = next(i for i in ans['items'] if i['id'] == 'A1-TEACH-2')
assert item['status'] == 'revise'
his = item['your_version']
assert hashlib.sha256(his.encode('utf-8')).hexdigest() == '2f545bb2abcdf361fbf21b9f2fe6d1f9805e800d1107eb39d758d743a6ed4fdc'
LINKS = {
    'Intensive Short-Term Dynamic Psychotherapy': 'https://psykologtidsskriftet.no/debatt/2021/09/intensive-short-term-dynamic-psychotherapy-methods-evidence-indications-and',
    'Affect Phobia Therapy': 'https://psykologtidsskriftet.no/node/15971/pdf',
    'Accelerated Experiential Dynamic Psychotherapy': 'https://www.apa.org/pubs/videos/4310759',
}
paras = his.split('\n\n')
out_paras = []
for p in paras:
    for name, url in LINKS.items():
        if p.count(name) == 1:
            p = p.replace(name, '[%s](%s)' % (name, url))
    out_paras.append(p)
assert sum(p.count('](') for p in out_paras) == 3
assert '\n\n'.join(plain(p) for p in out_paras) == his
out = []
for a in json.loads((D / 'ADDITIONS-29.json').read_text(encoding='utf-8')):
    a = dict(a)
    if a['id'] == 'A1':
        a['paragraphs'] = out_paras
        a['his'] = ('his version of the whole section, card A1-TEACH-2, answers of 2026-11-28 09:44 UTC; his check: Human '
                    'Written, one High window (https://www.pangram.com/history/f8c3bc68-d6eb-4694-ba54-2671741ab8c6)')
    a['draft'] = 31
    a['text'] = '\n\n'.join(plain(p) for p in a['paragraphs'])
    a['sha256'] = hashlib.sha256(a['text'].encode('utf-8')).hexdigest(); a['words'] = len(a['text'].split())
    out.append(a)
(D / 'ADDITIONS-31.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
a1 = next(a for a in out if a['id'] == 'A1')
print(a1['sha256'], a1['words'], 'words')
for p in a1['paragraphs']:
    print('-', p[:150])
