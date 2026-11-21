#!/usr/bin/env python3
"""apply_tags.py - his round-46 evidence tags (review/r46/ANSWERS-R46-20261120-2359.json, his comment: "almost all
these are my exp plus experiences of friends (except creatien for now just me)"), each on its own line just under the
remedy heading he picked in round 47, as the round-47 page showed him, for the eight remedies whose heading, tag and
first paragraph read Human High in every window by themselves (humanize/h66-20261121/RESULTS.md; apply_gate.py refuses
any that didn't). The six whose paragraphs read AI (zeolite, activated charcoal, the oils, DMSO, beach morning glory,
niacin) get theirs with their fixes.

  python3 articles/bad-trips/review/r47/apply_tags.py        (from the repo root, after apply_r47.py)
"""
import json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
REPO = ART.parents[1]
sys.path.insert(0, str(REPO / 'tools' / 'humanization'))
import apply_gate  # noqa: E402

BJ, MD = ART / 'GUIDE-SO-FAR-blocks.json', ART / 'GUIDE-SO-FAR.md'
TAGS = {'B166': 'Tried by Me and Friends', 'B181': 'Tried by Me and Friends', 'B183': 'Tried by Me and Friends',
        'H54-CREATINE-H': 'Tried by Me', 'H54-MANGO-H': 'Tried by Me and Friends', 'R30-RUE1': 'Tried by Me and Friends',
        'B185': 'Tried by Me and Friends', 'B189': 'Tried by Me and Friends'}


def main():
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    units = []
    for hid, tag in TAGS.items():
        i = [b['id'] for b in B].index(hid)
        if B[i + 1]['id'] == hid + '-TAG':
            continue
        line = '**[%s]**' % tag
        B.insert(i + 1, {'id': hid + '-TAG', 'kind': 'p', 'md': line, 'text': None})
        units.append('\n'.join([B[i]['md'], line, B[i + 2]['md']]))
    # each heading with its tag line and first paragraph, as the reader meets them: a check of exactly that, by itself
    apply_gate.require(str(ART / 'humanize' / 'pangram-ledger.jsonl'), units)
    MD.write_text('\n\n'.join(x['md'] for x in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('tags in under', len(units), 'headings')


if __name__ == '__main__':
    main()
