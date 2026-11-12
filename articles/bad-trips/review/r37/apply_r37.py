#!/usr/bin/env python3
"""apply_r37.py - his round-37 answers (export of 2026-11-12 16:47:47 UTC, ANSWERS-R37-20261112-1647.json) into the guide.

- TEACH-CHEST revised: his version of Chest Pain and Injury's branch paragraph, the text of his last check (cabd68b6,
  Human Written, High 46, Medium 9, High 70), in whole: its lead-in in B124, his six lines as a list (R37-CHEST-LIST) and
  his last sentence (R37-CHEST-2). He started from my chest-c3 (h46) and took it through twelve checks
  (../../experiments/t37-answers/JOEL-TRIES-TEACH-CHEST.md). Magnesium chloride for chest pain is said as topical ("on the
  chest") here, and the guide names it for chest pain nowhere else ("everywhere it's mentioned, tho hopefully only here").
- SS-THESE: "a" ("these" stays, as the guide has it), with "no need to ask me for obvious corrections".

  python3 articles/bad-trips/review/r37/apply_r37.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]
i = ids.index('B124')
assert B[i]['md'].startswith('Mild, familiar, non-progressive discomfort')
B[i]['md'] = ("For steady chest pain that's mild, I'd just use DMSO + magnesium chloride on the chest, as long as they're fully "
              "alert. For the following more serious signs (or if unsure), I'd also call medics:")
B[i + 1:i + 1] = [
    {'id': 'R37-CHEST-LIST', 'kind': 'ul', 'text': None, 'md': '\n'.join([
        '- The pain is worsening.',
        '- Hard movement (like dancing or climbing) brought it on.',
        '- It spreads from the chest into an arm or the jaw.',
        '- Shortness of breath or sweating shows up also.',
        '- Any of the stroke signs from the brain checks above show up, like slurred speech or a drooping face.',
        '- They feel faint, or they collapse.'])},
    {'id': 'R37-CHEST-2', 'kind': 'p', 'text': None,
     'md': ('Keep in mind that DMSO can also block pain signals, so even if the pain fades, it could still be worth having a '
            'medical checkup later.')},
]
MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
have = {e.get('id') for e in oe['entries']}
new = [
    {'id': 'r37-teach-chest', 'status': 'applied',
     'what': ('Chest Pain and Injury\'s branch paragraph is his version, the text of his last check cabd68b6: the mild case '
              'with DMSO + magnesium chloride on the chest, "For the following more serious signs (or if unsure), I\'d also '
              'call medics:", his six signs, and a later checkup since DMSO can block pain (round 37, card TEACH-CHEST; '
              'review/r37/apply_r37.py)'),
     'joel': ('2026-11-12 16:47:47 UTC: round 37\'s export, TEACH-CHEST revised, with his twelve tries; "i want to add '
              'magnesium chloride and explain this is topical for chest pain"'),
     'must_contain_exact': ["I'd just use DMSO + magnesium chloride on the chest",
                            "For the following more serious signs (or if unsure), I'd also call medics:",
                            '- Shortness of breath or sweating shows up also.'],
     'must_not_contain': ['Mild, familiar, non-progressive discomfort', 'In the second branch']},
]
oe['entries'] += [e for e in new if e['id'] not in have]
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('in:', B[i]['md'][:80], '|', len('\n\n'.join(b['md'] for b in B).split()), 'words')
