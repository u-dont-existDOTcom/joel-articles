"""apply_r52.py - his round-52 answers (ANSWERS-R52-20261124-0126.json, 2026-11-24 01:25 UTC) into the guide, from the
repo root:

  python3 articles/bad-trips/review/r52/apply_r52.py --b a3-dance   (as applied; --a and --b pick the tries, --copy DIR)

--copy writes the guide's two files into DIR instead (for the fidelity check on a copy, lesson bad-trips-2026-11-23f).
Each text goes in exactly as it was checked through the Pangram API on his laptop with his key
(humanize/h71-20261124/RESULTS.md), with its links back:

- His MDMA paragraph (B119), from WOMEN-RISK: his sentence that women are most at risk, with what it rests on (one in four
  women vs 3% of men at a rave in the Netherlands, and California's poison control's four times the odds); the dance line
  moves to the next paragraph, and why plain water lowers sodium is said in fewer words.
- A new paragraph after it (R52-DANCE), from DANCE-ENERGY and the field vs lab note of WOMEN-RISK: no dancing on MDMA,
  San Pedro or mescaline for dancing, real MDMA as couch lock (his and everyone he knows'), a pill that makes someone feel
  like dancing as one he suspects, and the lab study where women's sodium dropped no more than men's, with his reading of
  it and the other way the lab differed (doses by weight).
"""
import argparse
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
H71 = ART / 'humanize' / 'h71-20261124'


def text(key):
    return (H71 / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', default='a2-mdma')
    ap.add_argument('--b', default='a2-dance')
    ap.add_argument('--copy', default='')
    o = ap.parse_args()
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    ids = [x['id'] for x in blocks]
    by = {x['id']: x for x in blocks}
    old = by['B119']['md']
    assert old.startswith('Once their jaw tenses'), old[:60]
    by['B119']['md'] = text(o.a)
    if 'R52-DANCE' in by:
        by['R52-DANCE']['md'] = text(o.b)
    else:
        blocks.insert(ids.index('B119') + 1, {'id': 'R52-DANCE', 'kind': 'p', 'md': text(o.b), 'text': None})
    out = pathlib.Path(o.copy) if o.copy else ART
    out.mkdir(parents=True, exist_ok=True)
    (out / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (out / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied to %s: his MDMA paragraph (%s), the dance paragraph after it (%s)' % (out, o.a, o.b))


if __name__ == '__main__':
    main()
