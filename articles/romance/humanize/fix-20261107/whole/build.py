#!/usr/bin/env python3
"""Build the fixed version's files from PLAN.json (assemble.py) and LIVE-CHANGED.json (the live words of every changed
paragraph, copied from the post page and checked against LIVE-INDEX.txt's fingerprints):
  CHANGE-MAP.json and CHANGE-MAP.md  each change: the check that read it, the live words, the new words;
  REPLACEMENTS.json                  for the draft builder in the browser: live paragraph -> its new paragraphs
                                     (a run of n live paragraphs changed into n new ones goes one to one, so a list item
                                     stays a list item; otherwise the first live paragraph takes all the new ones and the
                                     rest go);
  ORIGINAL-CHANGED.md, REWRITE-CHANGED.md  the changed paragraphs only, under one heading per change, for the reads."""
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
P = json.load(open(HERE / 'PLAN.json', encoding='utf-8'))
LIVE = {int(k): v for k, v in json.load(open(HERE / 'LIVE-CHANGED.json', encoding='utf-8')).items()}
idx = {int(l.split()[0]): l.split()[2] for l in (HERE / 'LIVE-INDEX.txt').read_text(encoding='utf-8').splitlines()}
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
for i, t in LIVE.items():
    assert hashlib.sha256(norm(t).encode('utf-8')).hexdigest()[:12] == idx[i], i
LINKS = {}
for line in (HERE.parents[1] / 'pangram-ledger.jsonl').read_text(encoding='utf-8').splitlines():
    d = json.loads(line)
    if d.get('type') == 'result' and d.get('link'):
        LINKS[d['prediction']] = d['link']

repl, cmap = {}, []
for n, o in enumerate(P['ops'], 1):
    assert o['op'] == 'replace', o
    lv, nw = o['live'], o['new']
    if len(lv) == len(nw):
        for a, b in zip(lv, nw):
            repl[a] = [b]
    else:
        repl[lv[0]] = nw
        for a in lv[1:]:
            repl[a] = []
    cmap.append({'n': n, 'check': o['check'], 'section': o['name'], 'result': LINKS.get(o['check'], ''),
                 'live_paragraphs': lv, 'live': [LIVE[i] for i in lv], 'new': nw})
# His answers as a layer over the checks' replacements (r30/HIS-T4.json, his Medium page of 2026-11-22): each of his
# versions replaces the paragraph its card showed; his three rewritten runs and his merge of 76 and 77 replace their
# live paragraphs whole. The live words of every paragraph he changed come from the post copy of 2026-11-22
# (live-check/LIVE-POST-BLOCKS-20261122.jsonl), checked against LIVE-INDEX.txt like the rest.
json.dump({str(k): v for k, v in sorted(repl.items())}, open(HERE / 'REPLACEMENTS-CHECKS.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)   # the checks' replacements alone, which the layers are made against
LAYERS = [HERE.parent / 'r30' / 'HIS-T4.json', HERE.parent / 'r31' / 'HIS-T5.json', HERE.parent / 'r33' / 'MINE-R33.json', HERE.parent / 'r33' / 'HIS-FLAWS.json']
POST = {}
for line in (HERE.parent / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r.get('n') is not None:
        POST[r['n']] = r
SECTION = {}
_head = ''
for line in (HERE.parent / 'live-check' / 'LIVE-POST-BLOCKS-20261123.jsonl').read_text(encoding='utf-8').splitlines():
    r = json.loads(line)
    if r['tag'] in ('H1', 'H2', 'H3', 'H4'):
        _head = r['text']
    if r.get('n') is not None:
        SECTION[r['n']] = _head
for layer in LAYERS:
    if not layer.exists():
        continue
    L = json.load(open(layer, encoding='utf-8'))
    for ch in L['changes']:
        if ch['kind'] == 'run':
            lv = ch['live']
            repl[lv[0]] = list(ch['after'])
            for a in lv[1:]:
                repl[a] = []
            for c in cmap:
                if set(c['live_paragraphs']) <= set(lv):
                    c['superseded_by'] = ch['card']
                elif set(c['live_paragraphs']) & set(lv):
                    c['partly_superseded_by'] = ch['card']
        else:
            lv = [ch['live']]
            cur = repl.get(ch['live'])
            if cur is None:
                repl[ch['live']] = list(ch['after'])
            else:
                k = cur.index(ch['before'])
                repl[ch['live']] = cur[:k] + list(ch['after']) + cur[k + 1:]
        for a in lv:
            if a not in LIVE:
                LIVE[a] = POST[a]['text']
                assert hashlib.sha256(norm(LIVE[a]).encode('utf-8')).hexdigest()[:12] == idx[a], a
        cmap.append({'n': len(cmap) + 1, 'check': ('my tested change %s (%s)' if L.get('whose') == 'mine' else 'his answer %s (%s)') % (ch['card'], layer.name),
                     'section': SECTION.get(lv[0], ''), 'result': (ch.get('his_checks') or [''])[-1],
                     'live_paragraphs': lv, 'live': [LIVE[a] for a in lv], 'new': list(ch['after']),
                     'before_in_fixed': ch.get('before', '')})
    json.dump({str(k): v for k, v in sorted(LIVE.items())}, open(HERE / 'LIVE-CHANGED.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
json.dump({str(k): v for k, v in sorted(repl.items())}, open(HERE / 'REPLACEMENTS.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump(cmap, open(HERE / 'CHANGE-MAP.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
md = ['# The fixed version: every changed paragraph', '',
      'The live post ("Romance Advice I Wish My Parents Taught Me") with each section\'s and spot\'s best tested text in '
      'place (`assemble.py`, `build.py`), and his own versions from his answers over them (`../r30/HIS-T4.json`, his '
      'Medium page of 2026-11-22). Paragraph numbers are the post page\'s paragraph list (`LIVE-INDEX.txt`). '
      '"Two Pillars" 332 is his own new version (it was the owner lock). %d changes, %d live paragraphs changed.' % (
          len(cmap), len(repl)), '']
for c in cmap:
    md += ['## %d. %s (live %s)%s' % (c['n'], c['section'], ', '.join(map(str, c['live_paragraphs'])),
                                    ' (replaced by %s)' % c['superseded_by'] if c.get('superseded_by') else
                                    ' (partly replaced by %s)' % c['partly_superseded_by'] if c.get('partly_superseded_by') else ''), '',
           'Read by %s%s.' % (c['check'], (': [result](%s)' % c['result']) if c['result'] else ''), '', '**Live:**', '']
    md += ['> ' + t for t in c['live'] for _ in [0]]
    md += ['', '**New:**', '']
    md += ['> ' + t for t in c['new']]
    md += ['']
(HERE / 'CHANGE-MAP.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
orig, new = ['# Changed paragraphs: the live post', ''], ['# Changed paragraphs: the fixed version', '']
for c in cmap:
    h = '## %d. %s (live %s)' % (c['n'], c['section'], ', '.join(map(str, c['live_paragraphs'])))
    orig += [h, ''] + sum([[t, ''] for t in c['live']], [])
    new += [h, ''] + sum([[t, ''] for t in c['new']], [])
(HERE / 'ORIGINAL-CHANGED.md').write_text('\n'.join(orig), encoding='utf-8')
(HERE / 'REWRITE-CHANGED.md').write_text('\n'.join(new), encoding='utf-8')
# sizes of the whole fixed text, paragraph by paragraph, for the split of the draft at a top heading
content = P['content']
H1 = [2, 11, 43, 104, 193, 252, 313, 330, 341, 370, 406, 420, 427, 448]
total, before = 0, {}
for (i, tag, h) in content:
    for b in H1:
        if i >= b and b not in before:
            before[b] = total
    texts = repl.get(i, None)
    t = (LIVE[i] if i in LIVE else None)
    if texts is None:
        total += -1  # placeholder: the live length comes from the page (lengths not stored here)
    else:
        total += sum(len(x) for x in texts)
print('changes', len(cmap), 'replacement keys', len(repl))
print('new text of changed paragraphs: %d chars; live: %d chars' % (sum(len(x) for c in cmap for x in c['new']),
                                                                   sum(len(x) for c in cmap for x in c['live'])))
