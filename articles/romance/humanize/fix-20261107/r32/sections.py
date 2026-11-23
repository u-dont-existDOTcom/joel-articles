#!/usr/bin/env python3
"""Every section of the fixed version by itself (gate E307; lesson romance-2026-11-22c): whole/FIXED.md cut at every
heading, each section's paragraphs as one check text (links as their words, notes out), a section of more than six
paragraphs or 600 words in parts of at most six paragraphs (his "a section check of about 5-6 paragraphs in the GUI is
fine"), and a section under 50 words with the next one. Writes checks/CHECK-<key>.txt and SECTIONS.json."""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
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
        key = 'r32-%02d-%s%s' % (len(checks) + 1, slug, ('-p%d' % k) if len(parts) > 1 else '')
        text = '\n\n'.join(part)
        (HERE / 'checks' / ('CHECK-%s.txt' % key)).write_text(text, encoding='utf-8')
        checks.append({'key': key, 'heading': s['heading'], 'part': k, 'parts': len(parts), 'paragraphs': len(part),
                       'words': len(text.split()), 'sha256': hashlib.sha256(text.encode('utf-8')).hexdigest()})
(HERE / 'SECTIONS.json').write_text(json.dumps(checks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(checks), 'checks,', sum(c['words'] for c in checks), 'words; max', max(c['words'] for c in checks))
