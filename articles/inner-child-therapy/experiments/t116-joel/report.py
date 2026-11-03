#!/usr/bin/env python3
"""Turn 116: EDITS.md from EDITS.json (compare.py): his guide in his order, each paragraph with what happened to it.

For each paragraph of his that isn't kept word for word: where it came from (the base section, and "moved" when that
isn't where it is now), each edited sentence as the base had it and as he has it (a word diff: [-cut-] {+added+}), each
new sentence, and the sentences of its base paragraph that he cut. Then the base sections whose paragraphs went
nowhere, and the outline of both versions side by side.

  python3 report.py"""
import difflib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
E = json.loads((HERE / 'EDITS.json').read_text(encoding='utf-8'))


def wdiff(a, b):
    aw, bw = a.split(), b.split()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, aw, bw, autojunk=False).get_opcodes():
        if op == 'equal':
            out.append(' '.join(aw[i1:i2]))
        if op in ('delete', 'replace'):
            out.append('[-' + ' '.join(aw[i1:i2]) + '-]')
        if op in ('insert', 'replace'):
            out.append('{+' + ' '.join(bw[j1:j2]) + '+}')
    return ' '.join(out)


def main():
    J, BS, PARAS, BB = E['joel'], E['base'], E['paragraphs'], E['base_blocks']
    by_block = {}
    for r in J:
        by_block.setdefault(r['block'], []).append(r)
    cut_by_block = {}
    for s in BS:
        if not s['used'] and s['src'] == 'base' and s['kind'] == 'p':
            cut_by_block.setdefault(s['block'], []).append(s['text'])
    used_homes = set()
    lines = ['# What his edits and reorganization did (turn 116)', '',
             'His guide in his order. Each paragraph that isn\'t kept word for word shows where it came from, each edited '
             'sentence as a word diff ([-cut-] {+added+}), each new sentence (+), and the sentences of its base paragraph '
             'he cut (-). Counts: %s.' % json.dumps(E['counts']), '']
    pmap = {p['block']: p for p in PARAS}
    for j, b in enumerate(E['joel_blocks']):
        if b['kind'] == 'h':
            hr = by_block.get(j, [{}])[0]
            mark = {'KEPT': '', 'EDITED': ' (heading reworded: %s)' % (BS[hr['match']]['text'] if hr.get('match') is not None else ''),
                    'NEW': ' (new heading)'}.get(hr.get('fate'), '')
            lines += ['', '#' * min(b['path'].__len__() + 1, 6) + ' ' + b['text'] + mark, '']
            continue
        p = pmap[j]
        rs = by_block.get(j, [])
        home = p['home']
        for h in p['sources']:
            used_homes.add(h)
        fates = p['fates']
        if fates.get('KEPT', 0) == len(rs) and not p['moved'] and not cut_by_block.get(home):
            continue
        where = ('from "%s"%s' % (' > '.join(p['home_path'][-2:]), ' (MOVED)' if p['moved'] else '')) if home is not None else 'all new'
        lines.append('**P%d**, %s; %s' % (j, where, ', '.join('%s %d' % kv for kv in sorted(fates.items()))))
        for r in rs:
            if r['fate'] == 'EDITED':
                lines.append('  ~ ' + wdiff(BS[r['match']]['text'], r['text']))
            elif r['fate'] == 'NEW':
                lines.append('  + ' + r['text'])
        for h in p['sources']:
            for c in cut_by_block.get(h, []):
                lines.append('  - ' + c)
            cut_by_block.pop(h, None)
        lines.append('')
    # base paragraphs whose cut sentences weren't shown under any of his paragraphs
    rest = [(h, cs) for h, cs in cut_by_block.items() if cs]
    lines += ['', '## Cut, from paragraphs none of his paragraphs came from (%d paragraphs)' % len(rest), '']
    for h, cs in sorted(rest):
        lines.append('**base P%d**, "%s"' % (h, ' > '.join(BB[h]['path'][-2:])))
        for c in cs:
            lines.append('  - ' + c)
        lines.append('')
    (HERE / 'EDITS.md').write_text('\n'.join(lines).rstrip('\n') + '\n', encoding='utf-8')
    print('wrote EDITS.md', len(lines), 'lines')


if __name__ == '__main__':
    main()
