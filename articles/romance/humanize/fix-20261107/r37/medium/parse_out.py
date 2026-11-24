#!/usr/bin/env python3
"""Read the Medium pass writer's OUT.md: each item's rewrite of its section, checked against the section as the fixed
version has it (r36/checks), sentence by sentence. Writes texts/<key>.txt (the rewritten section, the check text) and
DIFF.json (each item's changed sentences, old and new, with whose words each old one was: HIS for his page versions).
A rewrite that changed a sentence nobody marked is listed, so it can be looked at before anything goes to Pangram."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
FIX = HERE.parents[1]
out = (HERE / 'OUT.md').read_text(encoding='utf-8')
paras = (HERE / 'PARAS.md').read_text(encoding='utf-8')
SPLIT = re.compile(r'(?<=[.!?…”"])\s+(?=[A-Z“"(])')


def sentences(t):
    return [s.strip() for p in t.split('\n\n') for s in SPLIT.split(p.strip()) if s.strip()]


items = re.split(r'^## Item (\d+) \(([^)]+)\)\s*$', out, flags=re.M)
marked = {}
for m in re.finditer(r'^## Item (\d+) \(([^)]+)\)\n\nSection: (.*?)\n\n(.*?)(?=^## Item |\Z)', paras, flags=re.M | re.S):
    body = m.group(4)
    marks = re.findall(r'\[\[(MEDIUM \((?:HIS|MODEL)\)|FLAG): (.*?)(?: \|\| .*?)?\]\]', body, flags=re.S)
    marked[m.group(2)] = {'heading': m.group(3), 'marks': marks}
diff, problems = {}, []
for i in range(1, len(items), 3):
    key, block = items[i + 1], items[i + 2]
    rw = block.split('REWRITE:\n', 1)[1].split('\nCHANGES:', 1)[0].strip()
    orig = (FIX / 'r36' / 'checks' / ('CHECK-%s.txt' % key)).read_text(encoding='utf-8').strip()
    (HERE / 'texts').mkdir(exist_ok=True)
    (HERE / 'texts' / ('%s.txt' % key)).write_text(rw, encoding='utf-8')
    so, sn = sentences(orig), sentences(rw)
    gone = [s for s in so if s not in sn]
    new = [s for s in sn if s not in so]
    marks = marked[key]['marks']
    his_marked = [t for tag, t in marks if 'HIS' in tag]
    unmarked = [s for s in gone if not any(t.strip() in s or s in t for _, t in marks)]
    if orig.count('\n\n') != rw.count('\n\n'):
        problems.append('%s: paragraphs %d -> %d' % (key, orig.count('\n\n') + 1, rw.count('\n\n') + 1))
    diff[key] = {'heading': marked[key]['heading'], 'gone': gone, 'new': new, 'unmarked_changed': unmarked,
                 'his_touched': [s for s in gone if any(t.strip() in s or s in t for t in his_marked)],
                 'words': [len(orig.split()), len(rw.split())]}
(HERE / 'DIFF.json').write_text(json.dumps(diff, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
for k, d in diff.items():
    print('%s: %d gone, %d new, words %d -> %d%s%s' % (k, len(d['gone']), len(d['new']), d['words'][0], d['words'][1],
          ', his touched %d' % len(d['his_touched']) if d['his_touched'] else '',
          ', UNMARKED %d' % len(d['unmarked_changed']) if d['unmarked_changed'] else ''))
for p in problems:
    print('PROBLEM', p)
