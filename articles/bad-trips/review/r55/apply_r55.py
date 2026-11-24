"""apply_r55.py - his round-55 versions (ANSWERS-R55-20261124-1953.json, 2026-11-24 19:53 UTC) and turn 66's checked texts
of MDMA: Magnesium Alarm into the guide, from the repo root:

  python3 articles/bad-trips/review/r55/apply_r55.py

- B114: his TEACH-JAW version, as his check 6c2c336b had it (the API: Human High, one window, 666cad89).
- B118: his TEACH-WIFE version, as his check 38fe09f7 had it, one double space made single (the API: High 37 / Medium 38
  with one space, 590654bf; High 75 in one window with his double space, 9a72854c). Round 56 offers him one phrase for its
  last sentence (WIFE-LAST).
- B115: his amounts with why magnesium chloride, from his TEACH-JAW question ("have we made sure to explain why i use
  magnesium chloride though?"): Human High 109, one window (af5fd4f9), in six tries (humanize/h74-20261124/RESULTS.md).
- B117: from his post's text with the ways of his round-55 fixes: Human High 62, one window (686d3bd1).
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H74 = ART / 'humanize' / 'h74-20261124'
PAIRS = [('his-b114', 'B114'), ('his-b118', 'B118'), ('a7-b115', 'B115'), ('a3-b117', 'B117')]


def main():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    for key, bid in PAIRS:
        by[bid]['md'] = (H74 / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: ' + ', '.join('%s=%s' % p for p in PAIRS))


if __name__ == '__main__':
    main()
