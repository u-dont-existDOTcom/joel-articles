#!/usr/bin/env python3
"""apply_r42.py - his round-42 answer (ANSWERS-R42-20261119-1606.json, exported 2026-11-19 16:06 UTC) into the guide:
MED-MDMA approved, his MDMA paragraph with the two medical fixes (Human High 157 by itself, 597c5351), the single-dose
trial linked on his words as before.

  python3 articles/bad-trips/review/r42/apply_r42.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
A = {i['id']: i for i in json.loads((HERE / 'ANSWERS-R42-20261119-1606.json').read_text(encoding='utf-8'))['items']}
LINK = ('even a single normal MDMA dose', '[even a single normal MDMA dose](https://pubmed.ncbi.nlm.nih.gov/39546312/)')


def main():
    c = A['MED-MDMA']
    assert c['status'] == 'approved'
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    b = next(x for x in B if x['id'] == 'B119')
    new = c['my_version'].replace(*LINK)
    assert b['md'] in (c['before'].replace(*LINK), new), b['md'][:80]
    b['md'] = new
    MD.write_text('\n\n'.join(x['md'] for x in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    if 'r42-med-mdma' not in {e['id'] for e in oe['entries']}:
        oe['entries'].append({
            'id': 'r42-med-mdma', 'status': 'applied',
            'what': ("MDMA paragraph's two medical fixes (round 42, MED-MDMA): something very salty while waiting for medics if "
                     "alert and not vomiting, in place of \"too late for an easy fix\"; low sodium, magnesium or potassium in "
                     "the seizure line"),
            'joel': ('approved card MED-MDMA, 2026-11-19 16:05 UTC, after his message of 15:41 UTC ("what about hypertonic '
                     'fluids? wouldn\'t it make sense unless they aren\'t able to keep it down or swallow?")'),
            'applied_by': 'review/r42/ANSWERS-R42-20261119-1606.json, put in by review/r42/apply_r42.py',
            'must_contain': ["give them something very salty instead, like strong broth or salty snacks",
                             'A seizure or collapse can result from low sodium, magnesium or potassium'],
            'must_not_contain': ['it could be too late for an easy fix']})
        OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied |', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
