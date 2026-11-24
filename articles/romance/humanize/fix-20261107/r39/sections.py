#!/usr/bin/env python3
"""r39 (a copy of r38/sections.py that writes to r39/checks and refuses to write over them without --again): the current cut, and the sections whose text now is not one a check read (his cards still to answer, or new). The recheck after r33 to r36 (one per changed section, docs/PANGRAM-PRODUCTION-BUDGET-20261020.md): r32's cut of
whole/FIXED.md as it stands now, written to r36/checks, and the sections whose text differs from r32's listed in
CHANGED.json. r32's description follows.
Every section of the fixed version by itself (gate E307; lesson romance-2026-11-22c): whole/FIXED.md cut at every
heading, each section's paragraphs as one check text (links as their words, notes out), a section of more than six
paragraphs or 600 words in parts of at most six paragraphs (his "a section check of about 5-6 paragraphs in the GUI is
fine"), and a section under 50 words with the next one. Writes checks/CHECK-<key>.txt and SECTIONS.json."""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
import sys
if (HERE / 'checks').exists() and '--again' not in sys.argv:
    sys.exit('r39/checks exists: these are the check texts of this round; run with --again to write over them')
(HERE / 'checks').mkdir(exist_ok=True)
md = (HERE.parent / 'whole' / 'FIXED.md').read_text(encoding='utf-8')
blocks = [b.strip() for b in re.split(r'\n\s*\n', md) if b.strip()]
vis = lambda b: re.sub(r'<!--.*?-->', '', b, flags=re.S).strip()
plain = lambda t: re.sub(r'\[([^\]]+)\]\((?:[^()\s]|\([^()\s]*\))+\)', r'\1', t)
secs, cur = [], None
for b in blocks:
    v = vis(b)
    if not v:
        continue
    if v.startswith('#'):
        cur = {'heading': v.lstrip('#').strip(), 'paras': []}
        secs.append(cur)
        continue
    if cur is None:
        cur = {'heading': '(the opening)', 'paras': []}
        secs.append(cur)
    cur['paras'].append(plain(v[2:] if v.startswith('- ') else v))
secs = [s for s in secs if s['paras']]
# a section under 50 words goes with the next one
merged = []
for s in secs:
    if merged and sum(len(p.split()) for p in merged[-1]['paras']) < 50:
        merged[-1] = {'heading': merged[-1]['heading'] + ' + ' + s['heading'], 'paras': merged[-1]['paras'] + s['paras']}
    else:
        merged.append(dict(s))
checks = []
for s in merged:
    ps = s['paras']
    words = sum(len(p.split()) for p in ps)
    if len(ps) <= 6 and words <= 600:
        parts = [ps]
    else:
        n = -(-len(ps) // 6)
        size = -(-len(ps) // n)
        parts = [ps[i:i + size] for i in range(0, len(ps), size)]
    for k, part in enumerate(parts, 1):
        slug = re.sub(r'[^a-z0-9]+', '-', s['heading'].lower()).strip('-')[:40]
        key = 'r39-%02d-%s%s' % (len(checks) + 1, slug, ('-p%d' % k) if len(parts) > 1 else '')
        text = '\n\n'.join(part)
        (HERE / 'checks' / ('CHECK-%s.txt' % key)).write_text(text, encoding='utf-8')
        checks.append({'key': key, 'heading': s['heading'], 'part': k, 'parts': len(parts), 'paragraphs': len(part),
                       'words': len(text.split()), 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()})
(HERE / 'SECTIONS.json').write_text(json.dumps(checks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
old = {(c['heading'], c['part'], c['parts']): c for c in json.loads((HERE.parent / 'r32' / 'SECTIONS.json').read_text(encoding='utf-8'))}
# the latest checked text of each section's lineage, from the ledger: a section whose text now is not one Pangram read is listed
LATEST = {}
for line in (HERE.parents[1] / 'pangram-ledger.jsonl').read_text(encoding='utf-8').splitlines():
    d = json.loads(line)
    if d.get('type') == 'prediction' and (d.get('lineage') or '').startswith('romance-e307-'):
        LATEST.setdefault(d['lineage'], set()).add(d.get('sha256'))
changed = [dict(c, was=(old.get((c['heading'], c['part'], c['parts'])) or {}).get('key', '')) for c in checks
           if (old.get((c['heading'], c['part'], c['parts'])) or {}).get('sha256') != c['sha256']]
(HERE / 'CHANGED.json').write_text(json.dumps(changed, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(changed), 'changed since r32')
unread = [c['key'] for c in checks if c['sha256'] not in LATEST.get('romance-e307-%s' % c['key'][4:6], set()) and c['sha256'] != (old.get((c['heading'], c['part'], c['parts'])) or {}).get('sha256')]
print(len(unread), 'sections whose text now no check read:', ', '.join(unread))
print(len(checks), 'checks,', sum(c['words'] for c in checks), 'words; max', max(c['words'] for c in checks))
