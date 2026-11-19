#!/usr/bin/env python3
"""apply_r40.py - his round-40 answer (ANSWERS-R40-20261119-0052.json): TEACH-CHEST-EVID revised, his version in whole, as
his final check has it (e8688033, Human Written, Human High 88, one window; the page's box and database hold the same
text). The study links go on his words: the rat study on "gave it to rats for three days before a heart attack", the
tissue-factor study on "slowed clotting, in mice", the human platelet study on "in human platelets".

The paragraph it replaces (B123), kept here so it can be undone:
  "The cardiovascular science is preclinical but relevant. In rats, DMSO pretreatment reduced myocardial infarct size by
  about three quarters and sharply reduced cardiac injury markers. Other work found inhibition of tissue factor, platelet
  activation, and arterial thrombus formation. [Myocardial-ischemia study](https://pubmed.ncbi.nlm.nih.gov/19904216/);
  [tissue-factor and thrombosis study](https://pubmed.ncbi.nlm.nih.gov/17000906/); [human platelet study]
  (https://pubmed.ncbi.nlm.nih.gov/20035720/)."

  python3 articles/bad-trips/review/r40/apply_r40.py      (from the repo root)
"""
import json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parents[1]
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
B = json.loads(BJ.read_text(encoding='utf-8'))
assert '\n\n'.join(b['md'] for b in B) + '\n' == MD.read_text(encoding='utf-8')
ids = [b['id'] for b in B]
ans = json.loads((HERE / 'ANSWERS-R40-20261119-0052.json').read_text(encoding='utf-8'))
HIS = [i for i in ans['items'] if i['id'] == 'TEACH-CHEST-EVID'][0]['your_version']
LINKED = (HIS.replace('When they gave it to rats for three days before a heart attack,',
                      'When they [gave it to rats for three days before a heart attack](https://pubmed.ncbi.nlm.nih.gov/19904216/),')
             .replace('DMSO also slowed clotting, in mice and in human platelets (the blood cells that start clots) in a dish.',
                      'DMSO also [slowed clotting, in mice](https://pubmed.ncbi.nlm.nih.gov/17000906/) and [in human platelets]'
                      '(https://pubmed.ncbi.nlm.nih.gov/20035720/) (the blood cells that start clots) in a dish.'))
assert LINKED.count('](https://pubmed') == 3, LINKED
i = ids.index('B123')
if B[i]['md'] != LINKED:
    assert B[i]['md'].startswith('The cardiovascular science is preclinical but relevant.'), B[i]['md'][:80]
    B[i]['md'] = LINKED
MD.write_text('\n\n'.join(b['md'] for b in B) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(B, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')

OE = ART / 'OWNER-EDITS.json'
oe = json.loads(OE.read_text(encoding='utf-8'))
if 'r40-chest-evid' not in {e['id'] for e in oe['entries']}:
    oe['entries'].append({
        'id': 'r40-chest-evid', 'status': 'applied',
        'what': ("Chest Pain's evidence paragraph is his round-40 version, whole (e8688033, Human High 88), the three studies "
                 "linked on his words (review/r40/apply_r40.py)"),
        'joel': '2026-11-19 00:52 UTC, his round-40 export: TEACH-CHEST-EVID revised',
        'must_contain': ['So far, the heart research on DMSO has only been in animals and lab dishes, and only as a prophylactic '
                         '(preventative treatment).', "those rats lost about three quarters less heart muscle than the rats who "
                         "didn't get DMSO."],
        'must_not_contain': ['The cardiovascular science is preclinical but relevant.']})
OE.write_text(json.dumps(oe, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('applied: his chest pain evidence paragraph |', len(MD.read_text(encoding='utf-8').split()), 'words')
