#!/usr/bin/env python3
"""apply_r30.py - round 30's answers (Joel, exported 2026-11-09 18:43:50 UTC; ANSWERS-R30-20261109-1843.json) put into the
guide.

- RUE-OIL, approved: his Syrian rue oil entry after DMSO (after B207, DMSO's last block), as the card had it.
- OILS, approved: his essential-oils entry after Humic Acid (after B184).
- HERBS-NAMED, approved: his restlessness line names the herbs.
- RUE-WARN, rejected: "no what they should be careful about is vaping the whole seeds, that could be more likely to have
  an MAOi effect, there's almost no MAOi in 1-2mL of the rue seed oil, although with any new substance people should be
  careful to see how it affects them with smaller amounts which i think i said somewhere." His entry says the vaping
  caution, and My Acute Rescue Hierarchy's opening says to try every remedy in very low, increasing doses before it is
  needed. Recorded in OWNER-EDITS.json (r30-rue-caution-his) so no pass adds the general caution back.
- TOC: "a sure rename them so readers can find them, and brain should be at top yeah that's kind of one of the most common
  things people say". Option A as he chose it: the brain section stays first, and the three headings fresh readers had to
  guess at are renamed, his words kept (../../humanize/h39-20261109/toc/plan_toc.py, which this runs after the cards).

  python3 apply_r30.py      write the guide after round 30 and print what changed
"""
import hashlib
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ART = HERE.parent.parent
BJ = ART / 'GUIDE-SO-FAR-blocks.json'
MD = ART / 'GUIDE-SO-FAR.md'
BLOCKS = json.loads(BJ.read_text(encoding='utf-8'))
before_md = MD.read_text(encoding='utf-8')
assert '\n\n'.join(b['md'] for b in BLOCKS) + '\n' == before_md, 'the blocks and the guide disagree'
A = json.loads((HERE / 'ANSWERS-R30-20261109-1843.json').read_text(encoding='utf-8'))
R = json.loads((HERE / 'REVIEW-R30.json').read_text(encoding='utf-8'))
assert A['review_id'] == R['review_id'] == 'bad-trips-r30'
assert hashlib.sha256((HERE / 'PAGE-R30.md').read_bytes()).hexdigest() == A['article']['sha256']
I = {x['id']: x for x in A['items']}
C = {s['id']: s for s in R['suggestions']}
assert I['RUE-OIL']['status'] == I['OILS']['status'] == I['HERBS-NAMED']['status'] == 'approved'
assert I['RUE-WARN']['status'] == 'rejected'
assert I['TOC']['comment'].startswith('a sure rename them')
UNIT = {b['id']: b for b in BLOCKS}


def md_of(ins):
    return ('#' * int(ins['kind'][1]) + ' ' + ins['text']) if ins['kind'].startswith('h') else ins['text']


def insert_after(after_id, new_blocks):
    k = [b['id'] for b in BLOCKS].index(after_id) + 1
    BLOCKS[k:k] = new_blocks


rue = sorted(C['RUE-OIL']['inserts'], key=lambda x: x['seq'])
insert_after('B207', [{'id': 'R30-RUE%d' % (n + 1), 'kind': ins['kind'], 'md': md_of(ins), 'text': None}
                      for n, ins in enumerate(rue)])
oils = sorted(C['OILS']['inserts'], key=lambda x: x['seq'])
insert_after('B184', [{'id': 'R30-OILS%d' % (n + 1), 'kind': ins['kind'], 'md': md_of(ins), 'text': None}
                      for n, ins in enumerate(oils)])
e = C['HERBS-NAMED']['edits'][0]
old = "I'd still go for my trusty relaxing herbs and natural antipsychotics listed above first."
new = ("I'd still go for my trusty relaxing herbs first, like beach morning glory, Syrian rue oil or the Metta NMT sniffer, "
       "and natural antipsychotics like DMSO and niacin.")
assert e['after'].endswith(new)
assert UNIT['B426']['md'].count(old) == 1
UNIT['B426']['md'] = UNIT['B426']['md'].replace(old, new)

MD.write_text('\n\n'.join(b['md'] for b in BLOCKS) + '\n', encoding='utf-8')
BJ.write_text(json.dumps(BLOCKS, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
subprocess.run([sys.executable, str(ART / 'humanize/h39-20261109/toc/plan_toc.py'), 'A', '--apply'], check=True,
               stdout=subprocess.DEVNULL)
after = MD.read_text(encoding='utf-8')
print('words: %d -> %d' % (len(before_md.split()), len(after.split())))
print('inserted: Syrian rue oil (%d blocks) after DMSO, essential oils (%d blocks) after humic acid; herbs named; the '
      'contents as A with the brain section first and three headings renamed' % (len(rue), len(oils)))
