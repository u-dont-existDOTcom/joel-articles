"""apply_r57.py - his round-57 version (ANSWERS-R57-20261124-2327.json, exported 2026-11-24 23:27 UTC, sent with his message
of 2026-11-25 01:24 UTC) and turn 68's checked text into the guide, from the repo root:

  python3 articles/bad-trips/review/r57/apply_r57.py

- B120, the kidney paragraph (TEACH-KIDNEY, revised): his version, whole. The page's box came back unchanged, so the text
  is read from the last of the six checks his comment links (33a4d738, Human High 115 in one window; every check is in
  HIS-CHECKS-R57.md). His bold lead stays on the words it sat on, and the kidney study's link, which his plain text could
  not carry, is back on its claim ("injure the kidneys"; gate E380). The API reads it Human High 115 in one window too
  (a1673899).
- B130, the opening of Serotonin Syndrome (SS)?: mine, from his post's text, Human High 116 in one window in two tries
  (a2d82519; humanize/h76-20261125/RESULTS.md). Every substance and the warning are kept.

The charcoal and poison control paragraphs (B127, B128) read Human High 200 in one window in my first try (75a2458d) and
are NOT applied here: the try adds the first hour, slow-release pills and two examples from the review the paragraph cites,
so it is round 58's card for him to approve (humanize/h76-20261125/TEST-a2-b127-b128.txt).
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H76 = ART / 'humanize' / 'h76-20261125'
PAIRS = [('his-b120', 'B120'), ('a3-b130', 'B130')]


def main():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    for key, bid in PAIRS:
        by[bid]['md'] = (H76 / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: ' + ', '.join('%s=%s' % p for p in PAIRS))


if __name__ == '__main__':
    main()
