#!/usr/bin/env python3
"""diffs.py - each pair as a word diff ([-what went-]{+what he put+}), for reading them one by one. Writes DIFFS.md.

  python3 diffs.py [LANE ...]
"""
import difflib, json, pathlib, re, sys
HERE = pathlib.Path(__file__).resolve().parent
D = json.loads((HERE / 'PAIRS.json').read_text(encoding='utf-8'))['kept']
S = json.loads((HERE / 'SERIES.json').read_text(encoding='utf-8'))


def wdiff(a, b):
    ta, tb = re.findall(r'\S+|\n', a), re.findall(r'\S+|\n', b)
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append(' '.join(ta[i1:i2]))
        else:
            if i2 > i1:
                out.append('[-' + ' '.join(ta[i1:i2]) + '-]')
            if j2 > j1:
                out.append('{+' + ' '.join(tb[j1:j2]) + '+}')
    return re.sub(r' ?\n ?', '\n', ' '.join(out))


lanes = sys.argv[1:]
md = ['# His fixes, word by word', '']
n = 0
for p in D:
    if lanes and p['lane'] not in lanes:
        continue
    n += 1
    md += ['## %d. %s %s (%s): %s' % (n, p['lane'], p['id'], p['type'], (p['title'] or '')[:80]), '',
           '`%s`, %d words to %d, shared %.2f' % (p['file'], p['words_before'], p['words_his'], p['shared']), '']
    if p['comment']:
        md += ['His comment: %s' % p['comment'][:600].replace('\n', ' / '), '']
    md += [wdiff(p['before'], p['his']), '']
if not lanes or 'bad-trips' in lanes:
    for k, v in S.items():
        prev = v.get('mine_he_started_from') or v['before']
        for t in v['tries']:
            n += 1
            md += ['## %d. bad-trips %s, his try %s (%s): %s' % (n, k, t['id'], t['reading'], t['note'][:120]), '',
                   wdiff(prev, t['text']), '']
            prev = t['text']
(HERE / ('DIFFS%s.md' % ('-' + '-'.join(lanes) if lanes else ''))).write_text('\n'.join(md) + '\n', encoding='utf-8')
print(n, 'diffs')
