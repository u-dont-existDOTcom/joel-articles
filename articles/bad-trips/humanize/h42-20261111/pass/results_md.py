#!/usr/bin/env python3
"""results_md.py - RESULTS.md for the h42a batch: every unit's Pangram result with its link, each window's label and
confidence, and the words of every window that isn't Human High (his: always the links and the confidence; Medium
windows shown too, since he fixes those himself).

  python3 results_md.py      reads UNITS.json, PREDICTIONS-h42a.json and RESULTS-h42a.json; writes ../RESULTS.md
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
U = json.loads((HERE / 'UNITS.json').read_text(encoding='utf-8'))
P = json.loads((HERE / 'PREDICTIONS-h42a.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'RESULTS-h42a.json').read_text(encoding='utf-8'))
LINK = 'https://www.pangram.com/history%s'
# A unit the web app wouldn't check: its Check for AI button stays off under 50 words.
NOT_CHECKED = {'h42-47': 'not checked: 37 words, under the web app\'s 50-word minimum (its prediction voided; it gets '
                         'checked with a neighbour after the humanize edits)'}


def windows(s):
    out = []
    for w in [w for w in (s or '').split('; ') if w]:
        parts = [x.strip() for x in w.rsplit(', ', 2)]
        out.append(parts if len(parts) == 3 else [w, '', ''])
    return out


rows, worst = [], []
counts = {'Human High only': 0, 'Medium somewhere': 0, 'Low somewhere': 0, 'AI somewhere': 0}
for u in U:
    r = R.get(u['key'])
    if not r:
        why = NOT_CHECKED.get(u['key'], 'not read')
        rows.append('| %s | %s | %d | %s | | |' % (u['key'], u['title'], u['words'], why))
        continue
    head, ai, words, wins, utc, tail = r[:6]
    flagged = r[6] if len(r) > 6 else []
    ws = windows(wins)
    labels = ', '.join('%s %s %s' % (l, c, n) for l, c, n in ws)
    has_ai = any(l.startswith('AI') for l, c, n in ws)
    has_low = any(c == 'Low' for l, c, n in ws)
    has_med = any(c == 'Medium' for l, c, n in ws)
    if has_ai:
        counts['AI somewhere'] += 1
    elif has_low:
        counts['Low somewhere'] += 1
    elif has_med:
        counts['Medium somewhere'] += 1
    else:
        counts['Human High only'] += 1
    rows.append('| %s | %s | %d | %s, %d%% AI | %s | [%s](%s) |' % (u['key'], u['title'], u['words'], head, round(ai * 100),
                                                               labels, tail.strip('/')[:8], LINK % tail))
    if has_ai or has_low or has_med:
        worst.append((0 if has_ai else 1 if has_low else 2, u, r, ws, flagged))
md = ['# The guide as it stands after round 33, in Pangram (2026-11-11, batch h42a)', '',
      'Pangram\'s web app on his account (Pangram Professional), each unit typed as its text file in `pass/units/` (SHA-256 '
      'checked before each click), its prediction in `../pangram-ledger.jsonl` first (`pass/write_predictions.py`). '
      'A unit is a section, or a run of one (at most about six paragraphs). Each window: its label, Pangram\'s confidence '
      '(High, Medium or Low) and its words.', '',
      '**Totals:** %d units, %d checked; %d read Human High in every window, %d have a Medium window, %d a Low window, %d an '
      'AI window.' % (len(U), len(U) - len(NOT_CHECKED), counts['Human High only'], counts['Medium somewhere'],
                      counts['Low somewhere'], counts['AI somewhere']), '',
      '| unit | section | words | result | windows (label, confidence, words) | link |', '|---|---|---|---|---|---|'] + rows
md += ['', '## Every window that isn\'t Human High', '']
for rank, u, r, ws, flagged in sorted(worst, key=lambda x: (x[0], x[1]['key'])):
    md += ['### %s, %s ([result](%s))' % (u['key'], u['title'], LINK % r[5]), '']
    below = r[7] if len(r) > 7 else []
    md += ['- %s' % f for f in flagged] + ['- %s' % f for f in below]
    md += ['']
(HERE.parent / 'RESULTS.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(counts)
