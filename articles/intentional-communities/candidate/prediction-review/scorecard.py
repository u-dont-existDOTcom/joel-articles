#!/usr/bin/env python3
"""scorecard.py OUT.json - every Pangram call the community lane predicted, scored (2026-10-12).

Joel, 2026-10-12 17:23 UTC: "regarding the prediction misses file i also don't know where that is, keep that updated i want
to see you improving on that or if you need help lmk i can tell you why stuff sounds human or AI." This reads every
PREDICTIONS table in the lane (the parser of parse_preds.py), numbers each call by its batch, and writes the scorecard's
data: accuracy per ten batches against always saying AI, and every miss since the 2026-10-10 review (batch 199g on), with
the checked text where the batch file has it. Pass means "Human Written" (100% Human); "Mostly Human" is not a pass.
"""
import glob, json, os, re, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.dirname(HERE)
sys.argv, out_path = [sys.argv[0]], sys.argv[1]
exec(open(os.path.join(HERE, 'parse_preds.py')).read().split('for f in sorted(glob.glob')[0])  # norm_pred, norm_res
# parse_preds.py sets C to the old lane's checkout path; this folder's parent is the candidate folder wherever it's
# checked out (2026-10-14: after the move to articles/intentional-communities/, the scorecard found 0 calls).
C = os.path.dirname(HERE)
rows = []


def chance(cell):
    """A prediction's chance of a 100% Human result (2026-10-18): "0.7", "70%" or "70 %", else None."""
    m = re.search(r'(\d+(?:\.\d+)?)\s*(%)?', cell or '')
    if not m:
        return None
    v = float(m.group(1))
    v = v / 100 if m.group(2) or v > 1 else v
    return v if 0 <= v <= 1 else None


files = sorted(glob.glob(C + '/s*/PREDICTIONS-*.md')) + sorted(glob.glob(C + '/s*/*/PREDICTIONS-*.md'))
files += sorted(glob.glob(C + '/fix-*/PREDICTIONS-scored.md'))  # 2026-10-14 on: fix_preds.py's rows
files += sorted(glob.glob(C + '/fix-*/b[0-9]*/PREDICTIONS-scored.md'))  # 2026-10-17: a turn's batches in its fix folder
for f in files:
    sec = os.path.relpath(f, C).split('/')[0]
    lines = open(f, encoding='utf-8').read().split('\n')
    hdr = None
    for i, ln in enumerate(lines):
        if not ln.startswith('|'):
            if ln.strip() == '':
                pass
            else:
                hdr = None if not ln.startswith('|') and ln.strip() else hdr
            continue
        cells = [c.strip() for c in ln.strip().strip('|').split('|')]
        if all(re.fullmatch(r':?-+:?', c) for c in cells if c):
            continue
        low = [c.lower() for c in cells]
        if 'mine' in low and any(c.startswith('pangram') for c in low):
            hdr = {'mine': low.index('mine'), 'why': next((k for k, c in enumerate(low) if c.startswith('why')), None),
                   'res': next(k for k, c in enumerate(low) if c.startswith('pangram')),
                   'p': next((k for k, c in enumerate(low) if c.startswith('chance')), None)}
            continue
        if not hdr or len(cells) <= hdr['res']:
            continue
        name = re.sub(r'[*`]', '', cells[0]).strip()
        m = re.match(r'(\d+)g-', name)
        if not m:
            continue
        res, pct = norm_res(cells[hdr['res']])
        mine = norm_pred(cells[hdr['mine']])
        if res in ('none', 'unparsed') or mine == 'other':
            continue
        name_only = re.sub(r'\s*\(\d+\)$', '', name)
        rows.append({'sec': sec, 'batch': int(m.group(1)), 'name': name_only, 'mine': mine,
                     'why': cells[hdr['why']] if hdr['why'] is not None else '', 'res': res, 'pct': pct,
                     'res_raw': re.sub(r'\*', '', cells[hdr['res']]), 'where': os.path.relpath(f, C) + ':' + str(i + 1),
                     'p': chance(cells[hdr['p']]) if hdr.get('p') is not None and len(cells) > hdr['p'] else None})
texts = {}
for v in glob.glob(C + '/s*/v*.json') + glob.glob(C + '/s*/*/v*.json'):
    try:
        d = json.load(open(v, encoding='utf-8'))
    except Exception:
        continue
    if not isinstance(d, dict):  # s13/vNN-fixes.json are lists of fixes, not texts (2026-10-15)
        continue
    for k, t in (d.get('texts') or {}).items():
        texts[k] = t
for r in rows:
    r['passed'] = r['res'] == 'Human'
    r['right'] = (r['mine'] == 'Human') == r['passed']
windows = defaultdict(list)
for r in rows:
    windows[(r['batch'] // 10) * 10].append(r)
win = []
for lo in sorted(windows):
    rs = windows[lo]
    n = len(rs); ok = sum(r['right'] for r in rs); p = sum(r['passed'] for r in rs)
    win.append({'from': lo, 'to': lo + 9, 'calls': n, 'right': ok, 'passed': p, 'always_ai_right': n - p})
misses = [dict(r, text=texts.get(r['name'], '')) for r in rows if not r['right'] and r['batch'] >= 199]
since = [r for r in rows if r['batch'] >= 199]
summary = {'calls': len(rows), 'right': sum(r['right'] for r in rows),
           'since_review': {'calls': len(since), 'right': sum(r['right'] for r in since), 'passed': sum(r['passed'] for r in since)},
           'today': {'calls': len([r for r in rows if r['batch'] >= 261]), 'right': sum(r['right'] for r in rows if r['batch'] >= 261),
                     'passed': sum(r['passed'] for r in rows if r['batch'] >= 261)}}
json.dump({'summary': summary, 'windows': win, 'misses': misses}, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# The dashboard's rows (2026-10-17, Joel at 23:10 UTC: "your scorecard is always empty"). The page's calcs read one row per call
# (batch, right and passed as 1 or 0, the call's id as its "text" key, section, mine, pangram, why, excerpt), and the summary
# file above isn't rows, so the page had nothing to count. Excerpts come from the batch folders' drafts.json and the section
# drafts' texts.
for d in glob.glob(C + '/**/b[0-9]*/drafts.json', recursive=True):
    m = re.search(r'/b(\d+)/drafts\.json$', d)
    try:
        dd = json.load(open(d, encoding='utf-8'))
    except Exception:
        continue
    for k, t in dd.items():
        texts.setdefault('%sg-%s' % (m.group(1), k), t['text'] if isinstance(t, dict) else t)
# 2026-10-18 (Joel, 01:29 UTC: "improve the scorecard especially for predictions and fixes, as well as the speed of fixing"):
# each check's kind from its batch's gate record (screen, draft, edit: my rewrites; owner: his words; section: a whole section),
# so the page can show how often my rewrites pass on their first check, and an always-Human baseline beside always-AI.
kinds = {}
for g in glob.glob(C + '/**/b[0-9]*/GATE.json', recursive=True):
    m = re.search(r'/b(\d+)/GATE\.json$', g)
    try:
        gg = json.load(open(g, encoding='utf-8'))
    except Exception:
        continue
    al_path = os.path.join(os.path.dirname(g), 'aliases.json')
    al = json.load(open(al_path, encoding='utf-8')) if os.path.exists(al_path) else {}
    for k, rec in gg.items():
        if isinstance(rec, dict) and rec.get('kind'):
            kinds['%sg-%s' % (m.group(1), k)] = rec['kind']
    for k, v in al.items():
        if isinstance(gg.get(v), dict):
            kinds.setdefault('%sg-%s' % (m.group(1), k), gg[v].get('kind'))
seen = defaultdict(int)
out_rows = []
for r in sorted(rows, key=lambda r: (r['batch'], r['name'])):
    seen[r['name']] += 1
    key = r['name'] if seen[r['name']] == 1 else '%s (%d)' % (r['name'], seen[r['name']])
    ex = (texts.get(r['name']) or '').replace('\n\n', ' / ')
    out_rows.append({'batch': r['batch'], 'text': key, 'section': r['sec'], 'mine': r['mine'], 'pangram': r['res_raw'],
                     'why': r['why'], 'excerpt': ex[:300] + ('…' if len(ex) > 300 else ''), 'right': int(r['right']),
                     'passed': int(r['passed']), 'said_human': int(r['mine'] == 'Human'), 'kind': kinds.get(r['name'], ''),
                     'chance': r.get('p')})
rows_path = os.path.join(os.path.dirname(os.path.abspath(out_path)), 'prediction-calls-rows.json')
json.dump({'rows': out_rows}, open(rows_path, 'w', encoding='utf-8'), ensure_ascii=False)
print(rows_path, len(out_rows), 'rows,', sum(1 for r in out_rows if r['excerpt']), 'with an excerpt')
print(json.dumps(summary))
for w in win:
    print(w)
print(len(misses), 'misses since 199g')
