"""apply_r56.py - his round-56 answers (ANSWERS-R56-20261124-2126.json, 2026-11-24 21:26 UTC) into the guide, from the
repo root:

  python3 articles/bad-trips/review/r56/apply_r56.py

- B115 (CHLORIDE-CLAIM: "remove the source then if there's no source, but i definitely can't recommend using anything
  other than what i know works best"): the absorption study's link is out, and the sentence says his claim as what he
  knows, in the words of his round-55 comment: "I use it mostly because it's what I know works best: it absorbs faster
  and better than any other form, so you can see how it's helping, usually within a minute." The API: Human High 118,
  one window (f330e220).
- B118 (WIFE-LAST: "a"): its last phrase is "since potassium gets depleted once magnesium runs low". The API: Human
  High 77, one window (e74a7e6b).

The kidney paragraph (B120) is not changed: his post's text reads AI High by itself (df3704bf) and so did this turn's
two tries (7afc3e5b, f880b3a3); it is on round 57 as a teaching card (humanize/h75-20261124/RESULTS.md).
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
PAIRS = [(ART / 'humanize' / 'h75-20261124' / 'TEST-a1-b115.txt', 'B115'),
         (ART / 'humanize' / 'h74-20261124' / 'TEST-fix-b118.txt', 'B118')]


def main():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    for path, bid in PAIRS:
        by[bid]['md'] = path.read_text(encoding='utf-8').strip()
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: ' + ', '.join('%s=%s' % (p.name, b) for p, b in PAIRS))


if __name__ == '__main__':
    main()
