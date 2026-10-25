#!/usr/bin/env python3
"""Turn 110: OWNER-EDITS.json gets his decision of 2026-10-25 17:26 UTC on the Pink question (Y1 on the turn-109 sheet):
the paragraph stays as he wrote it. Nothing else in the article changes this turn; the agreed changes wait on his review
sheet (experiments/t110-review/). Applied once; it refuses to run again."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
P = HERE.parents[1] / 'OWNER-EDITS.json'
data = json.loads(P.read_text(encoding='utf-8'))
assert not any(e['id'] == 'joel-110-20261025' for e in data['entries']), 'already applied'
data['entries'].append({
    'id': 'joel-110-20261025',
    'status': 'applied',
    'what': 'Y1 decided: "Pink" is not her real name, so How This Relates to IFS keeps his paragraph as he wrote it, "my friend '
            'Pink" and her account included. No text changes.',
    'joel': '2026-10-25 17:26 UTC (experiments/t110-answers/JOEL-20261025-1726.md): "don\'t worry, "Pink" is not her real name"',
    'where': 'How This Relates to IFS',
    'must_contain': ['as my friend Pink, who has been healing her Dissociative Identity Disorder, explained'],
})
P.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('joel-110-20261025 added')
