#!/usr/bin/env python3
"""section_map.py - which of the guide's words the published post's Pangram check read AI, section by section.

E354 (pull request 293; Joel, 2026-11-04 14:41 UTC: "we need to first fix any windows we can see before we check the
article"): before any new whole-guide check, the windows already seen are the work. This maps each block of the guide as
it stands (GUIDE-SO-FAR-blocks.json) to the baseline window (baseline-20261103/RESULT-20261018.json, the check of the
published v5.5) whose six-word runs it shares most, and counts each section's words by that window's label and
confidence. A block with no run in any window is "new" (written or changed since). Quotes and dashes are made straight
first, since the standard swap changed them.

  python3 articles/bad-trips/humanize/section_map.py   (from the repo root; writes SECTION-MAP.md beside it)
"""
import json, re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE.parent
K = 6
COLS = ['AI High', 'AI Medium', 'AI Low', 'Human Low', 'Human Medium', 'Human High', 'new']


def words(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', ' - ').replace('–', ' - ')
    s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[*_#>`]', ' ', s)
    return re.findall(r"[a-z0-9']+", s.lower())


def main():
    d = json.loads((HERE / 'baseline-20261103' / 'RESULT-20261018.json').read_text())
    text = d['text']
    run_label = {}
    for w in d['windows']:
        ww = words(text[w['start_index']:w['end_index']])
        key = ('AI ' if w['label'].startswith('AI') else 'Human ') + w['confidence']
        for i in range(len(ww) - K + 1):
            run_label.setdefault(tuple(ww[i:i + K]), key)
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text())
    sec, order, tot = '(top)', ['(top)'], defaultdict(Counter)
    for b in blocks:
        md = b.get('md') or ''
        if b['kind'] in ('h1', 'h2'):
            sec = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', md).lstrip('# ').strip()
            order.append(sec)
        w = words(md)
        if not w:
            continue
        runs = [tuple(w[i:i + K]) for i in range(len(w) - K + 1)] or [tuple(w)]
        labs = Counter(run_label.get(r, 'new') for r in runs)
        lab, c = labs.most_common(1)[0]
        if lab == 'new' and c / len(runs) < 0.6 and len(labs) > 1:
            lab = labs.most_common(2)[1][0]
        tot[sec][lab] += len(w)
    lines = ['# The guide against the published post\'s check, section by section', '',
             'Made by `section_map.py` from `../GUIDE-SO-FAR-blocks.json` (the guide as it stands) and the baseline check of the '
             'published post ([82%% AI](%s)). Words of each section by the label and confidence of the baseline window its '
             'blocks share most six-word runs with; "new" is text written or changed since.' % d.get('link', ''), '',
             '| Section | Words | ' + ' | '.join(COLS) + ' |', '|---|---:|' + '---:|' * len(COLS)]
    g = Counter()
    for s in order:
        t = tot[s]
        g.update(t)
        lines.append('| %s | %d | %s |' % (s, sum(t.values()), ' | '.join(str(t.get(c, 0)) for c in COLS)))
    lines.append('| **All** | %d | %s |' % (sum(g.values()), ' | '.join(str(g.get(c, 0)) for c in COLS)))
    (HERE / 'SECTION-MAP.md').write_text('\n'.join(lines) + '\n')
    print('all: %d words; %s' % (sum(g.values()), ', '.join('%s %d' % (c, g.get(c, 0)) for c in COLS)))


if __name__ == '__main__':
    main()
