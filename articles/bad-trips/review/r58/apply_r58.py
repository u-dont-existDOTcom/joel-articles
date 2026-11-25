"""apply_r58.py - his round-58 answer (ANSWERS-R58-20261125-1742.json, exported 2026-11-25 17:42 UTC, sent 17:43 UTC) into
the guide, from the repo root:

  python3 articles/bad-trips/review/r58/apply_r58.py

- B127 and B128, the charcoal and poison control paragraphs of Swallowed Too Much? (CHARCOAL-HOUR, answered): his version
  of both, whole, as his comment has it ("so it shall read:"). My version, which the card asked about, does not go in: it
  had poison control as who to ask about charcoal, which he does not recommend, and the review's first hour, which is not
  true of plant medicines that take hours to digest (his experience). The guide's link is back on "Activated charcoal"
  and the review's link on "The usual advice", which is what that review states (a citation missing from his plain text
  is not taken as cut: gate E380). The API reads the two paragraphs Human High 166 in one window (7b62fe4a).
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H77 = ART / 'humanize' / 'h77-20261125'
PAIRS = [('his-b127', 'B127'), ('his-b128', 'B128')]


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
