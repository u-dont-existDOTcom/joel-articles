"""apply_r59.py - his round-59 answer to POISON-LINE (ANSWERS-R59-20261126-1555.json, exported 2026-11-26 15:55 UTC, sent
15:56 UTC) into the guide, from the repo root:

  python3 articles/bad-trips/review/r59/apply_r59.py

- B128, the poison control paragraph of Swallowed Too Much? (POISON-LINE, answered "b"): the version the card showed. His
  clause "even if they often can't give actionable advice for liability reasons" goes; two sentences say what happened to
  the person he knows, with Poison Control's own page linked on "they aren't allowed to tell anyone to take it". His other
  three sentences stay word for word. It read Human High 74 in one window on its first check (9afb6a77, turn 69).

His GUT-SIGNS answers are new text of mine from his words, so they go in from humanize/h78-20261126/apply_h78.py once
read and checked.
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H77 = ART / 'humanize' / 'h77-20261125'
PAIRS = [('b2-b128', 'B128')]


def main():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    for key, bid in PAIRS:
        by[bid]['md'] = (H77 / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: ' + ', '.join('%s=%s' % p for p in PAIRS))


if __name__ == '__main__':
    main()
