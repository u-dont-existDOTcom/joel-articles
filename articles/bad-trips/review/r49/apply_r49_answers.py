"""apply_r49_answers.py - his SS-ASKED answers (a, c, d, e) carried into steps 2 and 8 of the serotonin steps, after two
rounds of fresh reads, each step Human High by itself (humanize/h68-20261122/RESULTS.md: 9e72f856, a3c02dd9). Run after
apply_r49.py, from the repo root:

  python3 articles/bad-trips/review/r49/apply_r49_answers.py

- Step 2: his step, whole, and one line after it from his answer (a): most people won't have it at home, since it needs a
  prescription in the US (a telehealth doctor might write one quickly), and only some countries sell it without one.
- Step 8: his line on topical magnesium chloride kept as he wrote it; niacin's reason from his answer (c), checked against
  the NIH fact sheet; the Syrian rue oil from his answer (e), framed as "leave out for now", which round 50 asks him
  about; magnesium's reason from his answer (d) and the nursing review he sent. His "Niacinamide would be safer" and his
  dose-raising for the oil stay out of an emergency step (said in the turn's report).
- Step 6 waits: his drink answer (b and BOLD-56) raises questions only he can answer (round 50, SS-DRINK).
"""
import json
import pathlib

REPO = pathlib.Path(__file__).resolve().parents[4]
ART = REPO / 'articles' / 'bad-trips'
MD = ART / 'GUIDE-SO-FAR.md'
BL = ART / 'GUIDE-SO-FAR-blocks.json'
H68 = REPO / 'articles' / 'bad-trips' / 'humanize' / 'h68-20261122'


def main():
    blocks = json.loads(BL.read_text(encoding='utf-8'))
    b = {x['id']: x for x in blocks}['B136']
    lines = b['md'].split('\n')
    s2 = (H68 / 'DRAFT-ss2.md').read_text(encoding='utf-8').strip()
    s8 = (H68 / 'DRAFT-ss8.md').read_text(encoding='utf-8').strip()
    assert s2.startswith(lines[1][3:]), 'step 2 must start with his step as the guide has it'
    assert lines[7].endswith("Topical magnesium chloride if they're not able to swallow."), lines[7][-80:]
    assert s8.endswith("Topical magnesium chloride if they're not able to swallow.")
    lines[1] = '2. ' + s2
    lines[7] = '8. ' + s8
    b['md'] = '\n'.join(lines)
    MD.write_text('\n\n'.join(x['md'] for x in blocks) + '\n', encoding='utf-8')
    BL.write_text(json.dumps(blocks, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    p = ART / 'OWNER-EDITS.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    e = {'id': 'r49-asked-answers', 'status': 'applied',
         'what': ('his SS-ASKED answers carried into the serotonin steps: (a) getting cyproheptadine, at the end of his step 2; '
                  '(c) why niacin is unsafe, (d) why magnesium, with the review he sent, and (e) the Syrian rue oil, in step 8, '
                  'his topical magnesium line kept (review/r49/apply_r49_answers.py)'),
         'joel': '2026-11-22 17:21 UTC: his round-49 export (articles/bad-trips/review/r49/ANSWERS-R49-20261122-1721.json), SS-ASKED',
         'applied_by': 'review/r49/apply_r49_answers.py',
         'must_contain_exact': ["And most people won't have it at home anyway, since it needs a prescription in the US",
                                'Niacin is actually unsafe with serotonin syndrome, since at the doses used to end a trip',
                                "I'd also leave out this guide's Syrian rue oil for now",
                                'Magnesium chloride is the one I would consider, since many people with serotonin syndrome run low on magnesium',
                                "Topical magnesium chloride if they're not able to swallow."]}
    if not any(x['id'] == e['id'] for x in d['entries']):
        d['entries'].append(e)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('applied: step 2 with his answer (a), step 8 with his answers (c), (d), (e)')


if __name__ == '__main__':
    main()
