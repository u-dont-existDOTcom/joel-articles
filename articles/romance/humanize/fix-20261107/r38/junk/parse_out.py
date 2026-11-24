#!/usr/bin/env python3
"""Read the junk pass writer's OUT.md: each item's rewritten flagged paragraphs, put back in their section (r38/checks).
Writes texts/<key>.txt (the section with the rewrites, the check text) and DIFF.json (each item's changed sentences, old
and new, the writer's JUDGED and MEANING lines, and any sentence it changed that nobody flagged)."""
import json
import pathlib
import re
import difflib

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
out = (HERE / 'OUT.md').read_text(encoding='utf-8')
ITEMS = json.loads((HERE / 'ITEMS.json').read_text(encoding='utf-8'))
SPLIT = re.compile(r'(?<=[.!?…”"])\s+(?=[A-Z“"(])')
sents = lambda t: [s.strip() for p in t.split('\n\n') for s in SPLIT.split(p.strip()) if s.strip()]
by_key = {}
for it in ITEMS:
    by_key.setdefault(it['key'], []).append(it)
blocks = re.split(r'^## Item (\d+) \(([^)]+)\)\s*$', out, flags=re.M)
diff, problems = {}, []
for i in range(1, len(blocks), 3):
    key, block = blocks[i + 1].strip(), blocks[i + 2]
    judged = block.split('JUDGED:', 1)[1].split('REWRITE:', 1)[0].strip()
    rw = block.split('REWRITE:', 1)[1].split('MEANING:', 1)[0].strip()
    meaning = block.split('MEANING:', 1)[1].strip() if 'MEANING:' in block else ''
    orig = (FIX / 'r38' / 'checks' / ('CHECK-%s.txt' % key)).read_text(encoding='utf-8').strip()
    paras = orig.split('\n\n')
    new_paras = [p.strip() for p in rw.split('\n\n') if p.strip() and not p.strip().startswith('(')]
    text = list(paras)
    for np_ in new_paras:
        # the paragraph it rewrites: the flagged paragraph it overlaps most
        flagged = [j for j, p in enumerate(paras) if any(it['paragraph'] == p for it in by_key[key])]
        best = max(flagged, key=lambda j: difflib.SequenceMatcher(a=paras[j], b=np_, autojunk=False).ratio())
        text[best] = np_
    t = '\n\n'.join(text)
    (HERE / 'texts').mkdir(exist_ok=True)
    (HERE / 'texts' / ('%s.txt' % key)).write_text(t, encoding='utf-8')
    so, sn = sents(orig), sents(t)
    gone = [s for s in so if s not in sn]
    new = [s for s in sn if s not in so]
    marks = [m for it in by_key[key] for m in it['marks']]
    unmarked = [s for s in gone if not any(m in s or s in m for m in marks)]
    diff[key] = {'items': [it['id'] for it in by_key[key]], 'heading': by_key[key][0]['heading'], 'gone': gone, 'new': new,
                 'unmarked_changed': unmarked, 'judged': judged, 'meaning': meaning,
                 'words': [len(orig.split()), len(t.split())]}
(HERE / 'DIFF.json').write_text(json.dumps(diff, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, d in diff.items():
    print('%s %s: %d gone, %d new, words %d -> %d%s' % (k[:34], ','.join(d['items']), len(d['gone']), len(d['new']),
          d['words'][0], d['words'][1], ', UNFLAGGED %d' % len(d['unmarked_changed']) if d['unmarked_changed'] else ''))
missing = set(by_key) - set(diff)
if missing:
    print('NOT IN OUT.md:', sorted(missing))
