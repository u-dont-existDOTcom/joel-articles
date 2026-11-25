"""apply_h77.py - turn 69's two checked texts of mine into the guide, from the repo root:

  python3 articles/bad-trips/humanize/h77-20261125/apply_h77.py

- B86 (My Acute Rescue Remedies): four words of its list sentence, "all get read as spiritual signs" for "all become
  spiritual content". With the two paragraphs before it the sentence read Human Low 14 as his post has it, Medium 16 after
  "get read as", and the three paragraphs Human High 72 in one window after "signs" (6058dbfc).
- B141 (the same section): from his post's text, Human High 75 in one window (8f7d99cd). Every sign is kept, and his own
  last line, "A gut-driven mental hell is often mistaken as shadow work.", stays word for word (keep-as-is K2): my first
  checked try had joined it to the sentence before (Human High 76, 6f789f5b) and was taken back out when keep_as_is.py
  caught it. "A different branch" is the remedies below and the shadow work further down.
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H77 = ART / 'humanize' / 'h77-20261125'
PAIRS = [('a3-b86', 'B86'), ('a3-b141', 'B141')]


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
