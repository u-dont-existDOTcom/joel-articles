#!/usr/bin/env python3
"""summarize.py - the counts in HOW-HE-FIXES.md, from the five annotation files (ANNOT-BT.json, my read of the bad-trips
fixes; ANNOT-A to D.json, four fresh readers' reads of the other lanes' fixes, each given BRIEF.md). Prints the table.

  python3 summarize.py
"""
import collections, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
NAMES = {
    'A': 'A list unpacked: each item its own clause, with what happens or what to do',
    'B': 'A correction or contrast frame removed ("does not mean X; it means Y", "rather than", "not X but Y")',
    'C': 'A repeated sentence shape broken: items built different ways, with different connectors',
    'D': 'Bare commands joined to their reason ("They\'re feeling overwhelmed, so dim the lights")',
    'E': 'A referent made exact: who, to what, what counts ("hurt somebody" to "hurt themselves")',
    'F': 'A term explained right where it is used, or the plain word for jargon',
    'G': 'A quip, aphorism, thesis or summing-up line cut, or replaced by the thing to do',
    'H': 'The reader made the one who acts or thinks ("We can use the same Hunter criteria that clinicians use")',
    'I': 'His own stance, story or example added',
    'J': 'A hedge or slack added ("maybe don\'t", "you can still change your mind")',
    'K': 'Normal versus danger said, with its limit ("not just regular sweating", "up to a point")',
    'L': 'A spoken register: contractions, "for that matter", "go ahead and", "So"',
    'M': 'Something cut as unneeded or said twice',
    'N': 'Something added that the reader needed (a missing step, case, reason or fact)',
    'O': 'Other (word choice, punctuation, joins, order: listed in the annotation files)',
}
files = ['ANNOT-BT.json', 'ANNOT-A.json', 'ANNOT-B.json', 'ANNOT-C.json', 'ANNOT-D.json']
rows = [e for f in files for e in json.loads((HERE / f).read_text(encoding='utf-8'))]
made, biggest = collections.Counter(), collections.Counter()
for e in rows:
    for c in set(k[0] for k in (e.get('codes') or {})):
        made[c] += 1
    if e.get('other'):
        made['O'] += 1
    b = (e.get('biggest') or ' ')[0]
    if b in NAMES:
        biggest[b] += 1
print('%d fixes read' % len(rows))
print('| what he changed | in how many of the %d fixes | the biggest change in |' % len(rows))
print('|---|---|---|')
for c, n in sorted(made.items(), key=lambda x: -x[1]):
    print('| %s | %d | %d |' % (NAMES[c], n, biggest[c]))
