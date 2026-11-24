"""apply_h73.py - turn 65's paragraphs of MDMA: Magnesium Alarm into the guide, each exactly as it read through the
Pangram API on his laptop (RESULTS.md), with its links and bold back. From the repo root:

  python3 articles/bad-trips/humanize/h73-20261124/apply_h73.py KEY=BLOCK ... [--copy DIR]

e.g. a2-b114=B114 a2-b115=B115. --copy writes the guide's two files into DIR instead (the fidelity check on a copy).
"""
import argparse
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pairs', nargs='+')
    ap.add_argument('--copy', default='')
    o = ap.parse_args()
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    by = {x['id']: x for x in blocks}
    for pair in o.pairs:
        key, bid = pair.split('=')
        by[bid]['md'] = (HERE / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()
    out = pathlib.Path(o.copy) if o.copy else ART
    out.mkdir(parents=True, exist_ok=True)
    (out / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    (out / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied to %s: %s' % (out, ', '.join(o.pairs)))


if __name__ == '__main__':
    main()
