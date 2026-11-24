"""apply_r53.py - his round-53 answer (ANSWERS-R53-20261124-1420.json, 2026-11-24 14:20 UTC) and the Medium windows of
steps 6 and 8, into the guide, from the repo root:

  python3 articles/bad-trips/review/r53/apply_r53.py --c a2-ss8   (as applied; --a, --b and --c pick the tries, --copy DIR)

--copy writes the guide's two files into DIR instead (for the fidelity check on a copy, lesson bad-trips-2026-11-23f).
Each text goes in exactly as it was checked through the Pangram API on his laptop with his key
(humanize/h72-20261124/RESULTS.md), with its links back:

- The dance paragraph (R52-DANCE), from MAPS-SETTING: his own answer that the setting isn't what does it, as the evidence
  for the sentence after it (a pill that makes someone feel like dancing is one he suspects).
- Step 6 (B136, line 6): its Medium window, the high-potassium line, with the act first; the potassium line before it
  read for the same ways (AGENTS.md's done rule of 2026-11-24, way 28).
- Step 8 (B136, line 8): the dose of its niacin line named where the reader meets it ("at that dose", for the trip-ending
  doses said twice) and the sign said as what happens (a drop in blood pressure). Both of step 8's Medium windows went
  with that one fix, so his oil and brew sentence is untouched; the ledger refused the bigger rewrite first (43% of the
  words after a try that read Human, lesson bad-trips-2026-11-19b).
"""
import argparse
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H72 = ART / 'humanize' / 'h72-20261124'


def text(key):
    return (H72 / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', default='a2-dance')
    ap.add_argument('--b', default='a2-ss6')
    ap.add_argument('--c', default='a2-ss8')
    ap.add_argument('--copy', default='')
    o = ap.parse_args()
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    by['R52-DANCE']['md'] = text(o.a)
    lines = by['B136']['md'].split('\n')
    assert len(lines) == 8 and lines[5].startswith('6. ') and lines[7].startswith('8. ')
    lines[5] = '6. ' + text(o.b)
    lines[7] = '8. ' + text(o.c)
    by['B136']['md'] = '\n'.join(lines)
    out = pathlib.Path(o.copy) if o.copy else ART
    out.mkdir(parents=True, exist_ok=True)
    (out / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (out / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied to %s: the dance paragraph (%s), step 6 (%s), step 8 (%s)' % (out, o.a, o.b, o.c))


if __name__ == '__main__':
    main()
