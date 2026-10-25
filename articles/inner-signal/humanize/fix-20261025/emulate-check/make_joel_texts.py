"""JOEL-TEXTS.txt for the guide's Emulate check: his own words given in this lane, after his published post.

  python3 articles/inner-signal/humanize/fix-20261025/emulate-check/make_joel_texts.py

His messages as saved word for word (joel-*-message.txt in this lane's fix folders) and the versions of his own that
went into the guide (the "new" text of every edit recorded as his: EDITS-joel-*.json, and EDITS41.json's entries whose
source is "Joel's own words" or "Joel's own edit"). The first readers' run went without these and called his own
paragraph of 2026-10-23 12:30 UTC ("There are actually multiple patents on using screens ...") Emulate's.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
LANE = HERE.parents[1]
parts = [p.read_text(encoding='utf-8') for p in sorted(LANE.rglob('joel-*-message.txt'))]
n_edits = 0
for f in sorted(LANE.rglob('EDITS-joel-*.json')) + [LANE / 'fix-20261020' / 'EDITS41.json']:
    d = json.loads(f.read_text(encoding='utf-8'))
    items = d if isinstance(d, list) else d.get('edits', d.get('items', []))
    for x in items:
        if not isinstance(x, dict):
            continue
        src = str(x.get('source', ''))
        if f.name.startswith('EDITS-joel-') or src.startswith(("Joel's own words", "Joel's own edit")):
            for k in ('new', 'after', 'text'):
                if isinstance(x.get(k), str) and x[k].strip():
                    parts.append(x[k])
                    n_edits += 1
(HERE / 'JOEL-TEXTS.txt').write_text('\n\n'.join(p.strip() for p in parts if p.strip()) + '\n', encoding='utf-8')
print(len(parts) - n_edits, 'messages,', n_edits, 'edits of his,', sum(len(p.split()) for p in parts), 'words')
