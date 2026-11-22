#!/usr/bin/env python3
"""collect.py - every fix Joel sent on a review page in this repository (an item's "your_version" that differs from the
text the card showed), paired with what it replaced, for the systematic read he asked for on 2026-11-12 14:45 UTC
("have you systematically looked at all of the fixes i've shown you and what are the idfferences in how you write vs how
i fix?").

Writes PAIRS.json (every pair, with its lane, round file, card, type and comment) and prints what was kept and why the
rest was left out (a short answer, or a text that shares too little with what the card showed to be a rewrite of it).

  python3 collect.py        (from anywhere)
"""
import difflib, glob, json, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[4]


def words(t):
    return re.findall(r"[A-Za-z0-9'’]+", t.lower())


# read one by one (2026-11-12): these "your_version" boxes hold something other than his rewrite of the card's text
NOT_A_REWRITE = {'SC-106': 'a pasted exchange with another model, not his rewrite',
                 'R-755': 'his note on a check with the text after it; the text is read with the try series instead'}
pairs, left = [], []
for f in sorted(glob.glob(str(REPO / 'articles/**/ANSWERS*.json'), recursive=True)):
    try:
        d = json.loads(pathlib.Path(f).read_text(encoding='utf-8'))
    except Exception:
        continue
    for it in (d.get('items') or []) if isinstance(d, dict) else []:
        his = (it.get('your_version') or '').strip()
        before = (it.get('my_version') or it.get('before') or '').strip()
        if not his or his == before:
            continue
        rel = str(pathlib.Path(f).relative_to(REPO))
        a, b = words(before), words(his)
        sim = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() if a and b else 0.0
        rec = {'lane': rel.split('/')[1], 'file': rel, 'id': it.get('id'), 'type': it.get('type'), 'title': it.get('title'),
               'before': before, 'his': his, 'comment': (it.get('comment') or '').strip(), 'words_before': len(a),
               'words_his': len(b), 'shared': round(sim, 2)}
        if len(b) < 12 or not a:
            rec['left_out'] = 'a short answer or nothing shown to rewrite'
        elif rec['id'] in NOT_A_REWRITE:
            rec['left_out'] = NOT_A_REWRITE[rec['id']]
        elif sim < 0.05:
            rec['left_out'] = 'shares too little with what the card showed to be a rewrite of it'
        (left if 'left_out' in rec else pairs).append(rec)
(HERE / 'PAIRS.json').write_text(json.dumps({'kept': pairs, 'left_out': left}, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
import collections
print(len(pairs), 'pairs kept', dict(collections.Counter(p['lane'] for p in pairs)))
print(len(left), 'left out', dict(collections.Counter(p['left_out'][:20] for p in left)))
