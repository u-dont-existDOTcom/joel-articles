"""apply_h78.py - turn 70's checked texts into the guide, from the repo root:

  python3 articles/bad-trips/humanize/h78-20261126/apply_h78.py

All from his round-59 answers to GUT-SIGNS (review/r59/ANSWERS-R59-20261126-1555.json), each read Human High in one window
by itself through the API on its first check:

- B141 (My Acute Rescue Remedies): the signs, with his two terms explained where they are first used (7a9e0fdc);
- R59-GUT-DO, a new paragraph after it: what to do, with his "address the gut first" and his kept last line (af2c0ec5);
- B151 (Gut-Toxin & Die-Off Tools) with "the come-up" explained and an example for "more mysterious", and
  R59-GUT-COMMON, a new paragraph after it from his answer 2.2 (a53a2ce3, the two together).

And the next paragraph on the list of what is left, which read AI High as it stood (fc82fa68, with B151):

- B153 (ZeoCharge & Ferment): the two remedies first, its run of seven signs taken apart; Human High 104 in one window
  with B154 as it stands (73808644).
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
HERE = ART / 'humanize' / 'h78-20261126'


def text(key):
    return (HERE / ('TEST-%s.txt' % key)).read_text(encoding='utf-8').strip()


def main():
    blocks = json.loads((ART / 'GUIDE-SO-FAR-blocks.json').read_text(encoding='utf-8'))
    ids = [x['id'] for x in blocks]
    gut = text('a4-gutintro').split('\n\n')
    assert len(gut) == 2
    new = {'B141': text('a4-b141-signs'), 'B151': gut[0], 'B153': text('a1-b153')}
    after = {'B141': ('R59-GUT-DO', text('a5-b141-do')), 'B151': ('R59-GUT-COMMON', gut[1])}
    out = []
    for x in blocks:
        if x['id'] in new:
            x['md'] = new[x['id']]
        if x['id'] in ('R59-GUT-DO', 'R59-GUT-COMMON'):
            continue          # written again below, so a second run changes nothing
        out.append(x)
        if x['id'] in after:
            nid, md = after[x['id']]
            y = {k: v for k, v in x.items() if k not in ('id', 'md')}
            y.update({'id': nid, 'md': md})
            out.append(y)
    (ART / 'GUIDE-SO-FAR.md').write_text('\n\n'.join(x['md'] for x in out) + '\n', encoding='utf-8')
    (ART / 'GUIDE-SO-FAR-blocks.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: B141, R59-GUT-DO, B151, R59-GUT-COMMON, B153; %d blocks (were %d)' % (len(out), len(ids)))


if __name__ == '__main__':
    main()
