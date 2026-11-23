#!/usr/bin/env python3
"""Write RESULTS.md for the Self-Hypnosis guide's contents test (step 2 of the contents lane's method,
work/toc-long-articles-20261122/README.md): how fresh readers found their way with the contents as the sidebar shows
it today, and which headings they called hard.

  python3 score_reads.py && python3 make_results.py
"""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', '..', 'tools', 'humanization'))
import toc_sidebar as ts

GH = 'https://github.com/u-dont-existDOTcom/joel-articles/blob/main/articles/inner-signal/experiments/toc-20261123/'
POST = 'https://ibogaqueen.substack.com/p/guide-to-self-hypnosis-and-app-including'


def main():
    S = json.load(open(os.path.join(HERE, 'SCORES.json'), encoding='utf-8'))
    C = json.load(open(os.path.join(HERE, 'CONTENTS-NOW.json'), encoding='utf-8'))
    lines = {n['n']: n['id'] for n in json.load(open(os.path.join(HERE, 'LINES-NOW.json')))}
    by_id = {e['id']: e for e in C}
    key = json.load(open(os.path.join(HERE, S['key']), encoding='utf-8'))['situations']
    sit = {m.group(1): m.group(2) for m in re.finditer(r'^(\d+)\. (.+)$', open(os.path.join(HERE, 'SITUATIONS.md'),
                                                                                  encoding='utf-8').read(), re.M)}
    n = len(key)
    out = ['# Self-Hypnosis guide: the contents test (2026-11-23)', '',
           'Step 2 of the contents lane ([the method and order](https://github.com/u-dont-existDOTcom/joel-articles/blob/'
           'main/work/toc-long-articles-20261122/README.md)), on [the live post](%s) as last updated on 2026-11-20 '
           '(v. 7.0): 165 sections, 164 of them listed in the contents sidebar, %d cut off with "…", 29,554 words.' % (
               POST, sum(1 for e in C if not ts.shown(e['heading'], e['level'])[0])), '',
           '%d situations, each a reader looking for one thing, were written by an agent that saw only the text with its '
           'headings taken out ([situations](%sSITUATIONS.md)); a second agent checked the answer key against the whole '
           'text ([key](%s%s)). Fresh readers then saw only the contents ([as the sidebar shows it](%sTOC-NOW-SIDEBAR.md), '
           'or [with whole headings](%sTOC-NOW-FULL.md)) and said where they would look first ([brief](%sBRIEF.md)).' % (
               n, GH, GH, S['key'], GH, GH, GH), '',
           '| Read | Contents | Right on first try (of %d) | Near (its parent) | Wrong | Guessed | Found in two tries |' % n,
           '|---|---|---|---|---|---|---|']
    for f, r in S['reads'].items():
        t = r['tally']
        name = re.match(r'READ-(.+)-(\d+)\.md$', f)
        what = {'NOW-SIDEBAR': 'as the sidebar shows it', 'NOW-FULL': 'whole headings'}.get(name.group(1), name.group(1))
        out.append('| [%s](%sreads/%s) | %s | %d | %d | %d | %d | %d |' % (f[:-3], GH, f, what, t['right'], t['near'],
                                                                        t['wrong'], t['guess'], t['found']))
    # the situations most readers missed, with where they looked
    side = [r for f, r in S['reads'].items() if 'SIDEBAR' in f]
    miss = []
    for k in key:
        kinds = [r['per'].get(k, {}).get('kind') if isinstance(r['per'].get(k), dict) else 'missing' for r in side]
        if kinds.count('right') < len(side):
            firsts = [r['per'][k]['first'] for r in side if isinstance(r['per'].get(k), dict)]
            miss.append((kinds.count('right'), k, firsts))
    miss.sort(key=lambda x: (x[0], int(x[1])))
    out += ['', '## Situations the sidebar readers missed', '',
            'Situation, the section the key gives, and where each sidebar reader looked first.', '',
            '| # | Situation | Right section | First picks |', '|---|---|---|---|']
    for right, k, firsts in miss:
        want = key[k]['right']
        out.append('| %s | %s | %s | %s |' % (k, sit.get(k, ''), ', '.join('%s (%s)' % (by_id[i]['heading'], i)
                                                                         for i in want if i in by_id),
                                              ', '.join(('%s (%s)' % (by_id[i]['heading'], i)) if i in by_id else '?'
                                                        for i in firsts)))
    # the hard headings, counted over every read
    hard = collections.defaultdict(list)
    for f in S['reads']:
        for m in re.finditer(r'^\s*[-*]?\s*`?HARD:\s*(\d+)\s*\|\s*(.+?)`?\s*$', open(os.path.join(HERE, 'reads', f),
                                                                                   encoding='utf-8').read(), re.M):
            sid = lines.get(int(m.group(1)))
            if sid:
                hard[sid].append((f[:-3], m.group(2).strip()))
    out += ['', '## Headings the readers called hard', '',
            'Each heading with how many reads called it hard, how the sidebar shows it, and one reader\'s reason.', '',
            '| Section | Heading | Sidebar | Reads | One reason |', '|---|---|---|---|---|']
    for sid, rs in sorted(hard.items(), key=lambda x: (-len(x[1]), x[0])):
        e = by_id[sid]
        fits, shown = ts.shown(e['heading'], e['level'])[:2]
        out.append('| %s | %s %s | %s | %d | %s |' % (sid, '#' * e['level'], e['heading'],
                                                      'fits' if fits else 'cut: "%s"' % shown, len(rs),
                                                      rs[0][1].replace('|', '/')))
    open(os.path.join(HERE, 'RESULTS.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('RESULTS.md: %d reads, %d situations missed by a sidebar reader, %d headings called hard' % (
        len(S['reads']), len(miss), len(hard)))


if __name__ == '__main__':
    main()
