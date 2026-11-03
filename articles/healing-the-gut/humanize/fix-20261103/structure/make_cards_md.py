#!/usr/bin/env python3
"""Write STRUCTURE-CARDS.md, the GitHub-readable copy of the structure page's cards, from STRUCTURE-SPEC.json."""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
s = json.loads((HERE / 'STRUCTURE-SPEC.json').read_text(encoding='utf-8'))
out = ['# ' + s['title'], '', 'This is the same content as the interactive structure page (Approve / Revise / Reject with a note on each), to read on GitHub.', '']
out += [p + '\n' for p in s['intro']]
groups = {g['id']: g for g in s['groups']}
for g in s['groups']:
    out += ['## ' + g['title'], '', g['intro'], '']
    for it in [i for i in s['items'] if i['group'] == g['id']]:
        out += ['### %s. %s' % (it['id'], it['title']), '', '*%s. %s*' % (it['section'], it['whose']), '']
        for b in it.get('blocks', []):
            out += ['**%s**' % b['label'], '']
            for para in b['paras']:
                out.append('> ' + ''.join(('~~%s~~' % x if m == 'del' else '**%s**' % x if m in ('mark', 'ins') else x) for x, m in para))
                out.append('')
        for f in it.get('fields', []):
            out += ['**%s**' % f['label'], '']
            if 'list' in f:
                out += ['- ' + x for x in f['list']] + ['']
            else:
                out += [f['text'], '']
        if it.get('links'):
            out += ['Pangram: ' + ', '.join('[%s](%s)' % (l['text'], l['url']) for l in it['links']), '']
        out += ['Approve: %s Reject: %s' % (it.get('approve', g['approve']), it.get('reject', g['reject'])), '']
(HERE / 'STRUCTURE-CARDS.md').write_text('\n'.join(out), encoding='utf-8')
print('ok')
