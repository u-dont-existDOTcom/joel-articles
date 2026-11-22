#!/usr/bin/env python3
"""apply_r41.py - his round-41 answers (ANSWERS-R41-20261119-1515.json, exported 2026-11-19 15:15 UTC) into the guide.

- B106-ORDER approved: his three bleed lines first, my two after them in plain words (Human High by itself, d7836ec9).
- TEACH-CYP revised: his version of step 2, whole, from his check cc5e6563 (Human High 58); the case series linked on his
  "case reports" and the review on his "a recent review".
- TEACH-MDMA revised: his version, whole, from his check c45651d9 (Human High 132); the single-dose trial linked on his
  "even a single normal MDMA dose". His version leaves out the kidney review; as the card proposed, it goes on the next
  paragraph's "acute kidney injury" (B120), the same claim, so its citation stays where something rests on it (E380).

What his comment asked to check medically goes to round 42's card, his words untouched here.

  python3 articles/bad-trips/review/r41/apply_r41.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
ANS = json.loads((HERE / 'ANSWERS-R41-20261119-1515.json').read_text(encoding='utf-8'))
A = {i['id']: i for i in ANS['items']}

B106_NEW = A['B106-ORDER']['my_version']
CYP_HIS = A['TEACH-CYP']['your_version']
MDMA_HIS = A['TEACH-MDMA']['your_version']

CYP_MD = ('2. ' + CYP_HIS
          .replace('If the person is fully alert and able to swallow, I would give cyproheptadine early,',
                   '**If the person is fully alert and able to swallow, I would give cyproheptadine early**,')
          .replace('only been case reports', 'only been [case reports](https://pubmed.ncbi.nlm.nih.gov/9696181/)')
          .replace('a recent review found', '[a recent review](https://pubmed.ncbi.nlm.nih.gov/39791184/) found'))
MDMA_MD = MDMA_HIS.replace('even a single normal MDMA dose',
                           '[even a single normal MDMA dose](https://pubmed.ncbi.nlm.nih.gov/39546312/)')
KIDNEY_OLD = 'and acute kidney injury.'
KIDNEY_NEW = 'and [acute kidney injury](https://pubmed.ncbi.nlm.nih.gov/27917269/).'


def main():
    assert A['B106-ORDER']['status'] == 'approved' and A['TEACH-CYP']['status'] == 'revise' == A['TEACH-MDMA']['status']
    B = json.loads(BJ.read_text(encoding='utf-8'))
    assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
    ids = [b['id'] for b in B]
    blk = lambda i: B[ids.index(i)]
    assert blk('B106')['md'] in (A['B106-ORDER']['before'], B106_NEW)
    blk('B106')['md'] = B106_NEW
    items = blk('B136')['md'].split('\n')
    assert items[1].startswith('2. **If the person is fully alert'), items[1][:60]
    items[1] = CYP_MD
    blk('B136')['md'] = '\n'.join(items)
    blk('B119')['md'] = MDMA_MD
    b120 = blk('B120')['md']
    if KIDNEY_NEW not in b120:
        assert b120.count(KIDNEY_OLD) == 1
        blk('B120')['md'] = b120.replace(KIDNEY_OLD, KIDNEY_NEW)
    MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
    BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

    OE = ART / 'OWNER-EDITS.json'
    oe = json.loads(OE.read_text(encoding='utf-8'))
    have = {e['id'] for e in oe['entries']}
    by = 'review/r41/ANSWERS-R41-20261119-1515.json (exported 2026-11-19 15:15 UTC), put in by review/r41/apply_r41.py'
    new = [
     {'id': 'r41-b106-order', 'status': 'applied',
      'what': "My Brain Feels Damaged's bleed paragraph: his three bleed lines first, my two after them in plain words (round 41, B106-ORDER)",
      'joel': 'approved card B106-ORDER, 2026-11-19 10:53 UTC', 'applied_by': by,
      'must_contain': ['They can feel better on DMSO with a clot or a bleed still there.'],
      'must_not_contain': ['The larger adjacent risk is losing a treatment window']},
     {'id': 'r41-cyp-his', 'status': 'applied',
      'what': "Suspected Serotonin Syndrome's step 2, his version whole (round 41, TEACH-CYP; his check cc5e6563, Human High 58)",
      'joel': ('2026-11-19 15:14 UTC: "i made 2 changes, and i checked each one. each was necessary to get to fully high conf '
               'human. first i clarified what "it" was referring to, then i clarified what "too weak" meant"'),
      'applied_by': by, 'must_contain': ['So far, the evidence for this med has only been']},
     {'id': 'r41-mdma-his', 'status': 'applied',
      'what': "MDMA's paragraph after his second wife's story, his version whole (round 41, TEACH-MDMA; his check c45651d9, Human High 132)",
      'joel': ('2026-11-19 15:07 UTC: "alright i tried to fully clarify it and not repeat 3 times to call medics, now it\'s '
               'human high conf, altho i\'m not sure i clarified it correctly medically speaking. check to make sure."'),
      'applied_by': by, 'must_contain': ['The following indicators would justify calling medics:']},
    ]
    oe['entries'] += [e for e in new if e['id'] not in have]
    OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied |', len(MD.read_text(encoding='utf-8').split()), 'words')


if __name__ == '__main__':
    main()
